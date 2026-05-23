#!/usr/bin/env python3
"""
Assemble dist/ for GitHub Pages (deploy artifact only).

Run after generate-servico-pages.py and generate-sitemap.py, or via the
integrated pipeline at the end of generate-servico-pages.py.

Contents mirror the live site root:
  index.html, sitemap.xml, robots.txt, CNAME, .nojekyll,
  style.css, script.js, logo.webp, images/, en/, es/, fr/,
  servico-*.html, *-lisboa.html
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

ROOT_FILES = (
    "index.html",
    "sitemap.xml",
    "robots.txt",
    "CNAME",
    ".nojekyll",
    "style.css",
    "script.js",
    "logo.webp",
)

LANG_DIRS = ("en", "es", "fr")


def _copy_file(src: Path, dest: Path) -> None:
    if not src.is_file():
        raise FileNotFoundError(f"Missing deploy file: {src.relative_to(ROOT)}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def _copy_tree(src: Path, dest: Path) -> None:
    if not src.is_dir():
        raise FileNotFoundError(f"Missing deploy directory: {src.relative_to(ROOT)}")
    shutil.copytree(src, dest, dirs_exist_ok=True)


def build_dist() -> Path:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    for name in ROOT_FILES:
        _copy_file(ROOT / name, DIST / name)

    _copy_tree(ROOT / "images", DIST / "images")

    for lang in LANG_DIRS:
        _copy_tree(ROOT / lang, DIST / lang)

    for pattern in ("servico-*.html", "*-lisboa.html"):
        for src in sorted(ROOT.glob(pattern)):
            if src.is_file():
                _copy_file(src, DIST / src.name)

    return DIST


def main() -> None:
    out = build_dist()
    html_count = len(list(out.rglob("*.html")))
    print(f"Wrote {out.relative_to(ROOT)}/ ({html_count} HTML files)")


if __name__ == "__main__":
    main()
