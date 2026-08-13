# Analytics tracking — FAZDETUDO.PT

Preparação para Google Analytics 4 (conversões e contactos de parceiros).

## Estado actual

- **Measurement ID:** vazio por omissão (`GA4_MEASUREMENT_ID = ""` em `scripts/site_config.py`).
- **Sem ID válido:** nenhum `gtag.js` é carregado; `trackEvent` é no-op seguro.
- **Com ID válido:** o loader **só** arranca depois de `FazdetudoAnalytics.grantConsent()`.
- Consentimento CMP / banner **ainda não** está implementado nesta tarefa (preparação apenas).

## Como activar GA4 mais tarde

1. Em `scripts/site_config.py`:

```python
GA4_MEASUREMENT_ID = "G-XXXXXXXX"  # o teu ID real
```

2. Regenerar o site (`python scripts/generate-servico-pages.py`).
3. Quando existir CMP, chamar após consentimento analítico:

```js
window.FazdetudoAnalytics.grantConsent();
```

Até lá, **não** chamar `grantConsent()` automaticamente.

## API JavaScript

Exposta em `window.FazdetudoAnalytics`:

| Método | Função |
|--------|--------|
| `trackEvent(name, params)` | Envia evento GA4 se `gtag` + consentimento + ID válidos |
| `grantConsent()` | Marca consentimento e carrega `gtag.js` se o ID for válido |
| `revokeConsent()` | Desactiva envio (não remove scripts já carregados) |
| `trackServiceSelect(category)` | Atalho para `partner_service_select` |

Config inline no `<head>`:

```js
window.__FAZDETUDO_ANALYTICS__ = { measurementId: "", consentGranted: false };
```

## Eventos

### 1. `partner_contact`

Contacto / acção num parceiro.

| Parâmetro | Valores |
|-----------|---------|
| `partner_id` | ex. `maria-limpezas`, `airfix`, `valeriu` |
| `partner_category` | ex. `limpezas`, `avac`, `remodelacoes-gerais` |
| `contact_method` | `phone` \| `whatsapp` \| `website` \| `profile` |
| `source_context` | ver abaixo |

**Exemplos**

```text
partner_contact
  partner_id=maria-limpezas
  partner_category=limpezas
  contact_method=phone
  source_context=service_page

partner_contact
  partner_id=caterina
  partner_category=limpezas
  contact_method=whatsapp
  source_context=homepage_partner_finder

partner_contact
  partner_id=airfix
  partner_category=avac
  contact_method=website
  source_context=partners_directory

partner_contact
  partner_id=maria-limpezas
  partner_category=limpezas
  contact_method=profile
  source_context=article
```

### 2. `fazdetudo_contact`

Contacto directo FAZDETUDO.PT (handyman).

| Parâmetro | Valores |
|-----------|---------|
| `contact_method` | `phone` \| `whatsapp` |
| `source_context` | `hero` \| `quick_repair` \| `header` \| `footer` \| `final_cta` \| `service_page` \| `article` \| `floating_widget` |

**Exemplo — reparação rápida**

```text
fazdetudo_contact
  contact_method=whatsapp
  source_context=quick_repair
```

### 3. `partner_service_select`

Utilizador escolhe uma categoria na pesquisa “Procura um serviço especializado?”.

| Parâmetro | Exemplo |
|-----------|---------|
| `service_category` | `limpezas`, `avac`, `remodelacoes-gerais`, … |

## `source_context` (parceiros)

| Valor | Onde |
|-------|------|
| `homepage_partner_finder` | Pesquisa de parceiros na homepage |
| `partners_directory` | `/parceiros/` |
| `service_page` | Sidebar das páginas de serviço |
| `partner_profile` | `/parceiros/<slug>/` |
| `article` | Cartões em artigos |

## Custom dimensions no GA4 (criar manualmente)

No Admin → Custom definitions, criar dimensões de evento com estes **nomes de parâmetro exactos**:

1. `partner_id`
2. `partner_category`
3. `contact_method`
4. `source_context`
5. `service_category`

Depois usar em Explorations / relatórios para tabelas do tipo:

- Parceiro × método (`phone` / `whatsapp` / `website` / `profile`)
- Origem (`source_context`) × contactos

## Privacidade

**Não** enviamos para analytics:

- números de telefone dos visitantes
- emails / nomes
- texto do WhatsApp / inputs
- conteúdo de formulários
- moradas

Apenas: evento + ids estruturados + método + contexto.

## Page views de perfis

As URLs `/parceiros/maria-limpezas/`, `/parceiros/airfix/`, etc. são medidas pelo `page_view` padrão do GA4 quando o GA estiver activo. Não há page_view duplicado custom.

## Como testar (DebugView)

1. Definir `GA4_MEASUREMENT_ID` com o ID real.
2. Regenerar o site.
3. Temporariamente (só em ambiente de teste) chamar `FazdetudoAnalytics.grantConsent()` na consola.
4. Abrir o site com [Google Analytics Debugger](https://chrome.google.com/webstore) ou parâmetro de debug.
5. No GA4 → Admin → DebugView, clicar Ligar / WhatsApp / Visitar site / Ver perfil / categorias.
6. Confirmar parâmetros e que links continuam a funcionar com `gtag` ausente (ID vazio).

## Ficheiros principais

| Ficheiro | Papel |
|----------|--------|
| `scripts/site_config.py` | `GA4_MEASUREMENT_ID` |
| `scripts/analytics_bootstrap.py` | Config inline no `<head>` |
| `script.js` | `trackEvent`, delegation, consent gate |
| `scripts/partner_cards.py` | `data-track` nos botões de parceiros |
| `scripts/generate-partner-pages.py` | Tracking nos CTAs do perfil |
