# Fase 3 — Refactor estrutural

**Data:** 2026-05-20

## Nova arquitetura

```
scripts/
├── site_config.py          # Contactos, redes sociais, OG image, WA/tel helpers
├── slug_registry.py        # SERVICE_IDS, slugs por idioma, URLs, hreflang
├── template_engine.py      # load_template / render_partial / {{VARS}}
├── html_partials.py        # Compõe head, headers, footers, wa-widget
├── generate-servico-pages.py
├── generate-homepages.py
└── templates/
    ├── home.html           # Shell homepage
    ├── service.html        # Shell páginas de serviço
    └── partials/
        ├── head.html
        ├── header-home.html
        ├── header-service.html
        ├── footer.html
        ├── footer-service.html
        └── wa-widget.html
```

### Fluxo de geração

1. **Dados** — `home_page_i18n.py` / `service_page_i18n.py` (copy)
2. **URLs** — `slug_registry.py` (canonical, hreflang, paths)
3. **Contactos** — `site_config.py` (tel, email, WA, Facebook, Instagram)
4. **Layout** — `html_partials.py` monta fragmentos → `template_engine` injeta em `home.html` / `service.html`
5. **Output** — 4 homepages + 72 serviços (+ redirects Lisboa)

### Slug registry

- `SERVICE_IDS` — 18 identificadores estáveis (`canalizacoes`, `pinturas`, …)
- `SERVICE_SLUGS_BY_LANG` — hoje igual em PT/EN/ES/FR; preparado para slugs diferentes por idioma
- `render_hreflang_tags_for_service(service_id)` — alternates simétricos para a **mesma** página em `/`, `/en/`, `/es/`, `/fr/`
- `render_home_hreflang()` — homepages com URLs `/`, `/en/`, etc. (não raiz genérica em páginas de serviço)

### Removido (obsoleto)

- `scripts/index.template.html`
- `template-servico.html` (raiz)
- `scripts/partials/wa-widget.html` (pasta antiga)
- `build_index_template.py` — agora avisa deprecação

## Ficheiros alterados

| Área | Ficheiros |
|------|-----------|
| Novo | `slug_registry.py`, `template_engine.py`, `templates/**`, `docs/PHASE3-REPORT.md` |
| Refactor | `html_partials.py`, `site_config.py`, `generate-*.py`, `service_page_i18n.py`, `home_page_i18n.py` |
| Regenerado | `index.html`, `en/es/fr/index.html`, 72× `servico-*.html` |
| Docs | `README.md` |

## Riscos

| Risco | Mitigação |
|-------|-----------|
| Visual/CSS | Classes HTML idênticas; só reorganização de ficheiros |
| hreflang | Testado em `en/servico-canalizacoes.html` — URLs por idioma corretas |
| Deploy | Correr `python scripts/generate-servico-pages.py` após pull |

## Comando

```bash
python scripts/generate-servico-pages.py
python scripts/generate-sitemap.py
```
