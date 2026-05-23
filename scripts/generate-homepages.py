#!/usr/bin/env python3
"""
Generate index.html for PT (root) and en/es/fr from scripts/templates/home.html.

Hero copy and UI strings come from scripts/home_page_i18n.py (HOME_UI).
Normally invoked via scripts/generate-servico-pages.py — run that for a full site rebuild.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))

from home_page_i18n import (  # noqa: E402
    ADVANTAGES,
    FAQ_ITEMS,
    GOOGLE_RATING,
    HANDYMAN,
    HOME_META,
    HOME_UI,
    LANGS,
    RECENT_WORK_ITEMS,
    RECENT_WORK_WA,
    SERVICE_CARDS,
    TESTIMONIAL_CARDS,
    home_url,
    render_home_hreflang,
    render_lang_switcher,
)
from html_partials import (  # noqa: E402
    render_footer_home,
    render_head,
    render_header_home,
    render_wa_widget,
)
from slug_registry import LANG_HTML, asset_prefix  # noqa: E402
from site_config import (  # noqa: E402
    GOOGLE_REVIEWS_URL,
    LOGO_PATH,
    PHONE_DISPLAY,
    mailto_href,
    schema_telephone,
    tel_href,
    wa_href,
    wa_href_for_message,
)
from template_engine import render_template  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}


def _fa_icon(icon: str) -> str:
    return f"fa-solid fa-{icon}"


def _render_stars(rating: int = 5) -> str:
    return "".join(
        f'<i class="fa-solid fa-star{"" if i < rating else " google-star-empty"}" aria-hidden="true"></i>'
        for i in range(5)
    )


def build_advantages_grid(lang: str) -> str:
    blocks = []
    for item in ADVANTAGES:
        name, desc = item[lang]
        icon = item["icon"]
        blocks.append(
            f"""                <div class="advantage-card fade-in">
                    <div class="advantage-icon">
                        <i class="{_fa_icon(icon)}" aria-hidden="true"></i>
                    </div>
                    <h3>{html.escape(name)}</h3>
                    <p>{html.escape(desc)}</p>
                </div>"""
        )
    return "\n".join(blocks)


def build_testimonials_summary(lang: str) -> str:
    ui = HOME_UI[lang]
    rating = GOOGLE_RATING
    stars = _render_stars(int(rating))
    return f"""                <div class="reviews-aggregate fade-in">
                    <span class="reviews-score">{rating:.1f}</span>
                    <div class="reviews-stars" aria-label="{rating:.1f} / 5">{stars}</div>
                    <span class="reviews-count">{html.escape(ui["reviews_google_label"])}</span>
                    <span class="reviews-google" aria-hidden="true"><i class="fab fa-google" aria-hidden="true"></i></span>
                </div>"""


def build_testimonials_cards(lang: str) -> str:
    ui = HOME_UI[lang]
    blocks = []
    for card in TESTIMONIAL_CARDS:
        name, text = card[lang]
        initial = html.escape(name.strip()[0].upper())
        blocks.append(
            f"""                        <div class="swiper-slide">
                            <article class="google-review-card">
                                <div class="google-review-top">
                                    <div class="google-review-avatar google-review-avatar--initial" aria-hidden="true">{initial}</div>
                                    <div class="google-review-meta">
                                        <strong class="google-review-name">{html.escape(name)}</strong>
                                        <span class="google-review-source">
                                            <i class="fab fa-google" aria-hidden="true"></i>
                                            {html.escape(ui["google_review_source"])}
                                        </span>
                                    </div>
                                </div>
                                <div class="google-review-rating-row">
                                    <span class="google-review-stars" aria-label="5 / 5">{_render_stars(5)}</span>
                                </div>
                                <p class="google-review-text">{html.escape(text)}</p>
                            </article>
                        </div>"""
        )
    return "\n".join(blocks)


def build_faq_list(lang: str) -> str:
    blocks = []
    for i, item in enumerate(FAQ_ITEMS):
        question, answer = item[lang]
        blocks.append(
            f"""                <div class="faq-item fade-in">
                    <button type="button" class="faq-question" aria-expanded="false" aria-controls="faq-answer-{i}">
                        {html.escape(question)}
                        <i class="fa-solid fa-chevron-down" aria-hidden="true"></i>
                    </button>
                    <div class="faq-answer" id="faq-answer-{i}">
                        <div class="faq-answer-inner">{html.escape(answer)}</div>
                    </div>
                </div>"""
        )
    return "\n".join(blocks)


def build_recent_work_section(lang: str, asset_prefix: str) -> str:
    ui = HOME_UI[lang]
    cards = []
    for item in RECENT_WORK_ITEMS:
        category, title, description = item[lang]
        before_src = f"{asset_prefix}{item['before']}"
        after_src = f"{asset_prefix}{item['after']}"
        wa_link = wa_href_for_message(item["wa"][lang])
        alt_before = f"{ui['recent_work_before']} — {category}: {title}"
        alt_after = f"{ui['recent_work_after']} — {category}: {title}"
        cards.append(
            f"""                <article class="work-card fade-in">
                    <span class="work-category">{html.escape(category)}</span>
                    <div class="work-compare" role="group" aria-label="{html.escape(title)}">
                        <figure class="work-photo work-photo--before">
                            <img src="{before_src}" alt="{html.escape(alt_before)}" width="600" height="450" loading="lazy" decoding="async">
                            <figcaption>{html.escape(ui["recent_work_before"])}</figcaption>
                        </figure>
                        <figure class="work-photo work-photo--after">
                            <img src="{after_src}" alt="{html.escape(alt_after)}" width="600" height="450" loading="lazy" decoding="async">
                            <figcaption>{html.escape(ui["recent_work_after"])}</figcaption>
                        </figure>
                    </div>
                    <h3 class="work-card-title">{html.escape(title)}</h3>
                    <p class="work-card-text">{html.escape(description)}</p>
                    <a href="{wa_link}" class="btn btn-outline work-card-cta" target="_blank" rel="noopener noreferrer">
                        <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
                        <span>{html.escape(ui["recent_work_card_cta"])}</span>
                    </a>
                </article>"""
        )
    grid = "\n\n".join(cards)
    section_wa = wa_href_for_message(RECENT_WORK_WA[lang])
    return f"""    <section class="section" id="recent-work">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title" data-i18n="recent_work_title">{html.escape(ui["recent_work_title"])}</h2>
                <p class="section-subtitle" data-i18n="recent_work_subtitle">{html.escape(ui["recent_work_subtitle"])}</p>
            </div>
            <div class="recent-work-grid">
{grid}
            </div>
            <div class="recent-work-cta">
                <a href="{section_wa}" class="btn btn-primary btn-lg" id="recent-work-cta">
                    <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
                    <span data-i18n="recent_work_cta">{html.escape(ui["recent_work_cta"])}</span>
                    <i class="fa-solid fa-arrow-right" aria-hidden="true"></i>
                </a>
            </div>
        </div>
    </section>"""


def build_testimonials_footer(lang: str) -> str:
    label = HOME_UI[lang]["view_google_reviews"]
    return f"""            <div class="testimonials-footer">
                <a href="{GOOGLE_REVIEWS_URL}" class="btn-google-reviews" id="google-reviews-link" target="_blank" rel="noopener noreferrer">
                    <span data-i18n="view_google_reviews">{html.escape(label)}</span>
                </a>
            </div>"""


def build_footer_services(lang: str) -> str:
    lines = []
    for card in SERVICE_CARDS:
        title = card[lang][0]
        href = card["slug"]
        lines.append(f'                        <li><a href="{href}">{html.escape(title)}</a></li>')
    return "\n".join(lines)


def faq_json_ld(lang: str) -> str:
    entities = []
    for item in FAQ_ITEMS:
        question, answer = item[lang]
        entities.append(
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
        )
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def json_ld(lang: str) -> str:
    meta = HOME_META[lang]
    business = {
        "@type": "HomeAndConstructionBusiness",
        "name": "Faz de Tudo PT",
        "url": home_url(lang).rstrip("/"),
        "logo": "https://www.fazdetudo.pt/logo.webp",
        "image": "https://www.fazdetudo.pt/logo.webp",
        "description": meta["json_desc"],
        "telephone": schema_telephone(),
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
    data = {
        "@context": "https://schema.org",
        "@graph": [business],
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
        elif card["badge"] == "acabamentos_premium":
            badge = f'                    <span class="window-badge">{ui["badge_acabamentos_premium"]}</span>\n'
        elif card["badge"] == "muito_requisitado":
            badge = f'                    <span class="window-badge">{ui["badge_muito_requisitado"]}</span>\n'
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


def render_homepage(lang: str) -> str:
    meta = HOME_META[lang]
    ui = HOME_UI[lang]
    prefix = asset_prefix(lang)
    canonical = home_url(lang).rstrip("/")

    head = render_head(
        page_title=meta["title"],
        meta_description=meta["description"],
        canonical_url=canonical,
        hreflang_block=render_home_hreflang(),
        og_title=meta["og_title"],
        og_description=meta["description"],
        og_locale=OG_LOCALE[lang],
        json_ld=json_ld(lang),
        faq_json_ld=faq_json_ld(lang),
        asset_prefix=prefix,
        include_swiper_css=True,
    )
    header = render_header_home(
        asset_prefix=prefix,
        logo_href=home_url(lang),
        lang_switcher=render_lang_switcher(lang),
    )
    footer = render_footer_home(
        asset_prefix=prefix,
        email_href=mailto_href(),
        footer_services=build_footer_services(lang),
    )
    wa_widget = render_wa_widget(
        asset_prefix=prefix,
        wa_online=ui["wa_online"],
        wa_greeting=ui["wa_greeting"],
        wa_placeholder=ui["wa_placeholder"],
        wa_close=meta["wa_close"],
        wa_send=meta["wa_send"],
        wa_float_label=meta["wa_float"],
    )

    html = render_template(
        "home.html",
        {
            "HTML_LANG": LANG_HTML[lang],
            "PAGE_LANG": lang,
            "HEAD": head,
            "HEADER_HOME": header,
            "FOOTER": footer,
            "WA_WIDGET": wa_widget,
            "ASSET_PREFIX": prefix,
            "LOGO_PATH": LOGO_PATH,
            "SERVICE_CARDS": build_service_cards(lang),
            "HANDYMAN_SECTION": build_handyman_section(lang),
            "RECENT_WORK_SECTION": build_recent_work_section(lang, prefix),
            "ADVANTAGES_GRID": build_advantages_grid(lang),
            "TESTIMONIALS_SUMMARY": build_testimonials_summary(lang),
            "TESTIMONIALS_CARDS": build_testimonials_cards(lang),
            "TESTIMONIALS_FOOTER": build_testimonials_footer(lang),
            "FAQ_LIST": build_faq_list(lang),
            "WA_HREF": wa_href(lang),
            "TEL_HREF": tel_href(),
            "PHONE_DISPLAY": PHONE_DISPLAY,
            "GOOGLE_REVIEWS_URL": GOOGLE_REVIEWS_URL,
        },
    )
    html = apply_i18n_attributes(html, lang)
    html = apply_meta_strings(html, lang)
    return html


def output_path(lang: str) -> Path:
    if lang == "pt":
        return ROOT / "index.html"
    return ROOT / lang / "index.html"


def main() -> None:
    written = []
    for lang in LANGS:
        path = output_path(lang)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_homepage(lang), encoding="utf-8")
        written.append(path.relative_to(ROOT).as_posix())
        print(f"wrote {written[-1]}")

    print(f"\nTotal: {len(written)} homepages")


if __name__ == "__main__":
    main()
