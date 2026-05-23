# fazdetudo.pt — Site estático multilingue

Website profissional para **Faz de Tudo PT** (handyman, reparações e obras na Grande Lisboa e Margem Sul).

## Estrutura do projeto

```
fazdetudopt/
├── index.html              # Homepage PT
├── servico-*.html          # 18 páginas de serviço (PT)
├── en/ es/ fr/              # Homepages + serviços traduzidos
├── *-lisboa.html           # Redirects SEO legados → servico-*.html
├── style.css               # Estilos globais
├── script.js               # UI homepage (i18n client-side, reviews, WhatsApp)
├── template-servico.html   # Layout páginas de serviço
├── scripts/
│   ├── generate-servico-pages.py   # ★ Gerador principal (correr isto)
│   ├── generate-homepages.py
│   ├── home_page_i18n.py           # Textos homepage + cartões de serviços
│   ├── service_page_i18n.py        # Textos páginas de serviço
│   ├── html_partials.py            # Fragmentos HTML reutilizáveis
│   ├── partials/wa-widget.html     # Widget WhatsApp
│   ├── site_config.py              # Telefone, email, URLs
│   ├── generate-sitemap.py
│   ├── fix-fa-aria-hidden.py
│   └── bundle-for-gemini.py
├── images/                 # Hero (WebP)
├── logo.webp
├── sitemap.xml
└── docs/REFACTOR-REPORT.md
```

## Comandos essenciais

```bash
# Regenerar TODO o site (4 homepages + 72 serviços)
python scripts/generate-servico-pages.py

# Sitemap
python scripts/generate-sitemap.py

# Bundle para revisão IA
python scripts/bundle-for-gemini.py
```

## Fonte de verdade

| Conteúdo | Ficheiro |
|----------|----------|
| Hero, UI homepage, badges cartões | `scripts/home_page_i18n.py` |
| Páginas de serviço | `scripts/service_page_i18n.py` + `template-servico.html` |
| Layout homepage | `scripts/index.template.html` |
| Contactos / WhatsApp | `scripts/site_config.py` |
| Widget WhatsApp HTML | `scripts/partials/wa-widget.html` |

**Não editar manualmente** os HTML gerados em massa — alterar os templates/i18n e regenerar.

## Idiomas

- `pt` — raiz (`/`)
- `en` — `/en/`
- `es` — `/es/`
- `fr` — `/fr/`

Hreflang e canonical são gerados automaticamente.

## Deploy

Site estático (GitHub Pages). Branch `main` = produção.
