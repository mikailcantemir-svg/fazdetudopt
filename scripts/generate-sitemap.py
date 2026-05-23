#!/usr/bin/env python3
"""Regenerate sitemap.xml with today's date as lastmod (PT + en/es/fr service pages)."""

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://www.fazdetudo.pt"
TODAY = date.today().isoformat()

# Home pages (PT + localized)
URLS = [
    ("/", "weekly", "1.0"),
    ("/index.html", "weekly", "1.0"),
    ("/en/", "weekly", "1.0"),
    ("/en/index.html", "weekly", "1.0"),
    ("/es/", "weekly", "1.0"),
    ("/es/index.html", "weekly", "1.0"),
    ("/fr/", "weekly", "1.0"),
    ("/fr/index.html", "weekly", "1.0"),
]

# SYNC: slug order = script.js SERVICE_LANDING_SLUGS
SERVICE_SLUGS = [
    "servico-remodelacoes.html",
    "servico-recuperar-casa.html",
    "servico-pinturas.html",
    "servico-pintura-fachadas-alpinismo.html",
    "servico-canalizacoes.html",
    "servico-electricidade.html",
    "servico-carpintaria.html",
    "servico-reparacoes-gerais.html",
    "servico-manutencao.html",
    "servico-limpezas.html",
    "servico-jardinagem.html",
    "servico-mudancas.html",
    "servico-informatica.html",
    "servico-serralharia.html",
    "servico-climatizacao.html",
    "servico-estores-persianas.html",
    "servico-decoracao-interiores.html",
    "servico-piscinas.html",
]

LANG_PREFIXES = ("", "/en", "/es", "/fr")


def main():
    entries = []
    for path, freq, priority in URLS:
        entries.append(url_entry(path, freq, priority))

    for slug in SERVICE_SLUGS:
        for prefix in LANG_PREFIXES:
            entries.append(url_entry(f"{prefix}/{slug}", "weekly", "0.8"))

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Atualizar lastmod em cada deploy: python scripts/generate-sitemap.py -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out} with {len(entries)} URLs, lastmod={TODAY}")


def url_entry(path: str, freq: str, priority: str) -> str:
    return f"""    <url>
        <loc>{BASE}{path}</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>{freq}</changefreq>
        <priority>{priority}</priority>
    </url>"""


if __name__ == "__main__":
    main()
