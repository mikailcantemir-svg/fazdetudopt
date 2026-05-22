#!/usr/bin/env python3
"""Bundle all website source into one text file for Gemini review."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "fazdetudopt-codigo-gemini.txt"
EXT = {".html", ".css", ".js", ".xml", ".txt", ".py", ".md"}
SKIP = {"fazdetudopt-codigo-completo.zip", "fazdetudopt-codigo-gemini.txt"}

files = sorted(
    p
    for p in ROOT.rglob("*")
    if p.is_file()
    and p.suffix.lower() in EXT
    and ".git" not in p.parts
    and p.name not in SKIP
)

lines = [
    "FAZDETUDO.PT — CÓDIGO COMPLETO PARA REVISÃO",
    "Repositório: https://github.com/mikailcantemir-svg/fazdetudopt",
    f"Ficheiros incluídos: {len(files)}",
    "=" * 80,
    "",
]

for path in files:
    rel = path.relative_to(ROOT).as_posix()
    lines.append("")
    lines.append("=" * 80)
    lines.append(f"FILE: {rel}")
    lines.append("=" * 80)
    lines.append("")
    lines.append(path.read_text(encoding="utf-8"))

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Created {OUT.name} ({OUT.stat().st_size / 1024:.1f} KB, {len(files)} files)")
