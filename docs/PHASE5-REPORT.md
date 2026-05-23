# Fase 5 — Limpeza final e documentação

**Data:** 2026-05-20

## 1. Assets — candidatos a remoção (não apagados)

Lista completa em **`docs/ASSETS-CANDIDATES-REMOVAL.md`**.

| Categoria | Ficheiros | Ação |
|-----------|-----------|------|
| Hero legado | 6× `.png`/`.jpg` em `images/hero/` | Candidatos — site usa só `.webp` |
| Logo fonte | `logo.png` | Opcional manter para `optimize-images.py` |

**Nenhum asset foi removido** sem aprovação explícita.

## 2. Ficheiros / scripts removidos

| Item | Motivo |
|------|--------|
| `scripts/build_index_template.py` | Obsoleto (templates em `scripts/templates/`) |
| `scripts/partials/` (pasta vazia legada) | Substituída por `scripts/templates/partials/` |

## 3. Dead code removido

### `script.js`

- `SERVICE_ICONS` (não usado; cartões gerados em Python)
- Chaves `cat_*` em `T` (sem `data-i18n` no HTML)
- Ramo legado `button.lang-option` no lang switcher (só existem links `<a class="lang-option--nav">`)

### `service_page_i18n.py`

- `float_wa` / `float_tel` em `UI` (não usados nos templates)

### `fix-fa-aria-hidden.py`

- Referências a `template-servico.html` e `index.template.html` removidas
- Alvo: todos os `*.html` do repo

### `style.css`

- Mantido bloco `.floating-contact` / `.float-call-bar` (`display: none !important`) — proteção contra markup antigo, sem impacto visual

## 4. Documentação

- **`README.md`** — arquitetura, comandos, tabela de edição, guia novo idioma
- **`docs/ASSETS-CANDIDATES-REMOVAL.md`**
- Relatórios Fases 2–5 em `docs/`

## 5. Bundle IA

- **`scripts/bundle-for-gemini.py`** — inclui `scripts/templates/partials/`, ignora `__pycache__`, ordena templates primeiro, inclui `.htaccess`
- Regenerar: `python scripts/bundle-for-gemini.py`

## 6. Design e mobile

- **Sem alterações** a `style.css` de layout/componentes nesta fase
- Classes e estrutura HTML dos partials idênticas ao refactor Fase 3
- Media queries existentes intactas

## Veredito

Projeto **pronto para produção** com pipeline único, partials, registry de slugs e config centralizada. Dívida técnica residual aceitável: duplicação parcial `script.js` ↔ `home_page_i18n.py` (reviews/FAQ dinâmicos); opcional unificar numa fase futura.

**Nota estimada:** 9/10 para manutenção e deploy estático multilingue.
