#!/usr/bin/env python3
"""
Builds the single, concise 10-slide WP2 presentation (.pptx and .pdf),
matching the exact visual style and simplicity of WP1.
"""

import os
import sys
import zipfile
import textwrap
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.abspath(".venv/lib/python3.12/site-packages"))
os.environ["MPLCONFIGDIR"] = "/tmp/mpl_wp2_cache"

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

EMU = 914400
SLIDE_W = 13.333333
SLIDE_H = 7.50

# WP1 Exact Color Palette
NAVY       = "16253D"
NAVY_CARD  = "1E314F"
NAVY_LINE  = "3A4B66"
CREAM_BG   = "F5F3EE"
CARD_BG    = "FCFBF8"
MUTED_CARD = "ECE9E1"
BORDER     = "DDD8CC"
BORDER_DK  = "C4C2BE"
TERRA      = "B8462B"
PEACH      = "F0A47E"
BLUE       = "2D6A93"
BLUE_LT    = "E9F0F5"
TERRA_LT   = "F9EBE6"
GREEN_BG   = "E6F2EC"
GREEN_FG   = "1E6B45"
AMBER_BG   = "FBF2E3"
AMBER_FG   = "94580A"
SLATE      = "3C4757"
MUTED      = "6B7482"
LIGHT_TXT  = "B9C3D1"

FONT_SERIF = "Source Serif 4"
FONT_SANS  = "Public Sans"
FONT_MONO  = "Courier New"


def emu(inches: float) -> int:
    return int(round(inches * EMU))


class SlideBuilder:
    def __init__(self, slide_num: int, bg_color: str = CREAM_BG, notes: str = ""):
        self.slide_num = slide_num
        self.bg_color = bg_color
        self.notes = notes
        self.items = []
        self._next_id = 2

    def _id(self) -> int:
        i = self._next_id
        self._next_id += 1
        return i

    def add_rect(self, x, y, w, h, fill=CARD_BG, border=BORDER, border_w=0.75, rounded=True, radius=0.08):
        self.items.append({
            "kind": "rect", "id": self._id(),
            "x": x, "y": y, "w": w, "h": h,
            "fill": fill, "border": border, "border_w": border_w,
            "rounded": rounded, "radius": radius
        })

    def add_line(self, x1, y1, x2, y2, color=BORDER, width=1.0, dashed=False, arrow=False):
        self.items.append({
            "kind": "line", "id": self._id(),
            "x1": x1, "y1": y1, "x2": x2, "y2": y2,
            "color": color, "width": width, "dashed": dashed, "arrow": arrow
        })

    def add_text(self, x, y, w, h, paragraphs, align="l", valign="t", line_mult=1.22, nowrap=False):
        norm_paras = []
        for p in paragraphs:
            if isinstance(p, dict):
                norm_paras.append([p])
            elif isinstance(p, tuple):
                norm_paras.append([self._tuple_to_run(p)])
            elif isinstance(p, list):
                norm_paras.append([self._tuple_to_run(r) if isinstance(r, tuple) else r for r in p])
        self.items.append({
            "kind": "text", "id": self._id(),
            "x": x, "y": y, "w": w, "h": h,
            "paragraphs": norm_paras, "align": align, "valign": valign,
            "line_mult": line_mult, "nowrap": nowrap
        })

    def _tuple_to_run(self, t):
        text = t[0]
        size = t[1] if len(t) > 1 else 11.0
        bold = t[2] if len(t) > 2 else False
        color = t[3] if len(t) > 3 else SLATE
        font = t[4] if len(t) > 4 else FONT_SANS
        italic = t[5] if len(t) > 5 else False
        spc = t[6] if len(t) > 6 else 0
        return {"text": text, "size": size, "bold": bold, "color": color, "font": font, "italic": italic, "spc": spc}

    def add_header(self, kicker: str, title: str, subtitle: str = ""):
        self.add_text(
            0.89, 0.48, 11.55, 0.24,
            [(kicker, 10.5, True, TERRA, FONT_SANS, False, 140)],
            nowrap=True
        )
        self.add_text(
            0.89, 0.76, 11.55, 0.44,
            [(title, 20.5, True, NAVY, FONT_SERIF)],
            nowrap=True
        )
        if subtitle:
            self.add_text(
                0.89, 1.24, 11.55, 0.26,
                [(subtitle, 11.0, False, SLATE, FONT_SANS)],
                nowrap=True
            )

    def add_footer(self, source_note: str):
        self.add_text(
            0.89, 6.94, 10.80, 0.26,
            [(source_note, 9.0, False, MUTED, FONT_SANS)],
            nowrap=True
        )
        self.add_text(
            11.83, 6.94, 0.61, 0.26,
            [(str(self.slide_num), 10.5, True, MUTED, FONT_SANS)],
            align="r", nowrap=True
        )

    def add_badge(self, x, y, w, h, text, fill=TERRA, fg=CARD_BG, size=9.0, rounded=True):
        self.add_rect(x, y, w, h, fill=fill, border=None, border_w=0, rounded=rounded, radius=0.05)
        self.add_text(x, y, w, h, [(text, size, True, fg, FONT_SANS)], align="c", valign="m", nowrap=("\n" not in text))

    def add_table(self, x, y, col_widths, row_heights, rows, header_bg=NAVY, header_fg=CARD_BG,
                  zebra_a=CARD_BG, zebra_b="F3F0E8", border_color=BORDER_DK, font_size=9.5,
                  cell_fills=None, cell_text_colors=None, alignments=None):
        self.items.append({
            "kind": "table", "id": self._id(),
            "x": x, "y": y, "col_widths": col_widths, "row_heights": row_heights,
            "rows": rows, "header_bg": header_bg, "header_fg": header_fg,
            "zebra_a": zebra_a, "zebra_b": zebra_b, "border_color": border_color,
            "font_size": font_size, "cell_fills": cell_fills or {},
            "cell_text_colors": cell_text_colors or {}, "alignments": alignments or []
        })

    def to_pptx_xml(self) -> str:
        parts = [
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">',
            f'<p:cSld name="Slide {self.slide_num}">',
            f'<p:bg><p:bgPr><a:solidFill><a:srgbClr val="{self.bg_color}"/></a:solidFill></p:bgPr></p:bg>',
            '<p:spTree>',
            '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>',
            '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        ]
        for item in self.items:
            kind = item["kind"]
            if kind == "rect":
                parts.append(self._rect_to_xml(item))
            elif kind == "line":
                parts.append(self._line_to_xml(item))
            elif kind == "text":
                parts.append(self._text_to_xml(item))
            elif kind == "table":
                parts.append(self._table_to_xml(item))
        parts.append('</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')
        return "".join(parts)

    def _rect_to_xml(self, it) -> str:
        prst = "roundRect" if it["rounded"] else "rect"
        av = '<a:avLst><a:gd name="adj" fmla="val 3500"/></a:avLst>' if it["rounded"] else '<a:avLst/>'
        fill_xml = f'<a:solidFill><a:srgbClr val="{it["fill"]}"/></a:solidFill>' if it["fill"] else '<a:noFill/>'
        if it["border"] and it["border_w"] > 0:
            w_emu = int(round(it["border_w"] * 12700))
            ln_xml = f'<a:ln w="{w_emu}"><a:solidFill><a:srgbClr val="{it["border"]}"/></a:solidFill><a:prstDash val="solid"/></a:ln>'
        else:
            ln_xml = '<a:ln><a:noFill/></a:ln>'
        return (
            f'<p:sp><p:nvSpPr><p:cNvPr id="{it["id"]}" name="Shape {it["id"]}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(it["x"])}" y="{emu(it["y"])}"/><a:ext cx="{emu(it["w"])}" cy="{emu(it["h"])}"/></a:xfrm>'
            f'<a:prstGeom prst="{prst}">{av}</a:prstGeom>{fill_xml}{ln_xml}</p:spPr></p:sp>'
        )

    def _line_to_xml(self, it) -> str:
        x1, y1, x2, y2 = it["x1"], it["y1"], it["x2"], it["y2"]
        ox, oy = min(x1, x2), min(y1, y2)
        cx, cy = abs(x2 - x1), abs(y2 - y1)
        flipH = ' flipH="1"' if x2 < x1 else ''
        flipV = ' flipV="1"' if y2 < y1 else ''
        w_emu = int(round(it["width"] * 12700))
        dash = "dash" if it["dashed"] else "solid"
        tail = '<a:tailEnd type="triangle" w="med" len="med"/>' if it["arrow"] else ''
        return (
            f'<p:sp><p:nvSpPr><p:cNvPr id="{it["id"]}" name="Line {it["id"]}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm{flipH}{flipV}><a:off x="{emu(ox)}" y="{emu(oy)}"/><a:ext cx="{emu(cx)}" cy="{emu(cy)}"/></a:xfrm>'
            f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom><a:noFill/>'
            f'<a:ln w="{w_emu}"><a:solidFill><a:srgbClr val="{it["color"]}"/></a:solidFill><a:prstDash val="{dash}"/>{tail}</a:ln>'
            f'</p:spPr></p:sp>'
        )

    def _text_to_xml(self, it) -> str:
        algn = {"l": "l", "c": "ctr", "r": "r"}.get(it["align"], "l")
        anc = {"t": "t", "m": "ctr", "b": "b"}.get(it["valign"], "t")
        p_xmls = []
        for p in it["paragraphs"]:
            max_sz = max((r["size"] for r in p), default=11.0)
            spc_pts = int(round(max_sz * it["line_mult"] * 100))
            r_xmls = []
            for r in p:
                sz = int(round(r["size"] * 100))
                b = ' b="1"' if r.get("bold") else ''
                i = ' i="1"' if r.get("italic") else ''
                spc = f' spc="{r["spc"]}"' if r.get("spc") else ''
                fn = escape(r.get("font", FONT_SANS))
                col = r.get("color", SLATE)
                txt = escape(r.get("text", ""))
                r_xmls.append(
                    f'<a:r><a:rPr lang="en-US" sz="{sz}"{b}{i}{spc} dirty="0">'
                    f'<a:solidFill><a:srgbClr val="{col}"/></a:solidFill>'
                    f'<a:latin typeface="{fn}"/><a:ea typeface="{fn}"/><a:cs typeface="{fn}"/>'
                    f'</a:rPr><a:t>{txt}</a:t></a:r>'
                )
            p_xmls.append(
                f'<a:p><a:pPr algn="{algn}" indent="0" marL="0">'
                f'<a:lnSpc><a:spcPts val="{spc_pts}"/></a:lnSpc><a:buNone/></a:pPr>'
                f'{"".join(r_xmls)}'
                f'<a:endParaRPr lang="en-US" sz="{int(round(max_sz*100))}" dirty="0"/></a:p>'
            )
        return (
            f'<p:sp><p:nvSpPr><p:cNvPr id="{it["id"]}" name="Text {it["id"]}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(it["x"])}" y="{emu(it["y"])}"/><a:ext cx="{emu(it["w"])}" cy="{emu(it["h"])}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" rtlCol="0" anchor="{anc}"/>'
            f'<a:lstStyle/>{"".join(p_xmls)}</p:txBody></p:sp>'
        )

    def _table_to_xml(self, it) -> str:
        total_w = sum(it["col_widths"])
        total_h = sum(it["row_heights"])
        grid_cols = "".join(f'<a:gridCol w="{emu(cw)}"/>' for cw in it["col_widths"])
        tr_xmls = []
        bcol = it["border_color"]
        for r_idx, row in enumerate(it["rows"]):
            rh = it["row_heights"][r_idx]
            tc_xmls = []
            for c_idx, cell in enumerate(row):
                is_hdr = (r_idx == 0)
                bg = it["cell_fills"].get((r_idx, c_idx), it["header_bg"] if is_hdr else (it["zebra_a"] if r_idx % 2 == 1 else it["zebra_b"]))
                fg = it["cell_text_colors"].get((r_idx, c_idx), it["header_fg"] if is_hdr else SLATE)
                algn = it["alignments"][c_idx] if c_idx < len(it["alignments"]) else "l"
                algn_xml = {"l": "l", "c": "ctr", "r": "r"}.get(algn, "l")

                if isinstance(cell, str):
                    runs = [{"text": cell, "size": it["font_size"], "bold": is_hdr or (c_idx == 0), "color": (NAVY if (c_idx == 0 and not is_hdr and (r_idx, c_idx) not in it["cell_text_colors"]) else fg), "font": FONT_SANS}]
                else:
                    runs = [self._tuple_to_run(r) if isinstance(r, tuple) else r for r in cell]

                r_xmls = []
                for r in runs:
                    sz = int(round(r["size"] * 100))
                    b = ' b="1"' if r.get("bold") else ''
                    i = ' i="1"' if r.get("italic") else ''
                    fn = escape(r.get("font", FONT_SANS))
                    col = r.get("color", fg)
                    txt = escape(r.get("text", ""))
                    r_xmls.append(
                        f'<a:r><a:rPr lang="en-US" sz="{sz}"{b}{i} dirty="0">'
                        f'<a:solidFill><a:srgbClr val="{col}"/></a:solidFill>'
                        f'<a:latin typeface="{fn}"/><a:ea typeface="{fn}"/><a:cs typeface="{fn}"/>'
                        f'</a:rPr><a:t>{txt}</a:t></a:r>'
                    )
                ln_def = f'<a:solidFill><a:srgbClr val="{bcol}"/></a:solidFill><a:prstDash val="solid"/>'
                tc_xmls.append(
                    f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>'
                    f'<a:p><a:pPr algn="{algn_xml}" indent="0" marL="0">'
                    f'<a:lnSpc><a:spcPts val="{int(round(it["font_size"]*124))}"/></a:lnSpc><a:buNone/></a:pPr>'
                    f'{"".join(r_xmls)}'
                    f'<a:endParaRPr lang="en-US" sz="{int(round(it["font_size"]*100))}" dirty="0"/></a:p></a:txBody>'
                    f'<a:tcPr marL="60000" marR="60000" marT="40000" marB="40000" anchor="ctr">'
                    f'<a:lnL w="6350">{ln_def}</a:lnL><a:lnR w="6350">{ln_def}</a:lnR>'
                    f'<a:lnT w="6350">{ln_def}</a:lnT><a:lnB w="6350">{ln_def}</a:lnB>'
                    f'<a:solidFill><a:srgbClr val="{bg}"/></a:solidFill></a:tcPr></a:tc>'
                )
            tr_xmls.append(f'<a:tr h="{emu(rh)}">{"".join(tc_xmls)}</a:tr>')

        return (
            f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="{it["id"]}" name="Table {it["id"]}"/>'
            f'<p:cNvGraphicFramePr><a:graphicFrameLocks noGrp="1"/></p:cNvGraphicFramePr><p:nvPr/></p:nvGraphicFramePr>'
            f'<p:xfrm><a:off x="{emu(it["x"])}" y="{emu(it["y"])}"/><a:ext cx="{emu(total_w)}" cy="{emu(total_h)}"/></p:xfrm>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table">'
            f'<a:tbl><a:tblPr/><a:tblGrid>{grid_cols}</a:tblGrid>{"".join(tr_xmls)}</a:tbl>'
            f'</a:graphicData></a:graphic></p:graphicFrame>'
        )

    def render_to_pdf_page(self, pdf: PdfPages):
        fig = plt.figure(figsize=(SLIDE_W, SLIDE_H), dpi=150)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, SLIDE_W)
        ax.set_ylim(SLIDE_H, 0)
        ax.axis("off")

        ax.add_patch(Rectangle((0, 0), SLIDE_W, SLIDE_H, facecolor="#" + self.bg_color, edgecolor="none"))

        for it in self.items:
            kind = it["kind"]
            if kind == "rect":
                fc = "#" + it["fill"] if it["fill"] else "none"
                ec = "#" + it["border"] if (it["border"] and it["border_w"] > 0) else "none"
                lw = it["border_w"] if (it["border"] and it["border_w"] > 0) else 0
                if it["rounded"]:
                    patch = FancyBboxPatch(
                        (it["x"], it["y"]), it["w"], it["h"],
                        boxstyle=f"round,pad=0,rounding_size={it['radius']}",
                        facecolor=fc, edgecolor=ec, linewidth=lw
                    )
                else:
                    patch = Rectangle((it["x"], it["y"]), it["w"], it["h"], facecolor=fc, edgecolor=ec, linewidth=lw)
                ax.add_patch(patch)
            elif kind == "line":
                ls = "--" if it["dashed"] else "-"
                if it["arrow"]:
                    arr = FancyArrowPatch(
                        (it["x1"], it["y1"]), (it["x2"], it["y2"]),
                        arrowstyle="-|>,head_length=4,head_width=2.5",
                        color="#" + it["color"], linewidth=it["width"], linestyle=ls
                    )
                    ax.add_patch(arr)
                else:
                    ax.plot([it["x1"], it["x2"]], [it["y1"], it["y2"]], color="#" + it["color"], linewidth=it["width"], linestyle=ls)
            elif kind == "text":
                self._render_text_mpl(ax, it)
            elif kind == "table":
                self._render_table_mpl(ax, it)

        pdf.savefig(fig)
        plt.close(fig)

    def _map_font_mpl(self, font_name: str) -> str:
        if "Serif" in font_name:
            return "Georgia"
        if "Courier" in font_name:
            return "Courier New"
        return "Arial"

    def _render_text_mpl(self, ax, it):
        x, y, w, h = it["x"], it["y"], it["w"], it["h"]
        align = it["align"]
        valign = it["valign"]
        nowrap = it.get("nowrap", False)
        ha = {"l": "left", "c": "center", "r": "right"}.get(align, "left")
        tx = x if ha == "left" else (x + w / 2 if ha == "center" else x + w)

        visual_lines = []
        for p in it["paragraphs"]:
            full_str = "".join(r["text"] for r in p)
            max_sz = max((r["size"] for r in p), default=10.0)
            first_run = p[0] if p else {"text": "", "size": 10.0, "bold": False, "italic": False, "color": SLATE, "font": FONT_SANS}
            char_w_in = (max_sz / 72.0) * (0.52 if first_run.get("bold") else 0.48)
            if "Courier" in first_run.get("font", ""):
                char_w_in = (max_sz / 72.0) * 0.58
            max_chars = max(10, int(w / max(char_w_in, 0.035)))

            for raw_line in full_str.split("\n"):
                if nowrap:
                    visual_lines.append((raw_line, max_sz, first_run))
                else:
                    wrapped = textwrap.wrap(raw_line, width=max_chars, break_long_words=False, replace_whitespace=False) if raw_line.strip() else [""]
                    for wl in wrapped:
                        visual_lines.append((wl, max_sz, first_run))

        if not visual_lines:
            return

        line_heights = [(sz / 72.0) * it["line_mult"] for (_, sz, _) in visual_lines]
        total_text_h = sum(line_heights)
        if valign == "m":
            curr_y = y + max(0.0, (h - total_text_h) / 2.0)
        elif valign == "b":
            curr_y = y + max(0.0, h - total_text_h)
        else:
            curr_y = y

        for (wl, sz, r), lh in zip(visual_lines, line_heights):
            fam = self._map_font_mpl(r.get("font", FONT_SANS))
            weight = "bold" if r.get("bold") else "normal"
            style = "italic" if r.get("italic") else "normal"
            ax.text(
                tx, curr_y + lh * 0.78, wl,
                fontsize=sz, fontfamily=fam, fontweight=weight, fontstyle=style,
                color="#" + r.get("color", SLATE), ha=ha, va="baseline",
                parse_math=False
            )
            curr_y += lh

    def _render_table_mpl(self, ax, it):
        curr_y = it["y"]
        bcol = "#" + it["border_color"]
        for r_idx, row in enumerate(it["rows"]):
            rh = it["row_heights"][r_idx]
            curr_x = it["x"]
            is_hdr = (r_idx == 0)
            for c_idx, cell in enumerate(row):
                cw = it["col_widths"][c_idx]
                bg = it["cell_fills"].get((r_idx, c_idx), it["header_bg"] if is_hdr else (it["zebra_a"] if r_idx % 2 == 1 else it["zebra_b"]))
                fg = it["cell_text_colors"].get((r_idx, c_idx), it["header_fg"] if is_hdr else SLATE)
                algn = it["alignments"][c_idx] if c_idx < len(it["alignments"]) else "l"

                ax.add_patch(Rectangle((curr_x, curr_y), cw, rh, facecolor="#" + bg, edgecolor=bcol, linewidth=0.55))

                if isinstance(cell, str):
                    txt_str = cell
                    bold = is_hdr or (c_idx == 0)
                    col = NAVY if (c_idx == 0 and not is_hdr and (r_idx, c_idx) not in it["cell_text_colors"]) else fg
                else:
                    runs = [self._tuple_to_run(r) if isinstance(r, tuple) else r for r in cell]
                    txt_str = "".join(r["text"] for r in runs)
                    bold = any(r.get("bold") for r in runs)
                    col = runs[0].get("color", fg) if runs else fg

                sub_it = {
                    "x": curr_x + 0.08, "y": curr_y + 0.04,
                    "w": cw - 0.16, "h": rh - 0.08,
                    "paragraphs": [[{"text": txt_str, "size": it["font_size"], "bold": bold, "color": col, "font": FONT_SANS}]],
                    "align": algn, "valign": "m", "line_mult": 1.18, "nowrap": False
                }
                self._render_text_mpl(ax, sub_it)
                curr_x += cw
            curr_y += rh


def build_all_slides():
    slides = []

    # =========================================================================
    # SLIDE 1: CLEAN EXECUTIVE COVER (MATCHING WP1 SLIDE 1)
    # =========================================================================
    s1 = SlideBuilder(
        1, bg_color=NAVY,
        notes=(
            "Core idea: Public SPARCS arrives months after discharge, so it cannot drive a live 07:00 AM hospital worklist. "
            "WP2 builds two speeds: a Fast Path that scores ~275 new admissions at 06:30 every morning to flag the top 30% (~77–82 patients), "
            "and a Slow Path after discharge to measure our KPI and retrain the model. "
            "On this slide, point out the two boxes contrasting the morning decision vs. post-discharge tracking."
        )
    )
    s1.add_text(0.89, 0.89, 11.55, 0.30, [
        ("WP2 · DATA ENGINEERING · FOR THE CTO & PLATFORM TEAM", 14.0, True, PEACH, FONT_SANS, False, 150)
    ], nowrap=True)
    s1.add_text(0.89, 1.44, 11.55, 0.70, [
        ("From hospital systems to the 07:00 worklist", 34.0, True, CREAM_BG, FONT_SERIF)
    ], nowrap=True)
    s1.add_text(0.89, 2.34, 11.55, 0.36, [
        ("Finger Lakes Health System · 17 hospitals, Rochester, NY", 17.0, False, LIGHT_TXT, FONT_SANS)
    ], nowrap=True)

    # Concise 2-box summary on Cover: Why SPARCS is not the start -> Fast Path vs Slow Path
    s1.add_rect(0.89, 3.20, 5.55, 2.05, fill=NAVY_CARD, border=TERRA, border_w=1.2, rounded=True)
    s1.add_text(1.14, 3.40, 5.05, 0.26, [("FAST PATH · EVERY MORNING BY 07:00", 10.0, True, PEACH, FONT_SANS, False, 100)], nowrap=True)
    s1.add_text(1.14, 3.72, 5.05, 1.30, [
        ("Score ~275 new adult admissions at 06:30 and flag the top 30% (~77–82 patients/day) for Day-1 discharge planning.", 12.0, True, CREAM_BG),
        ("Streams live admissions, ED diagnoses, and nursing notes—because public SPARCS arrives 60–180 days after discharge.", 10.5, False, LIGHT_TXT)
    ], line_mult=1.25)

    s1.add_rect(6.89, 3.20, 5.55, 2.05, fill=NAVY_CARD, border=BLUE, border_w=1.2, rounded=True)
    s1.add_text(7.14, 3.40, 5.05, 0.26, [("SLOW PATH · AFTER DISCHARGE", 10.0, True, "9DB7CB", FONT_SANS, False, 100)], nowrap=True)
    s1.add_text(7.14, 3.72, 5.05, 1.30, [
        ("Track the monthly KPI (excess bed-days vs. the frozen 2017 P75 ruler) and retrain the model.", 12.0, True, CREAM_BG),
        ("Combines the 08:00 case-manager write-back with final coded DRG billing (5–14 days after discharge).", 10.5, False, LIGHT_TXT)
    ], line_mult=1.25)

    s1.add_line(0.89, 5.78, 12.44, 5.78, color=NAVY_LINE, width=1.0)
    s1.add_text(0.89, 6.18, 5.00, 0.38, [("Jin fa Zheng · Andrea Brugnera", 18.0, True, CREAM_BG, FONT_SANS)], nowrap=True)
    s1.add_text(8.44, 6.07, 4.00, 0.54, [
        ("Data Analysis", 13.0, False, LIGHT_TXT, FONT_SANS),
        ("UPM · November 2026", 13.0, False, LIGHT_TXT, FONT_SANS)
    ], align="r", nowrap=True)
    slides.append(s1)

    # =========================================================================
    # SLIDE 2: 1 · SOURCE SYSTEMS
    # =========================================================================
    s2 = SlideBuilder(
        2, bg_color=CREAM_BG,
        notes=(
            "Core idea: To act on Day 1, we replace the late public file with four live hospital systems plus two public feeds. "
            "Across 17 hospitals, HL7 traffic averages just 0.18 messages/sec, with afternoon bursts of 15–30 msg/sec—small enough for lightweight tools. "
            "Walking down the table: rows 1–3 give live admission, ED, and social signals; rows 4–6 supply billing, nursing-home beds, and historical benchmarks."
        )
    )
    s2.add_header(
        "1 · SOURCE SYSTEMS · CTO QUESTION #1 (THROUGHPUT & PROCESSES)",
        "Four hospital systems and two public feeds replace a static file",
        "Fills the 5 gaps in public SPARCS: patient ID, exact dates, diagnosis at admission, social factors, and nursing-home beds."
    )

    col_w_s2 = [2.15, 2.65, 2.45, 1.60, 2.70]
    row_h_s2 = [0.38, 0.78, 0.70, 0.76, 0.72, 0.70, 0.74]
    rows_s2 = [
        ["Source System & Owner", "What It Records", "Volume & Throughput (17 Hospitals)", "Refresh Rate", "Quality Issues to Handle"],
        [
            "1. Admission & Bed (HIS/ADT)\nOwner: Hospital IT",
            "Patient ID, age, sex, ZIP, payer, exact admit/discharge time, ward & bed.",
            "137,867 stays/yr (~275 adult med-surg/d).\n~15,000 HL7 msg/day\n(0.18 msg/s avg · 15–30 msg/s peak).",
            "Real-time stream\n(HL7 ADT within\nseconds)",
            "• Different local IDs per hospital.\n• Insurance often 'Pending' at night (updated next day)."
        ],
        [
            "2. Emergency Dept. (EDIS)\nOwner: Emergency IT",
            "ED arrival flag ('Y'/'N'), vitals, and provisional admission diagnosis.",
            "~600,000 ED visits/yr (~1,650/day;\n~250/day become inpatient stays).",
            "Real-time stream\nat admission order",
            "• Admission diagnosis is rougher than final DRG (drifts in 15–20% of stays)."
        ],
        [
            "3. Nursing Intake Notes\nOwner: Nursing Informatics",
            "Free-text Day-1 note: lives alone, family carer, stairs, prior SNF.",
            "1–2 intake notes/stay (~500k/yr,\n~15 MB/day of text).",
            "Near real-time\n(within hours of\nreaching ward)",
            "• Typos and negated text ('does not live alone').\n• 05:00–06:00 notes may lag."
        ],
        [
            "4. Coding & Billing\nOwner: Finance & Coding",
            "Final APR-DRG, severity (1–4), total costs, and state SPARCS claim.",
            "137,867 coded stays/yr\n(94,132 KPI-eligible = ~258/day).",
            "Nightly batch\n(5–14 days after\ndischarge)",
            "• Not available on Day 1 (using it as a live input would be data leakage)."
        ],
        [
            "5. NY SNF Bed Feed\nOwner: NYS DOH (uhyy-xp9s)",
            "Open beds at ~85 regional nursing homes accepting Medicare/Medicaid.",
            "~85 facilities (~1,200 rows/update,\n<5 MB via REST API).",
            "Daily batch\nat 06:00 AM",
            "• Small rural nursing homes sometimes miss weekend updates."
        ],
        [
            "6. Public SPARCS & Census\nOwner: NYS DOH / US Census",
            "Historical stays (frozen 2017 P75 ruler) + ZIP deprivation score (1–10).",
            "6,228,309 NY stays across 4 years\n(83 MB total in Parquet).",
            "Yearly batch\n(download_sparcs.py)",
            "• Caps LOS at '120 +', hides ~5,300 stays/yr, renames 3 columns after 2016."
        ]
    ]
    s2.add_table(0.89, 1.62, col_w_s2, row_h_s2, rows_s2, font_size=8.8)
    s2.add_footer("HL7 peak (15–30 msg/s) occurs at 11:00–16:00 during ward discharges and ED handovers. 4-year SPARCS Parquet measured in ./data/ (83 MB).")
    slides.append(s2)

    # =========================================================================
    # SLIDE 3: 2 · ARCHITECTURE & PRIVACY BOUNDARY
    # =========================================================================
    s3 = SlideBuilder(
        3, bg_color=CREAM_BG,
        notes=(
            "Core idea: Patient privacy splits our architecture in two—names and raw nursing notes stay inside the hospital firewall, while pseudonymised data run in AWS. "
            "Local NLP converts notes into yes/no flags, and a Privacy Gateway swaps names for a hashed ID before anything goes to the cloud. "
            "Walking through the details: trace the diagram left-to-right to the 06:30 scorer and back to the 07:00 EHR list, then highlight the bottom table's tech choices."
        )
    )
    s3.add_header(
        "2 · ARCHITECTURE & PRIVACY BOUNDARY · CTO QUESTION #2 (ARCHITECTURAL ELEMENTS)",
        "Patient names and notes stay in the hospital; pseudonymised data scale in the cloud"
    )

    # Left Zone: On-Premise
    s3.add_rect(0.89, 1.34, 5.20, 2.55, fill=CARD_BG, border=TERRA, border_w=1.4, rounded=True)
    s3.add_badge(1.05, 1.44, 4.88, 0.25, "ON-PREMISE HOSPITAL ZONE · PHI NEVER LEAVES", fill=TERRA, fg=CARD_BG, size=8.5)

    s3.add_rect(1.05, 1.80, 1.50, 0.68, fill=MUTED_CARD, border=BORDER_DK, border_w=0.8, rounded=True)
    s3.add_text(1.10, 1.84, 1.40, 0.60, [
        ("HIS / ADT & EDIS", 8.5, True, NAVY),
        ("Names, MRNs, Vitals", 7.6, False, SLATE),
        ("+ Coding & Billing", 7.6, True, BLUE)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(1.05, 2.58, 1.50, 0.68, fill=TERRA_LT, border=TERRA, border_w=0.8, rounded=True)
    s3.add_text(1.10, 2.62, 1.40, 0.60, [
        ("Intake Notes", 8.5, True, TERRA),
        ("Local On-Prem NLP", 7.6, True, NAVY),
        ("Text → 2 Bool Flags", 7.5, False, SLATE)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(2.73, 1.80, 1.52, 1.46, fill=BLUE_LT, border=BLUE, border_w=1.0, rounded=True)
    s3.add_text(2.78, 1.86, 1.42, 1.34, [
        ("On-Prem Vault &", 8.4, True, NAVY),
        ("PostgreSQL DB", 8.4, True, BLUE),
        ("Re-attaches Name", 7.5, False, SLATE),
        ("→ 07:00 EHR List", 7.8, True, TERRA),
        ("→ 08:00 Write-Back", 7.5, True, GREEN_FG)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(4.43, 1.80, 1.50, 1.46, fill=NAVY, border=NAVY, border_w=0.8, rounded=True)
    s3.add_text(4.48, 1.86, 1.40, 1.34, [
        ("Privacy Gateway", 8.5, True, PEACH),
        ("& Regional EMPI", 8.0, True, CREAM_BG),
        ("Strips Name/MRN", 7.5, False, LIGHT_TXT),
        ("→ Hashed ID", 7.5, False, LIGHT_TXT),
        ("master_patient_id", 7.5, True, PEACH)
    ], align="c", valign="m", nowrap=True)

    s3.add_line(2.55, 2.14, 2.73, 2.14, color=NAVY, width=1.1, arrow=True)
    s3.add_line(2.55, 2.92, 2.73, 2.92, color=TERRA, width=1.1, arrow=True)
    s3.add_line(4.25, 2.53, 4.43, 2.53, color=NAVY, width=1.1, arrow=True)
    s3.add_text(1.05, 3.38, 4.88, 0.42, [
        ("Raw notes stay on-site (local NLP sends only boolean flags); Vault keeps the Name ↔ ID lookup.", 8.2, False, SLATE)
    ], nowrap=True)

    # Firewall
    s3.add_line(6.24, 1.34, 6.24, 3.89, color=TERRA, width=1.3, dashed=True)
    s3.add_badge(5.98, 2.95, 0.52, 0.32, "HIPAA\nFW", fill=NAVY, fg=PEACH, size=7.2)

    # Right Zone: Cloud
    s3.add_rect(6.40, 1.34, 6.04, 2.55, fill=CARD_BG, border=BLUE, border_w=1.4, rounded=True)
    s3.add_badge(6.56, 1.44, 5.72, 0.25, "PSEUDONYMISED CLOUD ZONE · AWS US-EAST (NO NAMES, NO RAW TEXT)", fill=BLUE, fg=CARD_BG, size=8.5)

    s3.add_rect(6.56, 1.80, 1.32, 1.46, fill=MUTED_CARD, border=BORDER_DK, border_w=0.8, rounded=True)
    s3.add_text(6.61, 1.86, 1.22, 1.34, [
        ("Ingestion", 8.5, True, NAVY),
        ("MSK Serverless", 7.8, True, BLUE),
        ("(HL7 Stream)", 7.3, False, SLATE),
        ("Apache Airflow", 7.8, True, BLUE),
        ("(Billing, SNF,", 7.3, False, SLATE),
        ("SPARCS Batch)", 7.3, False, SLATE)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(8.04, 1.80, 1.36, 1.46, fill=BLUE_LT, border=BLUE, border_w=0.9, rounded=True)
    s3.add_text(8.09, 1.86, 1.26, 1.34, [
        ("S3 + Iceberg", 8.5, True, NAVY),
        ("Lakehouse", 8.0, True, BLUE),
        ("• Bronze (Raw)", 7.4, False, SLATE),
        ("• Silver (Clean)", 7.4, False, SLATE),
        ("• Gold (Star)", 7.4, False, SLATE)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(9.56, 1.80, 1.32, 1.46, fill=MUTED_CARD, border=BORDER_DK, border_w=0.8, rounded=True)
    s3.add_text(9.61, 1.86, 1.22, 1.34, [
        ("ETL & Quality", 8.5, True, NAVY),
        ("Polars (Daily)", 7.8, True, TERRA),
        ("<10s on 1 task", 7.3, False, SLATE),
        ("Glue PySpark", 7.8, True, BLUE),
        ("(6.2M Retrain)", 7.3, False, SLATE),
        ("+ 4 dbt Checks", 7.5, True, GREEN_FG)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(11.02, 1.80, 1.26, 0.68, fill=TERRA, border=TERRA, border_w=0.8, rounded=True)
    s3.add_text(11.06, 1.84, 1.18, 0.60, [
        ("06:30 Scorer", 8.2, True, CARD_BG),
        ("Top 30% (~77/d)", 7.4, False, CREAM_BG),
        ("→ On-Prem UI", 7.4, True, PEACH)
    ], align="c", valign="m", nowrap=True)

    s3.add_rect(11.02, 2.58, 1.26, 0.68, fill=NAVY, border=NAVY, border_w=0.8, rounded=True)
    s3.add_text(11.06, 2.62, 1.18, 0.60, [
        ("Redshift OLAP", 8.2, True, PEACH),
        ("Monthly KPI vs.", 7.3, False, CREAM_BG),
        ("2017 P75 Ruler", 7.3, False, LIGHT_TXT)
    ], align="c", valign="m", nowrap=True)

    s3.add_line(5.93, 2.35, 6.56, 2.35, color=BLUE, width=1.3, arrow=True)
    s3.add_line(7.88, 2.53, 8.04, 2.53, color=BLUE, width=1.1, arrow=True)
    s3.add_line(9.40, 2.53, 9.56, 2.53, color=BLUE, width=1.1, arrow=True)
    s3.add_line(10.88, 2.14, 11.02, 2.14, color=TERRA, width=1.1, arrow=True)
    s3.add_line(10.88, 2.92, 11.02, 2.92, color=NAVY, width=1.1, arrow=True)
    s3.add_text(6.56, 3.38, 5.72, 0.42, [
        ("06:30 Scorer pushes encounter_id + rank to On-Prem DB; 08:00 huddle claim syncs had_day1_planning back.", 8.2, False, SLATE)
    ], nowrap=True)

    col_w_s3 = [1.90, 2.35, 2.25, 5.05]
    row_h_s3 = [0.34, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42]
    rows_s3 = [
        ["Stage", "Our Choice", "Alternative Rejected", "Why Our Choice Fits Better"],
        ["Privacy Residency", "Hybrid On-Premise + Cloud", "All Cloud or All On-Prem", "Keeps names & notes inside hospital firewall (HIPAA) while scaling analytics in AWS."],
        ["Streaming Broker", "Amazon MSK Serverless (Kafka)", "3-Node Kafka ($600/mo) / SQS", "At 0.18 msg/s avg (30 msg/s peak), fixed brokers sit 99% idle; serverless costs ~$40/mo."],
        ["Orchestration", "Apache Airflow", "Linux cron scripts", "Manages the 06:00 → 06:30 → 07:00 dependency chain with retries and failure alerts."],
        ["Storage & Tables", "Amazon S3 + Apache Iceberg", "HDFS or plain folders", "$23/TB/mo storage with ACID MERGE updates when patients are discharged."],
        ["ETL & Scoring", "Polars (daily) + Glue PySpark", "24/7 Spark cluster", "275 daily patients (<50 MB) score in <10s on 1 container ($0.02/run) vs. 3-min Spark boot."],
        ["Serving DBs", "PostgreSQL (UI) + Redshift (BI)", "Single database for both", "Case managers need <15ms row lookups (OLTP); KPI queries scan 6.2M stays (OLAP)."]
    ]
    s3.add_table(0.89, 4.02, col_w_s3, row_h_s3, rows_s3, font_size=8.4)
    s3.add_footer("Architecture adapts the course reference pipeline (Sessions 06–08) to HIPAA privacy rules and hospital volume.")
    slides.append(s3)

    # =========================================================================
    # SLIDE 4: 3 · INGESTION STRATEGY (STREAMING VS. BATCH)
    # =========================================================================
    s4 = SlideBuilder(
        4, bg_color=CREAM_BG,
        notes=(
            "Core idea: We only stream data that the 07:00 morning worklist actually needs, and run everything else as scheduled batches. "
            "About 22% of emergency admissions arrive between midnight and 06:00 AM, so streaming ensures overnight patients are never delayed by 24 hours. "
            "Walking through the details: contrast the streaming box on the left with the three Airflow batches on the right, then trace the 24-hour timeline at the bottom."
        )
    )
    s4.add_header(
        "3 · INGESTION STRATEGY · STREAMING VS. SCHEDULED BATCH",
        "Stream overnight admissions for the 07:00 cut-off; batch post-discharge coding",
        "We do not stream everything—each source is ingested only as fast as the WP1 decision needs it."
    )

    s4.add_rect(0.89, 1.62, 5.60, 3.45, fill=CARD_BG, border=TERRA, border_w=1.3, rounded=True)
    s4.add_badge(1.09, 1.78, 5.20, 0.30, "REAL-TIME STREAMING · HL7 GATEWAY → MSK SERVERLESS", fill=TERRA, fg=CARD_BG, size=9.2)
    s4.add_text(1.09, 2.22, 5.20, 2.70, [
        ("Sources: 1. HIS / ADT,  2. ED System,  3. Nursing Intake Flags", 10.5, True, NAVY),
        ("Why streaming instead of a midnight batch:", 10.5, True, TERRA),
        ("• ~22% of emergency admissions arrive between 00:00 and 06:00 AM.\n• With a midnight batch, an overnight patient admitted at 01:30 would miss the 07:00 worklist and wait 24+ hours for a case manager.", 9.8, False, SLATE),
        ("How it handles hospital bursts:", 10.5, True, NAVY),
        ("• Partitioned by (facility_id, encounter_id) so admission and insurance updates stay in exact time order.\n• Buffers afternoon peaks (15–30 msg/s at 11:00–16:00) without slowing down the hospital EHR.", 9.8, False, SLATE)
    ], line_mult=1.24)

    s4.add_rect(6.85, 1.62, 5.59, 3.45, fill=CARD_BG, border=BLUE, border_w=1.3, rounded=True)
    s4.add_badge(7.05, 1.78, 5.19, 0.30, "SCHEDULED BATCH · APACHE AIRFLOW", fill=BLUE, fg=CARD_BG, size=9.2)
    s4.add_text(7.05, 2.22, 5.19, 2.70, [
        ("1. Nightly Incremental Batch (01:00 AM) — 4. Coding & Billing:", 10.5, True, NAVY),
        ("• Pulls newly coded stays (WHERE updated_at > last_run).\n• Why not real-time streaming? Coders assign final DRGs 5–14 days after discharge; streaming keystrokes adds database load for zero Day-1 value.", 9.6, False, SLATE),
        ("2. Morning API Poll (06:00 AM) — 5. Nursing Home Beds (uhyy-xp9s):", 10.5, True, BLUE),
        ("• Pulls open beds at ~85 regional nursing homes right before 06:30 scoring (aligned with nursing-home shift handovers).", 9.6, False, SLATE),
        ("3. Yearly Batch — 6. Public NY SPARCS & US Census:", 10.5, True, NAVY),
        ("• Runs download_sparcs.py (50,000 rows/page) and logs queries in manifest.json.", 9.6, False, SLATE)
    ], line_mult=1.24)

    s4.add_text(0.89, 5.26, 11.55, 0.24, [
        ("THE DAILY TIMELINE · FROM OVERNIGHT ADMISSION TO THE 08:00 HUDDLE", 9.5, True, NAVY, FONT_SANS, False, 100)
    ], nowrap=True)
    steps_s4 = [
        (0.89, "00:00 – 06:00", "Overnight Stream", "Admissions & ED events land in S3 Bronze (Avro).", TERRA),
        (3.84, "01:00 & 06:00", "Airflow Batches", "01:00 coded billing sync; 06:00 fresh SNF bed poll.", BLUE),
        (6.79, "06:15 – 06:30", "Clean, Test & Score", "Polars ETL + 4 dbt checks; model flags top 30% (~77–82).", NAVY),
        (9.74, "07:00 & 08:00", "Worklist & Write-Back", "07:00 EHR worklist live; 08:00 claim syncs back to lake.", GREEN_FG)
    ]
    for sx, stime, stitle, sdesc, scol in steps_s4:
        s4.add_rect(sx, 5.56, 2.70, 1.18, fill=CARD_BG, border=scol, border_w=1.1, rounded=True)
        s4.add_badge(sx + 0.14, 5.68, 1.25, 0.22, stime, fill=scol, fg=CARD_BG, size=8.0)
        s4.add_text(sx + 0.14, 5.96, 2.42, 0.24, [(stitle, 10.0, True, NAVY)], nowrap=True)
        s4.add_text(sx + 0.14, 6.22, 2.42, 0.44, [(sdesc, 8.6, False, SLATE)], line_mult=1.18)
        if sx < 9.0:
            s4.add_line(sx + 2.72, 6.15, sx + 2.93, 6.15, color=scol, width=1.3, arrow=True)

    s4.add_footer("All overnight admissions before 06:00 are scored at 06:30 and ready on the case manager's screen by 07:00.")
    slides.append(s4)

    # =========================================================================
    # SLIDE 5: 4 · RAW LAYER (BRONZE)
    # =========================================================================
    s5 = SlideBuilder(
        5, bg_color=CREAM_BG,
        notes=(
            "Core idea: The Bronze layer keeps raw data untouched in S3 using two binary formats—Avro for fast streaming writes and Parquet for compact analytics. "
            "In our workspace data folder, Parquet shrinks 6.2M hospital stays from ~1.2 GB in CSV down to just 83 MB (14× smaller). "
            "Walking through the details: compare Avro vs. Parquet at the top, then cover S3 partitioning, the 15-minute buffer against tiny files, and 7-year retention."
        )
    )
    s5.add_header(
        "4 · RAW LAYER (BRONZE) · FILE FORMATS, PARTITIONS & RETENTION",
        "Row-based Avro for fast stream appends; columnar Parquet for 14× smaller scans",
        "All incoming data are saved unchanged in s3://flhs-bronze/. We use two binary formats and avoid plain CSV or JSON."
    )

    s5.add_rect(0.89, 1.62, 5.60, 2.95, fill=CARD_BG, border=TERRA, border_w=1.3, rounded=True)
    s5.add_badge(1.09, 1.78, 5.20, 0.28, "APACHE AVRO · ROW-BASED BINARY (FOR STREAMS)", fill=TERRA, fg=CARD_BG, size=9.0)
    s5.add_text(1.09, 2.18, 5.20, 2.25, [
        ("Used for: Kafka streams (HIS/ADT, EDIS, Nursing Note flags).", 10.0, True, NAVY),
        ("• Fast stream writes: Events arrive one patient at a time. Because Avro is row-based, Kafka flushes micro-batches straight to disk without reorganising into columns.", 9.5, False, SLATE),
        ("• Schema evolution: Stores the schema in the file header so hospital EHR upgrades never break the pipeline.", 9.5, False, SLATE),
        ("• Why not JSON? JSON repeats column names on every row (3–5× larger) and has no strict types.", 9.5, True, TERRA)
    ], line_mult=1.22)

    s5.add_rect(6.85, 1.62, 5.59, 2.95, fill=CARD_BG, border=BLUE, border_w=1.3, rounded=True)
    s5.add_badge(7.05, 1.78, 5.19, 0.28, "APACHE PARQUET (ZSTD) · COLUMNAR BINARY (FOR BATCH & ANALYTICS)", fill=BLUE, fg=CARD_BG, size=9.0)
    s5.add_text(7.05, 2.18, 5.19, 2.25, [
        ("Used for: Batch feeds (Billing, SPARCS, SNF Beds) + all Silver & Gold tables.", 10.0, True, NAVY),
        ("• 14× smaller than CSV: Hospital columns repeat values ('Finger Lakes', 'Medicare'). Parquet shrinks our 6,228,309 NY stays in ./data/ from ~1.2 GB CSV to just 83 MB (~13.9 bytes/stay).", 9.5, False, SLATE),
        ("• Fast analytical reads: Queries read only needed columns and skip blocks via footer min/max stats.", 9.5, False, SLATE),
        ("• Why not CSV? Loses data types ('120 +' text) and scans every column of every row.", 9.5, True, BLUE)
    ], line_mult=1.22)

    bot_cards_s5 = [
        (0.89, NAVY, "PARTITIONING ON S3",
         "By source, hospital & date",
         "source=<name>/facility_id=<id>/\nyear=YYYY/month=MM/day=DD/\n\n• Morning jobs read only today's folder.\n• Re-running one hospital never scans the other 16."),
        (4.84, TERRA, "15-MIN / 64 MB BUFFER",
         "Avoids the 'small-files problem'",
         "Kafka buffers stream events for 15 min before writing an Avro file.\n\n• 10-sec flushes would create millions of tiny files.\n• 1-hr flushes would delay data past the 06:00 cut-off."),
        (8.79, BLUE, "7-YEAR RETENTION POLICY",
         "Hot replay + $1/TB/yr archive",
         "• 0–90 Days: S3 Standard ($23/TB/mo) for quick re-runs if an ETL bug is found.\n• 90 Days–7 Years: S3 Glacier Deep Archive (~$1/TB/yr) to meet NY medical audit rules.")
    ]
    for bx, bcol, bkicker, btitle, bbody in bot_cards_s5:
        s5.add_rect(bx, 4.78, 3.65, 1.96, fill=CARD_BG, border=bcol, border_w=1.1, rounded=True)
        s5.add_text(bx + 0.20, 4.92, 3.25, 0.22, [(bkicker, 8.6, True, bcol, FONT_SANS, False, 80)], nowrap=True)
        s5.add_text(bx + 0.20, 5.16, 3.25, 0.28, [(btitle, 12.0, True, NAVY, FONT_SERIF)], nowrap=True)
        s5.add_text(bx + 0.20, 5.48, 3.25, 1.18, [(bbody, 9.0, False, SLATE, FONT_SANS)], line_mult=1.20)

    s5.add_footer("Real storage measurement: ./WP1/data/B_stays_statewide_2017..2023.parquet = 6,228,309 stays in 83 MB total.")
    slides.append(s5)

    # =========================================================================
    # SLIDE 6: 5 · SILVER ETL & BEFORE -> AFTER EXAMPLE
    # =========================================================================
    s6 = SlideBuilder(
        6, bg_color=CREAM_BG,
        notes=(
            "Core idea: Silver ETL turns messy hospital messages into clean records while blocking future discharge data from leaking into Day-1 predictions. "
            "Every stay is cleanly split at 06:00 AM into Day-1 inputs vs. post-discharge outcomes. "
            "Walking through the details: go through the 5 rules on the left, then show the concrete Before/After example for patient SMH-8841 and the Polars snippet."
        )
    )
    s6.add_header(
        "5 · SILVER ETL · CTO QUESTION #3 (HOW ARE THE DATA TRANSFORMED?)",
        "Five rules clean the data and separate Day-1 inputs from outcomes"
    )

    rules_s6 = [
        ("1 · Unify patient ID across the 17 hospitals (EMPI)",
         "Links visits across Strong Memorial, Highland, etc. to one hashed master_patient_id to track 30-day readmissions."),
        ("2 · Deduplicate update messages (ADT^A08)",
         "Keeps the latest message per stay and saves two clean snapshots: what was known at 06:00 on Day 1 and the latest state."),
        ("3 · Standardise codes & extract social flags from notes",
         "Maps local insurance names to the 10 SPARCS payers; turns intake notes into lives_alone_flag & prior_nursing_home_flag."),
        ("4 · Apply WP1 adult med-surg scope & impute missing values",
         "Applies download_sparcs.py Rules 1–5 (flags deaths/transfers kpi_eligible=False). Fills missing payer with 'Pending' + is_imputed=True instead of dropping patients."),
        ("5 · Strict anti-leakage split (Fixed 06:00 AM cut-off)",
         "Splits stays into silver_stay_day1 (inputs known by 06:00 Day 1) and silver_stay_discharged (post-discharge LOS, final DRG, disposition, costs).")
    ]
    ry = 1.34
    for rtitle, rdesc in rules_s6:
        s6.add_rect(0.89, ry, 5.55, 1.02, fill=CARD_BG, border=BORDER_DK, border_w=0.9, rounded=True)
        s6.add_line(0.95, ry + 0.08, 0.95, ry + 0.94, color=TERRA if "5 ·" in rtitle else BLUE, width=2.8)
        s6.add_text(1.12, ry + 0.08, 5.20, 0.24, [(rtitle, 9.8, True, NAVY)], nowrap=True)
        s6.add_text(1.12, ry + 0.34, 5.20, 0.62, [(rdesc, 8.6, False, SLATE)], line_mult=1.18)
        ry += 1.10

    s6.add_text(6.68, 1.32, 5.76, 0.24, [
        ("BEFORE (RAW BRONZE) → AFTER (CURATED SILVER) · ONE STAY", 9.2, True, TERRA, FONT_SANS, False, 80)
    ], nowrap=True)
    col_w_s6 = [1.15, 2.20, 2.41]
    row_h_s6 = [0.32, 0.52, 0.52, 0.54, 0.56]
    rows_s6 = [
        ["Field", "Before: Raw (Bronze)", "After: Curated (Silver)"],
        ["Stay & ID", "local_mrn = 'SMH-8841'\nmsg_id = 'ADT_A08_2'", "encounter_id = 'enc_9f3a'\nmaster_patient_id = 'pat_4c12'"],
        ["Payer", "'  excellus medicaid pending '", "payment_typology_1 = 'Medicaid'\npayer_is_imputed = False"],
        ["Intake Note", "'79yo F, lives alone on 2nd fl,\ndenies prior SNF'", "lives_alone_flag = True\nprior_nursing_home_flag = False"],
        ["LOS & Ruler", "length_of_stay = '120 +'\n(DRG 194, Severity 3)", "los = 120, los_capped = True\np75_used = 6 → excess_bed_days = 114"]
    ]
    s6.add_table(6.68, 1.60, col_w_s6, row_h_s6, rows_s6, font_size=8.3)

    s6.add_rect(6.68, 4.20, 5.76, 2.56, fill=NAVY, border=NAVY_LINE, border_w=1.0, rounded=True)
    s6.add_badge(6.84, 4.30, 2.90, 0.22, "POLARS TRANSFORMATION SNIPPET", fill=TERRA, fg=CARD_BG, size=7.8)
    code_lines = (
        "silver_df = (\n"
        "  pl.read_parquet('s3://flhs-bronze/stays/*.parquet')\n"
        "  .sort('event_ts').unique(subset=['encounter_id'], keep='last')\n"
        "  .with_columns([\n"
        "    pl.col('payment_typology_1').str.strip_chars().str.to_lowercase()\n"
        "      .replace(PAYER_MAP, default='Pending').alias('payment_typology_1'),\n"
        "    pl.col('length_of_stay').str.contains(r'\\+').alias('los_capped'),\n"
        "    pl.col('length_of_stay').str.replace('+','').str.strip_chars()\n"
        "      .cast(pl.Int32).alias('los'),\n"
        "  ])\n"
        "  .join(ruler_2017, on=['apr_drg_code', 'apr_severity_of_illness_code'], how='left')\n"
        "  .with_columns(\n"
        "    pl.max_horizontal(0, pl.col('los') - pl.col('p75_used')).alias('excess_bed_days')\n"
        "  )\n"
        ")"
    )
    s6.add_text(6.84, 4.58, 5.48, 2.10, [(code_lines, 7.4, False, CREAM_BG, FONT_MONO)], line_mult=1.14, nowrap=True)

    s6.add_footer("Silver tables use Apache Iceberg on S3, keeping both the 06:00 Day-1 snapshot and the final discharged stay.")
    slides.append(s6)

    # =========================================================================
    # SLIDE 7: 6A · STAR SCHEMA, INDEXING & WRITE-BACK LOOP
    # =========================================================================
    s7 = SlideBuilder(
        7, bg_color=CREAM_BG,
        notes=(
            "Core idea: One Star Schema powers both fast morning lookups for nurses and historical analytics, plus an 08:00 feedback loop. "
            "PostgreSQL serves the 07:00 worklist in under 15 ms, Redshift tracks monthly excess bed-days against the frozen 2017 P75 ruler, and case-manager claims sync back to the lake. "
            "Walking through the details: show the 2 Fact tables and 4 Dimensions on the left, then explain the indexing and 08:00 write-back boxes on the right."
        )
    )
    s7.add_header(
        "6A · PERSISTENCE & DATA MODEL · STAR SCHEMA, INDEXING & WRITE-BACK",
        "One Star Schema across two databases, closed by an 08:00 write-back loop"
    )

    s7.add_rect(0.89, 1.34, 6.15, 5.42, fill=CARD_BG, border=BORDER_DK, border_w=1.0, rounded=True)
    s7.add_text(1.09, 1.44, 5.75, 0.24, [
        ("GOLD STAR SCHEMA (2 FACT TABLES · 4 DIMENSIONS)", 9.0, True, NAVY, FONT_SANS, False, 80)
    ], nowrap=True)

    s7.add_rect(1.05, 1.82, 1.72, 1.32, fill=MUTED_CARD, border=BORDER_DK, border_w=0.9, rounded=True)
    s7.add_badge(1.13, 1.90, 1.56, 0.22, "DIM_FACILITY", fill=NAVY, fg=CARD_BG, size=7.8)
    s7.add_text(1.13, 2.16, 1.56, 0.90, [
        ("PK permanent_facility_id", 7.4, True, NAVY, FONT_MONO),
        ("facility_name\nhospital_service_area\nbusiness_case_system", 7.3, False, SLATE, FONT_MONO)
    ], line_mult=1.18, nowrap=True)

    s7.add_rect(1.05, 3.38, 1.72, 1.52, fill=MUTED_CARD, border=BORDER_DK, border_w=0.9, rounded=True)
    s7.add_badge(1.13, 3.46, 1.56, 0.22, "DIM_PATIENT", fill=NAVY, fg=CARD_BG, size=7.8)
    s7.add_text(1.13, 3.72, 1.56, 1.12, [
        ("PK master_patient_id", 7.4, True, NAVY, FONT_MONO),
        ("age_group · gender\nzip_code_3_digits\ncensus_deprivation_decile\nrace · ethnicity", 7.3, False, SLATE, FONT_MONO)
    ], line_mult=1.18, nowrap=True)

    s7.add_rect(1.05, 5.14, 1.72, 1.40, fill=MUTED_CARD, border=BORDER_DK, border_w=0.9, rounded=True)
    s7.add_badge(1.13, 5.22, 1.56, 0.22, "DIM_DATE", fill=NAVY, fg=CARD_BG, size=7.8)
    s7.add_text(1.13, 5.48, 1.56, 0.98, [
        ("PK calendar_date", 7.4, True, NAVY, FONT_MONO),
        ("year · month\nday_of_week\nis_weekend", 7.3, False, SLATE, FONT_MONO)
    ], line_mult=1.18, nowrap=True)

    s7.add_rect(3.05, 1.76, 2.15, 2.36, fill=TERRA_LT, border=TERRA, border_w=1.3, rounded=True)
    s7.add_badge(3.15, 1.84, 1.95, 0.24, "FCT_DAY1_WORKLIST", fill=TERRA, fg=CARD_BG, size=8.0)
    s7.add_text(3.15, 2.12, 1.95, 1.94, [
        ("PK encounter_id", 7.5, True, TERRA, FONT_MONO),
        ("FK master_patient_id\nFK permanent_facility_id\nFK provisional_drg_sev_key", 7.2, True, NAVY, FONT_MONO),
        ("admit_ts · type_of_admission\nemergency_dept_indicator\npayment_typology_1\nlives_alone · prior_snf_flag\nopen_snf_beds_nearby\npredicted_excess_days\ndaily_hospital_rank\ncase_manager_status", 7.1, False, SLATE, FONT_MONO)
    ], line_mult=1.13, nowrap=True)

    s7.add_rect(3.05, 4.30, 2.15, 2.28, fill=BLUE_LT, border=BLUE, border_w=1.3, rounded=True)
    s7.add_badge(3.15, 4.38, 1.95, 0.24, "FCT_COMPLETED_STAY", fill=BLUE, fg=CARD_BG, size=8.0)
    s7.add_text(3.15, 4.66, 1.95, 1.86, [
        ("PK encounter_id", 7.5, True, BLUE, FONT_MONO),
        ("FK master_patient_id\nFK permanent_facility_id\nFK final_drg_sev_key\nFK discharge_date", 7.2, True, NAVY, FONT_MONO),
        ("los · los_capped · p75_used\nexcess_bed_days\nkpi_eligible\nhad_day1_planning (08:00)\npatient_disposition · costs", 7.1, False, SLATE, FONT_MONO)
    ], line_mult=1.14, nowrap=True)

    s7.add_rect(5.38, 2.90, 1.54, 2.40, fill=MUTED_CARD, border=NAVY, border_w=1.0, rounded=True)
    s7.add_badge(5.45, 2.98, 1.40, 0.24, "DIM_DRG_RULER", fill=NAVY, fg=PEACH, size=7.5)
    s7.add_text(5.45, 3.28, 1.40, 1.94, [
        ("PK drg_sev_key", 7.4, True, NAVY, FONT_MONO),
        ("apr_drg_code\napr_drg_desc\napr_severity (1..4)\napr_mdc_code\nn_ref_2017\np75_used (Frozen)\nthin_cell (<30)", 7.2, False, SLATE, FONT_MONO)
    ], line_mult=1.18, nowrap=True)

    s7.add_line(2.77, 2.40, 3.05, 2.40, color=NAVY, width=1.0, arrow=True)
    s7.add_line(2.77, 2.60, 3.05, 4.70, color=NAVY, width=0.9, arrow=True)
    s7.add_line(2.77, 3.90, 3.05, 3.20, color=NAVY, width=0.9, arrow=True)
    s7.add_line(2.77, 4.15, 3.05, 5.00, color=NAVY, width=1.0, arrow=True)
    s7.add_line(2.77, 5.80, 3.05, 5.80, color=NAVY, width=1.0, arrow=True)
    s7.add_line(5.38, 3.55, 5.20, 3.05, color=TERRA, width=1.0, arrow=True)
    s7.add_line(5.38, 4.45, 5.20, 5.05, color=BLUE, width=1.0, arrow=True)
    s7.add_line(4.12, 4.12, 4.12, 4.30, color=GREEN_FG, width=1.2, dashed=True, arrow=True)

    s7.add_rect(7.24, 1.34, 5.20, 1.68, fill=CARD_BG, border=TERRA, border_w=1.1, rounded=True)
    s7.add_badge(7.42, 1.46, 4.84, 0.24, "ON-PREM POSTGRESQL · FCT_DAY1_WORKLIST", fill=TERRA, fg=CARD_BG, size=8.4)
    s7.add_text(7.42, 1.78, 4.84, 1.16, [
        ("• B-Tree Index on (permanent_facility_id, admit_ts, daily_hospital_rank): Loads each hospital's morning worklist in <15 ms for 45 case managers.", 9.0, False, SLATE),
        ("• 06:30 Upsert: INSERT ... ON CONFLICT (encounter_id) DO UPDATE flags the top 30% (~77–82 patients/day).", 9.0, False, SLATE)
    ], line_mult=1.20)

    s7.add_rect(7.24, 3.16, 5.20, 1.72, fill=CARD_BG, border=BLUE, border_w=1.1, rounded=True)
    s7.add_badge(7.42, 3.28, 4.84, 0.24, "CLOUD REDSHIFT & ICEBERG · FCT_COMPLETED_STAY", fill=BLUE, fg=CARD_BG, size=8.4)
    s7.add_text(7.42, 3.60, 4.84, 1.20, [
        ("• Partition & Sort Key: Partitioned by discharge_year and sorted by (facility, DRG, severity) to skip irrelevant blocks (Zone Maps).", 9.0, False, SLATE),
        ("• Nightly MERGE INTO on encounter_id as billed stays arrive.", 9.0, False, SLATE)
    ], line_mult=1.20)

    s7.add_rect(7.24, 5.02, 5.20, 1.74, fill=NAVY, border=NAVY, border_w=1.1, rounded=True)
    s7.add_badge(7.42, 5.14, 4.84, 0.24, "CLOSING THE LOOP · 08:00 CASE MANAGER WRITE-BACK", fill=GREEN_FG, fg=CARD_BG, size=8.4)
    s7.add_text(7.42, 5.46, 4.84, 1.22, [
        ("• At 08:00, when a case manager takes a flagged patient on the EHR screen, PostgreSQL records case_manager_status = 'CLAIMED_DAY1'.", 8.8, False, CREAM_BG),
        ("• Syncs back to set had_day1_planning = True in FCT_COMPLETED_STAY—tracking our WP1 Leading Indicator (% of flagged patients started on Day 1).", 8.8, True, PEACH)
    ], line_mult=1.20)

    s7.add_footer("DIM_DRG_RULER is frozen on the 2017 NY reference year so the KPI benchmark never drifts.")
    slides.append(s7)

    # =========================================================================
    # SLIDE 8: 6B · GOLD DATA DICTIONARY
    # =========================================================================
    s8 = SlideBuilder(
        8, bg_color=CREAM_BG,
        notes=(
            "Core idea: This table is our anti-leakage contract—every Gold column is explicitly tagged by when it becomes available. "
            "Green fields are known at admission for scoring; blue fields come from the 06:30 model and 08:00 claim; amber is the static 2017 benchmark; red fields exist only after discharge. "
            "Walking through the details: highlight one example per color (e.g., lives_alone vs. had_day1_planning vs. excess_days) and note that race/ethnicity are kept only for fairness audits."
        )
    )
    s8.add_header(
        "6B · PERSISTENCE · GOLD DATA DICTIONARY & ANTI-LEAKAGE CONTRACT",
        "Every Gold column is tagged by source and Day-1 anti-leakage status"
    )

    s8.add_badge(0.89, 1.26, 2.65, 0.24, "YES · DAY-1 SAFE INPUT", fill=GREEN_BG, fg=GREEN_FG, size=8.2)
    s8.add_badge(3.68, 1.26, 2.75, 0.24, "06:30 SCORE / 08:00 WRITE-BACK", fill=BLUE_LT, fg=BLUE, size=8.2)
    s8.add_badge(6.57, 1.26, 2.65, 0.24, "STATIC 2017 RULER", fill=AMBER_BG, fg=AMBER_FG, size=8.2)
    s8.add_badge(9.36, 1.26, 3.08, 0.24, "NO · POST-DISCHARGE TARGET ONLY", fill=TERRA_LT, fg=TERRA, size=8.2)

    col_w_s8 = [2.40, 1.75, 0.80, 1.85, 1.35, 3.40]
    row_h_s8 = [0.32] + [0.305] * 16
    rows_s8 = [
        ["Column", "Table(s)", "Type", "Source", "Known Day 1?", "Role & Validation Rule"],
        ["encounter_id", "Both Facts", "STRING", "HIS / ADT", "YES (PK)", "Primary key (1 row = 1 stay). NOT NULL, Unique."],
        ["master_patient_id", "Facts, DIM_PATIENT", "STRING", "HIS (EMPI)", "YES (FK)", "Hashed patient ID across 17 hospitals (tracks readmissions)."],
        ["permanent_facility_id", "Facts, DIM_FACILITY", "STRING", "HIS / SPARCS", "YES (FK)", "6-digit NY hospital ID (e.g. 000413 Strong Memorial)."],
        ["admit_ts / discharge_date", "Facts, DIM_DATE", "TS/DATE", "HIS / ADT", "Admit: YES", "Exact admission hour & discharge date (fixes SPARCS gap)."],
        ["age_group, gender, zip_3", "DIM_PATIENT", "STRING", "HIS / SPARCS", "YES", "Patient demographics at admission (age_group != '0 to 17')."],
        ["census_deprivation_decile", "DIM_PATIENT", "INT", "US Census ADI", "YES", "Neighbourhood deprivation score (1..10) from 3-digit ZIP."],
        ["type_of_admission", "FCT_DAY1_WORKLIST", "STRING", "HIS / ADT", "YES", "Emergency, Urgent, Elective, Trauma (Newborn excluded)."],
        ["emergency_dept_indicator", "FCT_DAY1_WORKLIST", "STRING", "ED System", "YES", "'Y' if admitted through the ED, 'N' otherwise."],
        ["payment_typology_1", "FCT_DAY1_WORKLIST", "STRING", "HIS / ADT", "YES", "Primary payer (Medicare, Medicaid, Private, etc.)."],
        ["provisional_drg_sev_key", "FCT_DAY1_WORKLIST", "STRING", "ED System", "YES (FK)", "Working diagnosis & triage severity (1..4) at admission."],
        ["lives_alone, prior_snf_flag", "FCT_DAY1_WORKLIST", "BOOL", "EHR Notes", "YES", "Extracted on-prem from Day-1 nursing intake note."],
        ["open_snf_beds_nearby", "FCT_DAY1_WORKLIST", "INT", "SNF Bed API", "YES", "Open regional nursing-home beds accepting payer at 06:00."],
        ["predicted_excess_days, rank", "FCT_DAY1_WORKLIST", "FLT/INT", "06:30 Scorer", "06:30 SCORE", "Model score & hospital rank (1..N); flags top 30% (~77–82/d)."],
        ["had_day1_planning", "FCT_COMPLETED_STAY", "BOOL", "08:00 EHR UI", "08:00 LOOP", "True when case manager claims patient on Day 1 (Leading KPI)."],
        ["p75_used, thin_cell", "DIM_DRG_RULER", "INT/BOOL", "2017 SPARCS", "STATIC RULER", "Frozen 2017 NY P75 stay for DRG × severity (fallback n < 30)."],
        ["los, excess_days, disp, costs", "FCT_COMPLETED_STAY", "INT/FLT", "Billing / Derived", "NO (TARGET)", "Post-discharge outcomes: MAX(0, los - p75_used). Never Day-1 input."]
    ]
    fills_s8, tcols_s8 = {}, {}
    for r_i in range(1, 13):
        fills_s8[(r_i, 4)], tcols_s8[(r_i, 4)] = GREEN_BG, GREEN_FG
    for r_i in [13, 14]:
        fills_s8[(r_i, 4)], tcols_s8[(r_i, 4)] = BLUE_LT, BLUE
    fills_s8[(15, 4)], tcols_s8[(15, 4)] = AMBER_BG, AMBER_FG
    fills_s8[(16, 4)], tcols_s8[(16, 4)] = TERRA_LT, TERRA

    s8.add_table(0.89, 1.58, col_w_s8, row_h_s8, rows_s8, font_size=7.9,
                 cell_fills=fills_s8, cell_text_colors=tcols_s8,
                 alignments=["l", "l", "c", "l", "c", "l"])
    s8.add_footer("Note: race & ethnicity in DIM_PATIENT are used only for fairness checks across patient groups—never as model inputs.")
    slides.append(s8)

    # =========================================================================
    # SLIDE 9: 7 · SCALABILITY, SIZING & FINOPS
    # =========================================================================
    s9 = SlideBuilder(
        9, bg_color=CREAM_BG,
        notes=(
            "Core idea: Because 17 hospitals generate under 50 MB/day (~77–82 flagged patients), we avoid expensive 24/7 clusters and run serverless for ~$600–$900/month. "
            "That is under 0.06% of the $17.5M net annual savings from WP1, while still scaling smoothly to all ~200 NY hospitals. "
            "Walking through the details: compare Finger Lakes vs. Statewide volumes in the table, point out the FinOps card, and explain the 3 sizing cards (MSK Serverless, 1 Polars container, Glue PySpark)."
        )
    )
    s9.add_header(
        "7 · SCALABILITY, INFRASTRUCTURE SIZING & FINOPS",
        "Right-sized serverless compute runs all 17 hospitals for ~$750 a month"
    )

    col_w_s9 = [2.55, 1.80, 1.80]
    row_h_s9 = [0.36, 0.46, 0.48, 0.48, 0.46, 0.48, 0.46, 0.48]
    rows_s9 = [
        ["Measure", "Finger Lakes (17 Hospitals)", "All NY State (~200 Hospitals)"],
        ["Total admissions", "137,867 / yr (~380/day)", "2,125,754 / yr (~5,800/day)"],
        ["Adult stays scored on Day 1", "99,880 / yr (~275/day)", "1,471,788 / yr (~4,030/day)"],
        ["KPI-eligible stays (excl. deaths)", "94,132 / yr (~258/day)", "1,390,226 / yr (~3,810/day)"],
        ["Top 30% flagged on worklist", "~77–82 patients / day", "~1,140–1,210 / day"],
        ["HL7 stream (avg / peak)", "~15k/d (0.18/s · 30/s peak)", "~225k/d (2.6/s · 300/s peak)"],
        ["Daily new data volume", "~50 MB / day (~18 GB/yr)", "~750 MB / day (~270 GB/yr)"],
        ["4-yr historical stays (./data/)", "434,465 rows (~6 MB Parquet)", "6,228,309 rows (83 MB Parquet)"]
    ]
    s9.add_table(0.89, 1.34, col_w_s9, row_h_s9, rows_s9, font_size=8.4)

    s9.add_rect(0.89, 5.14, 6.15, 1.62, fill=NAVY, border=NAVY, border_w=1.0, rounded=True)
    s9.add_text(1.09, 5.26, 5.75, 0.22, [
        ("TOTAL CLOUD COST · FINGER LAKES (17 HOSPITALS)", 8.6, True, PEACH, FONT_SANS, False, 90)
    ], nowrap=True)
    s9.add_text(1.09, 5.52, 2.85, 0.44, [
        ("~$600 – $900 / mo", 19.5, True, CREAM_BG, FONT_SERIF)
    ], nowrap=True)
    s9.add_text(4.15, 5.52, 2.75, 0.44, [
        ("~$10k / yr  (< 0.06% of WP1's\n$17.5M / yr net savings)", 9.4, True, PEACH, FONT_SANS)
    ], nowrap=True)
    s9.add_text(1.09, 6.08, 5.75, 0.56, [
        ("S3 + Glacier (~$30/mo) · MSK Serverless (~$40/mo) · Fargate Polars + Airflow (~$180/mo) · Redshift + Glue (~$450/mo).", 8.4, False, LIGHT_TXT)
    ], nowrap=True)

    scale_cards = [
        (1.34, TERRA, "1 · STREAMING (<0.2 MSG/S AVG, 30 MSG/S PEAK)",
         "MSK Serverless instead of 3 fixed Kafka nodes",
         "• 17 hospitals send only ~15,000 messages/day with afternoon bursts.\n• A fixed 3-node cluster ($600+/mo) would sit 99% idle; MSK Serverless handles peaks for ~$40/mo and scales to 300 msg/s statewide."),
        (3.20, BLUE, "2 · DAILY 06:30 SCORING (~275 PATIENTS, <50 MB)",
         "Scale UP on 1 Polars container (<10 seconds)",
         "• Scoring 275 patients fits easily in memory on one small container (4 vCPU, 16 GB RAM) running Polars + LightGBM ($0.02/run).\n• Avoids paying for a 24/7 Spark cluster that takes minutes just to start."),
        (5.06, NAVY, "3 · YEARLY RETRAINING (6.2M – 20M+ ROWS)",
         "Scale OUT on demand with AWS Glue (PySpark)",
         "• Spins up 10 serverless PySpark workers only when retraining on multi-year statewide history.\n• Broadcasts DIM_DRG_RULER (16 KB) & DIM_FACILITY (<50 KB) in memory, then shuts down to $0.")
    ]
    for sy, scol, skicker, stitle, sbody in scale_cards:
        s9.add_rect(7.28, sy, 5.16, 1.70, fill=CARD_BG, border=scol, border_w=1.2, rounded=True)
        s9.add_text(7.46, sy + 0.12, 4.80, 0.20, [(skicker, 8.3, True, scol, FONT_SANS, False, 70)], nowrap=True)
        s9.add_text(7.46, sy + 0.36, 4.80, 0.26, [(stitle, 11.2, True, NAVY, FONT_SERIF)], nowrap=True)
        s9.add_text(7.46, sy + 0.66, 4.80, 0.94, [(sbody, 8.8, False, SLATE, FONT_SANS)], line_mult=1.20)

    s9.add_footer("Compute sizing follows Session 07 rules: single-node Polars for <10 GB daily jobs; distributed PySpark for multi-year backfills.")
    slides.append(s9)

    # =========================================================================
    # SLIDE 10: 8 · GOVERNANCE, QUALITY TESTS & KNOWN LIMITATIONS
    # =========================================================================
    s10 = SlideBuilder(
        10, bg_color=CREAM_BG,
        notes=(
            "Core idea: Four automated dbt tests at 06:15 guard the morning worklist before nurses see it, while we stay transparent about three real-world limits. "
            "The checks verify uniqueness, completeness, validity, and freshness (data up to 05:30 AM arrived), alongside a full Data Catalogue card. "
            "Walking through the details: explain the 4 checks and Catalogue card on top, then how WP2 closes all 6 SPARCS gaps and mitigates diagnosis drift, early-morning note lag, and out-of-region stays."
        )
    )
    s10.add_header(
        "8 · GOVERNANCE, QUALITY TESTS & KNOWN DEFECTS",
        "Four automated dbt checks and three known production limits"
    )

    s10.add_rect(0.89, 1.34, 6.10, 2.38, fill=CARD_BG, border=GREEN_FG, border_w=1.2, rounded=True)
    s10.add_badge(1.07, 1.46, 5.74, 0.24, "4 AUTOMATED DBT QUALITY CHECKS (RUN AT 06:15 BEFORE SCORING)", fill=GREEN_FG, fg=CARD_BG, size=8.3)
    s10.add_text(1.07, 1.78, 5.74, 1.84, [
        ("1. Uniqueness: encounter_id unique in both Facts; (DRG, severity) unique in DIM_DRG_RULER.", 8.8, False, SLATE),
        ("2. Completeness: facility, admit_ts, age, and admission type NOT NULL; alerts IT if any major hospital sends 0 overnight admissions.", 8.8, False, SLATE),
        ("3. Validity & Anti-Leakage: severity IN {1..4}; age != '0 to 17'; no feature recorded after 06:00 Day 1.", 8.8, False, SLATE),
        ("4. Freshness: MAX(admit_ts) >= 05:30 AM across main ED hubs before 06:30 scoring starts.", 8.8, True, NAVY)
    ], line_mult=1.20)

    s10.add_rect(7.20, 1.34, 5.24, 2.38, fill=NAVY, border=NAVY, border_w=1.2, rounded=True)
    s10.add_badge(7.38, 1.46, 4.88, 0.24, "DATA CATALOGUE ENTRY · GOLD.FCT_DAY1_WORKLIST", fill=PEACH, fg=NAVY, size=8.3)
    s10.add_text(7.38, 1.80, 4.88, 1.82, [
        ("• Owner: Director of Patient Flow · Data Platform Team", 8.7, True, CREAM_BG),
        ("• Grain: 1 row per adult admission (~275/day; top 30% = ~77–82 flagged)", 8.5, False, LIGHT_TXT),
        ("• Refresh SLA: Daily at 06:30 AM (ready before 07:00 shift start)", 8.5, False, LIGHT_TXT),
        ("• Privacy Tag: PSEUDONYMISED in Cloud · PHI_RESTRICTED On-Premise", 8.5, True, PEACH),
        ("• Lineage: HIS/ADT + EDIS + Notes + SNF API → silver_stay_day1 → LightGBM", 8.5, False, LIGHT_TXT),
        ("• Quality Status: 4 / 4 Automated dbt Checks Passing (Freshness < 30 min)", 8.6, True, "7CE3A3")
    ], line_mult=1.20)

    s10.add_rect(0.89, 3.86, 6.10, 2.92, fill=CARD_BG, border=BLUE, border_w=1.2, rounded=True)
    s10.add_badge(1.07, 3.96, 5.74, 0.24, "HOW WP2 SOLVES ALL 6 PUBLIC SPARCS GAPS FROM WP1", fill=BLUE, fg=CARD_BG, size=8.3)
    col_w_s10 = [2.45, 3.29]
    row_h_s10 = [0.28, 0.36, 0.36, 0.38, 0.36, 0.38, 0.36]
    rows_s10 = [
        ["Public SPARCS Gap (WP1)", "How WP2 Fixes It in Production"],
        ["1. No patient ID", "Linked across 17 hospitals via master_patient_id (EMPI)."],
        ["2. No dates, only year", "Exact admit_ts & discharge_date from HIS/ADT."],
        ["3. DRG coded at discharge", "Uses ED provisional diagnosis on Day 1."],
        ["4. '120 +' cap & hidden IDs", "Internal HIS keeps exact LOS & hospital ID."],
        ["5. No social factors", "Extracted from Day-1 nursing note + Census ZIP score."],
        ["6. No bed or SNF census", "Live ward events + 06:00 NY SNF bed API poll."]
    ]
    s10.add_table(1.07, 4.24, col_w_s10, row_h_s10, rows_s10, font_size=7.9)

    s10.add_rect(7.20, 3.86, 5.24, 2.92, fill=CARD_BG, border=TERRA, border_w=1.2, rounded=True)
    s10.add_badge(7.38, 3.96, 4.88, 0.24, "KNOWN LIMITS OF THE NEW SYSTEM (& MITIGATIONS)", fill=TERRA, fg=CARD_BG, size=8.3)
    s10.add_text(7.38, 4.30, 4.88, 2.38, [
        ("1. Provisional vs. final diagnosis drift (~15–20% of complex stays):", 9.0, True, NAVY),
        ("• The ED doctor's Day-1 diagnosis can change if complications arise later.\n• Mitigation: Re-score in-house patients on Day 3 if a new diagnosis or ICU transfer is logged.", 8.5, False, SLATE),
        ("2. Late-night nursing note lag (05:00–06:00 AM arrivals):", 9.0, True, NAVY),
        ("• Intake notes for 05:30 arrivals may not be typed by 06:30. Mitigation: Flag as is_imputed = True and score from ED/ADT data first.", 8.5, False, SLATE),
        ("3. Regional boundary of patient ID (17 Finger Lakes hospitals):", 9.0, True, NAVY),
        ("• Tracks readmissions across the 17 regional hospitals, but cannot see stays outside the region.", 8.5, False, SLATE)
    ], line_mult=1.18)

    s10.add_footer("Governance and quality checks follow Session 07 (Slides 26 & 92) and Session 08 healthcare standards.")
    slides.append(s10)

    return slides


def make_notes_xml(slide_num: int, notes_text: str) -> str:
    esc_txt = escape(notes_text)
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<p:notes xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
        '<p:cSld><p:spTree>'
        '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
        '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        '<p:sp><p:nvSpPr><p:cNvPr id="2" name="Slide Image Placeholder 1"/><p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldImg"/></p:nvPr></p:nvSpPr><p:spPr/></p:sp>'
        '<p:sp><p:nvSpPr><p:cNvPr id="3" name="Notes Placeholder 2"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr><p:spPr/>'
        f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="en-US" dirty="0"/><a:t>{esc_txt}</a:t></a:r><a:endParaRPr lang="en-US" dirty="0"/></a:p></p:txBody></p:sp>'
        '<p:sp><p:nvSpPr><p:cNvPr id="4" name="Slide Number Placeholder 3"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr><p:nvPr><p:ph type="sldNum" sz="quarter" idx="10"/></p:nvPr></p:nvSpPr><p:spPr/>'
        f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:fld id="{{F7021451-1387-4CA6-816F-3879F97B5CBC}}" type="slidenum"><a:rPr lang="en-US"/><a:t>{slide_num}</a:t></a:fld><a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>'
        '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>'
    )


def make_slide_rels_xml(slide_num: int) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout2.xml"/>'
        f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide" Target="../notesSlides/notesSlide{slide_num}.xml"/>'
        '</Relationships>'
    )


def export_pptx(slides, template_pptx: str, out_pptx: str):
    with zipfile.ZipFile(template_pptx, "r") as zin:
        with zipfile.ZipFile(out_pptx, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                fname = item.filename
                if fname.startswith("ppt/slides/slide") and fname.endswith(".xml"):
                    continue
                if fname.startswith("ppt/slides/_rels/slide") and fname.endswith(".xml.rels"):
                    continue
                if fname.startswith("ppt/notesSlides/notesSlide") and fname.endswith(".xml"):
                    continue
                if fname.startswith("ppt/media/image-"):
                    continue
                data = zin.read(fname)
                if fname == "docProps/core.xml":
                    txt = data.decode("utf-8").replace(
                        "WP1 – Early Discharge Planning Business Case",
                        "WP2 – Data Engineering: From Hospital Systems to the Morning Worklist"
                    )
                    data = txt.encode("utf-8")
                zout.writestr(item, data)

            for s in slides:
                i = s.slide_num
                zout.writestr(f"ppt/slides/slide{i}.xml", s.to_pptx_xml().encode("utf-8"))
                zout.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", make_slide_rels_xml(i).encode("utf-8"))
                zout.writestr(f"ppt/notesSlides/notesSlide{i}.xml", make_notes_xml(i, s.notes).encode("utf-8"))


def export_pdf(slides, out_pdf: str):
    with PdfPages(out_pdf) as pdf:
        for s in slides:
            s.render_to_pdf_page(pdf)


if __name__ == "__main__":
    slides = build_all_slides()
    template_path = "WP1/WP1 – Early Discharge Planning Business Case.pptx"
    out_pptx_path = "WP2/WP2 – Data Engineering Architecture.pptx"
    out_pdf_path  = "WP2/WP2 – Data Engineering Architecture.pdf"

    export_pptx(slides, template_path, out_pptx_path)
    export_pdf(slides, out_pdf_path)
    print(f"Successfully generated:\n  - {out_pptx_path}\n  - {out_pdf_path}")
