#!/usr/bin/env python3
"""Bundle site source (templates, scripts, assets) for AI review."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "fazdetudopt-codigo-gemini.txt"

EXT = {".html", ".css", ".js", ".xml", ".txt", ".py", ".md"}
SKIP_DIRS = {".git", "__pycache__"}
SKIP_NAMES = {
    "fazdetudopt-codigo-completo.zip",
    "fazdetudopt-codigo-gemini.txt",
}

# Templates e scripts primeiro no bundle
PRIORITY_PREFIXES = (
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
    if path.name == ".htaccess":
        return True
    return path.suffix.lower() in EXT


def collect_files() -> list[Path]:
    paths = [p for p in ROOT.rglob("*") if p.is_file() and should_include(p)]
    return sorted(paths, key=sort_key)


def main() -> None:
    files = collect_files()
    lines = [
        "FAZDETUDO.PT — CÓDIGO FONTE PARA REVISÃO (pós-refactor Fases 1–5)",
        "Repositório: https://github.com/mikailcantemir-svg/fazdetudopt",
        "Inclui: scripts/templates/partials/, slug_registry, site_config, geradores",
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
    print(f"Created {OUT.name} ({OUT.stat().st_size / 1024:.1f} KB, {len(files)} files)")


if __name__ == "__main__":
    main()
