# -*- coding: utf-8 -*-
"""Reusable HTML fragments for page generators."""

from __future__ import annotations

from pathlib import Path

PARTIALS_DIR = Path(__file__).resolve().parent / "partials"


def load_partial(name: str) -> str:
    path = PARTIALS_DIR / name
    return path.read_text(encoding="utf-8")


def render_wa_widget(
    *,
    asset_prefix: str,
    wa_online: str,
    wa_greeting: str,
    wa_placeholder: str,
    wa_close: str,
    wa_send: str,
    wa_float_label: str,
) -> str:
    return (
        load_partial("wa-widget.html")
        .replace("{{ASSET_PREFIX}}", asset_prefix)
        .replace("{{WA_ONLINE}}", wa_online)
        .replace("{{WA_GREETING}}", wa_greeting)
        .replace("{{WA_PLACEHOLDER}}", wa_placeholder)
        .replace("{{WA_CLOSE}}", wa_close)
        .replace("{{WA_SEND}}", wa_send)
        .replace("{{WA_FLOAT_LABEL}}", wa_float_label)
    )
