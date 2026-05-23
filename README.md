# fazdetudo.pt — Site estático multilingue

Website profissional para **Faz de Tudo PT** (handyman, reparações e obras na Grande Lisboa e Margem Sul).

**Stack:** HTML/CSS/JS estático · gerado por Python · deploy GitHub Pages (`main`).

---

## Arquitetura (pós-refactor)

```
fazdetudopt/
├── index.html, servico-*.html     # Gerados — não editar à mão
├── en/ es/ fr/                    # Homepages + 18 serviços × idioma
├── *-lisboa.html (17)             # Redirects SEO legados
├── style.css, script.js           # Assets globais (raiz)
├── logo.webp
├── scripts/
│   ├── generate-servico-pages.py  # ★ Comando único de rebuild
│   ├── generate-service-pages.py  # Alias → generate-servico-pages.py
│   ├── site_config.py             # Telefone, email, redes, URLs
│   ├── slug_registry.py           # Slugs, URLs absolutas, hreflang
│   ├── template_engine.py         # {{PLACEHOLDERS}}
│   ├── html_partials.py           # Monta head / header / footer / WA
│   ├── home_page_i18n.py          # Textos homepage + cartões
│   ├── service_page_i18n.py       # Textos páginas de serviço
│   ├── generate-lisboa-redirects.py
│   ├── generate-sitemap.py
│   ├── fix-fa-aria-hidden.py
│   ├── bundle-for-gemini.py
│   └── templates/
│       ├── home.html
│       ├── service.html
│       └── partials/              # head, header-*, footer*, wa-widget
└── docs/                          # Relatórios por fase + assets candidatos
```

### Fluxo de geração

1. Editas **templates** (`scripts/templates/`), **partials**, **i18n** ou **`site_config.py`**
2. Corres o gerador principal
3. Opcional: sitemap e bundle IA

```bash
python scripts/generate-servico-pages.py
python scripts/generate-sitemap.py
python scripts/bundle-for-gemini.py
```

O gerador principal produz:

- 4 homepages (`index.html` + `en/es/fr/`)
- 72 páginas de serviço (18 × 4 idiomas)
- Passagem `aria-hidden` em ícones FA
- 17× `*-lisboa.html` + `.htaccess`

---

## Onde editar o quê

| Objetivo | Ficheiro |
|----------|----------|
| Telefone, email, Facebook, Instagram, URL Google Reviews | `scripts/site_config.py` |
| Hero, menu, FAQ (homepage), cartões de serviços | `scripts/home_page_i18n.py` |
| Textos de cada página `servico-*.html` | `scripts/service_page_i18n.py` (+ `service_rich_content.py` PT) |
| Layout HTML (estrutura, classes CSS) | `scripts/templates/` e `partials/` |
| Estilos visuais | `style.css` |
| Reviews, FAQ dinâmico, WhatsApp (homepage) | `script.js` |
| URLs e hreflang | `scripts/slug_registry.py` |
| Redirects `*-lisboa.html` | `scripts/generate-lisboa-redirects.py` (`REDIRECTS`) |

---

## Adicionar um novo idioma (ex.: `de`)

1. **`scripts/slug_registry.py`** — acrescentar `"de"` a `LANGS`, `LANG_HTML`, `HREFLANG_CODES`, `HOME_PATHS`, e entrada em `SERVICE_SLUGS_BY_LANG` (slug do ficheiro, hoje igual aos outros).
2. **`scripts/site_config.py`** — mensagem WhatsApp em `WA_MESSAGE["de"]`.
3. **`scripts/home_page_i18n.py`** — blocos `HOME_META["de"]`, `HOME_UI["de"]`, cartões em `SERVICE_CARDS`, `HANDYMAN["de"]`, `LANG_LABELS`.
4. **`scripts/service_page_i18n.py`** — `UI["de"]` e `SERVICE_COPY[slug]["de"]` para cada serviço.
5. **`scripts/generate-servico-pages.py`** — incluir `"de"` em `LANG_DIRS` se usar pasta `/de/`.
6. Regenerar: `python scripts/generate-servico-pages.py`
7. Atualizar `scripts/generate-sitemap.py` com prefixo `/de`.
8. Revisão humana das traduções.

---

## Idiomas atuais

| Código | URL base |
|--------|----------|
| `pt` | `https://www.fazdetudo.pt/` |
| `en` | `https://www.fazdetudo.pt/en/` |
| `es` | `https://www.fazdetudo.pt/es/` |
| `fr` | `https://www.fazdetudo.pt/fr/` |

Hreflang e canonical são gerados a partir de `slug_registry.py`.

---

## Deploy (GitHub Pages)

- Branch **`main`** = produção
- **`.htaccess`** é ignorado no GitHub Pages; redirects legados usam `meta refresh` nos HTML `*-lisboa.html`
- Em Apache, o `.htaccess` gerado aplica `301` antes do HTML

---

## Documentação interna

| Documento | Conteúdo |
|-----------|----------|
| `docs/REFACTOR-REPORT.md` | Refactor inicial |
| `docs/PHASE2-REPORT.md` | Redirects + pipeline |
| `docs/PHASE3-REPORT.md` | Partials + slug registry |
| `docs/PHASE4-REPORT.md` | SEO + performance |
| `docs/PHASE5-REPORT.md` | Limpeza final |
| `docs/ASSETS-CANDIDATES-REMOVAL.md` | PNG/JPG candidatos a apagar (aprovação) |

---

## Scripts utilitários (opcionais)

| Script | Uso |
|--------|-----|
| `optimize-images.py` | Gera `.webp` a partir de PNG/JPG |
| `apply-rich-text.py` / `scan-rich-text.py` | Conteúdo rico PT |
| `bundle-for-gemini.py` | Export `fazdetudopt-codigo-gemini.txt` |
