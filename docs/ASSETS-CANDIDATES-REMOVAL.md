# Candidatos a remoção de assets (aguarda aprovação)

**Análise Fase 5** — Nenhum ficheiro abaixo foi apagado automaticamente.

## Imagens hero substituídas por WebP (não referenciadas no site)

| Ficheiro | Substituído por | Tamanho aprox. |
|----------|-----------------|----------------|
| `images/hero/ferramentas.png` | `images/hero/ferramentas.webp` | fonte legado |
| `images/hero/ferramentas.jpg` | `images/hero/ferramentas.webp` | fonte legado |
| `images/hero/obra.png` | `images/hero/obra.webp` | fonte legado |
| `images/hero/obra.jpg` | `images/hero/obra.webp` | fonte legado |
| `images/hero/hero-3.jpg` | `images/hero/hero-3.webp` | fonte legado |
| `images/hero/hero-4.jpg` | `images/hero/hero-4.webp` | fonte legado |

**Em uso em produção:** apenas os 4 ficheiros `.webp` no hero (`scripts/templates/home.html`).

## Logo na raiz

| Ficheiro | Nota |
|----------|------|
| `logo.png` | Fonte para `optimize-images.py` → `logo.webp`. O site serve só `logo.webp`. Podes manter `logo.png` como master para regenerar WebP, ou apagar se já não precisares. |

## Ficheiros a manter (não remover)

- `logo.webp` — favicon, header, footer, OG
- Todos os `*-lisboa.html` — redirects SEO ativos
- `fazdetudopt-codigo-completo.zip` — já no `.gitignore`

## Como confirmar remoção

Após aprovação, por exemplo:

```powershell
Remove-Item images/hero/*.png, images/hero/*.jpg
# opcional: Remove-Item logo.png
```
