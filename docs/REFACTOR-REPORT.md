# Relatório de refactor profissional — fazdetudo.pt

**Data:** 2026-05-20  
**Branch:** `feature/improvement`  
**Princípio:** design visual mantido; foco em arquitetura, SEO, performance, a11y e manutenção.

---

## 1. O que foi corrigido

### Arquitetura e DRY
- Criado **`scripts/site_config.py`** — telefone, WhatsApp, email, URLs e mensagens WA centralizados.
- Criado **`scripts/html_partials.py`** + **`scripts/partials/wa-widget.html`** — widget WhatsApp único usado por homepage e páginas de serviço (elimina ~30 linhas duplicadas × 76 páginas na fonte).
- Templates passam a usar **`{{WA_WIDGET}}`**, **`{{LOGO_HREF}}`**, **`{{TEL_HREF}}`**, **`{{WA_HREF}}`**, **`{{EMAIL_HREF}}`**, **`{{GOOGLE_REVIEWS_URL}}`**.
- **`README.md`** com estrutura, comandos e fonte de verdade documentada.
- **`.gitignore`** para `__pycache__`, zip locais, etc.
- Gerador **`generate-servico-pages.py`** continua como ponto único de rebuild (homepages + serviços + aria-hidden).

### Links e HTML válido
- Removidos **`href="#"`** em CTAs, telefone, email, logo e Google Reviews nas homepages geradas (antes dependiam só de JS).
- Botões WhatsApp/chat com **`type="button"`** no partial.
- **`defer`** em `script.js` e Swiper na homepage.

### Acessibilidade
- **Skip link** «Saltar para o conteúdo» (`#main-content` / `#service-main`).
- Classe **`.visually-hidden`** + label no input do chat WA.
- **`aria-hidden="true"`** em ícones FAQ (chevron).
- Ícones Font Awesome já cobertos por `fix-fa-aria-hidden.py` no pipeline.

### Performance
- **`loading="lazy"`** + `decoding="async"` em imagens abaixo da dobra (logo secção serviços, avatar WA).
- **`rel="preload"`** do logo WebP no `<head>`.
- Scripts com **`defer`** para não bloquear parsing.

### Linguagem (PT-PT e i18n)
- Morada unificada: **«Grande Lisboa e Margem Sul, Portugal»** (meta + `script.js`).
- Correção ortográfica review PT: «móveis», «preços».
- FAQ EN: área de cobertura alinhada com **South Bank**.
- Morada ES em `HOME_META`: **«Gran Lisboa y Margen Sur»**.

### SEO técnico
- URLs de contacto semânticas no HTML estático (melhor para crawlers sem JS).
- URL Google Reviews simplificada e estável em `site_config.py`.
- Canonical/hreflang/schema mantidos via geradores existentes (sem regressão).

---

## 2. Ficheiros alterados

| Ficheiro | Tipo de alteração |
|----------|------------------|
| `scripts/site_config.py` | **Novo** |
| `scripts/html_partials.py` | **Novo** |
| `scripts/partials/wa-widget.html` | **Novo** |
| `scripts/index.template.html` | Links, skip link, partial WA, lazy, defer |
| `template-servico.html` | Partial WA, skip link, preload, defer |
| `scripts/generate-homepages.py` | Injeta partial + links |
| `scripts/generate-servico-pages.py` | Injeta partial WA |
| `scripts/home_page_i18n.py` | Moradas meta ES/PT |
| `style.css` | Utilitários a11y (skip-link, visually-hidden) |
| `script.js` | FAQ, morada, URL reviews, copy PT |
| `README.md` | **Novo** |
| `.gitignore` | **Novo** |
| `docs/REFACTOR-REPORT.md` | **Novo** |
| `index.html`, `en/es/fr/index.html` | **Regenerados** |
| 72× `servico-*.html` | **Regenerados** |

---

## 3. Problemas críticos encontrados (e estado)

| Problema | Gravidade | Estado |
|----------|-----------|--------|
| `href="#"` em todos os CTAs (SEO/a11y/sem JS) | Alta | **Corrigido** em templates |
| Widget WhatsApp duplicado em 76+ ficheiros na manutenção manual | Alta | **Corrigido** (partial) |
| `script.js` com traduções duplicadas vs `home_page_i18n.py` | Média | Parcial — homepage física usa HTML gerado; JS ainda tem `T` para switcher legado em alguns fluxos |
| Review Google em espanhol no bloco PT (`CONFIG`) | Baixa | Mantido (texto real de review); não alterado |
| 18× ficheiros `*-lisboa.html` redirects | Info | Mantidos de propósito (SEO legado) |
| `generate-service-pages.py` legado | Baixa | Alias para `generate-servico-pages.py` |
| Imagens PNG hero ainda no repo com WebP em uso | Baixa | Opcional limpar mais tarde |
| Pasta `/components` física no root | — | **Não criada** — partials em `scripts/partials/` (adequado a gerador estático) |

---

## 4. Melhorias de performance

- Preload logo WebP  
- Lazy load imagens não críticas  
- JS defer (main + Swiper)  
- Widget WA único (menos divergência, manutenção mais rápida)  
- Pipeline regeneração evita HTML órfão inconsistente  

**Estimativa:** melhoria moderada em LCP/TTI; medição Lighthouse recomendada após deploy.

---

## 5. Melhorias SEO

- Links `tel:` / `mailto:` / `wa.me` no HTML inicial  
- Google Reviews com URL estável  
- Morada regional consistente (Grande Lisboa e Margem Sul)  
- Sem alteração negativa a hreflang/canonical/sitemap  

---

## 6. Melhorias acessibilidade

- Skip link  
- Labels ocultos em inputs  
- `type="button"` em controlos não-navegação  
- FAQ chevrons decorativos ocultos a leitores de ecrã  
- Contraste Hero já melhorado em commit anterior  

---

## 7. Nota final do projeto

| Critério | Nota (1–10) | Comentário |
|----------|-------------|------------|
| Arquitetura | **8** | Gerador central + partials; falta unificar `script.js` i18n 100% |
| SEO técnico | **8.5** | Hreflang forte; keywords meta ainda longas (legado) |
| Performance | **7.5** | Boas bases; CDN externos (FA, Swiper, fonts) ainda pesados |
| Acessibilidade | **8** | Salto visível; testes teclado/screen reader recomendados |
| Manutenção | **9** | Um comando regenera 76 páginas |
| **Global** | **8.2 / 10** | Pronto para produção com fluxo de manutenção profissional |

---

## 8. O que ainda pode ser melhorado

1. **Unificar i18n** — exportar `HOME_UI` / `T` de um único JSON ou Python gerado para `script.js` (eliminar duplicação).
2. **Remover switcher JS** nas homepages se só existirem URLs `/en/`, `/es/`, `/fr/` (já parcialmente físicas).
3. **Self-host** Font Awesome subset ou SVG sprite (menos KB, menos requests).
4. **Critical CSS** inline mínimo para Hero LCP.
5. **Testes automatizados** — smoke test links + validação HTML em CI.
6. **Consolidar redirects** `*-lisboa.html` apenas via `.htaccess` se o hosting permitir.
7. **Tradução profissional** revisão humana EN/ES/FR (não só técnica).
8. **`footer_tagline`** chave i18n separada do `hero_title` (evitar tagline longa no rodapé).

---

## Comando pós-refactor

```bash
python scripts/generate-servico-pages.py
python scripts/generate-sitemap.py
```
