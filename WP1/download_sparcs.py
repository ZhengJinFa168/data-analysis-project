"""
WP1 data extract - NY SPARCS Hospital Inpatient Discharges (De-Identified)
Team: Jin fa Zheng, Andrea Brugnera

Downloads ONLY what the WP1 business case needs, filtered on the server
through the Health Data NY (Socrata SODA) API, and saves it as Parquet.
The rationale for every year, row and column kept is in the companion doc
"SPARCS Data Extract - Scope and Rationale (WP1)".

Usage
    pip install requests pandas pyarrow
    python download_sparcs.py                 # everything (~30-60 min, ~6M stays)
    python download_sparcs.py --only stays    # one table: ruler | stays | trend | funnel | lookups
    python download_sparcs.py --app-token XXX # optional, avoids API throttling
                                              # (free token: health.data.ny.gov > Developer settings)
Output: ./data/
"""
import argparse
import io
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

# --------------------------------------------------------------------------
# 1. CONFIGURATION - every scope decision lives here, nowhere else
# --------------------------------------------------------------------------
BASE = "https://health.data.ny.gov/resource/{id}.csv"

DATASETS = {          # Health Data NY dataset id per discharge year
    2016: "gnzp-ekau",
    2017: "22g3-z7e7",
    2018: "yjgt-tq93",
    2019: "4ny4-j5zv",
    2020: "nxi5-zj9x",
    2021: "tg3i-cinn",
    2022: "5dtw-tffi",  # listed for reference only: not downloaded (team decision)
    2023: "46xm-urtu",
    # 2024: "<id>",     # add when NYS DOH publishes it -> second test year
}

SYSTEM_HSA = "Finger Lakes"            # business-case system (KPI, cost scenario); a subset of B
REF_YEARS = [2017]                     # the frozen ruler (P75 typical stay), statewide
STAY_YEARS = [2017, 2018, 2019, 2023]  # train 2017 | validate 2018-2019 | test + baseline 2023
                                       # (add 2024 as a second test year when published)
TREND_YEARS = [2016, 2017, 2018, 2019, 2020, 2021, 2023]  # aggregates only; 2022 not downloaded
MIN_CELL = 30                          # fewer stays than this -> P75 at DRG level

EXCL_MDC = "('14','15','19','20')"     # obstetrics, newborns, psychiatry, substance use
EXCL_DRG = "('860','955','956')"       # rehabilitation, invalid dx, ungroupable
KPI_EXCL_DISP = "('Expired','Short-term Hospital')"  # stay did not end in a plannable discharge

PAGE = 50_000


def fields(year):
    """API field names that changed between releases."""
    old = year <= 2016
    return {
        "hsa": "health_service_area" if old else "hospital_service_area",
        "fac": "facility_id" if old else "permanent_facility_id",
        "medsurg": "apr_medical_surgical_description" if old else "apr_medical_surgical",
    }


# Row rules, applied in this order. Each one is reported in funnel.csv.
def rules(year):
    k = fields(year)
    return [
        ("1 facility known",            f"{k['fac']} IS NOT NULL"),
        ("2 no newborn / obstetrics / psychiatry / substance use",
                                         f"type_of_admission != 'Newborn' AND apr_mdc_code NOT IN {EXCL_MDC}"),
        ("3 adults only",               "age_group != '0 to 17'"),
        ("4 no rehab / ungroupable",    f"apr_drg_code NOT IN {EXCL_DRG}"),
    ]


def scope_where(year):
    return " AND ".join(w for _, w in rules(year))


KPI_WHERE = f"(patient_disposition IS NULL OR patient_disposition NOT IN {KPI_EXCL_DISP})"

STAY_COLUMNS = [  # Table B, 2017+ field names
    # known at admission -> model inputs
    "discharge_year", "hospital_service_area", "permanent_facility_id",
    "age_group", "gender", "zip_code_3_digits", "type_of_admission",
    "emergency_department_indicator", "payment_typology_1",
    "apr_mdc_code", "apr_drg_code", "apr_severity_of_illness_code", "apr_medical_surgical",
    # target
    "length_of_stay",
    # known only at discharge -> analysis only, never model inputs
    "total_costs", "patient_disposition", "race", "ethnicity",
]

# --------------------------------------------------------------------------
# 2. API HELPERS
# --------------------------------------------------------------------------
session = requests.Session()
QUERY_LOG = []   # every request sent, saved in manifest.json (lineage)


def get_csv(year, params, tries=4):
    url = BASE.format(id=DATASETS[year])
    QUERY_LOG.append({"year": year, "url": url, **{k: str(v) for k, v in params.items()}})
    for attempt in range(tries):
        try:
            r = session.get(url, params=params, timeout=600)
            r.raise_for_status()
            return pd.read_csv(io.StringIO(r.text), dtype=str)
        except requests.RequestException as e:
            if attempt == tries - 1:
                raise
            wait = 10 * (attempt + 1)
            print(f"    retry in {wait}s ({e})")
            time.sleep(wait)


def fetch(year, select, where, order, group=None):
    """All pages of one SoQL query. $order is required for stable paging."""
    frames, offset = [], 0
    while True:
        params = {"$select": select, "$where": where, "$order": order,
                  "$limit": PAGE, "$offset": offset}
        if group:
            params["$group"] = group
        df = get_csv(year, params)
        frames.append(df)
        print(f"    {year}: {offset + len(df):,} rows")
        if len(df) < PAGE:
            break
        offset += PAGE
    return pd.concat(frames, ignore_index=True)


def count(year, where):
    df = get_csv(year, {"$select": "count(*) AS n", "$where": where})
    return int(df["n"].iloc[0])


def los_to_int(s):
    """'120 +' is the top-coded value -> 120 (flagged separately)."""
    return pd.to_numeric(s.astype(str).str.replace("+", "", regex=False).str.strip(),
                         errors="coerce").astype("Int64")


def weighted_p75(freq, keys):
    """P75 of LOS from a frequency table, per group of `keys`.
    Inverted-CDF definition: the first LOS at which 75% of stays are reached."""
    g = freq.groupby(keys + ["los"], as_index=False)["n"].sum().sort_values(keys + ["los"])
    g["cum"] = g.groupby(keys)["n"].cumsum()
    g["tot"] = g.groupby(keys)["n"].transform("sum")
    hit = g[g["cum"] >= 0.75 * g["tot"]]
    return hit.groupby(keys, as_index=False).first()[keys + ["los", "tot"]] \
        .rename(columns={"los": "p75_los", "tot": "n_ref"})


# --------------------------------------------------------------------------
# 3. TABLES
# --------------------------------------------------------------------------
def table_ruler(out):
    """Table A: statewide LOS frequency per DRG x severity, reference year(s) -> frozen P75."""
    print(f"\n[A] Ruler: statewide frequency table {REF_YEARS}")
    parts = []
    for y in REF_YEARS:
        df = fetch(y,
                   select="apr_drg_code, apr_severity_of_illness_code, length_of_stay, count(*) AS n",
                   where=f"{scope_where(y)} AND {KPI_WHERE}",
                   group="apr_drg_code, apr_severity_of_illness_code, length_of_stay",
                   order="apr_drg_code, apr_severity_of_illness_code, length_of_stay")
        df["discharge_year"] = y
        parts.append(df)
    freq = pd.concat(parts, ignore_index=True)
    freq["n"] = freq["n"].astype(int)
    freq["los"] = los_to_int(freq["length_of_stay"])
    tag = "_".join(str(y) for y in REF_YEARS)
    freq.to_parquet(out / f"A_ruler_freq_statewide_{tag}.parquet", index=False)

    # P75 per DRG x severity (pooled if several reference years); thin cells -> DRG level
    keys = ["apr_drg_code", "apr_severity_of_illness_code"]
    cell = weighted_p75(freq, keys)
    drg = weighted_p75(freq, ["apr_drg_code"]) \
        .rename(columns={"p75_los": "p75_los_drg", "n_ref": "n_ref_drg"})
    ruler = cell.merge(drg, on="apr_drg_code", how="left")
    ruler["thin_cell"] = ruler["n_ref"] < MIN_CELL
    ruler["p75_used"] = ruler["p75_los"].where(~ruler["thin_cell"], ruler["p75_los_drg"])
    ruler.to_parquet(out / f"A_ruler_p75_{tag}.parquet", index=False)  # keeps codes as text
    ruler.to_csv(out / f"A_ruler_p75_{tag}.csv", index=False)          # human-readable copy
    print(f"    ruler: {len(ruler):,} DRG x severity cells, {ruler['thin_cell'].sum():,} thin")
    return len(freq)


def table_stays(out):
    """Table B: one row per stay, all 8 service areas (statewide), STAY_YEARS."""
    print(f"\n[B] Stays: statewide, {STAY_YEARS}")
    total = 0
    for y in STAY_YEARS:
        df = fetch(y,
                   select=", ".join(STAY_COLUMNS + ["facility_name"]),
                   where=scope_where(y),
                   order=":id")
        # facility names go to a lookup table, ids stay in the facts
        df[["permanent_facility_id", "facility_name"]].drop_duplicates() \
            .assign(discharge_year=y) \
            .to_csv(out / f"lookup_facilities_{y}.csv", index=False)
        df = df.drop(columns="facility_name")
        # typing: everything arrives as text
        df["los"] = los_to_int(df["length_of_stay"])
        df["los_capped"] = df["length_of_stay"].astype(str).str.contains(r"\+", regex=True)
        df["total_costs"] = pd.to_numeric(
            df["total_costs"].astype(str).str.replace(r"[^0-9.\-]", "", regex=True),
            errors="coerce")
        df["kpi_eligible"] = ~df["patient_disposition"].isin(["Expired", "Short-term Hospital"])
        df["business_case_system"] = df["hospital_service_area"] == SYSTEM_HSA
        # low-cardinality text -> category: ~1.5M rows a year stay light in memory and on disk
        for c in STAY_COLUMNS:
            if c not in ("length_of_stay", "total_costs") and df[c].nunique() < 2000:
                df[c] = df[c].astype("category")
        df.to_parquet(out / f"B_stays_statewide_{y}.parquet", index=False)
        total += len(df)
    return total


def table_trend(out):
    """Table C: LOS frequency per service area x DRG x severity, TREND_YEARS (no stay rows)."""
    print(f"\n[C] Trend: statewide frequency tables {TREND_YEARS}")
    parts = []
    for y in TREND_YEARS:
        hsa = fields(y)["hsa"]
        df = fetch(y,
                   select=f"{hsa} AS hospital_service_area, apr_drg_code, "
                          "apr_severity_of_illness_code, length_of_stay, count(*) AS n",
                   where=f"{scope_where(y)} AND {KPI_WHERE}",
                   group=f"{hsa}, apr_drg_code, apr_severity_of_illness_code, length_of_stay",
                   order=f"{hsa}, apr_drg_code, apr_severity_of_illness_code, length_of_stay")
        df["discharge_year"] = y
        parts.append(df)
    trend = pd.concat(parts, ignore_index=True)
    trend["n"] = trend["n"].astype(int)
    trend["los"] = los_to_int(trend["length_of_stay"])
    trend["covid_year"] = trend["discharge_year"].isin([2020, 2021])
    trend.to_parquet(out / "C_trend_freq_2016_2023.parquet", index=False)
    return len(trend)


def table_funnel(out):
    """Rows left after each rule: statewide and the business-case system, per stay year."""
    print("\n[funnel] counting rows after each rule")
    rows = []
    targets = [(a, y) for y in STAY_YEARS for a in ("New York State", SYSTEM_HSA)]
    for area, y in targets:
        base = f"hospital_service_area = '{SYSTEM_HSA}'" if area == SYSTEM_HSA else "1 = 1"
        acc = base
        rows.append({"area": area, "year": y, "step": "0 raw", "rows": count(y, acc)})
        for name, w in rules(y):
            acc = f"{acc} AND {w}"
            rows.append({"area": area, "year": y, "step": name, "rows": count(y, acc)})
        rows.append({"area": area, "year": y, "step": "5 KPI-eligible (no deaths / acute transfers)",
                     "rows": count(y, f"{acc} AND {KPI_WHERE}")})
    f = pd.DataFrame(rows)
    f.to_csv(out / "funnel.csv", index=False)
    print(f.pivot_table(index="step", columns=["area", "year"], values="rows").to_string())
    return len(f)


def table_lookups(out):
    """Code -> description for diagnosis groups and MDCs (2023 grouper)."""
    print("\n[lookups] DRG and MDC descriptions")
    drg = fetch(2023, select="apr_drg_code, apr_drg_description, apr_mdc_code, count(*) AS n_2023",
                where="apr_drg_code IS NOT NULL",
                group="apr_drg_code, apr_drg_description, apr_mdc_code",
                order="apr_drg_code")
    drg.to_csv(out / "lookup_apr_drg.csv", index=False)
    mdc = fetch(2023, select="apr_mdc_code, apr_mdc_description, count(*) AS n_2023",
                where="apr_mdc_code IS NOT NULL", group="apr_mdc_code, apr_mdc_description",
                order="apr_mdc_code")
    mdc.to_csv(out / "lookup_apr_mdc.csv", index=False)
    return len(drg) + len(mdc)


TABLES = {"lookups": table_lookups, "funnel": table_funnel, "ruler": table_ruler,
          "stays": table_stays, "trend": table_trend}


# --------------------------------------------------------------------------
# 4. RUN + MANIFEST (lineage: what was asked, when, how many rows came back)
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent / "data"))
    ap.add_argument("--only", choices=list(TABLES), nargs="*")
    ap.add_argument("--app-token")
    a = ap.parse_args()
    if a.app_token:
        session.headers["X-App-Token"] = a.app_token
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    manifest_path = out / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest["config"] = {
        "source": "Health Data NY - Hospital Inpatient Discharges (SPARCS De-Identified)",
        "datasets": DATASETS, "system_hsa": SYSTEM_HSA, "ref_years": REF_YEARS,
        "stay_years": STAY_YEARS, "trend_years": TREND_YEARS, "min_cell": MIN_CELL,
        "scope_where_2017plus": scope_where(2017), "kpi_where": KPI_WHERE,
        "stay_columns": STAY_COLUMNS,
    }
    for name in (a.only or list(TABLES)):
        t0 = time.time()
        n = TABLES[name](out)
        manifest.setdefault("tables", {})[name] = {
            "rows": n, "seconds": round(time.time() - t0),
            "downloaded_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        manifest.setdefault("queries", {})[name] = QUERY_LOG.copy()
        QUERY_LOG.clear()
        manifest_path.write_text(json.dumps(manifest, indent=2))
    print(f"\nDone. Files in {out.resolve()}")


if __name__ == "__main__":
    sys.exit(main())
