# -*- coding: utf-8 -*-
"""Analytics bootstrap HTML for page <head>.

Does NOT load Google Analytics by itself.
A valid GA4_MEASUREMENT_ID + FazdetudoAnalytics.grantConsent() are required.
"""

from __future__ import annotations

import json

from site_config import GA4_MEASUREMENT_ID


def analytics_bootstrap_html() -> str:
    """Inline config only — never injects a fake Measurement ID or gtag.js."""
    mid = (GA4_MEASUREMENT_ID or "").strip()
    payload = json.dumps(
        {
            "measurementId": mid,
            "consentGranted": False,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return (
        "<script>"
        f"window.__FAZDETUDO_ANALYTICS__={payload};"
        "</script>"
    )
