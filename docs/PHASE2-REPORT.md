# Fase 2 — Correções críticas (redirects, pipeline, tel:)

**Data:** 2026-05-20

## Problemas corrigidos

### 1. Redirects duplos/triplos (`*-lisboa.html`)

**Antes:** `meta refresh` + `location.replace()` + link (redundância; risco de duplo salto em alguns browsers).

**Depois:** Apenas `meta http-equiv="refresh"` + link `<a>` de fallback (sem JavaScript).  
Adicionado `meta name="robots" content="noindex, follow"` nas páginas legadas.

### 2. `.htaccess` dessincronizado do Python

**Antes:** Dicionário `REDIRECTS` e `.htaccess` mantidos à mão em paralelo.

**Depois:** `.htaccess` **gerado automaticamente** a partir de `REDIRECTS` em `generate-lisboa-redirects.py`.

### 3. Pipeline incompleto

**Antes:** `generate-servico-pages.py` não regenerava redirects.

**Depois:** Passo `--- Legacy SEO redirects ---` no final do gerador principal.

### 4. `setupLinks()` alterava `tel:` válidos

**Antes:** `CONFIG.phone` com espaço (`+351 932504112`) sobrescrevia `tel:+351932504112` do HTML gerado.

**Depois:** `CONFIG.phone = '+351932504112'`; `setupLinks()` não altera links `tel:` já corretos.

### 5. Documentação

- `README.md`: 17 redirects, tabela GitHub Pages vs Apache, `.htaccess` gerado.

## Ficheiros modificados

| Ficheiro | Alteração |
|----------|-----------|
| `scripts/generate-lisboa-redirects.py` | Refactor: `write_htaccess`, HTML sem JS, `noindex` |
| `scripts/generate-servico-pages.py` | Chama redirects no pipeline |
| `script.js` | `CONFIG.phone` E.164; `setupLinks()` idempotente |
| `README.md` | Deploy redirects, contagem 17 |
| `.htaccess` | Regenerado (cabeçalho AUTO-GENERATED) |
| 17× `*-lisboa.html` | Regenerados |

## Riscos / notas

| Risco | Mitigação |
|-------|-----------|
| GitHub Pages continua sem HTTP 301 real | Comportamento esperado; um salto via meta refresh |
| Apache com 301 | HTML legado não é servido — sem regressão |
| URLs legadas indexadas | Slugs destino inalterados |
| `setupLinks` ainda atualiza WA nos CTAs | Intencional para mensagem WA por idioma em runtime |

## Comando de verificação

```bash
python scripts/generate-lisboa-redirects.py
# Confirmar ausência de location.replace nos HTML:
# (nenhum resultado esperado)
```

## Próximo passo

**Fase 3** — partials header/head, `site_config` em `template-servico.html`, registry de slugs.
