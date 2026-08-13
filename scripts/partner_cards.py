# -*- coding: utf-8 -*-
"""Shared HTML builders for partner directory cards."""

from __future__ import annotations

import html

from recommended_partners import (
    PARTNER_CATEGORIES,
    PARTNER_STATUS_LABELS,
    partner_badge_keys,
    partner_category_ids,
    partner_zone_ids,
)
from slug_registry import service_page_href


def build_partner_directory_card(
    partner: dict,
    lang: str,
    prefix: str,
    *,
    hidden: bool = True,
    extra_class: str = "",
    show_secondary_cta: bool = True,
) -> str:
    """Render one partner card (homepage directory, /parceiros/, or service page).

    When show_secondary_cta is False (embedded on a service page), omit
    “Ver serviço” / secondary links that would loop back to the same page.
    """
    copy = partner["copy"][lang]
    category_id = partner["category"]
    category_ids = partner_category_ids(partner) or (
        [category_id] if category_id in PARTNER_CATEGORIES else []
    )
    category_label = PARTNER_CATEGORIES[category_id][lang]
    name = html.escape(partner["name"])
    cat_esc = html.escape(category_label)
    card_classes = [
        "partner-dir-card",
        f'partner-dir-card--{html.escape(partner["type"])}',
    ]
    if extra_class:
        card_classes.append(extra_class)
    card_class = " ".join(card_classes)

    status_flags = []
    if partner.get("recommended"):
        status_flags.append("recommended")
    if partner.get("featured"):
        status_flags.append("featured")
    status_attr = " ".join(status_flags) if status_flags else "partner"

    zones = partner_zone_ids(partner)
    zones_attr = html.escape(" ".join(zones), quote=True)
    categories_attr = html.escape(" ".join(category_ids), quote=True)

    badges_html = []
    for key in partner_badge_keys(partner):
        label = PARTNER_STATUS_LABELS[key][lang]
        mod = key.replace("_f", "")
        badges_html.append(
            f'<span class="partner-dir-badge partner-dir-badge--{html.escape(mod)}">'
            f"{html.escape(label)}</span>"
        )
    badges_block = "\n                            ".join(badges_html)

    hidden_attr = " hidden" if hidden else ""
    service_href = html.escape(
        service_page_href(partner["service_slug"], lang), quote=True
    )
    data_attrs = (
        f'data-partner-category="{html.escape(category_id)}" '
        f'data-partner-categories="{categories_attr}" '
        f'data-partner-zones="{zones_attr}" '
        f'data-partner-id="{html.escape(partner["id"])}" '
        f'data-partner-status="{html.escape(status_attr)}"'
    )

    location_html = ""
    if partner.get("location"):
        loc = partner["location"].get(lang) or partner["location"].get("pt")
        if loc:
            location_html = (
                f'\n                        <p class="partner-dir-location">'
                f'<i class="fa-solid fa-location-dot" aria-hidden="true"></i> '
                f"{html.escape(loc)}</p>"
            )

    secondary_cta = ""
    if show_secondary_cta:
        secondary_cta = (
            f'<a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">'
            f'{html.escape(copy["secondary_cta"])}</a>'
        )

    if partner["type"] == "external":
        website = html.escape(partner["website"], quote=True)
        logo = partner.get("logo")
        if logo:
            logo_src = html.escape(f"{prefix}{logo}", quote=True)
            wide = " partner-dir-media--wide" if partner.get("logo_wide") else ""
            media_html = (
                f'<div class="partner-dir-media{wide}">'
                f'<img src="{logo_src}" alt="{name}" width="72" height="72" '
                f'loading="lazy" decoding="async"></div>'
            )
        else:
            icon = html.escape(partner.get("icon") or "tv")
            media_html = (
                '<div class="partner-dir-media partner-dir-media--icon" aria-hidden="true">'
                f'<i class="fa-solid fa-{icon}"></i></div>'
            )
        actions = [
            f'<a class="partner-dir-btn partner-dir-btn--primary" href="{website}" '
            f'target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}">'
            f'{html.escape(copy["primary_cta"])}</a>'
        ]
        if secondary_cta:
            actions.append(secondary_cta)
        actions_html = "\n                            ".join(actions)
        return f"""                <article class="{card_class}" {data_attrs}{hidden_attr}>
                    {media_html}
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-blurb">{html.escape(copy["blurb"])}</p>{location_html}
                        <div class="partner-dir-actions">
                            {actions_html}
                        </div>
                    </div>
                </article>"""

    photo = partner.get("photo")
    logo = partner.get("logo")
    if logo:
        logo_src = html.escape(f"{prefix}{logo}", quote=True)
        media_html = (
            f'<div class="partner-dir-media">'
            f'<img src="{logo_src}" alt="{name}" width="72" height="72" '
            f'loading="lazy" decoding="async"></div>'
        )
    elif photo:
        photo_src = html.escape(f"{prefix}{photo}", quote=True)
        media_html = (
            f'<div class="partner-dir-media partner-dir-media--photo">'
            f'<img src="{photo_src}" alt="{name}" width="96" height="96" '
            f'loading="lazy" decoding="async"></div>'
        )
    else:
        icon = html.escape(partner.get("icon") or "helmet-safety")
        media_html = (
            '<div class="partner-dir-media partner-dir-media--icon '
            'partner-dir-media--fallback" aria-hidden="true">'
            f'<i class="fa-solid fa-{icon}"></i></div>'
        )

    tel_href_val = html.escape(partner["tel_href"], quote=True)
    actions = [
        f'<a class="partner-dir-btn partner-dir-btn--call" href="{tel_href_val}" '
        f'aria-label="{html.escape(copy["call_aria"])}">'
        f'<i class="fa-solid fa-phone" aria-hidden="true"></i>'
        f'<span>{html.escape(copy["call"])}</span></a>'
    ]
    wa_href = partner.get("whatsapp_href")
    if wa_href:
        wa_href_val = html.escape(wa_href, quote=True)
        wa_label = html.escape(copy.get("whatsapp", "WhatsApp"))
        wa_aria = html.escape(copy.get("wa_aria", wa_label))
        actions.append(
            f'<a class="partner-dir-btn partner-dir-btn--whatsapp" href="{wa_href_val}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="{wa_aria}">'
            f'<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
            f'<span>{wa_label}</span></a>'
        )
    if secondary_cta:
        actions.append(secondary_cta)
    actions_html = "\n                            ".join(actions)

    return f"""                <article class="{card_class}" {data_attrs}{hidden_attr}>
                    {media_html}
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-role">{html.escape(copy["role"])}</p>{location_html}
                        <p class="partner-dir-phone">{html.escape(partner["phone_display"])}</p>
                        <div class="partner-dir-actions">
                            {actions_html}
                        </div>
                    </div>
                </article>"""


def build_partner_sidebar_card(
    partner: dict,
    lang: str,
    prefix: str,
) -> str:
    """Compact partner card for service-page sidebar / mobile insert."""
    copy = partner["copy"][lang]
    category_id = partner["category"]
    category_label = PARTNER_CATEGORIES[category_id][lang]
    name = html.escape(partner["name"])
    cat_esc = html.escape(category_label)

    badges_html = []
    for key in partner_badge_keys(partner):
        label = PARTNER_STATUS_LABELS[key][lang]
        mod = key.replace("_f", "")
        badges_html.append(
            f'<span class="partner-dir-badge partner-dir-badge--{html.escape(mod)}">'
            f"{html.escape(label)}</span>"
        )
    badges_block = "".join(badges_html)

    location_html = ""
    if partner.get("location"):
        loc = partner["location"].get(lang) or partner["location"].get("pt")
        if loc:
            location_html = (
                f'<p class="partner-sidebar-location">'
                f'<i class="fa-solid fa-location-dot" aria-hidden="true"></i> '
                f"{html.escape(loc)}</p>"
            )

    if partner["type"] == "external":
        website = html.escape(partner["website"], quote=True)
        logo = partner.get("logo")
        if logo:
            logo_src = html.escape(f"{prefix}{logo}", quote=True)
            wide = " partner-sidebar-media--wide" if partner.get("logo_wide") else ""
            media_html = (
                f'<div class="partner-sidebar-media{wide}">'
                f'<img src="{logo_src}" alt="" width="56" height="56" '
                f'loading="lazy" decoding="async"></div>'
            )
        else:
            icon = html.escape(partner.get("icon") or "tv")
            media_html = (
                '<div class="partner-sidebar-media partner-sidebar-media--icon" aria-hidden="true">'
                f'<i class="fa-solid fa-{icon}"></i></div>'
            )
        actions = (
            f'<a class="partner-dir-btn partner-dir-btn--primary" href="{website}" '
            f'target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}">'
            f'{html.escape(copy["primary_cta"])}</a>'
        )
        blurb = html.escape(copy.get("blurb", ""))
        blurb_html = f'<p class="partner-sidebar-blurb">{blurb}</p>' if blurb else ""
        return f"""                    <article class="partner-sidebar-card partner-sidebar-card--external" data-partner-id="{html.escape(partner["id"])}">
                        <div class="partner-sidebar-top">
                            {media_html}
                            <div class="partner-sidebar-meta">
                                {badges_block}
                                <h3 class="partner-sidebar-name">{name}</h3>
                                <p class="partner-sidebar-category">{cat_esc}</p>
                            </div>
                        </div>
                        {blurb_html}{location_html}
                        <div class="partner-sidebar-actions">{actions}</div>
                    </article>"""

    photo = partner.get("photo")
    logo = partner.get("logo")
    if logo:
        logo_src = html.escape(f"{prefix}{logo}", quote=True)
        media_html = (
            f'<div class="partner-sidebar-media">'
            f'<img src="{logo_src}" alt="" width="56" height="56" '
            f'loading="lazy" decoding="async"></div>'
        )
    elif photo:
        photo_src = html.escape(f"{prefix}{photo}", quote=True)
        media_html = (
            f'<div class="partner-sidebar-media partner-sidebar-media--photo">'
            f'<img src="{photo_src}" alt="" width="56" height="56" '
            f'loading="lazy" decoding="async"></div>'
        )
    else:
        icon = html.escape(partner.get("icon") or "helmet-safety")
        media_html = (
            '<div class="partner-sidebar-media partner-sidebar-media--icon" aria-hidden="true">'
            f'<i class="fa-solid fa-{icon}"></i></div>'
        )

    actions = [
        f'<a class="partner-dir-btn partner-dir-btn--call" href="{html.escape(partner["tel_href"], quote=True)}" '
        f'aria-label="{html.escape(copy["call_aria"])}">'
        f'<i class="fa-solid fa-phone" aria-hidden="true"></i>'
        f'<span>{html.escape(copy["call"])}</span></a>'
    ]
    if partner.get("whatsapp_href"):
        wa_label = html.escape(copy.get("whatsapp", "WhatsApp"))
        wa_aria = html.escape(copy.get("wa_aria", wa_label))
        actions.append(
            f'<a class="partner-dir-btn partner-dir-btn--whatsapp" '
            f'href="{html.escape(partner["whatsapp_href"], quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="{wa_aria}">'
            f'<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
            f'<span>{wa_label}</span></a>'
        )
    actions_html = "".join(actions)
    phone_html = (
        f'<p class="partner-sidebar-phone">{html.escape(partner["phone_display"])}</p>'
    )

    return f"""                    <article class="partner-sidebar-card partner-sidebar-card--direct" data-partner-id="{html.escape(partner["id"])}">
                        <div class="partner-sidebar-top">
                            {media_html}
                            <div class="partner-sidebar-meta">
                                {badges_block}
                                <h3 class="partner-sidebar-name">{name}</h3>
                                <p class="partner-sidebar-category">{cat_esc}</p>
                            </div>
                        </div>
                        {location_html}
                        {phone_html}
                        <div class="partner-sidebar-actions">{actions_html}</div>
                    </article>"""
