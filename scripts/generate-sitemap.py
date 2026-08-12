#!/usr/bin/env python3
"""Regenerate sitemap.xml with today's date as lastmod (PT + en/es/fr service pages)."""

from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from site_config import BASE_URL
from slug_registry import SERVICE_SLUGS

try:
    from articles_data import ARTICLES, ARTICLES_INDEX
except ImportError:
    ARTICLES, ARTICLES_INDEX = [], None

TODAY = date.today().isoformat()

URLS = [
    ("/", "weekly", "1.0"),
    ("/en/", "weekly", "1.0"),
    ("/es/", "weekly", "1.0"),
    ("/fr/", "weekly", "1.0"),
    ("/parceiros/", "weekly", "0.9"),
    ("/en/parceiros/", "weekly", "0.9"),
    ("/es/parceiros/", "weekly", "0.9"),
    ("/fr/parceiros/", "weekly", "0.9"),
]

LANG_PREFIXES = ("", "/en", "/es", "/fr")


def main():
    entries = []
    for path, freq, priority in URLS:
        entries.append(url_entry(path, freq, priority))

    for slug in SERVICE_SLUGS:
        for prefix in LANG_PREFIXES:
            entries.append(url_entry(f"{prefix}/{slug}", "weekly", "0.8"))

    if ARTICLES_INDEX is not None:
        entries.append(url_entry("/artigos/", "monthly", "0.6"))
        for article in ARTICLES:
            entries.append(url_entry(f"/artigos/{article['slug']}", "monthly", "0.7"))

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Atualizar lastmod: python scripts/generate-sitemap.py -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out} with {len(entries)} URLs, lastmod={TODAY}")


def url_entry(path: str, freq: str, priority: str) -> str:
    return f"""    <url>
        <loc>{BASE_URL}{path}</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>{freq}</changefreq>
        <priority>{priority}</priority>
    </url>"""


if __name__ == "__main__":
    main()
