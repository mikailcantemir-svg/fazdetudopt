# -*- coding: utf-8 -*-
"""
Slug registry — fonte única para URLs de serviços, homepages e hreflang.

Cada service_id mapeia para o mesmo ficheiro em todos os idiomas (ex.: servico-canalizacoes.html).
Reservado para slugs por idioma no futuro via SERVICE_SLUGS_BY_LANG.
"""

from __future__ import annotations

from site_config import BASE_URL

LANGS = ("pt", "en", "es", "fr")

LANG_HTML = {
    "pt": "pt-PT",
    "en": "en",
    "es": "es",
    "fr": "fr",
}

HREFLANG_CODES: dict[str, tuple[str, ...]] = {
    "pt": ("pt-PT", "pt"),
    "en": ("en",),
    "es": ("es",),
    "fr": ("fr",),
}

# Ordem = grelha homepage / script.js SERVICE_LANDING_SLUGS / sitemap
SERVICE_IDS: tuple[str, ...] = (
    "remodelacoes",
    "recuperar-casa",
    "pinturas",
    "pintura-fachadas-alpinismo",
    "canalizacoes",
    "electricidade",
    "carpintaria",
    "reparacoes-gerais",
    "manutencao",
    "limpezas",
    "jardinagem",
    "mudancas",
    "informatica",
    "serralharia",
    "climatizacao",
    "estores-persianas",
    "decoracao-interiores",
    "piscinas",
)

# Slugs por idioma (hoje idênticos; chave reservada para hreflang assimétrico futuro)
SERVICE_SLUGS_BY_LANG: dict[str, dict[str, str]] = {
    sid: {lang: f"servico-{sid}.html" for lang in LANGS} for sid in SERVICE_IDS
}

SERVICE_SLUGS: tuple[str, ...] = tuple(SERVICE_SLUGS_BY_LANG[sid]["pt"] for sid in SERVICE_IDS)

HOME_PATHS: dict[str, str] = {
    "pt": "",
    "en": "en/",
    "es": "es/",
    "fr": "fr/",
}


def service_slug(service_id: str, lang: str = "pt") -> str:
    if service_id not in SERVICE_SLUGS_BY_LANG:
        raise KeyError(f"Unknown service_id: {service_id}")
    return SERVICE_SLUGS_BY_LANG[service_id][lang]


def service_id_from_slug(slug: str) -> str:
    if not slug.startswith("servico-") or not slug.endswith(".html"):
        raise ValueError(f"Not a service slug: {slug}")
    service_id = slug[len("servico-") : -len(".html")]
    if service_id not in SERVICE_SLUGS_BY_LANG:
        raise KeyError(f"Unknown service slug: {slug}")
    return service_id


def asset_prefix(lang: str) -> str:
    return "" if lang == "pt" else "../"


def index_href(lang: str) -> str:
    return "index.html" if lang == "pt" else "../index.html"


def home_url(lang: str) -> str:
    path = HOME_PATHS[lang]
    return f"{BASE_URL}/{path}" if path else f"{BASE_URL}/"


def service_page_url(service_id: str, lang: str) -> str:
    slug = service_slug(service_id, lang)
    if lang == "pt":
        return f"{BASE_URL}/{slug}"
    return f"{BASE_URL}/{lang}/{slug}"


def page_url(slug: str, lang: str) -> str:
    """URL absoluta a partir do nome de ficheiro servico-*.html."""
    return service_page_url(service_id_from_slug(slug), lang)


def render_hreflang_tags_for_service(service_id: str) -> str:
    lines: list[str] = []
    for lang in LANGS:
        url = service_page_url(service_id, lang)
        for code in HREFLANG_CODES[lang]:
            lines.append(f'    <link rel="alternate" hreflang="{code}" href="{url}">')
    lines.append(
        f'    <link rel="alternate" hreflang="x-default" href="{service_page_url(service_id, "pt")}">'
    )
    return "\n".join(lines)


def render_hreflang_tags(slug: str) -> str:
    return render_hreflang_tags_for_service(service_id_from_slug(slug))


def render_home_hreflang() -> str:
    lines = []
    for lang in LANGS:
        url = home_url(lang)
        for code in HREFLANG_CODES[lang]:
            lines.append(f'    <link rel="alternate" hreflang="{code}" href="{url}" />')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{home_url("pt")}" />')
    return "\n".join(lines)
