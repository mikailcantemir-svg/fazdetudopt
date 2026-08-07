#!/usr/bin/env python3
"""
Single entry point to regenerate the whole static site from templates + i18n.

Run from repo root:
    python scripts/generate-servico-pages.py

Outputs (overwrites):
  - index.html (PT) + en/es/fr/index.html
  - servico-*.html (PT) + en/es/fr/servico-*.html (18 services × 4 languages)
  - sitemap.xml, dist/, fazdetudopt-codigo-gemini.txt (auto)

Source of truth:
  - scripts/home_page_i18n.py  → homepage copy
  - scripts/service_page_i18n.py → service page copy
  - scripts/slug_registry.py → URLs + hreflang
  - scripts/site_config.py → contactos globais
  - scripts/templates/ → layouts + partials
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))

from html_partials import (  # noqa: E402
    render_footer_service,
    render_head,
    render_header_service,
    render_wa_widget,
)
from service_page_i18n import LANGS, LANG_HTML, SERVICE_COPY, UI, build_body_html, localized_meta  # noqa: E402
from slug_registry import (  # noqa: E402
    SERVICE_SLUGS,
    asset_prefix,
    index_href,
    page_url,
    render_hreflang_tags_for_service,
    service_id_from_slug,
)
from site_config import OG_IMAGE, schema_telephone, tel_href, wa_href_for_message  # noqa: E402
from template_engine import render_template  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}

CLEANING_PARTNER_PHONE = "+351963212185"
CLEANING_PARTNER_CTA = {
    "pt": {
        "text": "Procura uma empregada de limpeza? Pode ligar diretamente para a nossa parceira Caterina Cantemir para combinar disponibilidade e o serviço.",
        "call": "Ligar diretamente à Caterina · 963 212 185",
    },
    "en": {
        "text": "Looking for a cleaning professional? You can call our recommended partner Caterina Cantemir directly to discuss availability and the service.",
        "call": "Call Caterina directly · 963 212 185",
    },
    "es": {
        "text": "¿Busca una profesional de limpieza? Puede llamar directamente a nuestra colaboradora Caterina Cantemir para consultar disponibilidad y el servicio.",
        "call": "Llamar directamente a Caterina · 963 212 185",
    },
    "fr": {
        "text": "Vous cherchez une professionnelle du ménage ? Vous pouvez appeler directement notre partenaire Caterina Cantemir pour convenir des disponibilités et du service.",
        "call": "Appeler Caterina directement · 963 212 185",
    },
}

LANG_DIRS = ("en", "es", "fr")


def json_ld(slug: str, lang: str) -> str:
    meta = localized_meta(slug, lang)
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": meta["service_name"],
        "description": meta["meta_description"],
        "provider": {
            "@type": "HomeAndConstructionBusiness",
            "name": "FAZDETUDO.PT",
            "image": OG_IMAGE,
            "telephone": schema_telephone(),
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Lisboa",
                "addressCountry": "PT",
            },
        },
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def get_body_html(slug: str, lang: str) -> str:
    if lang == "pt":
        try:
            from service_rich_content import SERVICE_BODIES
        except ImportError:
            SERVICE_BODIES = {}
        if slug in SERVICE_BODIES:
            return SERVICE_BODIES[slug].strip()
    return build_body_html(slug, lang).strip()


def render_page(slug: str, lang: str) -> str:
    service_id = service_id_from_slug(slug)
    meta = localized_meta(slug, lang)
    ui = UI[lang]
    prefix = asset_prefix(lang)
    canonical = page_url(slug, lang)
    is_cleaning_partner = slug == "servico-limpezas.html"
    cta_p = ui["cta_p"].format(service=meta["service_name"])
    cta_call = ui["cta_call"]
    call_href = tel_href()
    if is_cleaning_partner:
        partner_cta = CLEANING_PARTNER_CTA[lang]
        cta_p = partner_cta["text"]
        cta_call = partner_cta["call"]
        call_href = f"tel:{CLEANING_PARTNER_PHONE}"

    head = render_head(
        page_title=meta["page_title"],
        meta_description=meta["meta_description"],
        canonical_url=canonical,
        hreflang_block=render_hreflang_tags_for_service(service_id),
        og_title=meta["og_title"],
        og_description=meta["meta_description"],
        og_locale=OG_LOCALE[lang],
        json_ld=json_ld(slug, lang),
        asset_prefix=prefix,
        include_swiper_css=False,
    )

    html = render_template(
        "service.html",
        {
            "HTML_LANG": LANG_HTML[lang],
            "PAGE_LANG": lang,
            "HEAD": head,
            "HEADER_SERVICE": render_header_service(
                asset_prefix=prefix,
                index_href=index_href(lang),
                back_label=ui["back"],
            ),
            "FOOTER": render_footer_service(footer_text=ui["footer"]),
            "WA_WIDGET": render_wa_widget(
                asset_prefix=prefix,
                wa_online=ui["wa_online"],
                wa_greeting=ui["wa_greeting"],
                wa_placeholder=ui["wa_placeholder"],
                wa_close=ui["wa_close"],
                wa_send=ui["wa_send"],
                wa_float_label=ui["wa_float_label"],
            ),
            "ASSET_PREFIX": prefix,
            "H1_TITLE": meta["h1"],
            "LEAD_TEXT": ui["lead"],
            "BODY_HTML": get_body_html(slug, lang),
            "CTA_H3": ui["cta_h3"],
            "CTA_P": cta_p,
            "CTA_WA": ui["cta_wa"],
            "CTA_CALL": cta_call,
            "WA_HREF": wa_href_for_message(meta["wa_message"]),
            "TEL_HREF": call_href,
        },
    )
    return html


def output_path(slug: str, lang: str) -> Path:
    if lang == "pt":
        return ROOT / slug
    return ROOT / lang / slug


def expected_service_paths() -> set[str]:
    paths = set()
    for slug in SERVICE_SLUGS:
        for lang in LANGS:
            paths.add(output_path(slug, lang).relative_to(ROOT).as_posix())
    return paths


def cleanup_stale_service_pages() -> list[str]:
    removed = []
    expected = expected_service_paths()
    for lang_dir in [ROOT, *[ROOT / code for code in LANG_DIRS]]:
        if not lang_dir.is_dir():
            continue
        for path in lang_dir.glob("servico-*.html"):
            rel = path.relative_to(ROOT).as_posix()
            if rel not in expected:
                path.unlink()
                removed.append(rel)
    return removed


def _run_generate_homepages() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_homepages",
        SCRIPTS / "generate-homepages.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_fix_fa_aria_hidden() -> None:
    spec = importlib.util.spec_from_file_location(
        "fix_fa_aria_hidden",
        SCRIPTS / "fix-fa-aria-hidden.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_lisboa_redirects() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_lisboa_redirects",
        SCRIPTS / "generate-lisboa-redirects.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_articles() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_articles",
        SCRIPTS / "generate-articles.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_sitemap() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_sitemap",
        SCRIPTS / "generate-sitemap.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_build_dist() -> None:
    spec = importlib.util.spec_from_file_location(
        "build_dist",
        SCRIPTS / "build-dist.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_bundle_for_gemini() -> None:
    spec = importlib.util.spec_from_file_location(
        "bundle_for_gemini",
        SCRIPTS / "bundle-for-gemini.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def main() -> None:
    print("=== Regenerating fazdetudo.pt static HTML ===\n")

    removed = cleanup_stale_service_pages()
    if removed:
        print("Removed stale pages:")
        for rel in removed:
            print(f"  - {rel}")
        print()

    print("--- Homepages (PT + en/es/fr) ---")
    _run_generate_homepages()

    print("\n--- Service pages (18 × 4 languages) ---")
    written = []
    for slug in SERVICE_SLUGS:
        for lang in LANGS:
            path = output_path(slug, lang)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_page(slug, lang), encoding="utf-8")
            rel = path.relative_to(ROOT).as_posix()
            written.append(rel)
            print(f"wrote {rel}")

    print("\n--- Articles (Guias e Dicas) ---")
    _run_generate_articles()

    print("\n--- Font Awesome aria-hidden pass ---")
    _run_fix_fa_aria_hidden()

    print("\n--- Legacy SEO redirects (17× *-lisboa.html + .htaccess) ---")
    _run_generate_lisboa_redirects()

    print("\n--- Sitemap ---")
    _run_generate_sitemap()

    print("\n--- dist/ (GitHub Pages artifact) ---")
    _run_build_dist()

    print("\n--- Gemini code bundle (fazdetudopt-codigo-gemini.txt) ---")
    _run_bundle_for_gemini()

    print(
        f"\nDone: {len(written)} service pages + 4 homepages "
        f"({len(SERVICE_SLUGS)} services × {len(LANGS)} languages)."
    )
    print("Templates: scripts/templates/ | Registry: scripts/slug_registry.py")
    print("Deploy: dist/ (favicons + static assets; see .github/workflows/pages.yml)")


if __name__ == "__main__":
    main()
