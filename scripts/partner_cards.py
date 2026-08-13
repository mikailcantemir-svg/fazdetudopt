# -*- coding: utf-8 -*-
"""Shared HTML builders for partner directory cards."""

from __future__ import annotations

import html

from recommended_partners import (
    PARTNER_CATEGORIES,
    PARTNER_PROFILE_UI,
    PARTNER_STATUS_LABELS,
    partner_badge_keys,
    partner_category_ids,
    partner_has_profile,
    partner_languages_compact_prefix,
    partner_profile_href,
    partner_spoken_languages_display,
    partner_whatsapp_href,
    partner_zone_ids,
)
from slug_registry import service_page_href


def _partner_track_attrs(
    partner: dict,
    *,
    contact_method: str,
    source_context: str,
) -> str:
    """Structured analytics attrs — never include phone numbers or messages."""
    return (
        'data-track="partner_contact" '
        f'data-partner-id="{html.escape(partner["id"], quote=True)}" '
        f'data-partner-category="{html.escape(partner["category"], quote=True)}" '
        f'data-contact-method="{html.escape(contact_method, quote=True)}" '
        f'data-source-context="{html.escape(source_context, quote=True)}"'
    )


def _infer_source_context(extra_class: str) -> str:
    classes = extra_class or ""
    if "partner-dir-card--finder" in classes:
        return "homepage_partner_finder"
    if "partners-listing-card" in classes:
        return "partners_directory"
    if "article-partner-card" in classes:
        return "article"
    return "partners_directory"


def _spoken_languages_items_html(partner: dict, lang: str) -> str:
    """Flag + label chips; flags are decorative (aria-hidden)."""
    items = partner_spoken_languages_display(partner, lang)
    if not items:
        return ""
    parts: list[str] = []
    for item in items:
        parts.append(
            '<span class="partner-lang">'
            f'<span class="partner-lang-flag" aria-hidden="true">'
            f'{html.escape(item["flag"])}</span>'
            f'<span class="partner-lang-label">{html.escape(item["label"])}</span>'
            "</span>"
        )
    return '<span class="partner-lang-sep" aria-hidden="true"> · </span>'.join(parts)


def _languages_line_html(
    partner: dict,
    lang: str,
    *,
    css_class: str,
) -> str:
    """Discreet languages line for cards/sidebars; empty when unknown."""
    items_html = _spoken_languages_items_html(partner, lang)
    if not items_html:
        return ""
    prefix = partner_languages_compact_prefix(partner, lang) or ""
    prefix_html = (
        f'<span class="partner-lang-prefix">{html.escape(prefix)}</span> '
        if prefix
        else ""
    )
    return (
        f'<p class="{css_class}">'
        f'<i class="fa-solid fa-language" aria-hidden="true"></i> '
        f"{prefix_html}{items_html}</p>"
    )


def _profile_action(partner: dict, lang: str, *, source_context: str) -> str:
    if not partner_has_profile(partner):
        return ""
    href = partner_profile_href(partner, lang)
    if not href:
        return ""
    ui = PARTNER_PROFILE_UI[lang]
    label = ui["profile_cta"]
    aria = ui["profile_aria"].format(name=partner["name"])
    track = _partner_track_attrs(
        partner, contact_method="profile", source_context=source_context
    )
    return (
        f'<a class="partner-dir-btn partner-dir-btn--secondary" '
        f'href="{html.escape(href, quote=True)}" '
        f'aria-label="{html.escape(aria, quote=True)}" {track}>'
        f"{html.escape(label)}</a>"
    )


def _profile_text_link(
    partner: dict, lang: str, *, css_class: str, source_context: str
) -> str:
    if not partner_has_profile(partner):
        return ""
    href = partner_profile_href(partner, lang)
    if not href:
        return ""
    ui = PARTNER_PROFILE_UI[lang]
    label = ui["profile_cta"]
    aria = ui["profile_aria"].format(name=partner["name"])
    track = _partner_track_attrs(
        partner, contact_method="profile", source_context=source_context
    )
    return (
        f'<a class="{css_class}" href="{html.escape(href, quote=True)}" '
        f'aria-label="{html.escape(aria, quote=True)}" {track}>'
        f"{html.escape(label)}</a>"
    )


def build_partner_directory_card(
    partner: dict,
    lang: str,
    prefix: str,
    *,
    hidden: bool = True,
    extra_class: str = "",
    show_secondary_cta: bool = True,
    source_context: str | None = None,
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
    ctx = source_context or _infer_source_context(extra_class)

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
        f'data-partner-status="{html.escape(status_attr)}" '
        f'data-source-context="{html.escape(ctx, quote=True)}"'
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
    languages_html = ""
    languages_line = _languages_line_html(
        partner, lang, css_class="partner-dir-languages"
    )
    if languages_line:
        languages_html = f"\n                        {languages_line}"

    secondary_cta = ""
    if show_secondary_cta:
        secondary_cta = (
            f'<a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">'
            f'{html.escape(copy["secondary_cta"])}</a>'
        )
    profile_cta = _profile_action(partner, lang, source_context=ctx)

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
        web_track = _partner_track_attrs(
            partner, contact_method="website", source_context=ctx
        )
        actions = [
            f'<a class="partner-dir-btn partner-dir-btn--primary" href="{website}" '
            f'target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}" '
            f"{web_track}>"
            f'{html.escape(copy["primary_cta"])}</a>'
        ]
        profile_footer = ""
        if "partner-dir-card--finder" in (extra_class or ""):
            text_link = _profile_text_link(
                partner,
                lang,
                css_class="partner-dir-profile-link",
                source_context=ctx,
            )
            if text_link:
                profile_footer = f"\n                        {text_link}"
        elif profile_cta:
            actions.append(profile_cta)
        elif secondary_cta:
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
                        <p class="partner-dir-blurb">{html.escape(copy["blurb"])}</p>{location_html}{languages_html}
                        <div class="partner-dir-actions">
                            {actions_html}
                        </div>{profile_footer}
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
    phone_track = _partner_track_attrs(
        partner, contact_method="phone", source_context=ctx
    )
    actions = [
        f'<a class="partner-dir-btn partner-dir-btn--call" href="{tel_href_val}" '
        f'aria-label="{html.escape(copy["call_aria"])}" {phone_track}>'
        f'<i class="fa-solid fa-phone" aria-hidden="true"></i>'
        f'<span>{html.escape(copy["call"])}</span></a>'
    ]
    wa_href = partner_whatsapp_href(partner, lang)
    if wa_href:
        wa_href_val = html.escape(wa_href, quote=True)
        wa_label = html.escape(copy.get("whatsapp", "WhatsApp"))
        wa_aria = html.escape(copy.get("wa_aria", wa_label))
        wa_track = _partner_track_attrs(
            partner, contact_method="whatsapp", source_context=ctx
        )
        actions.append(
            f'<a class="partner-dir-btn partner-dir-btn--whatsapp" href="{wa_href_val}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="{wa_aria}" {wa_track}>'
            f'<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
            f'<span>{wa_label}</span></a>'
        )
    if profile_cta and "partner-dir-card--finder" not in (extra_class or ""):
        actions.append(profile_cta)
    elif (not profile_cta) and secondary_cta:
        actions.append(secondary_cta)
    actions_html = "\n                            ".join(actions)

    profile_footer = ""
    if "partner-dir-card--finder" in (extra_class or ""):
        text_link = _profile_text_link(
            partner,
            lang,
            css_class="partner-dir-profile-link",
            source_context=ctx,
        )
        if text_link:
            profile_footer = f"\n                        {text_link}"

    return f"""                <article class="{card_class}" {data_attrs}{hidden_attr}>
                    {media_html}
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-role">{html.escape(copy["role"])}</p>{location_html}{languages_html}
                        <p class="partner-dir-phone">{html.escape(partner["phone_display"])}</p>
                        <div class="partner-dir-actions">
                            {actions_html}
                        </div>{profile_footer}
                    </div>
                </article>"""


def build_partner_sidebar_card(
    partner: dict,
    lang: str,
    prefix: str,
    *,
    source_context: str = "service_page",
) -> str:
    """Compact partner card for service-page sidebar / mobile insert."""
    copy = partner["copy"][lang]
    category_id = partner["category"]
    category_label = PARTNER_CATEGORIES[category_id][lang]
    name = html.escape(partner["name"])
    cat_esc = html.escape(category_label)
    ctx = source_context
    partner_data = (
        f'data-partner-id="{html.escape(partner["id"])}" '
        f'data-partner-category="{html.escape(category_id)}" '
        f'data-source-context="{html.escape(ctx, quote=True)}"'
    )

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
    languages_html = _languages_line_html(
        partner, lang, css_class="partner-sidebar-languages"
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
        web_track = _partner_track_attrs(
            partner, contact_method="website", source_context=ctx
        )
        actions = (
            f'<a class="partner-dir-btn partner-dir-btn--primary" href="{website}" '
            f'target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}" '
            f"{web_track}>"
            f'{html.escape(copy["primary_cta"])}</a>'
        )
        profile_link = _profile_text_link(
            partner,
            lang,
            css_class="partner-sidebar-profile",
            source_context=ctx,
        )
        profile_block = f"\n                        {profile_link}" if profile_link else ""
        blurb = html.escape(copy.get("blurb", ""))
        blurb_html = f'<p class="partner-sidebar-blurb">{blurb}</p>' if blurb else ""
        return f"""                    <article class="partner-sidebar-card partner-sidebar-card--external" {partner_data}>
                        <div class="partner-sidebar-top">
                            {media_html}
                            <div class="partner-sidebar-meta">
                                {badges_block}
                                <h3 class="partner-sidebar-name">{name}</h3>
                                <p class="partner-sidebar-category">{cat_esc}</p>{profile_block}
                            </div>
                        </div>
                        {blurb_html}{location_html}{languages_html}
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

    phone_track = _partner_track_attrs(
        partner, contact_method="phone", source_context=ctx
    )
    actions = [
        f'<a class="partner-dir-btn partner-dir-btn--call" href="{html.escape(partner["tel_href"], quote=True)}" '
        f'aria-label="{html.escape(copy["call_aria"])}" {phone_track}>'
        f'<i class="fa-solid fa-phone" aria-hidden="true"></i>'
        f'<span>{html.escape(copy["call"])}</span></a>'
    ]
    wa_href = partner_whatsapp_href(partner, lang)
    if wa_href:
        wa_label = html.escape(copy.get("whatsapp", "WhatsApp"))
        wa_aria = html.escape(copy.get("wa_aria", wa_label))
        wa_track = _partner_track_attrs(
            partner, contact_method="whatsapp", source_context=ctx
        )
        actions.append(
            f'<a class="partner-dir-btn partner-dir-btn--whatsapp" '
            f'href="{html.escape(wa_href, quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" aria-label="{wa_aria}" {wa_track}>'
            f'<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
            f'<span>{wa_label}</span></a>'
        )
    actions_html = "".join(actions)
    phone_html = (
        f'<p class="partner-sidebar-phone">{html.escape(partner["phone_display"])}</p>'
    )
    profile_link = _profile_text_link(
        partner,
        lang,
        css_class="partner-sidebar-profile",
        source_context=ctx,
    )
    profile_block = f"\n                        {profile_link}" if profile_link else ""

    return f"""                    <article class="partner-sidebar-card partner-sidebar-card--direct" {partner_data}>
                        <div class="partner-sidebar-top">
                            {media_html}
                            <div class="partner-sidebar-meta">
                                {badges_block}
                                <h3 class="partner-sidebar-name">{name}</h3>
                                <p class="partner-sidebar-category">{cat_esc}</p>{profile_block}
                            </div>
                        </div>
                        {location_html}
                        {languages_html}
                        {phone_html}
                        <div class="partner-sidebar-actions">{actions_html}</div>
                    </article>"""
