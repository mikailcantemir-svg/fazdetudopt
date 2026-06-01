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


IMG_VERAO = "../images/artigos/reparacoes-verao-lisboa"

ARTICLES = [
    {
        "slug": "10-reparacoes-em-casa-antes-do-verao-lisboa.html",
        "category": "Guias de Manutenção",
        "published": "2026-06-01",
        "updated": "2026-06-01",
        "h1": "10 Reparações em Casa que Deve Fazer Antes do Verão em Lisboa",
        "page_title": "10 Reparações em Casa Antes do Verão | FAZDETUDO.PT",
        "meta_description": (
            "Conheça 10 reparações em casa que deve fazer antes do verão em Lisboa, "
            "Cascais e Setúbal para evitar avarias, infiltrações e gastos de emergência."
        ),
        "og_title": "10 Reparações em Casa Antes do Verão em Lisboa",
        "lead": (
            "Muitos proprietários só percebem que a casa precisa de atenção quando o calor "
            "aperta e surge uma avaria ou uma infiltração. Reunimos dez intervenções práticas "
            "para fazer na primavera na Grande Lisboa e Margem Sul — antes do pico de verão."
        ),
        "excerpt": (
            "Dez reparações e manutenções para fazer na primavera em Lisboa: ar condicionado, "
            "terraços, canalização, pintura, eletricidade, piscina e mais."
        ),
        "related_service_url": f"{BASE_URL}/servico-reparacoes-gerais.html",
        "related_service_label": "Ver serviço de Reparações Gerais e Faz-Tudo",
        "related_intro": "Quer tratar várias tarefas numa só visita?",
        "wa_message": (
            "Olá! Gostaria de pedir um orçamento para reparações e manutenção "
            "em casa antes do verão."
        ),
        "cta_h3": "Precisa de preparar a casa antes do verão?",
        "cta_p": (
            "Fale connosco pelo WhatsApp e peça uma avaliação sem compromisso. "
            "Atendemos Lisboa, Cascais, Almada, Setúbal e arredores."
        ),
        "cta_button": "Pedir orçamento para reparações antes do verão",
        "body_html": f"""
                <p>Muitos proprietários em Lisboa só percebem que a casa precisa de atenção quando o problema já está instalado no meio do verão — com calor intenso, equipamentos a falhar ou humidade a aparecer nas paredes. As <strong>reparações preventivas na primavera</strong> ajudam a evitar avarias, infiltrações e despesas de emergência. Se precisar de apoio, a <a href="{BASE_URL}/servico-reparacoes-gerais.html">equipa de reparações gerais</a> da FAZDETUDO.PT pode tratar várias tarefas numa só visita.</p>

                <h2>1. Verificação e Limpeza do Ar Condicionado</h2>
                <p>Na prática, o ar condicionado é um dos equipamentos mais usados no verão e também um dos que mais falhas regista quando não é revisto a tempo. Muitas famílias ligam o aparelho pela primeira vez em junho e só então descobrem filtros entupidos ou falta de gás refrigerante.</p>
                <figure class="article-figure">
                    <img src="{IMG_VERAO}/ar-condicionado-lisboa-limpeza-filtros.webp"
                         alt="Técnico a limpar filtros de ar condicionado split em Lisboa"
                         width="1024" height="1024" loading="eager" decoding="async">
                    <figcaption>Limpeza de filtros e revisão do split antes da época de calor.</figcaption>
                </figure>
                <p>A limpeza dos filtros internos deve ser feita pelo menos duas vezes por ano; a revisão completa — gás, serpentinas e inspeção elétrica — deve ser feita por um técnico certificado antes do calor. Em Cascais e na Linha de Sintra, onde há muitos sistemas mais antigos, este ponto é ainda mais relevante.</p>
                <p><strong>Dica:</strong> peça ao técnico para verificar a unidade exterior. Poeira, folhas e insetos reduzem a dissipação de calor e podem forçar o compressor a trabalhar mais do que o necessário.</p>
                <p>Filtros sujos podem <strong>aumentar o consumo de energia</strong> e reduzir a eficiência do equipamento. Vale a pena tratar o assunto antes de usar o ar condicionado horas seguidas nos dias mais quentes.</p>
                <p>Saiba mais no nosso serviço de <a href="{BASE_URL}/servico-climatizacao.html">climatização e ar condicionado</a>.</p>

                <h2>2. Impermeabilização de Terraços e Varandas</h2>
                <p>A impermeabilização de terraços é uma das intervenções com melhor relação custo-benefício. As chuvas do inverno criam infiltrações que só se tornam visíveis meses depois — muitas vezes já com calor, quando a dilatação térmica empurra a humidade para o interior.</p>
                <figure class="article-figure">
                    <img src="{IMG_VERAO}/impermeabilizacao-terraco-lisboa.webp"
                         alt="Impermeabilização de terraço e varanda em habitação na Grande Lisboa"
                         width="1024" height="1024" loading="lazy" decoding="async">
                    <figcaption>Tratar terraços e varandas a seco, na primavera, evita obras de urgência.</figcaption>
                </figure>
                <p>Não basta aplicar tinta impermeabilizante por cima do material antigo. Uma <strong>impermeabilização eficaz</strong> exige remover o degradado, preparar a superfície, aplicar primário e demãos adequadas ao suporte. Fazer isto em março ou abril é muito mais simples do que reparar uma laje saturada no outono.</p>
                <p>Verifique juntas, beirais e encontros entre paredes e pavimento — zonas onde a água encontra caminho com facilidade.</p>

                <h2>3. Revisão da Canalização e Deteção de Fugas</h2>
                <p>No verão o consumo de água tende a subir: mais duches, rega, piscina e lavagens. Uma rede com microfugas ou pressão mal regulada pode transformar-se em desperdício e em danos em paredes ou soalhos.</p>
                <figure class="article-figure">
                    <img src="{IMG_VERAO}/deteccao-fugas-canalizacao-lisboa.webp"
                         alt="Revisão de canalização e deteção de fugas de água em casa"
                         width="1024" height="1024" loading="lazy" decoding="async">
                    <figcaption>Detetar fugas cedo poupa água e evita danos ocultos na habitação.</figcaption>
                </figure>
                <p>Queda de pressão gradual na torneira ou no chuveiro pode indicar calcário nos bicos — ou uma fuga lenta na rede interior. Em ambos os casos, convém agir antes do aumento de consumo.</p>
                <p>Segundo a ERSAR, uma parte relevante da água consumida em habitações pode perder-se em fugas internas não detetadas. Uma revisão por <a href="{BASE_URL}/servico-canalizacoes.html">canalizador</a> ajuda a confirmar o estado da instalação.</p>
                <p><strong>Dica:</strong> feche todas as torneiras e aparelhos, observe o contador durante cerca de 30 minutos sem consumir água. Se o mostrador avançar, há uma fuga ativa a resolver.</p>

                <h2>4. Pintura e Tratamento de Paredes Exteriores</h2>
                <p>A fachada na Grande Lisboa sofre humidade no inverno, salitre costeiro e calor forte no verão. A primavera costuma ser a janela mais adequada para <a href="{BASE_URL}/servico-pinturas.html">pintura e tratamento exterior</a>: temperaturas moderadas e menor humidade favorecem a aderência.</p>
                <p>Manchas de humidade ou bolhas devem ser tratadas <em>antes</em> de pintar — não por cima. Aplicar tinta sobre humidade ativa tende a ser dinheiro mal gasto; o problema costuma regressar.</p>
                <p>Em Cascais, fachadas em pedra calcária pedem produtos permeáveis ao vapor que não aprisionem humidade no interior do material.</p>

                <h2>5. Revisão da Instalação Elétrica</h2>
                <p>O verão aumenta a carga: ar condicionado, ventoinhas, frigoríficos, bombas de piscina e iluminação exterior. Em apartamentos antigos de Lisboa, o quadro elétrico pode não estar dimensionado para esta sobrecarga.</p>
                <p>Disjuntores que disparam com frequência indicam sobrecarga ou falha de isolamento. Uma verificação por <a href="{BASE_URL}/servico-electricidade.html">eletricista certificado</a> inclui o quadro, resistências de isolamento e ligação à terra — muitas vezes ausente em habitações antigas.</p>

                <h2>6. Manutenção da Piscina</h2>
                <p>Abril e maio são os meses certos para abrir a piscina: pH, cloro, bomba de filtração, revestimento e filtro de areia. Uma piscina mal tratada no inverno chega à primavera com água verde, algas ou fissuras que exigem intervenção mais pesada.</p>
                <p>A manutenção preventiva em abril costuma ser mais económica do que uma urgência em agosto, quando técnicos e produtos estão mais pressionados. <a href="{BASE_URL}/servico-piscinas.html">Manutenção de piscinas</a> na Margem Sul e Setúbal é especialmente relevante nesta época.</p>

                <h2>7. Reparação de Portões, Fechaduras e Estores</h2>
                <p>Estores de enrolar e motores elétricos falham muitas vezes no verão — precisamente quando mais protegem do calor. Corrigir correias ou motores com antecedência evita divisões sem proteção solar durante dias.</p>
                <p>Portões de garagem devem ser lubrificados e regulados; o calor dilata trilhos metálicos. Fechaduras expostas ao exterior beneficiam de inspeção e lubrificação antes do calor seco degradar os mecanismos.</p>
                <p>Consulte <a href="{BASE_URL}/servico-estores-persianas.html">reparação de estores e persianas</a> e serviços de serralharia quando necessário.</p>

                <h2>8. Limpeza de Caleiras e Rufos</h2>
                <p>Caleiras entupidas fazem transbordar água pelas paredes na primavera — um problema fácil de prevenir e caro de remediar. Em jardins com árvores, limpar pelo menos duas vezes por ano; pinheiros (comuns em Sintra ou Azeitão) entopem caleiras com particular rapidez.</p>
                <p>Rufos de zinco ou alumínio degradados criam entradas de água invisíveis do chão. Uma inspeção anual na cobertura ajuda a detetar o problema a tempo. <a href="{BASE_URL}/servico-manutencao.html">Manutenção preventiva</a> pode incluir estes trabalhos de acesso.</p>

                <h2>9. Jardinagem e Preparação de Espaços Exteriores</h2>
                <p>Preparar o exterior não é só estética: poda de árvores junto à casa reduz risco de queda de ramos em trovoadas; remover vegetação seca ajuda na prevenção de incêndio em zonas como Sintra, Palmela ou Sesimbra.</p>
                <p>Teste sistemas de rega em março ou abril. Decks e madeira exterior devem ser limpos e tratados antes do calor intenso — sem proteção, a madeira seca e racha mais depressa.</p>
                <p>Veja o nosso serviço de <a href="{BASE_URL}/servico-jardinagem.html">jardinagem</a>.</p>

                <h2>10. Inspeção do Telhado e Cobertura</h2>
                <p>O telhado é a zona que menos atenção recebe até aparecer uma mancha no teto. Uma inspeção na primavera identifica telhas partidas, deslocadas ou vedantes degradados.</p>
                <p>Em coberturas planas ou terraços, verifique membranas, ralos e juntas de dilatação. Um ralo entupido com detritos pode causar acumulação de água e infiltrações difíceis de localizar.</p>

                <h2>Comparação: Fazer Agora vs. Adiar para o Verão</h2>
                <p>Adiar reparações domésticas pode parecer poupança, mas muitas vezes acaba por sair mais caro ou mais stressante. Resumo de três intervenções frequentes:</p>
                <table class="article-comparison-table">
                    <thead>
                        <tr>
                            <th>Intervenção</th>
                            <th>Fazer na primavera</th>
                            <th>Adiar para o verão</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Ar condicionado</td>
                            <td>Agenda disponível, equipamento pronto para o calor</td>
                            <td>Técnicos sobrecarregados, risco de avaria em agosto</td>
                        </tr>
                        <tr>
                            <td>Impermeabilização de terraço</td>
                            <td>Condições de temperatura e humidade adequadas</td>
                            <td>Calor pode comprometer aderência; chuva no outono atrasa obra</td>
                        </tr>
                        <tr>
                            <td>Piscina</td>
                            <td>Abertura normal, pronta a usar em junho</td>
                            <td>Urgência pode sair bastante mais cara; risco de não ficar a tempo</td>
                        </tr>
                    </tbody>
                </table>

                <p>Precisa de preparar a sua casa antes do verão? Fale connosco pelo WhatsApp e peça uma avaliação sem compromisso.</p>
        """,
        "faq": [
            {
                "q": "Qual é o melhor mês para fazer reparações em casa em Lisboa antes do verão?",
                "a": (
                    "Março e abril são, em geral, os meses mais indicados: temperaturas amenas, "
                    "humidade em descida e maior disponibilidade de profissionais. Em maio ainda "
                    "é possível fazer a maioria das intervenções, mas as agendas começam a "
                    "encher."
                ),
            },
            {
                "q": "Quanto custa contratar um handyman no Grande Lisboa para uma lista de reparações?",
                "a": (
                    "O custo depende do número e tipo de tarefas. Intervenções pontuais "
                    "costumam ser faturadas por hora de mão de obra; para listas combinadas "
                    "pode pedir um orçamento fechado após avaliação no local."
                ),
            },
            {
                "q": "Como posso detetar fugas de água em casa sem chamar um técnico?",
                "a": (
                    "Feche torneiras e aparelhos, observe o contador de água durante cerca de "
                    "30 minutos sem consumir. Se o mostrador avançar, há provável fuga na rede "
                    "interior — nesse caso convém um canalizador confirmar a origem."
                ),
            },
            {
                "q": "Os serviços em Cascais e Setúbal têm custos diferentes dos de Lisboa?",
                "a": (
                    "Os preços base são frequentemente semelhantes, mas pode haver deslocação "
                    "adicional para zonas mais afastadas. O ideal é pedir orçamento indicando "
                    "a morada e o tipo de trabalho."
                ),
            },
            {
                "q": "É possível fazer estas reparações sozinho ou é necessário um profissional?",
                "a": (
                    "Limpeza de filtros de ar condicionado, lubrificação de portões ou caleiras "
                    "acessíveis podem ser feitas pelo proprietário. Impermeabilização de coberturas, "
                    "revisão elétrica, gás de AVAC e fugas na canalização devem ser feitas por "
                    "técnicos habilitados."
                ),
            },
            {
                "q": "Com quanta antecedência devo reservar manutenção doméstica antes do verão?",
                "a": (
                    "Contactar em março para trabalhos em abril ou maio é uma boa referência. "
                    "Em junho, as agendas no Grande Lisboa costumam estar cheias, com esperas "
                    "de uma a duas semanas em muitos serviços."
                ),
            },
        ],
    },
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
