#!/usr/bin/env python3
"""
Generate index.html for PT (root) and en/es/fr from scripts/index.template.html.

Hero copy and UI strings come from scripts/home_page_i18n.py (HOME_UI).
Normally invoked via scripts/generate-servico-pages.py — run that for a full site rebuild.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "scripts" / "index.template.html"

sys.path.insert(0, str(Path(__file__).parent))

from home_page_i18n import (  # noqa: E402
    HANDYMAN,
    HOME_META,
    HOME_UI,
    LANGS,
    SERVICE_CARDS,
    home_url,
    render_home_hreflang,
    render_lang_switcher,
)
from service_page_i18n import LANG_HTML, asset_prefix  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}


def json_ld(lang: str) -> str:
    meta = HOME_META[lang]
    data = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": "Faz de Tudo PT",
        "url": home_url(lang).rstrip("/"),
        "logo": "https://www.fazdetudo.pt/logo.webp",
        "image": "https://www.fazdetudo.pt/logo.webp",
        "description": meta["json_desc"],
        "telephone": "+351932504112",
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Lisboa",
            "addressRegion": "Grande Lisboa e Margem Sul",
            "addressCountry": "PT",
        },
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
            {"@type": "AdministrativeArea", "name": "Azeitão"},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def build_service_cards(lang: str) -> str:
    ui = HOME_UI[lang]
    blocks = []
    for card in SERVICE_CARDS:
        title, desc = card[lang]
        feat = " service-window-featured" if card["featured"] else ""
        badge = ""
        if card["badge"] == "premium":
            badge = f'                    <span class="window-badge">{ui["badge_premium"]}</span>\n'
        elif card["badge"] == "specialty":
            badge = f'                    <span class="window-badge">{ui["badge_specialty"]}</span>\n'
        blocks.append(
            f"""                <div class="service-window-card{feat}">
{badge}                    <div class="service-window-icon"><i class="fa-solid fa-{card["icon"]}" aria-hidden="true"></i></div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                    <a href="{card["slug"]}" class="service-window-link">{ui["learn_more"]} <i class="fa-solid fa-chevron-right" aria-hidden="true"></i></a>
                </div>"""
        )
    return "\n\n".join(blocks)


def build_handyman_section(lang: str) -> str:
    h = HANDYMAN[lang]
    boxes = []
    for title, icon, items in h["boxes"]:
        lis = "\n".join(
            f'                        <li><i class="fa-solid fa-check" aria-hidden="true"></i> {item}</li>'
            for item in items
        )
        boxes.append(
            f"""                <div class="handyman-detail-box">
                    <div class="handyman-box-header">
                        <i class="fa-solid fa-{icon}" aria-hidden="true"></i>
                        <h3>{title}</h3>
                    </div>
                    <ul class="handyman-list">
{lis}
                    </ul>
                </div>"""
        )
    grid = "\n\n".join(boxes)
    return f"""    <section class="section handyman-details" id="handyman-details">
        <div class="container">
            <div class="section-header handyman-details-header">
                <span class="handyman-badge">{h["badge"]}</span>
                <h2 class="section-title">{h["title"]}</h2>
                <p class="section-subtitle">{h["subtitle"]}</p>
            </div>

            <div class="handyman-detailed-grid">
{grid}
            </div>

            <div class="handyman-cta-wrap">
                <a href="servico-reparacoes-gerais.html" class="btn btn-primary btn-lg handyman-cta-btn">
                    <span>{h["cta"]}</span>
                    <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
                </a>
            </div>
        </div>
    </section>"""


def apply_i18n_attributes(html: str, lang: str) -> str:
    ui = HOME_UI[lang]
    for key, text in ui.items():
        html = re.sub(
            rf'(data-i18n="{re.escape(key)}">)([^<]*)',
            rf"\1{text}",
            html,
        )
    return html


def apply_meta_strings(html: str, lang: str) -> str:
    meta = HOME_META[lang]
    html = html.replace('aria-label="Navegação principal"', f'aria-label="{meta["nav_aria"]}"')
    html = html.replace('alt="Faz de Tudo PT - Serviços de faz tudo em Lisboa"', f'alt="{meta["logo_alt"]}"')
    html = html.replace('alt="Profissional faz tudo"', f'alt="{meta["section_logo_alt"]}"')
    html = html.replace('aria-label="Open menu"', f'aria-label="{meta["menu_aria"]}"')
    html = html.replace('aria-label="Crítica anterior"', f'aria-label="{meta["review_prev"]}"')
    html = html.replace('aria-label="Crítica seguinte"', f'aria-label="{meta["review_next"]}"')
    html = html.replace(">Ver críticas no Google\n", f">{meta['view_google']}\n")
    html = html.replace('aria-label="Fechar chat"', f'aria-label="{meta["wa_close"]}"')
    html = html.replace('aria-label="Enviar mensagem"', f'aria-label="{meta["wa_send"]}"')
    html = html.replace('aria-label="Contact via WhatsApp"', f'aria-label="{meta["wa_float"]}"')
    html = html.replace('aria-label="Ligar agora"', f'aria-label="{meta["float_call"]}"')
    html = html.replace('id="footer-address-text">Lisboa, Portugal</', f'id="footer-address-text">{meta["address"]}</')
    html = html.replace('id="wa-greeting">Como posso ajudar?</', f'id="wa-greeting">{HOME_UI[lang]["wa_greeting"]}</')
    html = html.replace(
        'placeholder="Escreva uma mensagem..."',
        f'placeholder="{HOME_UI[lang]["wa_placeholder"]}"',
    )
    html = html.replace(">Online</span>", f">{HOME_UI[lang]['wa_online']}</span>", 1)
    return html


def render_homepage(lang: str, template: str) -> str:
    meta = HOME_META[lang]
    prefix = asset_prefix(lang)
    html = (
        template.replace("{{HTML_LANG}}", LANG_HTML[lang])
        .replace("{{PAGE_LANG}}", lang)
        .replace("{{PAGE_TITLE}}", meta["title"])
        .replace("{{META_DESCRIPTION}}", meta["description"])
        .replace("{{OG_TITLE}}", meta["og_title"])
        .replace("{{OG_DESCRIPTION}}", meta["description"])
        .replace("{{CANONICAL_URL}}", home_url(lang).rstrip("/"))
        .replace("{{OG_LOCALE}}", OG_LOCALE[lang])
        .replace("{{HREFLANG_BLOCK}}", render_home_hreflang())
        .replace("{{JSON_LD}}", json_ld(lang))
        .replace("{{ASSET_PREFIX}}", prefix)
        .replace("{{LANG_SWITCHER}}", render_lang_switcher(lang))
        .replace("{{SERVICE_CARDS}}", build_service_cards(lang))
        .replace("{{HANDYMAN_SECTION}}", build_handyman_section(lang))
    )
    html = apply_i18n_attributes(html, lang)
    html = apply_meta_strings(html, lang)
    return html


def output_path(lang: str) -> Path:
    if lang == "pt":
        return ROOT / "index.html"
    return ROOT / lang / "index.html"


def main() -> None:
    if not TEMPLATE_PATH.exists():
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "build_index_template",
            ROOT / "scripts" / "build_index_template.py",
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    written = []
    for lang in LANGS:
        path = output_path(lang)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_homepage(lang, template), encoding="utf-8")
        written.append(path.relative_to(ROOT).as_posix())
        print(f"wrote {written[-1]}")

    print(f"\nTotal: {len(written)} homepages")


if __name__ == "__main__":
    main()
