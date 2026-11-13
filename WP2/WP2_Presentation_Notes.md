# WP2 Presentation Speaker Notes — From Hospital Systems to the 07:00 Worklist

---

## Slide 1 — Cover: From hospital systems to the 07:00 worklist

- **Core concept:** Public SPARCS arrives months after discharge, so it cannot drive a live 07:00 AM hospital worklist. WP2 builds two speeds: a **Fast Path** that scores ~275 new admissions at 06:30 every morning to flag the top 30% (~77–82 patients), and a **Slow Path** after discharge to measure our KPI and retrain the model.
- **Walk into details:** Point out the two cards contrasting the morning clinical decision vs. post-discharge tracking.

---

## Slide 2 — 1 · Source Systems

- **Core concept:** To act on Day 1, we replace the late public file with four live hospital systems plus two public feeds. Across 17 hospitals, HL7 traffic averages just **0.18 messages/sec**, with afternoon bursts of **15–30 msg/sec**—small enough for lightweight tools.
- **What are Facts vs. Professor's Slides vs. Assumptions:**
  - **Facts (verified from NY SPARCS data, Health Data NY & NY regulations):**
    - Finger Lakes has **17 hospitals** with **137,867 stays/yr** (~275 adult med-surg admissions/day scored; 94,132/yr KPI-eligible = ~258/day).
    - The 4-year statewide SPARCS Parquet extract (`6,228,309` stays) measures **83 MB** on disk in `./WP1/data/`.
    - Public SPARCS (`10 NYCRR § 400.18`) is submitted after discharge (final coding takes **5–14 days**), caps LOS at `120 +`, hides ~5,300 redacted stays/yr, and renames 3 columns after 2016.
    - The NY SNF Bed Feed (`uhyy-xp9s`) covers **~85 regional nursing homes** (~1,200 rows/update, <5 MB).
    - `HL7 ADT` is the standard real-time hospital messaging protocol.
  - **From the Professor's Slides (Course Reference — Session 08):**
    - Using the 4 standard internal hospital systems (`HIS/ADT`, `EDIS`, `EHR Nursing Notes`, `Coding & Billing`) and `HL7 ADT` update events (*Session 08, Slides 5–10*).
    - Unstructured note quality challenges—typos, abbreviations, and negated phrases like `"does NOT live alone"` (*Session 08, Slide 19*).
  - **Assumptions (engineering sizing & operational workflow):**
    - **HL7 throughput:** ~15,000 messages/day across the 17 hospitals (**~0.18 msg/sec** average; **15–30 msg/sec** peak between 11:00–16:00 during ward discharges and ED handovers).
    - **ED & Notes volume:** ~600,000 ED visits/yr (~1,650/day, ~250/day admitted); 1–2 intake notes/stay (~500k/yr, ~15 MB/day of text) written near real-time; 05:00–06:00 notes may lag past the 06:30 scoring cutoff.
    - **Workflow quirks & schedule:** Local patient IDs differ per hospital, overnight insurance is often `"Pending"`, admission diagnosis drifts from final DRG in ~15–20% of complex stays, SNF beds are polled at **06:00 AM**, and small rural nursing homes occasionally miss weekend updates.
- **Walk into details:** Go down the table: rows 1–3 supply live admission, ED, and social signals; rows 4–6 provide billing, nursing-home beds, and historical benchmarks.

---

## Slide 3 — 2 · Architecture & Privacy Boundary

- **Core concept:** Patient privacy splits our architecture in two: names and raw nursing notes stay inside the hospital firewall, while pseudonymised data run in AWS. Local NLP converts notes into yes/no flags, and a Privacy Gateway swaps names for a hashed ID before anything goes to the cloud.
- **Walk into details:** Trace the diagram left-to-right to the 06:30 scorer and back to the 07:00 EHR list, then highlight the bottom comparison table of technology choices.

---

## Slide 4 — 3 · Ingestion Strategy

- **Core concept:** We only stream data that the 07:00 morning worklist actually needs, and run everything else as scheduled batches. About **22%** of emergency admissions arrive between midnight and 06:00 AM, so streaming ensures overnight patients are never delayed by 24 hours.
- **Walk into details:** Contrast the streaming box on the left with the three Airflow batches on the right, then trace the 24-hour timeline at the bottom.

---

## Slide 5 — 4 · Raw Layer (Bronze)

- **Note:** **Bronze, Silver, and Gold** are the three stages of the **Medallion Architecture**—a standard way to organise a cloud Data Lakehouse (`S3 + Iceberg` in Slide 3 & Slide 5) so data gets cleaner and more useful step by step.
- **Core concept:** The Bronze layer keeps raw data untouched in S3 using two binary formats: **Avro** for fast streaming writes and **Parquet** for compact analytics. In our workspace data folder, Parquet shrinks 6.2M hospital stays from ~1.2 GB in CSV down to just **83 MB** (14× smaller).
- **Walk into details:** Compare Avro vs. Parquet at the top, then cover S3 partitioning, the 15-minute buffer against tiny files, and 7-year retention.

---

## Slide 6 — 5 · Silver ETL

- **Core concept:** Silver ETL turns messy hospital messages into clean records while blocking future discharge data from leaking into Day-1 predictions. Every stay is split at 06:00 AM into Day-1 inputs vs. post-discharge outcomes.
- **Walk into details:** Walk through the 5 rules on the left, then show the concrete Before/After example for patient `SMH-8841` and the Polars snippet.

---

## Slide 7 — 6A · Persistence & Star Schema

- **Core concept:** One Star Schema powers both fast morning lookups for nurses and historical analytics, plus an 08:00 feedback loop. PostgreSQL serves the 07:00 worklist in **<15 ms**, Redshift tracks monthly excess bed-days against the frozen 2017 P75 ruler, and case-manager claims sync back to the lake.
- **Note:**
  - **In the center = Fact tables** (the events we measure, like *"today's admissions"* or *"completed stays"*).
  - **Around the outside = Dimension tables** (small lookup tables that describe the *who, where, when, and benchmark*).
  - Silver cleans the raw hospital data and runs the 06:30 risk model. The **Gold layer** takes those clean tables + the model score + the frozen 2017 ruler and outputs **two final Fact tables**:
    1. `FCT_DAY1_WORKLIST` $\rightarrow$ served in **PostgreSQL** for the 07:00 AM case-manager list (<15 ms).
    2. `FCT_COMPLETED_STAY` $\rightarrow$ stored in **Redshift** for monthly excess bed-day KPIs and model retraining.
- **Walk into details:** Show the 2 Fact tables and 4 Dimensions on the left, then explain the indexing and 08:00 write-back boxes on the right.

---

## Slide 8 — 6B · Gold Data Dictionary

- **Core concept:** This table is our anti-leakage contract—every Gold column is tagged by when it becomes available. Green fields are known at admission for scoring; blue fields come from the 06:30 model and 08:00 claim; amber is the static 2017 benchmark; red fields exist only after discharge.
- **Walk into details:** Highlight one example per color (`lives_alone` vs. `had_day1_planning` vs. `excess_days`) and note that race/ethnicity are kept only for fairness audits.

---

## Slide 9 — 7 · Scalability, Sizing & FinOps

- **Core concept:** Because 17 hospitals generate under **50 MB/day** (~77–82 flagged patients), we avoid expensive 24/7 clusters and run serverless for **~$600–$900/month** (<0.06% of WP1's $17.5M annual savings), while still scaling cleanly to all ~200 NY hospitals.
- **Walk into details:** Compare Finger Lakes vs. Statewide volumes in the table, point out the FinOps card, and explain the 3 sizing cards (MSK Serverless, 1 Polars container, Glue PySpark).

---

## Slide 10 — 8 · Governance, Quality Tests & Known Defects

- **Core concept:** Four automated **`dbt` (data build tool)** tests at 06:15 guard the morning worklist before nurses see it, while we stay transparent about three real-world limits. The checks verify uniqueness, completeness, validity, and freshness (`MAX(admit_ts) >= 05:30 AM`), alongside a Data Catalogue card.
- **Note:** Imagine 6 months from now, a new data analyst, a hospital director, or a HIPAA privacy auditor opens the database and sees a table called `gold.fct_day1_worklist`. They will immediately ask 6 questions (who owns it, what 1 row means, update SLA, privacy level, data lineage, and quality status)—and the **Data Catalogue Entry** (the dark card on the top-right of Slide 10) answers all 6 in one place.
- **Walk into details:** Explain the 4 checks and Catalogue card on top, then how WP2 closes all 6 SPARCS gaps and mitigates diagnosis drift, early-morning note lag, and out-of-region stays.
