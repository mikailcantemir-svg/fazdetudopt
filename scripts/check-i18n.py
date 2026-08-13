#!/usr/bin/env python3
"""Targeted i18n sanity checks for partner profiles and shared CTAs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from recommended_partners import (  # noqa: E402
    PARTNER_PROFILE_UI,
    partner_profile_content,
    partner_profile_href,
    partner_profile_path,
    partner_profile_seo,
    partner_profile_url,
    partners_with_profiles,
)
from slug_registry import LANGS  # noqa: E402

ERRORS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)


def main() -> int:
    partners = partners_with_profiles()
    if len(partners) != 5:
        fail(f"Expected 5 partners with profiles, got {len(partners)}")

    for lang in LANGS:
        if lang not in PARTNER_PROFILE_UI:
            fail(f"Missing PARTNER_PROFILE_UI[{lang}]")

    for partner in partners:
        pid = partner["id"]
        for lang in LANGS:
            try:
                seo = partner_profile_seo(partner, lang)
                content = partner_profile_content(partner, lang)
            except ValueError as exc:
                fail(str(exc))
                continue
            if not seo or not content:
                fail(f"{pid}/{lang}: empty seo/content")
                continue
            path = partner_profile_path(partner, lang)
            href = partner_profile_href(partner, lang)
            url = partner_profile_url(partner, lang)
            if not path or not href or not url:
                fail(f"{pid}/{lang}: missing path/href/url")
                continue
            html_path = ROOT / path / "index.html"
            if not html_path.is_file():
                fail(f"Missing file: {path}index.html")
                continue
            html = html_path.read_text(encoding="utf-8")
            if f'rel="canonical" href="{url}"' not in html and f"href=\"{url}\"" not in html:
                # canonical may use exact url
                if url not in html:
                    fail(f"{pid}/{lang}: canonical URL missing in HTML")
            for alt_lang in LANGS:
                alt = partner_profile_url(partner, alt_lang)
                if alt and alt not in html:
                    fail(f"{pid}/{lang}: hreflang URL missing for {alt_lang}")
            # Language-specific CTA labels must not leak PT into EN/FR
            if lang == "en" and "Ver perfil" in html:
                fail(f"{pid}/en: found Portuguese 'Ver perfil'")
            if lang == "fr" and "Ver perfil" in html:
                fail(f"{pid}/fr: found Portuguese 'Ver perfil'")
            if lang == "en" and "Voltar aos parceiros" in html:
                fail(f"{pid}/en: found Portuguese back link")
            if lang == "fr" and "Voltar aos parceiros" in html:
                fail(f"{pid}/fr: found Portuguese back link")

    # Generated listing / homepage / service pages
    checks = [
        ("en/index.html", "Ver perfil", "/en/parceiros/"),
        ("en/parceiros/index.html", "Ver perfil", "/en/parceiros/"),
        ("en/servico-limpezas.html", "Ver perfil", "/en/parceiros/"),
        ("fr/index.html", "Ver perfil", "/fr/parceiros/"),
        ("fr/parceiros/index.html", "Ver perfil", "/fr/parceiros/"),
        ("es/parceiros/index.html", None, "/es/parceiros/"),
    ]
    for rel, forbidden, must_contain in checks:
        path = ROOT / rel
        if not path.is_file():
            fail(f"Missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if forbidden and forbidden in text:
            fail(f"{rel}: still contains '{forbidden}'")
        if "View profile" in text or "Ver perfil" in text or "Voir le profil" in text:
            # profile links must be language-prefixed where required
            if must_contain and "parceiros/" in text:
                # Ensure EN/FR profile hrefs are prefixed
                if rel.startswith("en/") and re.search(
                    r'href="/(?!en/)parceiros/[^"]+"', text
                ):
                    fail(f"{rel}: unprefixed /parceiros/ profile link")
                if rel.startswith("fr/") and re.search(
                    r'href="/(?!fr/)parceiros/[^"]+"', text
                ):
                    fail(f"{rel}: unprefixed /parceiros/ profile link")
                if rel.startswith("es/") and re.search(
                    r'href="/(?!es/)parceiros/[^"]+"', text
                ):
                    fail(f"{rel}: unprefixed /parceiros/ profile link")

    # EN must use View profile CTA
    en_parceiros = (ROOT / "en/parceiros/index.html").read_text(encoding="utf-8")
    if "View profile →" not in en_parceiros:
        fail("en/parceiros/: missing 'View profile →'")
    fr_parceiros = (ROOT / "fr/parceiros/index.html").read_text(encoding="utf-8")
    if "Voir le profil →" not in fr_parceiros:
        fail("fr/parceiros/: missing 'Voir le profil →'")

    if ERRORS:
        print(f"check-i18n FAILED ({len(ERRORS)} issues):")
        for err in ERRORS:
            print(f"  - {err}")
        return 1

    print("check-i18n OK")
    print(f"  partners with profiles: {len(partners)}")
    print(f"  profile pages expected: {len(partners) * len(LANGS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
