#!/usr/bin/env python3
"""
Assemble dist/ for GitHub Pages (deploy artifact only).

Run after generate-servico-pages.py (includes sitemap), or standalone.

Contents mirror the live site root:
  index.html, sitemap.xml, robots.txt, favicons, CNAME, .nojekyll, .htaccess,
  style.css, script.js, logo.webp, logo.png, images/, assets/, en/, es/, fr/,
  servico-*.html, *-lisboa.html
"""

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

ROOT_FILES = (
    "index.html",
    "sitemap.xml",
    "robots.txt",
    "CNAME",
    ".nojekyll",
    "style.css",
    "script.js",
    "logo.webp",
    "logo.png",
    *FAVICON_FILES,
)

LANG_DIRS = ("en", "es", "fr")
EXTRA_ROOT_FILES = (".htaccess",)


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

    for name in EXTRA_ROOT_FILES:
        src = ROOT / name
        if src.is_file():
            _copy_file(src, DIST / name)

    _copy_tree(ROOT / "images", DIST / "images")
    assets = ROOT / "assets"
    if assets.is_dir():
        _copy_tree(assets, DIST / "assets")

    videos = ROOT / "videos"
    if videos.is_dir():
        _copy_tree(videos, DIST / "videos")

    for lang in LANG_DIRS:
        _copy_tree(ROOT / lang, DIST / lang)

    articles = ROOT / "artigos"
    if articles.is_dir():
        _copy_tree(articles, DIST / "artigos")

    for pattern in ("servico-*.html", "*-lisboa.html"):
        for src in sorted(ROOT.glob(pattern)):
            if src.is_file():
                _copy_file(src, DIST / src.name)

    return DIST


def main() -> None:
    out = build_dist()
    html_count = len(list(out.rglob("*.html")))
    print(f"Wrote dist/ ({html_count} HTML files)")


if __name__ == "__main__":
    main()
