#!/usr/bin/env python3
"""Bundle site source (templates, scripts, assets) for AI review."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "fazdetudopt-codigo-gemini.txt"

EXT = {".html", ".css", ".js", ".xml", ".txt", ".py", ".md", ".yml", ".yaml"}
EXTRA_NAMES = {".nojekyll", ".htaccess"}
SKIP_DIRS = {".git", "__pycache__"}
SKIP_NAMES = {
    "fazdetudopt-codigo-completo.zip",
    "fazdetudopt-codigo-gemini.txt",
}

# Templates e scripts primeiro no bundle
PRIORITY_PREFIXES = (
    ".github/workflows/",
    "scripts/templates/",
    "scripts/",
    "docs/",
)


def sort_key(path: Path) -> tuple:
    rel = path.relative_to(ROOT).as_posix()
    for i, prefix in enumerate(PRIORITY_PREFIXES):
        if rel.startswith(prefix):
            return (i, rel)
    return (len(PRIORITY_PREFIXES), rel)


def should_include(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.name in SKIP_NAMES:
        return False
    if path.name in EXTRA_NAMES:
        return True
    return path.suffix.lower() in EXT


def collect_files() -> list[Path]:
    paths = [p for p in ROOT.rglob("*") if p.is_file() and should_include(p)]
    return sorted(paths, key=sort_key)


def write_bundle() -> Path:
    """Write fazdetudopt-codigo-gemini.txt; called after every site rebuild."""
    from datetime import datetime, timezone

    files = collect_files()
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "FAZDETUDO.PT — CÓDIGO FONTE PARA REVISÃO (Gemini / AI)",
        "Repositório: https://github.com/mikailcantemir-svg/fazdetudopt",
        "Gerado automaticamente por scripts/bundle-for-gemini.py",
        f"Atualizado: {stamp}",
        "Inclui: HTML, CSS, JS, templates, scripts, sitemap, robots, docs",
        f"Ficheiros: {len(files)}",
        "=" * 80,
        "",
    ]

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        lines.extend(["", "=" * 80, f"FILE: {rel}", "=" * 80, ""])
        try:
            lines.append(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            lines.append(f"[binary skipped: {rel}]")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    return OUT


def main() -> None:
    out = write_bundle()
    print(f"Created {out.name} ({out.stat().st_size / 1024:.1f} KB, {len(collect_files())} files)")


if __name__ == "__main__":
    main()
