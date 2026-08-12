# -*- coding: utf-8 -*-
"""
Slug registry — fonte única para URLs de serviços, homepages, páginas
institucionais e hreflang.

Cada service_id mapeia para o mesmo ficheiro em todos os idiomas (ex.: servico-canalizacoes.html).
Reservado para slugs por idioma no futuro via SERVICE_SLUGS_BY_LANG.

Páginas institucionais (ex.: /parceiros/) vivem em INSTITUTIONAL_PAGES —
nunca em SERVICE_IDS.
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
    "pt": ("pt-PT",),
    "en": ("en",),
    "es": ("es",),
    "fr": ("fr",),
}

# Páginas institucionais multilíngues (path relativo à raiz do site, com / final)
INSTITUTIONAL_PAGES: dict[str, dict[str, str]] = {
    "parceiros": {
        "pt": "parceiros/",
        "en": "en/parceiros/",
        "es": "es/parceiros/",
        "fr": "fr/parceiros/",
    },
}

# Ordem = grelha homepage / script.js SERVICE_LANDING_SLUGS / sitemap
SERVICE_IDS: tuple[str, ...] = (
    "remodelacoes",
    "recuperar-casa",
    "pinturas",
    "limpezas",
    "canalizacoes",
    "electricidade",
    "carpintaria",
    "reparacoes-gerais",
    "manutencao",
    "jardinagem",
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
    """Prefix for assets from homepage or lang-root pages (en/index.html)."""
    return "" if lang == "pt" else "../"


def institutional_path(page_id: str, lang: str) -> str:
    if page_id not in INSTITUTIONAL_PAGES:
        raise KeyError(f"Unknown institutional page: {page_id}")
    return INSTITUTIONAL_PAGES[page_id][lang]


def institutional_href(page_id: str, lang: str) -> str:
    """Root-absolute path for nav links (e.g. /parceiros/ or /en/parceiros/)."""
    return f"/{institutional_path(page_id, lang)}"


def institutional_url(page_id: str, lang: str) -> str:
    return f"{BASE_URL}/{institutional_path(page_id, lang)}"


def institutional_asset_prefix(lang: str) -> str:
    """Prefix for assets from /parceiros/ (pt) or /{lang}/parceiros/."""
    return "../" if lang == "pt" else "../../"


def index_href(lang: str) -> str:
    """Link relativo/raiz para a homepage canónica (sem index.html)."""
    if lang == "pt":
        return "/"
    return f"/{lang}/"


def home_url(lang: str) -> str:
    path = HOME_PATHS[lang]
    return f"{BASE_URL}/{path}" if path else f"{BASE_URL}/"


def service_page_url(service_id: str, lang: str) -> str:
    slug = service_slug(service_id, lang)
    if lang == "pt":
        return f"{BASE_URL}/{slug}"
    return f"{BASE_URL}/{lang}/{slug}"


def service_page_href(service_slug_name: str, lang: str) -> str:
    """Root-absolute href for a servico-*.html file (safe from nested dirs)."""
    if lang == "pt":
        return f"/{service_slug_name}"
    return f"/{lang}/{service_slug_name}"


def page_url(slug: str, lang: str) -> str:
    """URL absoluta a partir do nome de ficheiro servico-*.html."""
    return service_page_url(service_id_from_slug(slug), lang)


def _render_hreflang_for_urls(urls_by_lang: dict[str, str], *, self_closing: bool = False) -> str:
    end = " />" if self_closing else ">"
    lines: list[str] = []
    for lang in LANGS:
        url = urls_by_lang[lang]
        for code in HREFLANG_CODES[lang]:
            lines.append(f'    <link rel="alternate" hreflang="{code}" href="{url}"{end}')
    lines.append(
        f'    <link rel="alternate" hreflang="x-default" href="{urls_by_lang["pt"]}"{end}'
    )
    return "\n".join(lines)


def render_hreflang_tags_for_service(service_id: str) -> str:
    urls = {lang: service_page_url(service_id, lang) for lang in LANGS}
    return _render_hreflang_for_urls(urls, self_closing=False)


def render_hreflang_tags(slug: str) -> str:
    return render_hreflang_tags_for_service(service_id_from_slug(slug))


def render_home_hreflang() -> str:
    urls = {lang: home_url(lang) for lang in LANGS}
    return _render_hreflang_for_urls(urls, self_closing=True)


def render_institutional_hreflang(page_id: str) -> str:
    urls = {lang: institutional_url(page_id, lang) for lang in LANGS}
    return _render_hreflang_for_urls(urls, self_closing=False)
