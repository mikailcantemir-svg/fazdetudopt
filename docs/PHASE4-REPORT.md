# Fase 4 — Otimização SEO e Performance

**Data:** 2026-05-20

## Alterações aplicadas

### 1. SEO — `meta keywords` removida

- Removido `META_KEYWORDS_LINE` de `partials/head.html`
- Removido `HOME_KEYWORDS` e parâmetro `include_keywords` de `html_partials.py` / geradores
- Homepages regeneradas sem a tag

### 2. Redirects `*-lisboa.html`

- Já estavam sem `location.replace` (Fase 2); confirmado em todos os 17 ficheiros
- Apenas `<meta http-equiv="refresh">` + link de fallback

### 3. Performance (Core Web Vitals)

- **`defer`** — já presente em Swiper e `script.js` nos templates `home.html` / `service.html` (mantido)
- **`preconnect`** — movido para o topo do `<head>` (fonts + cdn.jsdelivr + cdnjs.cloudflare)
- Duplicados de preconnect no final do head removidos

### 4. Segurança e acessibilidade

- **Email ofuscado** — `geral&#64;fazdetudo.pt` no footer (`site_config.EMAIL_OBFUSCATED`); `mailto:` mantém email real
- **`script.js`** — `applyTexts()` usa `innerHTML` com entidade; não repõe `@` em claro
- **`href="#"`** — nenhum nos templates atuais; widget WA já usa `<button type="button">`
- Removido `preventDefault` desnecessário no botão flutuante WA

## Ficheiros fonte alterados

| Ficheiro |
|----------|
| `scripts/templates/partials/head.html` |
| `scripts/templates/partials/footer.html` |
| `scripts/html_partials.py` |
| `scripts/site_config.py` |
| `scripts/generate-homepages.py` |
| `scripts/generate-servico-pages.py` |
| `script.js` |

## Ficheiros regenerados

- `index.html`, `en/es/fr/index.html` (sem keywords; email ofuscado; preconnect)
- 72× `servico-*.html`
- 17× `*-lisboa.html` (pipeline; sem alteração de conteúdo)

## Não alterado (fora de âmbito Fase 4)

- Self-host Font Awesome / critical CSS (Fase 5 ou backlog)
- Unificação i18n `script.js` ↔ Python
- `fazdetudopt-codigo-gemini.txt` (regenerar em Fase 5 se desejado)

## Verificação rápida

```bash
# Sem keywords nas homepages
rg "meta name=\"keywords\"" index.html en/index.html

# Sem location.replace nos redirects
rg "location.replace" *-lisboa.html

# Email ofuscado no footer
rg "geral&#64;" index.html
```
