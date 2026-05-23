#!/usr/bin/env python3
"""
Gera redirects SEO legados *-lisboa.html → servico-*.html.

Fonte única: REDIRECTS (17 URLs).
Saídas:
  - 17× HTML na raiz (meta refresh + link; sem JavaScript duplicado)
  - .htaccess com Redirect 301 (Apache; ignorado no GitHub Pages)

GitHub Pages não suporta .htaccess — aí só o HTML faz o redirect (soft).
Em Apache, o 301 ocorre antes do HTML ser servido.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Fonte única — manter sincronizado com sitemap / slugs servico-*
REDIRECTS: dict[str, str] = {
    "pinturas-lisboa.html": "servico-pinturas.html",
    "pintura-fachadas-alpinismo-lisboa.html": "servico-pintura-fachadas-alpinismo.html",
    "canalizacoes-lisboa.html": "servico-canalizacoes.html",
    "eletricidade-lisboa.html": "servico-electricidade.html",
    "carpintaria-lisboa.html": "servico-carpintaria.html",
    "reparacoes-gerais-lisboa.html": "servico-reparacoes-gerais.html",
    "manutencao-lisboa.html": "servico-manutencao.html",
    "limpezas-lisboa.html": "servico-limpezas.html",
    "jardinagem-lisboa.html": "servico-jardinagem.html",
    "mudancas-lisboa.html": "servico-mudancas.html",
    "informatica-lisboa.html": "servico-informatica.html",
    "serralharia-lisboa.html": "servico-serralharia.html",
    "climatizacao-lisboa.html": "servico-climatizacao.html",
    "remodelacoes-lisboa.html": "servico-remodelacoes.html",
    "reparacao-estores-lisboa.html": "servico-estores-persianas.html",
    "decoracao-interiores-lisboa.html": "servico-decoracao-interiores.html",
    "manutencao-piscinas-lisboa.html": "servico-piscinas.html",
}


def redirect_html(target: str) -> str:
    """Um único mecanismo client-side (meta refresh); fallback <a> sem JS."""
    canonical = f"https://www.fazdetudo.pt/{target}"
    return f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, follow">
    <meta http-equiv="refresh" content="0; url={target}">
    <link rel="canonical" href="{canonical}">
    <title>Redirecionamento | Faz de Tudo PT</title>
</head>
<body>
    <p>Esta página foi movida. <a href="{target}">Continuar para o novo endereço</a>.</p>
</body>
</html>
"""


def htaccess_content() -> str:
    lines = [
        "# AUTO-GENERATED — scripts/generate-lisboa-redirects.py (não editar à mão)",
        "# Redirect 301: URLs legadas *-lisboa.html → servico-*.html (Apache mod_alias)",
        "# GitHub Pages ignora este ficheiro; usa os HTML *-lisboa.html na raiz.",
        "",
    ]
    for old in sorted(REDIRECTS):
        lines.append(f"Redirect 301 /{old} /{REDIRECTS[old]}")
    lines.append("")
    return "\n".join(lines)


def write_redirect_pages(root: Path | None = None) -> list[str]:
    root = root or ROOT
    written = []
    for old, target in REDIRECTS.items():
        path = root / old
        path.write_text(redirect_html(target), encoding="utf-8")
        written.append(f"{old} -> {target}")
    return written


def write_htaccess(root: Path | None = None) -> Path:
    root = root or ROOT
    path = root / ".htaccess"
    path.write_text(htaccess_content(), encoding="utf-8")
    return path


def main() -> None:
    for line in write_redirect_pages():
        print(line)
    htaccess_path = write_htaccess()
    print(f"\nWrote {htaccess_path.relative_to(ROOT)} ({len(REDIRECTS)} rules)")


if __name__ == "__main__":
    main()
