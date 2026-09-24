#!/usr/bin/env python3
"""Generate resumen-hoja-de-vida.pdf from resumen-hoja-de-vida.md.

The MyST typst templates are academic-paper layouts (cover page, English
"Contents", one section per page), which is wrong for an institutional CV
summary form. This renders the same markdown as a compact A4 document.

Usage: python generate_resumen.py
Output: resumen-hoja-de-vida.typ and .pdf (needs the typst CLI and ./fonts)
"""

import re
import subprocess
from pathlib import Path

from generate_cv import escape_typst, parse_table  # reuse the typst escaping

BASE = Path(__file__).parent
SRC = BASE / "resumen-hoja-de-vida.md"
OUT_TYP = BASE / "resumen-hoja-de-vida.typ"
OUT_PDF = BASE / "resumen-hoja-de-vida.pdf"

PREAMBLE = """#set document(title: "Resumen Hoja de Vida")
#set page(
  paper: "a4",
  margin: (x: 1.5cm, top: 1.5cm, bottom: 1.3cm),
  numbering: "1 / 1",
  number-align: center,
)
#set text(font: ("Source Sans Pro",), size: 8.5pt, lang: "es")
#set par(justify: false, leading: 0.55em)
#show link: set text(fill: rgb("#1D5B7E"))
"""


def column_weights(rows):
    """Proportional column widths from the longest cell in each column."""
    widths = [max(len(str(c)) for c in col) + 6 for col in zip(*rows)]
    total = sum(widths)
    return [max(0.10, w / total) for w in widths]


def render_table(block):
    rows = parse_table("\n".join(block))
    if not rows:
        return ""
    headers = list(rows[0].keys())
    grid = [headers] + [[r.get(h, "") for h in headers] for r in rows]
    weights = column_weights(grid)
    cols = ", ".join(f"{w:.3f}fr" for w in weights)
    cells = []
    for i, row in enumerate(grid):
        for cell in row:
            body = escape_typst(cell)
            cells.append(f"  [{'*' + body + '*' if i == 0 else body}],")
    return (
        f"#table(\n  columns: ({cols}),\n  stroke: 0.4pt + luma(160),\n"
        "  inset: (x: 4pt, y: 3pt),\n"
        "  fill: (_, y) => if y == 0 { luma(232) },\n"
        + "\n".join(cells)
        + "\n)\n"
    )


def convert(md):
    body = md.split("---\n", 2)[-1] if md.startswith("---") else md
    out, table = [], []
    for line in body.split("\n"):
        stripped = line.strip()
        if stripped.startswith("|"):
            table.append(stripped)
            continue
        if table:
            out.append(render_table(table))
            table = []
        if not stripped or stripped == "---":
            continue
        if stripped.startswith("# "):
            out.append(
                "#align(center)[#text(size: 15pt, weight: \"bold\")"
                f"[{escape_typst(stripped[2:])}]]\n#v(2pt)\n"
            )
        elif stripped.startswith("## "):
            out.append(
                "#v(6pt)\n#block(width: 100%, fill: luma(228), inset: 5pt)"
                f"[#text(size: 10pt, weight: \"bold\")[{escape_typst(stripped[3:])}]]\n#v(3pt)\n"
            )
        elif stripped.startswith("### "):
            out.append(
                f"#v(4pt)\n#text(size: 9pt, weight: \"bold\", fill: rgb(\"#1D5B7E\"))"
                f"[{escape_typst(stripped[4:])}]\n#v(2pt)\n"
            )
        else:
            out.append(escape_typst(stripped) + "\n")
    if table:
        out.append(render_table(table))
    return PREAMBLE + "\n" + "\n".join(out)


def main():
    typ = convert(SRC.read_text(encoding="utf-8"))
    for section in ("I.- ESTUDIOS", "II.- EXPERIENCIA", "III.- EXPERIENCIA",
                    "IV.- PRODUCCIÓN", "V.- INVESTIGACIÓN", "VI.- DISTINCIONES"):
        assert section in typ, f"missing section: {section}"
    OUT_TYP.write_text(typ, encoding="utf-8")
    print(f"Generated {OUT_TYP} ({len(typ):,} bytes)")

    cmd = ["typst", "compile", str(OUT_TYP), str(OUT_PDF)]
    if (BASE / "fonts").is_dir():
        cmd += ["--font-path", str(BASE / "fonts"), "--ignore-system-fonts"]
    subprocess.run(cmd, check=True)
    print(f"Compiled {OUT_PDF} ({OUT_PDF.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
