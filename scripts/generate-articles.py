#!/usr/bin/env python3
"""Gera a secção de Artigos (Guias e Dicas) em /artigos/.

Saídas:
  - /artigos/index.html  (listagem)
  - /artigos/<slug>      (um ficheiro por artigo)

Fonte de conteúdo: scripts/articles_data.py
Integrado no fluxo principal por scripts/generate-servico-pages.py.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from articles_data import ARTICLES, ARTICLES_INDEX  # noqa: E402
from html_partials import (  # noqa: E402
    render_footer_service,
    render_head,
    render_header_service,
    render_wa_widget,
)
from service_page_i18n import UI  # noqa: E402
from site_config import BASE_URL, OG_IMAGE, tel_href, wa_href_for_message  # noqa: E402
from template_engine import render_template  # noqa: E402

ARTICLES_DIR = ROOT / "artigos"
LANG = "pt"
HTML_LANG = "pt-PT"
OG_LOCALE = "pt_PT"
ASSET_PREFIX = "../"
INDEX_HREF = "/"

_MONTHS_PT = (
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
)


def _format_date_pt(iso: str) -> str:
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{d} de {_MONTHS_PT[m - 1]} de {y}"


def article_url(slug: str) -> str:
    return f"{BASE_URL}/artigos/{slug}"


def _common_parts(*, page_title: str, meta_description: str, canonical: str,
                  og_title: str, json_ld: str, faq_json_ld: str = "") -> dict:
    ui = UI[LANG]
    head = render_head(
        page_title=page_title,
        meta_description=meta_description,
        canonical_url=canonical,
        hreflang_block="",  # secção PT-only: sem alternates inexistentes
        og_title=og_title,
        og_description=meta_description,
        og_locale=OG_LOCALE,
        json_ld=json_ld,
        asset_prefix=ASSET_PREFIX,
        include_swiper_css=False,
        faq_json_ld=faq_json_ld,
    )
    header = render_header_service(
        asset_prefix=ASSET_PREFIX,
        index_href=INDEX_HREF,
        back_label=ui["back"],
    )
    footer = render_footer_service(footer_text=ui["footer"])
    wa_widget = render_wa_widget(
        asset_prefix=ASSET_PREFIX,
        wa_online=ui["wa_online"],
        wa_greeting=ui["wa_greeting"],
        wa_placeholder=ui["wa_placeholder"],
        wa_close=ui["wa_close"],
        wa_send=ui["wa_send"],
        wa_float_label=ui["wa_float_label"],
    )
    return {"HEAD": head, "HEADER_SERVICE": header, "FOOTER": footer, "WA_WIDGET": wa_widget}


def _faq_section_html(faq: list[dict]) -> str:
    if not faq:
        return ""
    items = ["                <h2>Perguntas frequentes</h2>"]
    for entry in faq:
        items.append(f"                <h3>{entry['q']}</h3>")
        items.append(f"                <p>{entry['a']}</p>")
    return "\n" + "\n".join(items)


def _faq_json_ld(faq: list[dict]) -> str:
    if not faq:
        return ""
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": entry["q"],
                "acceptedAnswer": {"@type": "Answer", "text": entry["a"]},
            }
            for entry in faq
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def _article_json_ld(article: dict, canonical: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["h1"],
        "description": article["meta_description"],
        "inLanguage": "pt-PT",
        "datePublished": article["published"],
        "dateModified": article["updated"],
        "image": OG_IMAGE,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "author": {"@type": "Organization", "name": "FAZDETUDO.PT", "url": BASE_URL},
        "publisher": {
            "@type": "Organization",
            "name": "FAZDETUDO.PT",
            "logo": {"@type": "ImageObject", "url": OG_IMAGE},
        },
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_article(article: dict) -> str:
    canonical = article_url(article["slug"])
    parts = _common_parts(
        page_title=article["page_title"],
        meta_description=article["meta_description"],
        canonical=canonical,
        og_title=article["og_title"],
        json_ld=_article_json_ld(article, canonical),
        faq_json_ld=_faq_json_ld(article.get("faq", [])),
    )

    meta_line = (
        f'<p class="article-meta">{html.escape(article["category"])} · '
        f'Atualizado em {_format_date_pt(article["updated"])}</p>'
    )
    body = article["body_html"].rstrip() + _faq_section_html(article.get("faq", []))

    related_block = ""
    if article.get("related_service_url"):
        related_block = (
            '                    <div class="article-related">\n'
            f'                        <p>{article.get("related_intro", "Serviço relacionado:")}</p>\n'
            f'                        <a href="{article["related_service_url"]}" class="btn btn-outline">'
            f'{article["related_service_label"]}</a>\n'
            '                    </div>'
        )

    return render_template(
        "article.html",
        {
            "HTML_LANG": HTML_LANG,
            "PAGE_LANG": LANG,
            "HEAD": parts["HEAD"],
            "HEADER_SERVICE": parts["HEADER_SERVICE"],
            "FOOTER": parts["FOOTER"],
            "WA_WIDGET": parts["WA_WIDGET"],
            "ASSET_PREFIX": ASSET_PREFIX,
            "ARTICLE_META": meta_line,
            "H1_TITLE": article["h1"],
            "LEAD_TEXT": article["lead"],
            "BODY_HTML": body,
            "RELATED_BLOCK": related_block,
            "CTA_H3": article["cta_h3"],
            "CTA_P": article["cta_p"],
            "CTA_WA": article["cta_button"],
            "CTA_CALL": UI[LANG]["cta_call"],
            "WA_HREF": wa_href_for_message(article["wa_message"]),
            "TEL_HREF": tel_href(),
        },
    )


def _index_body_html() -> str:
    cards = ['                <ul class="article-list">']
    for article in ARTICLES:
        cards.append('                    <li class="article-card">')
        cards.append(
            f'                        <h2><a href="{article["slug"]}">{article["h1"]}</a></h2>'
        )
        cards.append(
            f'                        <p class="article-meta">{html.escape(article["category"])} · '
            f'{_format_date_pt(article["updated"])}</p>'
        )
        cards.append(f'                        <p>{article["excerpt"]}</p>')
        cards.append(
            f'                        <a href="{article["slug"]}" class="article-readmore">'
            'Ler artigo <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></a>'
        )
        cards.append('                    </li>')
    cards.append('                </ul>')
    return "\n".join(cards)


def _index_json_ld(canonical: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": ARTICLES_INDEX["h1"],
        "description": ARTICLES_INDEX["meta_description"],
        "url": canonical,
        "inLanguage": "pt-PT",
        "publisher": {"@type": "Organization", "name": "FAZDETUDO.PT", "url": BASE_URL},
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_index() -> str:
    canonical = f"{BASE_URL}/artigos/"
    parts = _common_parts(
        page_title=ARTICLES_INDEX["page_title"],
        meta_description=ARTICLES_INDEX["meta_description"],
        canonical=canonical,
        og_title=ARTICLES_INDEX["og_title"],
        json_ld=_index_json_ld(canonical),
    )
    return render_template(
        "article.html",
        {
            "HTML_LANG": HTML_LANG,
            "PAGE_LANG": LANG,
            "HEAD": parts["HEAD"],
            "HEADER_SERVICE": parts["HEADER_SERVICE"],
            "FOOTER": parts["FOOTER"],
            "WA_WIDGET": parts["WA_WIDGET"],
            "ASSET_PREFIX": ASSET_PREFIX,
            "ARTICLE_META": "",
            "H1_TITLE": ARTICLES_INDEX["h1"],
            "LEAD_TEXT": ARTICLES_INDEX["lead"],
            "BODY_HTML": _index_body_html(),
            "RELATED_BLOCK": "",
            "CTA_H3": "Precisa de ajuda em casa?",
            "CTA_P": (
                "Fale com a equipa da FAZDETUDO.PT para um orçamento gratuito na "
                "Grande Lisboa e Margem Sul."
            ),
            "CTA_WA": "Pedir orçamento gratuito",
            "CTA_CALL": UI[LANG]["cta_call"],
            "WA_HREF": wa_href_for_message("Olá! Gostaria de pedir um orçamento."),
            "TEL_HREF": tel_href(),
        },
    )


def main() -> None:
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    written = []

    index_path = ARTICLES_DIR / ARTICLES_INDEX["slug"]
    index_path.write_text(render_index(), encoding="utf-8")
    written.append(index_path.relative_to(ROOT).as_posix())
    print(f"wrote {index_path.relative_to(ROOT).as_posix()}")

    for article in ARTICLES:
        path = ARTICLES_DIR / article["slug"]
        path.write_text(render_article(article), encoding="utf-8")
        written.append(path.relative_to(ROOT).as_posix())
        print(f"wrote {path.relative_to(ROOT).as_posix()}")

    print(f"Total: {len(written)} article pages (index + {len(ARTICLES)} articles)")


if __name__ == "__main__":
    main()
