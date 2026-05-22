#!/usr/bin/env python3
"""Replace *-lisboa.html with 301-style redirects to servico-*.html (static meta + JS)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REDIRECTS = {
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


def redirect_html(old: str, target: str) -> str:
    canonical = f"https://www.fazdetudo.pt/{target}"
    return f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0; url={target}">
    <link rel="canonical" href="{canonical}">
    <title>Redirecionamento | Faz de Tudo PT</title>
    <script>location.replace("{target}");</script>
</head>
<body>
    <p>Esta página foi movida. <a href="{target}">Continuar para o novo endereço</a>.</p>
</body>
</html>
"""


def main():
    for old, target in REDIRECTS.items():
        path = ROOT / old
        path.write_text(redirect_html(old, target), encoding="utf-8")
        print(f"{old} -> {target}")


if __name__ == "__main__":
    main()
