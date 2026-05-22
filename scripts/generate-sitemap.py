#!/usr/bin/env python3
"""Regenerate sitemap.xml with today's date as lastmod."""

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://www.fazdetudo.pt"
TODAY = date.today().isoformat()

URLS = [
    ("/", "weekly", "1.0"),
    ("/index.html", "weekly", "1.0"),
    ("/servico-remodelacoes.html", "weekly", "0.8"),
    ("/servico-pinturas.html", "weekly", "0.8"),
    ("/servico-pintura-fachadas-alpinismo.html", "weekly", "0.8"),
    ("/servico-canalizacoes.html", "weekly", "0.8"),
    ("/servico-electricidade.html", "weekly", "0.8"),
    ("/servico-carpintaria.html", "weekly", "0.8"),
    ("/servico-reparacoes-gerais.html", "weekly", "0.8"),
    ("/servico-manutencao.html", "weekly", "0.8"),
    ("/servico-limpezas.html", "weekly", "0.8"),
    ("/servico-jardinagem.html", "weekly", "0.8"),
    ("/servico-mudancas.html", "weekly", "0.8"),
    ("/servico-informatica.html", "weekly", "0.8"),
    ("/servico-serralharia.html", "weekly", "0.8"),
    ("/servico-climatizacao.html", "weekly", "0.8"),
    ("/servico-estores-persianas.html", "weekly", "0.8"),
    ("/servico-decoracao-interiores.html", "weekly", "0.8"),
    ("/servico-piscinas.html", "weekly", "0.8"),
]


def main():
    entries = []
    for path, freq, priority in URLS:
        entries.append(f"""    <url>
        <loc>{BASE}{path}</loc>
        <lastmod>{TODAY}</lastmod>
        <changefreq>{freq}</changefreq>
        <priority>{priority}</priority>
    </url>""")

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- Atualizar lastmod em cada deploy: python scripts/generate-sitemap.py -->
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out} with lastmod={TODAY}")


if __name__ == "__main__":
    main()
