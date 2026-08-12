#!/usr/bin/env python3
"""
Single entry point to regenerate the whole static site from templates + i18n.

Run from repo root:
    python scripts/generate-servico-pages.py

Outputs (overwrites):
  - index.html (PT) + en/es/fr/index.html
  - servico-*.html (PT) + en/es/fr/servico-*.html (16 services × 4 languages)
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
from recommended_partners import get_partner  # noqa: E402
from site_config import (  # noqa: E402
    BASE_URL,
    OG_IMAGE,
    PRIMARY_OFFICE_STREET_LINE1,
    PRIMARY_OFFICE_STREET_LINE2,
    schema_telephone,
    tel_href,
    wa_href_for_message,
)
from template_engine import render_template  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}

# Sidebar CTA overrides for services executed by partners (not FAZDETUDO.PT).
PARTNER_SERVICE_CTA = {
    "servico-limpezas.html": {
        "partner_id": "caterina",
        "mode": "phone_whatsapp",
        "schema_provider": {
            "@type": "Person",
            "name": "Caterina",
            "telephone": "+351963212185",
        },
        "pt": {
            "text": (
                "Serviço realizado por parceira FAZDETUDO.PT. "
                "Contacte a Caterina diretamente para combinar disponibilidade."
            ),
            "call": "Ligar · 963 212 185",
            "whatsapp": "WhatsApp · 963 212 185",
        },
        "en": {
            "text": (
                "Service provided by a FAZDETUDO.PT partner. "
                "Contact Caterina directly to arrange availability."
            ),
            "call": "Call · 963 212 185",
            "whatsapp": "WhatsApp · 963 212 185",
        },
        "es": {
            "text": (
                "Servicio realizado por colaboradora FAZDETUDO.PT. "
                "Contacte a Caterina directamente para concertar disponibilidad."
            ),
            "call": "Llamar · 963 212 185",
            "whatsapp": "WhatsApp · 963 212 185",
        },
        "fr": {
            "text": (
                "Service réalisé par une partenaire FAZDETUDO.PT. "
                "Contactez Caterina directement pour convenir des disponibilités."
            ),
            "call": "Appeler · 963 212 185",
            "whatsapp": "WhatsApp · 963 212 185",
        },
    },
    "servico-remodelacoes.html": {
        "partner_id": "valeriu-cantemir",
        "mode": "phone_only",
        "schema_provider": {
            "@type": "Person",
            "name": "Valeriu Cantemir",
            "telephone": "+351964400960",
        },
        "pt": {
            "text": (
                "Serviço disponibilizado através de parceiro FAZDETUDO.PT "
                "especializado em obras e remodelações."
            ),
            "call": "Ligar para Valeriu Cantemir · 964 400 960",
        },
        "en": {
            "text": (
                "Service provided through a FAZDETUDO.PT partner specialised "
                "in construction and renovations."
            ),
            "call": "Call Valeriu Cantemir · 964 400 960",
        },
        "es": {
            "text": (
                "Servicio disponible a través de colaborador FAZDETUDO.PT "
                "especializado en obras y reformas."
            ),
            "call": "Llamar a Valeriu Cantemir · 964 400 960",
        },
        "fr": {
            "text": (
                "Service proposé via un partenaire FAZDETUDO.PT spécialisé "
                "en travaux et rénovations."
            ),
            "call": "Appeler Valeriu Cantemir · 964 400 960",
        },
    },
    "servico-recuperar-casa.html": {
        "partner_id": "valeriu-cantemir",
        "mode": "phone_only",
        "schema_provider": {
            "@type": "Person",
            "name": "Valeriu Cantemir",
            "telephone": "+351964400960",
        },
        "pt": {
            "text": (
                "Serviço disponibilizado através de parceiro FAZDETUDO.PT "
                "especializado em obras e remodelações."
            ),
            "call": "Ligar para Valeriu Cantemir · 964 400 960",
        },
        "en": {
            "text": (
                "Service provided through a FAZDETUDO.PT partner specialised "
                "in construction and renovations."
            ),
            "call": "Call Valeriu Cantemir · 964 400 960",
        },
        "es": {
            "text": (
                "Servicio disponible a través de colaborador FAZDETUDO.PT "
                "especializado en obras y reformas."
            ),
            "call": "Llamar a Valeriu Cantemir · 964 400 960",
        },
        "fr": {
            "text": (
                "Service proposé via un partenaire FAZDETUDO.PT spécialisé "
                "en travaux et rénovations."
            ),
            "call": "Appeler Valeriu Cantemir · 964 400 960",
        },
    },
    "servico-climatizacao.html": {
        "partner_id": "airfix",
        "mode": "website",
        "schema_provider": {
            "@type": "Organization",
            "name": "AirFix.pt",
            "url": "https://airfix.pt/",
        },
        "pt": {
            "text": (
                "Serviço especializado realizado através da AirFix.pt, "
                "parceiro FAZDETUDO.PT."
            ),
            "visit": "Visitar AirFix.pt",
        },
        "en": {
            "text": (
                "Specialist service provided through AirFix.pt, "
                "a FAZDETUDO.PT partner."
            ),
            "visit": "Visit AirFix.pt",
        },
        "es": {
            "text": (
                "Servicio especializado realizado a través de AirFix.pt, "
                "colaborador FAZDETUDO.PT."
            ),
            "visit": "Visitar AirFix.pt",
        },
        "fr": {
            "text": (
                "Service spécialisé réalisé via AirFix.pt, "
                "partenaire FAZDETUDO.PT."
            ),
            "visit": "Visiter AirFix.pt",
        },
    },
}

LANG_DIRS = ("en", "es", "fr")


def _default_provider() -> dict:
    return {
        "@type": "HomeAndConstructionBusiness",
        "name": "FAZDETUDO.PT",
        "url": BASE_URL,
        "image": OG_IMAGE,
        "telephone": schema_telephone(),
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": PRIMARY_OFFICE_STREET_LINE1,
            "addressLocality": "Pontinha",
            "postalCode": PRIMARY_OFFICE_STREET_LINE2.split()[0],
            "addressCountry": "PT",
        },
    }


def json_ld(slug: str, lang: str) -> str:
    meta = localized_meta(slug, lang)
    override = PARTNER_SERVICE_CTA.get(slug)
    if override and override.get("schema_provider"):
        provider = dict(override["schema_provider"])
        brand = {"@type": "Brand", "name": "FAZDETUDO.PT", "url": BASE_URL}
    else:
        provider = _default_provider()
        brand = None
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": meta["service_name"],
        "description": meta["meta_description"],
        "provider": provider,
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
        ],
    }
    if brand:
        data["brand"] = brand
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
    cta_p = ui["cta_p"].format(service=meta["service_name"])
    cta_call = ui["cta_call"]
    cta_wa = ui["cta_wa"]
    call_href = tel_href()
    wa_link = wa_href_for_message(meta["wa_message"])
    show_wa = True
    hide_float_wa = False

    override = PARTNER_SERVICE_CTA.get(slug)
    cta_actions = ""
    if override:
        partner = get_partner(override["partner_id"])
        copy = override[lang]
        cta_p = copy["text"]
        hide_float_wa = True
        mode = override["mode"]
        if mode == "phone_only":
            show_wa = False
            cta_call = copy["call"]
            call_href = partner["tel_href"] if partner else call_href
            cta_actions = (
                f'                    <a href="{call_href}" class="btn btn-primary btn-lg service-cta-call">\n'
                f'                        <i class="fa-solid fa-phone" aria-hidden="true"></i> {cta_call}\n'
                f"                    </a>"
            )
        elif mode == "website":
            show_wa = False
            visit = copy["visit"]
            site = partner.get("website", "https://airfix.pt/") if partner else "https://airfix.pt/"
            cta_actions = (
                f'                    <a href="{site}" class="btn btn-primary btn-lg" '
                f'target="_blank" rel="noopener noreferrer">\n'
                f'                        <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i> {visit}\n'
                f"                    </a>"
            )
        else:
            cta_call = copy["call"]
            call_href = partner["tel_href"] if partner else call_href
            cta_wa = copy["whatsapp"]
            wa_link = partner.get("whatsapp_href", wa_link) if partner else wa_link
            cta_actions = (
                f'                    <a href="{wa_link}" class="btn btn-primary btn-lg" '
                f'target="_blank" rel="noopener noreferrer">\n'
                f'                        <i class="fa-brands fa-whatsapp" aria-hidden="true"></i> {cta_wa}\n'
                f"                    </a>\n"
                f'                    <a href="{call_href}" class="btn btn-outline btn-lg service-cta-call">\n'
                f'                        <i class="fa-solid fa-phone" aria-hidden="true"></i> {cta_call}\n'
                f"                    </a>"
            )

    if not cta_actions:
        if show_wa:
            cta_actions = (
                f'                    <a href="{wa_link}" class="btn btn-primary btn-lg" '
                f'target="_blank" rel="noopener noreferrer">\n'
                f'                        <i class="fa-brands fa-whatsapp" aria-hidden="true"></i> {cta_wa}\n'
                f"                    </a>\n"
                f'                    <a href="{call_href}" class="btn btn-outline btn-lg service-cta-call">\n'
                f'                        <i class="fa-solid fa-phone" aria-hidden="true"></i> {cta_call}\n'
                f"                    </a>"
            )
        else:
            cta_actions = (
                f'                    <a href="{call_href}" class="btn btn-primary btn-lg service-cta-call">\n'
                f'                        <i class="fa-solid fa-phone" aria-hidden="true"></i> {cta_call}\n'
                f"                    </a>"
            )

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

    wa_widget = ""
    if not hide_float_wa:
        wa_widget = render_wa_widget(
            asset_prefix=prefix,
            wa_online=ui["wa_online"],
            wa_greeting=ui["wa_greeting"],
            wa_placeholder=ui["wa_placeholder"],
            wa_close=ui["wa_close"],
            wa_send=ui["wa_send"],
            wa_float_label=ui["wa_float_label"],
        )

    html = render_template(
        "service.html",
        {
            "HTML_LANG": LANG_HTML[lang],
            "PAGE_LANG": lang,
            "HEAD": head,
            "SKIP_LINK": ui["skip_link"],
            "HEADER_SERVICE": render_header_service(
                asset_prefix=prefix,
                index_href=index_href(lang),
                back_label=ui["back"],
            ),
            "FOOTER": render_footer_service(footer_text=ui["footer"]),
            "WA_WIDGET": wa_widget,
            "ASSET_PREFIX": prefix,
            "H1_TITLE": meta["h1"],
            "LEAD_TEXT": ui["lead"],
            "BODY_HTML": get_body_html(slug, lang),
            "CTA_H3": ui["cta_h3"],
            "CTA_P": cta_p,
            "CTA_ACTIONS": cta_actions,
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
    # Keep soft-redirect stubs for retired services (rewritten by generate-lisboa-redirects)
    spec = importlib.util.spec_from_file_location(
        "generate_lisboa_redirects",
        SCRIPTS / "generate-lisboa-redirects.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    keep = set()
    for old in getattr(mod, "RETIRED_SERVICE_REDIRECTS", {}):
        keep.add(old)
        for lang in LANG_DIRS:
            keep.add(f"{lang}/{old}")

    for lang_dir in [ROOT, *[ROOT / code for code in LANG_DIRS]]:
        if not lang_dir.is_dir():
            continue
        for path in lang_dir.glob("servico-*.html"):
            rel = path.relative_to(ROOT).as_posix()
            if rel in expected or rel in keep:
                continue
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


def _run_generate_parceiros() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_parceiros",
        SCRIPTS / "generate-parceiros.py",
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

    print("\n--- Service pages (16 × 4 languages) ---")
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

    print("\n--- Partners directory (/parceiros/) ---")
    _run_generate_parceiros()

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
