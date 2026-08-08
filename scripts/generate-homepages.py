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
    PARTNER_RECRUIT,
    RECENT_WORK,
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
from recommended_partners import (  # noqa: E402
    FILTER_CATEGORY_IDS,
    HOW_IT_WORKS,
    PARTNER_CATEGORIES,
    PARTNER_DIRECTORY_UI,
    PARTNER_STATUS_LABELS,
    active_partners,
    partner_badge_keys,
)
from slug_registry import LANG_HTML, asset_prefix  # noqa: E402
from site_config import (  # noqa: E402
    GOOGLE_REVIEWS_URL,
    LOGO_PATH,
    PHONE_DISPLAY,
    PRIMARY_OFFICE_STREET_LINE1,
    PRIMARY_OFFICE_STREET_LINE2,
    SECOND_OFFICE_STREET_LINE1,
    SECOND_OFFICE_STREET_LINE2,
    mailto_href,
    schema_telephone,
    tel_href,
    wa_href_for_message,
    wa_href_home,
    HOME_WA_MESSAGE,
)
from template_engine import render_template  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}

CLEANING_PARTNER = {
    "name": "Caterina",
    "phone_display": "963 212 185",
    "tel_href": "tel:+351963212185",
    "whatsapp_href": "https://wa.me/351963212185",
    "labels": {
        "pt": {
            "badge": "Parceira recomendada",
            "role": "Empregada de limpeza · contacto direto",
            "call": "Ligar",
            "details": "Ver serviço",
            "aria": "Ligar diretamente para Caterina, parceira de limpezas",
        },
        "en": {
            "badge": "Recommended partner",
            "role": "Cleaning professional · direct contact",
            "call": "Call",
            "details": "View service",
            "aria": "Call Caterina directly, recommended cleaning partner",
        },
        "es": {
            "badge": "Colaboradora recomendada",
            "role": "Profesional de limpieza · contacto directo",
            "call": "Llamar directamente",
            "details": "Ver servicio",
            "aria": "Llamar directamente a Caterina, colaboradora de limpieza",
        },
        "fr": {
            "badge": "Partenaire recommandée",
            "role": "Professionnelle du ménage · contact direct",
            "call": "Appeler",
            "details": "Voir le service",
            "aria": "Appeler directement Caterina, partenaire ménage recommandée",
        },
    },
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
        text_block = (
            f'\n                                <p class="google-review-text">{html.escape(text)}</p>'
            if text
            else ""
        )
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
                                </div>{text_block}
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


def _recent_work_gallery_id(item: dict) -> str:
    if item.get("gallery_id"):
        return str(item["gallery_id"])
    stem = Path(item["image"]).stem
    stem = re.sub(r"-lisboa-\d+$", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"-\d+$", "", stem)
    return stem


def _recent_work_img_markup(
    src: str,
    alt: str,
    w: int,
    h: int,
    *,
    loading: str = "lazy",
) -> str:
    return (
        f"""<img class="recent-work-media" src="{src}" alt="{alt}" """
        f"""width="{w}" height="{h}" loading="{loading}" decoding="async">"""
    )


def _recent_work_video_overlay(ui: dict) -> str:
    badge = html.escape(ui.get("work_video_badge", "Vídeo"))
    return (
        '<span class="work-video-play" aria-hidden="true">\n'
        '    <i class="fa-solid fa-play"></i>\n'
        "</span>\n"
        f'<span class="work-video-badge">{badge}</span>'
    )


def _recent_work_lightbox_trigger(
    media_html: str,
    *,
    media_type: str,
    full_src: str,
    title: str,
    ui: dict,
    gallery_id: str,
    index: int,
    poster_src: str = "",
) -> str:
    poster_attr = (
        f' data-poster="{html.escape(poster_src, quote=True)}"' if poster_src else ""
    )
    trigger_label = (
        ui["work_lightbox_open_video"]
        if media_type == "video"
        else ui["work_lightbox_open_image"]
    )
    video_class = (
        " work-lightbox-trigger--video" if media_type == "video" else ""
    )
    overlay = (
        "\n" + _recent_work_video_overlay(ui) if media_type == "video" else ""
    )
    return (
        f'<button type="button" class="work-lightbox-trigger{video_class}" '
        f'data-gallery="{html.escape(gallery_id, quote=True)}" data-index="{index}" '
        f'data-type="{media_type}" data-full="{html.escape(full_src, quote=True)}" '
        f'data-title="{html.escape(title, quote=True)}"{poster_attr} '
        f'aria-label="{html.escape(trigger_label)}">\n'
        f"{media_html}\n"
        f"{overlay}\n"
        f"</button>"
    )


def _recent_work_carousel_slides(
    item: dict,
    copy: dict,
    prefix: str,
    w: int,
    h: int,
    ui: dict,
) -> list[str]:
    slides: list[str] = []
    slide_index = 0
    gallery_id = _recent_work_gallery_id(item)
    mixed_media = item.get("media")
    if mixed_media:
        alts = copy.get("alts") or [copy["alt"]] * len(mixed_media)
        for i, media_item in enumerate(mixed_media):
            media_type = media_item.get("type", "image")
            title = alts[i] if i < len(alts) else copy["alt"]
            slide_alt = html.escape(title)
            loading = "eager" if slide_index == 0 else "lazy"
            if media_type == "video":
                poster_src = f"{prefix}{media_item['poster']}"
                video_src = f"{prefix}{media_item['video']}"
                img = _recent_work_img_markup(
                    poster_src, slide_alt, w, h, loading=loading
                )
                trigger = _recent_work_lightbox_trigger(
                    img,
                    media_type="video",
                    full_src=video_src,
                    title=title,
                    ui=ui,
                    gallery_id=gallery_id,
                    index=slide_index,
                    poster_src=poster_src,
                )
            else:
                src = f"{prefix}{media_item['src']}"
                img = _recent_work_img_markup(src, slide_alt, w, h, loading=loading)
                trigger = _recent_work_lightbox_trigger(
                    img,
                    media_type="image",
                    full_src=src,
                    title=title,
                    ui=ui,
                    gallery_id=gallery_id,
                    index=slide_index,
                )
            slides.append(trigger)
            slide_index += 1
        return slides
    gallery_images = item.get("images") or [item["image"]]
    alts = copy.get("alts") or [copy["alt"]] * len(gallery_images)
    video_alts = copy.get("video_alts") or []
    for i, rel_path in enumerate(gallery_images):
        title = alts[i] if i < len(alts) else copy["alt"]
        slide_alt = html.escape(title)
        src = f"{prefix}{rel_path}"
        loading = "eager" if slide_index == 0 else "lazy"
        img = _recent_work_img_markup(src, slide_alt, w, h, loading=loading)
        trigger = _recent_work_lightbox_trigger(
            img,
            media_type="image",
            full_src=src,
            title=title,
            ui=ui,
            gallery_id=gallery_id,
            index=slide_index,
        )
        slides.append(trigger)
        slide_index += 1
    for vi, vid in enumerate(item.get("gallery_videos") or []):
        poster_src = f"{prefix}{vid['poster']}"
        video_src = f"{prefix}{vid['video']}"
        title = video_alts[vi] if vi < len(video_alts) else copy["alt"]
        slide_alt = html.escape(title)
        img = _recent_work_img_markup(poster_src, slide_alt, w, h, loading="lazy")
        trigger = _recent_work_lightbox_trigger(
            img,
            media_type="video",
            full_src=video_src,
            title=title,
            ui=ui,
            gallery_id=gallery_id,
            index=slide_index,
            poster_src=poster_src,
        )
        slides.append(trigger)
        slide_index += 1
    return slides


def _build_work_carousel_markup(slides: list[str], ui: dict, alt: str) -> str:
    if not slides:
        return ""
    if len(slides) == 1:
        return f"""                    <div class="work-carousel work-carousel--single" data-work-carousel>
                        <div class="work-carousel-track">
                            <div class="work-carousel-slide active">
                                {slides[0]}
                            </div>
                        </div>
                    </div>"""

    slide_blocks = []
    for i, slide_html in enumerate(slides):
        active = " active" if i == 0 else ""
        slide_blocks.append(
            f"""                            <div class="work-carousel-slide{active}">
                                {slide_html}
                            </div>"""
        )
    dot_blocks = []
    for i in range(len(slides)):
        active = " active" if i == 0 else ""
        n = i + 1
        dot_blocks.append(
            f"""                            <button type="button" class="work-carousel-dot{active}" """
            f"""data-slide-to="{i}" role="tab" aria-label="{n} / {len(slides)}" """
            f"""aria-selected="{"true" if i == 0 else "false"}"></button>"""
        )

    return f"""                    <div class="work-carousel" data-work-carousel>
                        <button type="button" class="work-carousel-btn work-carousel-prev" aria-label="{html.escape(ui["work_lightbox_prev"])}">‹</button>
                        <div class="work-carousel-track">
{chr(10).join(slide_blocks)}
                        </div>
                        <button type="button" class="work-carousel-btn work-carousel-next" aria-label="{html.escape(ui["work_lightbox_next"])}">›</button>
                        <div class="work-carousel-dots" role="tablist" aria-label="{html.escape(alt)}">
{chr(10).join(dot_blocks)}
                        </div>
                    </div>"""


def build_work_lightbox_markup(lang: str) -> str:
    ui = HOME_UI[lang]
    return f"""    <div class="work-lightbox" id="work-lightbox" aria-hidden="true">
        <div class="work-lightbox-backdrop" data-lightbox-close></div>
        <div class="work-lightbox-dialog" role="dialog" aria-modal="true" aria-label="{html.escape(ui["work_lightbox_dialog"])}" data-i18n-aria-label="work_lightbox_dialog">
            <button type="button" class="work-lightbox-close" id="work-lightbox-close" aria-label="{html.escape(ui["work_lightbox_close"])}" data-i18n-aria-label="work_lightbox_close">
                ×
            </button>
            <button type="button" class="work-lightbox-nav work-lightbox-prev" id="work-lightbox-prev" aria-label="{html.escape(ui["work_lightbox_prev"])}" data-i18n-aria-label="work_lightbox_prev" hidden>
                ‹
            </button>
            <button type="button" class="work-lightbox-nav work-lightbox-next" id="work-lightbox-next" aria-label="{html.escape(ui["work_lightbox_next"])}" data-i18n-aria-label="work_lightbox_next" hidden>
                ›
            </button>
            <div class="work-lightbox-counter" id="work-lightbox-counter" aria-live="polite" hidden></div>
            <div class="work-lightbox-content" id="work-lightbox-content"></div>
            <p class="work-lightbox-title" id="work-lightbox-title"></p>
        </div>
    </div>"""


def build_recent_work_section(lang: str) -> str:
    ui = HOME_UI[lang]
    prefix = asset_prefix(lang)
    cards = []
    for item in RECENT_WORK:
        copy = item[lang]
        img_src = f"{prefix}{item['image']}"
        w = item["width"]
        h = item["height"]
        alt = html.escape(copy["alt"])
        gallery_images = item.get("images")
        gallery_videos = item.get("gallery_videos")
        mixed_media = item.get("media")
        use_carousel = (
            (mixed_media and len(mixed_media) > 1)
            or (gallery_images and len(gallery_images) > 1)
            or gallery_videos
        )
        card_title = copy["title"]
        gallery_id = _recent_work_gallery_id(item)
        if use_carousel:
            slides = _recent_work_carousel_slides(item, copy, prefix, w, h, ui)
            media = _build_work_carousel_markup(slides, ui, copy["alt"])
        elif item.get("video"):
            img = _recent_work_img_markup(img_src, alt, w, h, loading="eager")
            trigger = _recent_work_lightbox_trigger(
                img,
                media_type="video",
                full_src=f"{prefix}{item['video']}",
                title=card_title,
                ui=ui,
                gallery_id=gallery_id,
                index=0,
                poster_src=img_src,
            )
            media = f"""                    {trigger}"""
        else:
            img = _recent_work_img_markup(img_src, alt, w, h, loading="lazy")
            trigger = _recent_work_lightbox_trigger(
                img,
                media_type="image",
                full_src=img_src,
                title=card_title,
                ui=ui,
                gallery_id=gallery_id,
                index=0,
            )
            media = f"""                    {trigger}"""
        href = f"{prefix}{item['slug']}"
        gallery_class = " recent-work-media-wrap--gallery" if use_carousel else ""
        cards.append(
            f"""                <article class="recent-work-card fade-in">
                    <div class="recent-work-media-wrap{gallery_class}">
{media}
                    </div>
                    <div class="recent-work-body">
                        <h3 class="recent-work-title">{html.escape(copy["title"])}</h3>
                        <dl class="recent-work-meta">
                            <div class="recent-work-meta-row">
                                <dt>{html.escape(ui["recent_work_zone"])}</dt>
                                <dd>{html.escape(copy["zone"])}</dd>
                            </div>
                            <div class="recent-work-meta-row">
                                <dt>{html.escape(ui["recent_work_service"])}</dt>
                                <dd>{html.escape(copy["service_type"])}</dd>
                            </div>
                        </dl>
                        <p class="recent-work-desc">{html.escape(copy["description"])}</p>
                        <a href="{href}" class="recent-work-link">{html.escape(ui["recent_work_link"])} <i class="fa-solid fa-chevron-right" aria-hidden="true"></i></a>
                    </div>
                </article>"""
        )
    grid = "\n\n".join(cards)
    return f"""    <section class="section section-light" id="recent-work">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title" data-i18n="recent_work_title">{html.escape(ui["recent_work_title"])}</h2>
                <p class="section-subtitle" data-i18n="recent_work_subtitle">{html.escape(ui["recent_work_subtitle"])}</p>
            </div>
            <div class="recent-work-grid" id="recent-work-grid">
{grid}
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
        "name": "FAZDETUDO.PT",
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


def build_service_cards(lang: str, prefix: str = "") -> str:
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
        is_hvac_pt = lang == "pt" and card["slug"] == "servico-climatizacao.html"
        is_cleaning_partner = card["slug"] == "servico-limpezas.html"
        partner_note = ""
        link_href = card["slug"]
        link_text = ui["learn_more"]
        secondary_link = ""
        show_default_link = True
        icon_html = (
            f'                    <div class="service-window-icon">'
            f'<i class="fa-solid fa-{card["icon"]}" aria-hidden="true"></i></div>'
        )
        if is_hvac_pt:
            feat = f"{feat} service-window-card--partner"
            badge = (
                '                    <span class="window-badge service-badge partner-recommended">'
                f'{ui["badge_parceiro_recomendado"]}</span>\n'
            )
            partner_note = f"""
                <div class="partner-mini-card">
                  <a class="partner-logo-pulse" href="https://airfix.pt/" target="_blank" rel="noopener" aria-label="Visitar AirFix.pt">
                    <span class="partner-pulse-ring" aria-hidden="true"></span>
                    <span class="partner-logo-circle">
                      <img src="{prefix}assets/partners/airfix-icon.png" alt="AirFix.pt" width="46" height="46" loading="lazy" decoding="async">
                    </span>
                  </a>

                  <div class="partner-mini-content">
                    <strong>AirFix.pt</strong>
                    <span>Especialista em ar condicionado</span>
                  </div>
                </div>

                <div class="partner-actions">
                  <a class="partner-primary-link" href="https://airfix.pt/" target="_blank" rel="noopener">
                    Ver parceiro AVAC
                    <span aria-hidden="true">›</span>
                  </a>

                  <a class="partner-secondary-link" href="servico-climatizacao.html">
                    Ver serviço FAZDETUDO
                    <span aria-hidden="true">›</span>
                  </a>
                </div>"""
            show_default_link = False
        if is_cleaning_partner:
            labels = CLEANING_PARTNER["labels"][lang]
            feat = f"{feat} service-window-card--cleaning-partner"
            badge = (
                '                    <span class="window-badge window-badge--cleaning-partner">'
                f'{html.escape(labels["badge"])}</span>\n'
            )
            icon_html = (
                '                    <div class="cleaning-partner-photo-wrap">\n'
                f'                      <img class="cleaning-partner-photo" '
                f'src="{prefix}assets/partners/caterina.jpg" '
                f'alt="{html.escape(CLEANING_PARTNER["name"], quote=True)}" '
                'width="96" height="96" loading="lazy" decoding="async">\n'
                '                    </div>'
            )
            partner_note = (
                '\n                    <div class="cleaning-partner-contact">'
                f'<span class="cleaning-partner-role">{html.escape(labels["role"])}</span>'
                f'<strong class="cleaning-partner-name">{html.escape(CLEANING_PARTNER["name"])}</strong>'
                f'<a class="cleaning-partner-call" href="{CLEANING_PARTNER["tel_href"]}" '
                f'aria-label="{html.escape(labels["aria"], quote=True)}">'
                '<i class="fa-solid fa-phone" aria-hidden="true"></i>'
                f'<span>{html.escape(labels["call"])}</span>'
                f'<strong>{html.escape(CLEANING_PARTNER["phone_display"])}</strong>'
                '</a>'
                f'<a class="cleaning-partner-call cleaning-partner-whatsapp" href="{CLEANING_PARTNER["whatsapp_href"]}" '
                'target="_blank" rel="noopener noreferrer" aria-label="Contactar Caterina por WhatsApp">'
                '<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
                '<span>WhatsApp</span>'
                '</a>'
                '</div>'
            )
            link_text = labels["details"]
        default_link = ""
        if show_default_link:
            default_link = (
                f'                    <a href="{link_href}" class="service-window-link">'
                f'{link_text} <i class="fa-solid fa-chevron-right" aria-hidden="true"></i></a>'
                f'{secondary_link}'
            )
        blocks.append(
            f"""                <div class="service-window-card{feat}">
{badge}{icon_html}
                    <h3>{title}</h3>
                    <p>{desc}</p>
{partner_note}
{default_link}
                </div>"""
        )
    return "\n\n".join(blocks)


def build_hvac_partner_block(lang: str, prefix: str) -> str:
    # Bloco grande removido: o destaque AirFix fica só no mini-card do serviço AVAC.
    return ""


def _build_partner_directory_card(partner: dict, lang: str, prefix: str) -> str:
    copy = partner["copy"][lang]
    category_id = partner["category"]
    category_label = PARTNER_CATEGORIES[category_id][lang]
    name = html.escape(partner["name"])
    cat_esc = html.escape(category_label)
    card_class = f'partner-dir-card partner-dir-card--{html.escape(partner["type"])}'
    status_flags = []
    if partner.get("recommended"):
        status_flags.append("recommended")
    if partner.get("featured"):
        status_flags.append("featured")
    status_attr = " ".join(status_flags) if status_flags else "partner"

    badges_html = []
    for key in partner_badge_keys(partner):
        label = PARTNER_STATUS_LABELS[key][lang]
        mod = key.replace("_f", "")
        badges_html.append(
            f'<span class="partner-dir-badge partner-dir-badge--{html.escape(mod)}">'
            f"{html.escape(label)}</span>"
        )
    badges_block = "\n                            ".join(badges_html)

    if partner["type"] == "external":
        logo_src = html.escape(f'{prefix}{partner["logo"]}', quote=True)
        website = html.escape(partner["website"], quote=True)
        service_href = html.escape(partner["service_slug"], quote=True)
        return f"""                <article class="{card_class}" data-partner-category="{html.escape(category_id)}" data-partner-id="{html.escape(partner["id"])}" data-partner-status="{html.escape(status_attr)}" hidden>
                    <div class="partner-dir-media">
                        <img src="{logo_src}" alt="{name}" width="72" height="72" loading="lazy" decoding="async">
                    </div>
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-blurb">{html.escape(copy["blurb"])}</p>
                        <div class="partner-dir-actions">
                            <a class="partner-dir-btn partner-dir-btn--primary" href="{website}" target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}">{html.escape(copy["primary_cta"])}</a>
                            <a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">{html.escape(copy["secondary_cta"])}</a>
                        </div>
                    </div>
                </article>"""

    # direct_contact (e.g. Caterina)
    photo_src = html.escape(f'{prefix}{partner["photo"]}', quote=True)
    tel_href_val = html.escape(partner["tel_href"], quote=True)
    wa_href_val = html.escape(partner["whatsapp_href"], quote=True)
    service_href = html.escape(partner["service_slug"], quote=True)
    return f"""                <article class="{card_class}" data-partner-category="{html.escape(category_id)}" data-partner-id="{html.escape(partner["id"])}" data-partner-status="{html.escape(status_attr)}" hidden>
                    <div class="partner-dir-media partner-dir-media--photo">
                        <img src="{photo_src}" alt="{name}" width="96" height="96" loading="lazy" decoding="async">
                    </div>
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-role">{html.escape(copy["role"])}</p>
                        <p class="partner-dir-phone">{html.escape(partner["phone_display"])}</p>
                        <div class="partner-dir-actions">
                            <a class="partner-dir-btn partner-dir-btn--call" href="{tel_href_val}" aria-label="{html.escape(copy["call_aria"])}">
                                <i class="fa-solid fa-phone" aria-hidden="true"></i>
                                <span>{html.escape(copy["call"])}</span>
                            </a>
                            <a class="partner-dir-btn partner-dir-btn--whatsapp" href="{wa_href_val}" target="_blank" rel="noopener noreferrer" aria-label="{html.escape(copy["wa_aria"])}">
                                <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
                                <span>{html.escape(copy["whatsapp"])}</span>
                            </a>
                            <a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">{html.escape(copy["secondary_cta"])}</a>
                        </div>
                    </div>
                </article>"""


def build_partner_directory_section(lang: str, prefix: str = "") -> str:
    """Client-facing partner search bar + on-demand results (after hero)."""
    ui = PARTNER_DIRECTORY_UI[lang]
    options = [
        f'                            <option value="" selected>{html.escape(ui["select_placeholder"])}</option>'
    ]
    for cat_id in FILTER_CATEGORY_IDS:
        label = PARTNER_CATEGORIES[cat_id][lang]
        options.append(
            f'                            <option value="{html.escape(cat_id)}">{html.escape(label)}</option>'
        )
    cards = "\n".join(
        _build_partner_directory_card(p, lang, prefix) for p in active_partners()
    )
    return f"""    <section class="partner-directory-section" id="parceiros-recomendados" aria-labelledby="partner-directory-title">
        <div class="container">
            <div class="partner-directory-bar" id="partner-directory-bar">
                <div class="partner-directory-bar-title">
                    <span class="partner-directory-bar-icon" aria-hidden="true"><i class="fa-solid fa-star"></i></span>
                    <div>
                        <h2 id="partner-directory-title">{html.escape(ui["title"])}</h2>
                        <p>{html.escape(ui["subtitle"])}</p>
                    </div>
                </div>
                <div class="partner-directory-bar-controls">
                    <label class="partner-directory-select-wrap" for="partner-category-select">
                        <span class="partner-directory-field-label">{html.escape(ui["select_label"])}</span>
                        <select id="partner-category-select" name="category" aria-label="{html.escape(ui["select_aria"])}">
{chr(10).join(options)}
                        </select>
                    </label>
                </div>
            </div>
            <div class="partner-directory-results" id="partner-directory-results" hidden aria-live="polite" aria-label="{html.escape(ui["results_aria"])}">
                <div class="partner-directory-grid" id="partner-directory-grid">
{cards}
                </div>
                <p class="partner-directory-empty" id="partner-directory-empty" hidden>{html.escape(ui["empty"])}</p>
            </div>
        </div>
    </section>"""


def build_how_it_works_section(lang: str) -> str:
    copy = HOW_IT_WORKS[lang]
    steps = []
    for num, icon, title, text in copy["steps"]:
        steps.append(
            f"""                <div class="how-it-works-step">
                    <div class="how-it-works-step-top">
                        <span class="how-it-works-num" aria-hidden="true">{html.escape(num)}</span>
                        <span class="how-it-works-icon" aria-hidden="true"><i class="fa-solid fa-{html.escape(icon)}"></i></span>
                    </div>
                    <h3>{html.escape(title)}</h3>
                    <p>{html.escape(text)}</p>
                </div>"""
        )
    return f"""    <section class="how-it-works-section" id="como-funciona" aria-labelledby="how-it-works-title">
        <div class="container">
            <div class="how-it-works-header">
                <h2 id="how-it-works-title">{html.escape(copy["title"])}</h2>
            </div>
            <div class="how-it-works-grid">
{chr(10).join(steps)}
            </div>
        </div>
    </section>"""


def build_partner_recruit_section(lang: str) -> str:
    """Secção para angariar profissionais/parceiros (mensalidade)."""
    copy = PARTNER_RECRUIT[lang]
    wa_link = wa_href_for_message(copy["wa_message"])
    benefits = []
    for icon, title, text in copy["benefits"]:
        benefits.append(
            f"""                <div class="partner-recruit-benefit">
                    <div class="partner-recruit-benefit-icon" aria-hidden="true">
                        <i class="fa-solid fa-{html.escape(icon)}"></i>
                    </div>
                    <h3>{html.escape(title)}</h3>
                    <p>{html.escape(text)}</p>
                </div>"""
        )
    benefits_html = "\n".join(benefits)
    return f"""    <section class="partner-recruit-section" id="tornar-parceiro" aria-labelledby="partner-recruit-title">
        <div class="container">
            <div class="partner-recruit-panel">
                <span class="partner-recruit-badge">{html.escape(copy["badge"])}</span>
                <h2 id="partner-recruit-title">{html.escape(copy["title"])}</h2>
                <p class="partner-recruit-lead">{html.escape(copy["text"])}</p>
                <div class="partner-recruit-benefits">
{benefits_html}
                </div>
                <div class="partner-recruit-cta-wrap">
                    <a href="{html.escape(wa_link, quote=True)}"
                       class="btn btn-lg partner-recruit-cta"
                       target="_blank"
                       rel="noopener noreferrer"
                       aria-label="{html.escape(copy["cta_aria"])}">
                        <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
                        <span>{html.escape(copy["cta"])}</span>
                    </a>
                    <p class="partner-recruit-note">{html.escape(copy["note"])}</p>
                </div>
            </div>
        </div>
    </section>"""


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
    ui = HOME_UI[lang]
    html = html.replace('aria-label="Navegação principal"', f'aria-label="{meta["nav_aria"]}"')
    html = html.replace('alt="FAZDETUDO.PT - Serviços de handyman em Lisboa"', f'alt="{meta["logo_alt"]}"')
    html = html.replace('alt="Profissional faz tudo"', f'alt="{meta["section_logo_alt"]}"')
    html = html.replace('aria-label="Open menu"', f'aria-label="{meta["menu_aria"]}"')
    html = html.replace('aria-label="Crítica anterior"', f'aria-label="{meta["review_prev"]}"')
    html = html.replace('aria-label="Crítica seguinte"', f'aria-label="{meta["review_next"]}"')
    html = html.replace('aria-label="Fechar chat"', f'aria-label="{meta["wa_close"]}"')
    html = html.replace('aria-label="Enviar mensagem"', f'aria-label="{meta["wa_send"]}"')
    html = html.replace('aria-label="Contact via WhatsApp"', f'aria-label="{meta["wa_float"]}"')
    html = html.replace('aria-label="Ligar agora"', f'aria-label="{meta["float_call"]}"')
    html = html.replace('aria-label="Localizações"', f'aria-label="{ui["contact_locations_aria"]}"')
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
    canonical = home_url(lang)

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
    home_wa_message = HOME_WA_MESSAGE.get(lang, HOME_WA_MESSAGE["pt"])
    wa_message_attr = html.escape(home_wa_message, quote=True)

    page_html = render_template(
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
            "PARTNER_DIRECTORY_SECTION": build_partner_directory_section(lang, prefix),
            "HOW_IT_WORKS_SECTION": build_how_it_works_section(lang),
            "SERVICE_CARDS": build_service_cards(lang, prefix),
            "HVAC_PARTNER_BLOCK": build_hvac_partner_block(lang, prefix),
            "PARTNER_RECRUIT_SECTION": build_partner_recruit_section(lang),
            "HANDYMAN_SECTION": build_handyman_section(lang),
            "RECENT_WORK_SECTION": build_recent_work_section(lang),
            "WORK_LIGHTBOX": build_work_lightbox_markup(lang),
            "ADVANTAGES_GRID": build_advantages_grid(lang),
            "TESTIMONIALS_SUMMARY": build_testimonials_summary(lang),
            "TESTIMONIALS_CARDS": build_testimonials_cards(lang),
            "TESTIMONIALS_FOOTER": build_testimonials_footer(lang),
            "FAQ_LIST": build_faq_list(lang),
            "WA_HREF": wa_href_home(lang),
            "WA_MESSAGE_ATTR": wa_message_attr,
            "TEL_HREF": tel_href(),
            "PHONE_DISPLAY": PHONE_DISPLAY,
            "GOOGLE_REVIEWS_URL": GOOGLE_REVIEWS_URL,
            "PRIMARY_OFFICE_STREET_LINE1": PRIMARY_OFFICE_STREET_LINE1,
            "PRIMARY_OFFICE_STREET_LINE2": PRIMARY_OFFICE_STREET_LINE2,
            "SECOND_OFFICE_STREET_LINE1": SECOND_OFFICE_STREET_LINE1,
            "SECOND_OFFICE_STREET_LINE2": SECOND_OFFICE_STREET_LINE2,
        },
    )
    page_html = apply_i18n_attributes(page_html, lang)
    page_html = apply_meta_strings(page_html, lang)
    return page_html


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
