# -*- coding: utf-8 -*-
"""Conteúdo da secção de Artigos (Guias e Dicas) — fonte única.

Cada artigo é publicado manualmente em /artigos/<slug>.
Os artigos são, por agora, apenas em português (mercado local).
Para acrescentar um artigo novo: adicionar uma entrada a ARTICLES e correr
`python scripts/generate-servico-pages.py`.
"""

from __future__ import annotations

from site_config import BASE_URL

# Metadados da página índice /artigos/
ARTICLES_INDEX = {
    "slug": "index.html",
    "h1": "Guias e Dicas",
    "lead": (
        "Artigos práticos sobre manutenção, reparações e obras em casa, "
        "escritos pela equipa da FAZDETUDO.PT para a Grande Lisboa e Margem Sul."
    ),
    "page_title": "Guias e Dicas para Casa em Lisboa | FAZDETUDO.PT",
    "meta_description": (
        "Guias e dicas práticas sobre manutenção, reparações e obras em casa "
        "na Grande Lisboa e Margem Sul, pela equipa da FAZDETUDO.PT."
    ),
    "og_title": "Guias e Dicas para Casa | FAZDETUDO.PT",
}


ARTICLES = [
    {
        "slug": "ar-condicionado-lisboa-instalar-limpar-manter-split.html",
        "category": "Climatização",
        "published": "2026-06-01",
        "updated": "2026-06-01",
        "h1": "Ar Condicionado em Lisboa: Instalar, Limpar e Manter o Split",
        "page_title": "Ar Condicionado em Lisboa: Instalar e Manter | FAZDETUDO.PT",
        "meta_description": (
            "Guia prático para instalar, limpar e manter o ar condicionado (split) "
            "em Lisboa e Margem Sul. Dicas de manutenção e quando pedir assistência."
        ),
        "og_title": "Ar Condicionado em Lisboa: Instalar, Limpar e Manter o Split",
        "lead": (
            "Um ar condicionado bem instalado e com manutenção regular trabalha melhor, "
            "consome menos e dura mais anos. Reunimos o essencial sobre instalação, "
            "limpeza e manutenção de splits para casas e escritórios na Grande Lisboa e Margem Sul."
        ),
        "excerpt": (
            "Como escolher, instalar, limpar e manter um split de ar condicionado em casa "
            "— e quando vale a pena chamar um técnico."
        ),
        "related_service_url": f"{BASE_URL}/servico-climatizacao.html",
        "related_service_label": "Ver serviço de Climatização e Ar Condicionado",
        "related_intro": "Precisa de ajuda profissional com o seu equipamento?",
        "wa_message": (
            "Olá! Gostaria de pedir um orçamento para ar condicionado "
            "(instalação, limpeza ou manutenção)."
        ),
        "cta_h3": "Precisa de ar condicionado ou de uma revisão?",
        "cta_p": (
            "Fale com a nossa equipa para instalação, limpeza ou manutenção de "
            "ar condicionado em Lisboa, Cascais, Almada e Setúbal."
        ),
        "cta_button": "Pedir orçamento para ar condicionado",
        "body_html": """
                <p>O ar condicionado deixou de ser um luxo e passou a ser parte do conforto
                de muitas casas e escritórios na região de Lisboa, tanto no calor do verão
                como no apoio ao aquecimento em dias mais frios. Para tirar o melhor partido
                do equipamento — e evitar surpresas — convém perceber três fases: a
                <strong>instalação</strong>, a <strong>limpeza</strong> e a
                <strong>manutenção</strong>.</p>

                <h2>1. Instalação do split: o que ter em conta</h2>
                <p>A instalação influencia diretamente o desempenho e o consumo do
                equipamento. Alguns pontos que ajudam a tomar uma boa decisão:</p>
                <ul>
                    <li><strong>Potência adequada à divisão.</strong> Um aparelho subdimensionado
                    trabalha sempre no máximo; um sobredimensionado liga e desliga em excesso.
                    A escolha depende da área, da exposição solar e do isolamento.</li>
                    <li><strong>Localização das unidades.</strong> A unidade interior deve
                    distribuir bem o ar, sem apontar diretamente para zonas de descanso; a
                    exterior precisa de ventilação e acesso para manutenção.</li>
                    <li><strong>Distância e percurso da tubagem.</strong> Percursos mais curtos
                    e bem isolados tendem a manter a eficiência do sistema.</li>
                    <li><strong>Instalação por técnico habilitado.</strong> O manuseamento de
                    gás refrigerante e a ligação elétrica devem ser feitos por profissionais,
                    por questões de segurança e de garantia do fabricante.</li>
                </ul>

                <h2>2. Limpeza do ar condicionado</h2>
                <p>A limpeza regular é, provavelmente, o gesto com melhor relação
                custo-benefício. Um equipamento limpo arrefece melhor e mantém o ar mais
                saudável.</p>
                <h3>O que pode fazer em casa</h3>
                <ul>
                    <li><strong>Filtros da unidade interior:</strong> retirar e lavar os filtros
                    com água morna a cada poucas semanas durante a época de maior utilização,
                    deixando secar bem antes de recolocar.</li>
                    <li><strong>Grelhas e exterior do aparelho:</strong> limpar o pó com um pano
                    húmido, com o equipamento desligado.</li>
                </ul>
                <h3>O que é trabalho de técnico</h3>
                <ul>
                    <li>Limpeza profunda da serpentina e da turbina interior.</li>
                    <li>Higienização e tratamento de odores.</li>
                    <li>Verificação e limpeza da unidade exterior e da drenagem de condensados.</li>
                </ul>

                <h2>3. Manutenção e sinais de alerta</h2>
                <p>Além da limpeza, uma revisão periódica ajuda a detetar pequenos problemas
                antes que se tornem avarias maiores. Alguns sinais que justificam contactar um
                profissional:</p>
                <ul>
                    <li>O aparelho arrefece (ou aquece) menos do que costumava.</li>
                    <li>Ruídos invulgares, vibração ou cheiros persistentes.</li>
                    <li>Água a pingar da unidade interior.</li>
                    <li>Aumento pouco habitual do consumo elétrico.</li>
                </ul>
                <p>Em equipamentos usados de forma intensa, é comum recomendar-se uma
                <strong>revisão anual</strong>; o intervalo ideal pode variar consoante o uso e
                as indicações do fabricante.</p>

                <h2>Quanto custa? Uma nota honesta</h2>
                <p>O valor de uma instalação ou de uma manutenção depende de vários fatores —
                tipo e potência do equipamento, dificuldade do acesso, comprimento da tubagem e
                estado do aparelho. Por isso, em vez de indicar preços que podem não corresponder
                ao seu caso, preferimos avaliar a situação e apresentar um
                <strong>orçamento claro e sem compromisso</strong>.</p>

                <h2>Porquê falar com a FAZDETUDO.PT</h2>
                <p>Fazemos <a href="https://www.fazdetudo.pt/servico-climatizacao.html">instalação,
                limpeza e manutenção de ar condicionado</a> em Lisboa, Cascais, Almada, Setúbal e
                arredores, com atendimento por marcação e orçamento prévio. Se preferir, pode
                falar connosco diretamente por WhatsApp e descrever o que precisa.</p>
        """,
        "faq": [
            {
                "q": "Com que frequência devo limpar os filtros do ar condicionado?",
                "a": (
                    "Durante a época de maior utilização, lavar os filtros a cada poucas "
                    "semanas costuma ser suficiente. Filtros limpos ajudam o aparelho a "
                    "arrefecer melhor e a manter o ar mais saudável."
                ),
            },
            {
                "q": "É preciso fazer manutenção mesmo que o aparelho pareça funcionar bem?",
                "a": (
                    "Sim, uma revisão periódica ajuda a manter a eficiência e a detetar "
                    "pequenos problemas cedo. Em equipamentos muito usados é comum "
                    "recomendar-se uma revisão anual, mas o intervalo pode variar."
                ),
            },
            {
                "q": "Posso instalar o ar condicionado por conta própria?",
                "a": (
                    "A instalação envolve gás refrigerante e ligações elétricas, pelo que "
                    "deve ser feita por um técnico habilitado, por razões de segurança e "
                    "para preservar a garantia do fabricante."
                ),
            },
            {
                "q": "Fazem ar condicionado fora de Lisboa?",
                "a": (
                    "Sim. Trabalhamos na Grande Lisboa e Margem Sul — incluindo Cascais, "
                    "Almada, Setúbal e arredores. Contacte-nos para confirmar a sua zona."
                ),
            },
        ],
    },
]
