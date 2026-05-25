#!/usr/bin/env python3
"""Assemble dist/ for GitHub Pages (HTML + static assets)."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

FAVICON_FILES = (
    "favicon.ico",
    "favicon-48x48.png",
    "favicon-192x192.png",
    "apple-touch-icon.png",
)

ROOT_ASSETS = (
    "style.css",
    "script.js",
    "logo.webp",
    "logo.png",
    "robots.txt",
    "sitemap.xml",
    *FAVICON_FILES,
)

LANG_DIRS = ("en", "es", "fr")
EXTRA_ROOT_FILES = (".nojekyll", ".htaccess")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()

    for path in sorted(ROOT.glob("*.html")):
        copy_file(path, DIST / path.name)

    for lang in LANG_DIRS:
        lang_dir = ROOT / lang
        if not lang_dir.is_dir():
            continue
        for html in sorted(lang_dir.rglob("*.html")):
            rel = html.relative_to(ROOT)
            copy_file(html, DIST / rel)

    for name in ROOT_ASSETS:
        src = ROOT / name
        if src.is_file():
            copy_file(src, DIST / name)
        else:
            print(f"warning: missing asset {name}")

    images = ROOT / "images"
    if images.is_dir():
        shutil.copytree(images, DIST / "images")

    for name in EXTRA_ROOT_FILES:
        src = ROOT / name
        if src.is_file():
            copy_file(src, DIST / name)

    html_count = len(list(DIST.rglob("*.html")))
    print(f"Wrote dist/ ({html_count} HTML files)")


if __name__ == "__main__":
    main()
