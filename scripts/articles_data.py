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
IMG_AC = "../images/artigos/ar-condicionado"

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
        "og_image": (
            f"{BASE_URL}/images/artigos/reparacoes-verao-lisboa/"
            "ar-condicionado-lisboa-limpeza-filtros.webp"
        ),
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
        "category": "Guias de Climatização",
        "published": "2026-06-01",
        "updated": "2026-06-01",
        "h1": "Ar Condicionado Lisboa: Instalar, Limpar e Manter o Split",
        "page_title": "Ar Condicionado Lisboa: Instalar Split | FAZDETUDO.PT",
        "meta_description": (
            "Guia prático sobre instalação, limpeza e manutenção de ar condicionado "
            "em Lisboa, Cascais e Setúbal. Saiba quando instalar, limpar filtros e pedir assistência."
        ),
        "og_title": "Ar Condicionado Lisboa: Instalar, Limpar e Manter o Split",
        "og_image": (
            f"{BASE_URL}/images/artigos/ar-condicionado/"
            "ar-condicionado-lisboa-split-sala.webp"
        ),
        "lead": (
            "Um split bem instalado e com manutenção regular trabalha melhor, pode consumir "
            "menos energia e tende a durar mais tempo. Reunimos o essencial sobre instalação, "
            "limpeza e revisão para casas e escritórios na Grande Lisboa, Cascais e Setúbal."
        ),
        "excerpt": (
            "Quando instalar, como limpar filtros, que manutenção fazer e quando pedir "
            "assistência técnica para o ar condicionado em Lisboa."
        ),
        "related_service_url": f"{BASE_URL}/servico-climatizacao.html",
        "related_service_label": "Ver serviço de Climatização e Ar Condicionado",
        "related_intro": "Precisa de instalar, limpar ou fazer manutenção ao equipamento?",
        "wa_message": (
            "Olá! Gostaria de pedir um orçamento para instalação ou manutenção de ar condicionado."
        ),
        "cta_h3": "Precisa de ar condicionado ou de uma revisão?",
        "cta_p": (
            "Fale connosco pelo WhatsApp para instalação, limpeza ou manutenção de "
            "ar condicionado em Lisboa, Cascais, Almada e Setúbal."
        ),
        "cta_button": "Pedir orçamento para ar condicionado",
        "body_html": f"""
                <p>O ar condicionado é hoje parte do conforto de muitas casas e escritórios na "
                "região de Lisboa — no calor do verão e também no apoio ao aquecimento em dias "
                "mais frios. Para tirar o melhor partido do equipamento e evitar surpresas, "
                "convém planear bem a <strong>instalação</strong>, manter a <strong>limpeza</strong> "
                "e não adiar a <strong>manutenção</strong>. Se precisar de apoio, a nossa equipa de "
                f'<a href="{BASE_URL}/servico-climatizacao.html">climatização e ar condicionado</a> '
                "pode avaliar o seu caso.</p>

                <h2>Primavera: A Janela Ideal para Instalação</h2>
                <figure class="article-figure">
                    <img src="{IMG_AC}/ar-condicionado-lisboa-split-sala.webp"
                         alt="Ar condicionado split instalado numa sala em Lisboa"
                         width="1024" height="1024" loading="eager" decoding="async">
                    <figcaption>Um split bem instalado melhora o conforto da casa e evita consumos desnecessários.</figcaption>
                </figure>
                <p>Março, abril e maio costumam ser meses favoráveis para instalar ou substituir um "
                "split: as temperaturas são mais amenas para o trabalho nas unidades exteriores, a "
                "procura de técnicos ainda não está no pico de verão e há tempo para testar o "
                "equipamento antes do calor intenso.</p>
                <p>Em muitos condomínios na Grande Lisboa, a instalação de unidades exteriores na "
                "fachada pode exigir autorização da administração. Vale a pena confirmar as regras "
                "do prédio antes de marcar a obra.</p>

                <h2>Inverno: Uma Oportunidade Subestimada</h2>
                <p>Os splits modernos com bomba de calor podem aquecer de forma eficiente mesmo com "
                "temperaturas externas baixas. Em Lisboa, onde o inverno é relativamente ameno, o "
                "modo aquecimento pode ser uma alternativa útil em divisões mal isoladas ou em "
                "escritórios com pouca exposição solar.</p>
                <p>Se está a planear instalar um split novo, pedir orçamento em setembro ou outubro "
                "pode dar mais margem de agenda. Muitas empresas — incluindo a FAZDETUDO.PT — têm "
                "disponibilidade mais flexível fora da época alta.</p>

                <h2>Tipos de Split para Casas e Escritórios em Lisboa</h2>
                <p>Nem todos os splits são iguais, e a escolha errada pode aumentar o consumo na "
                "fatura da luz. Para habitação na Grande Lisboa, estes são os formatos mais "
                "comuns:</p>
                <h3>Split Mono Inverter</h3>
                <p>É a opção mais frequente em apartamentos e moradias: uma unidade exterior alimenta "
                "uma unidade interior. A tecnologia inverter ajusta a potência ao necessário, o que "
                "pode ajudar a manter o conforto com menor desgaste do compressor.</p>
                <h3>Multi-Split</h3>
                <p>Uma unidade exterior serve várias unidades interiores. Pode fazer sentido quando o "
                "espaço na fachada ou na cobertura é limitado e quer climatizar mais do que uma "
                "divisão com um só sistema.</p>
                <h3>Cassete de Teto</h3>
                <p>Usada sobretudo em escritórios, lojas e espaços comerciais. Distribui o ar em "
                "várias direções e integra-se no teto falso — útil em salas amplas.</p>
                <p>Na faixa costeira de Cascais e Setúbal, a salinidade pode acelerar a corrosão "
                "das aletas da unidade exterior. Em zonas próximas do mar, convém considerar "
                "equipamentos com tratamento anticorrosivo e incluir a revisão da unidade exterior "
                "no plano de <a href="{BASE_URL}/servico-manutencao.html">manutenção</a>.</p>

                <h2>Limpeza de Filtros: O Que Acontece Quando se Ignora</h2>
                <p>Um filtro sujo é um dos problemas mais frequentes nos splits domésticos. Não é "
                "apenas estética: filtros entupidos obrigam o equipamento a trabalhar mais para "
                "atingir a temperatura desejada, o que <strong>pode reduzir a eficiência</strong> e "
                "<strong>pode aumentar o consumo</strong>. A qualidade do ar interior também tende "
                "a piorar.</p>
                <p>Durante os meses de uso intensivo (junho a setembro para arrefecimento, e "
                "dezembro a fevereiro para aquecimento), a limpeza regular dos filtros é "
                "recomendada. Em Lisboa e Cascais, onde o pó e o sal marinho podem acumular-se "
                "mais depressa junto à costa, convém não deixar passar demasiado tempo entre "
                "lavagens.</p>

                <h3>Como Limpar os Filtros de um Split em Casa</h3>
                <p>Num split de parede doméstico, o processo é simples: desligue o aparelho, abra a "
                "tampa frontal da unidade interior, retire os filtros (geralmente encaixados por "
                "clips), lave com água morna e detergente suave, enxague bem e deixe secar "
                "completamente antes de recolocar.</p>
                <figure class="article-figure">
                    <img src="{IMG_AC}/limpeza-filtros-ar-condicionado-split.webp"
                         alt="Limpeza de filtros de ar condicionado split"
                         width="1024" height="1024" loading="lazy" decoding="async">
                    <figcaption>A limpeza regular dos filtros ajuda o equipamento a trabalhar melhor e melhora a qualidade do ar.</figcaption>
                </figure>
                <p>Se ao abrir a tampa encontrar manchas escuras no evaporador ou um cheiro a mofo "
                "quando liga o equipamento, a limpeza caseira dos filtros já não chega — nesse "
                "caso, peça uma <a href="{BASE_URL}/servico-climatizacao.html">limpeza técnica "
                "profissional</a>.</p>

                <h3>Limpeza Profissional vs. Limpeza Doméstica</h3>
                <p>A limpeza dos filtros pelo utilizador é suficiente como manutenção regular. "
                "Uma vez por ano, habitualmente na primavera, convém contratar uma limpeza "
                "profunda: serpentina interior, turbina, bandeja de condensados e verificação da "
                "unidade exterior. Esta distinção entre manutenção mensal e revisão técnica anual "
                "é frequentemente ignorada — e pode encurtar a vida útil do equipamento se só se "
                "limparem os filtros.</p>

                <h2>Manutenção AVAC em Lisboa: O Que Inclui e Com Que Frequência</h2>
                <p>A manutenção de climatização abrange mais do que a limpeza dos filtros. Em "
                "habitação, um plano típico inclui verificação de pressões, estado das serpentinas, "
                "drenagem de condensados, ligações elétricas e teste de funcionamento nos modos "
                "frio e calor. A <a href="{BASE_URL}/servico-electricidade.html">parte elétrica</a> "
                "deve ser verificada por quem tem competência para o efeito.</p>
                <p>Em sistemas comerciais ou de maior dimensão, podem existir requisitos legais e "
                "técnicos específicos. Trabalhos que envolvam gases refrigerantes, pressões do "
                "circuito ou intervenção técnica no equipamento devem ser realizados por técnicos "
                "habilitados ou certificados.</p>
                <blockquote>
                    <p>A falta de manutenção nos sistemas de climatização pode contribuir para "
                    "desperdício energético em edifícios — por isso, uma revisão preventiva antes "
                    "do verão costuma compensar.</p>
                </blockquote>

                <h3>Calendário de Manutenção Recomendado para Lisboa</h3>
                <p>Abril é, para muitas famílias, um bom mês para a manutenção anual: o verão ainda "
                "não chegou, há tempo para corrigir pequenas falhas e o equipamento entra na época "
                "quente em melhores condições.</p>
                <ul>
                    <li><strong>Habitação:</strong> manutenção anual na primavera; limpeza dos "
                    "filtros de junho a setembro (e no aquecimento, se usar com frequência).</li>
                    <li><strong>Comércio e serviços:</strong> intervalos mais curtos, consoante "
                    "horas de funcionamento e normas internas do edifício.</li>
                </ul>

                <h2>Instalação, Manutenção Própria vs. Serviço Profissional</h2>
                <p>A questão mais comum entre proprietários em Lisboa é simples: o que posso fazer "
                "eu mesmo e o que exige um técnico? A resposta prática, em cartões:</p>
                <div class="article-task-cards">
                    <article class="article-task-card">
                        <h3>Instalação da unidade</h3>
                        <p><strong>Abordagem:</strong> Deve ser feita por técnico habilitado, com "
                        "formação adequada para gases refrigerantes e ligação elétrica segura.</p>
                        <p><strong>Em Lisboa e Cascais:</strong> Peça orçamento a instalador "
                        "certificado; instalação incorreta pode invalidar a garantia e aumentar "
                        "riscos.</p>
                    </article>
                    <article class="article-task-card">
                        <h3>Limpeza de filtros</h3>
                        <p><strong>Abordagem:</strong> Pode ser feita pelo utilizador com "
                        "regularidade durante a época de uso.</p>
                        <p><strong>Em Lisboa e Cascais:</strong> Reserve alguns minutos por mês; "
                        "filtros limpos ajudam o aparelho a trabalhar melhor.</p>
                    </article>
                    <article class="article-task-card">
                        <h3>Limpeza do evaporador e condensador</h3>
                        <p><strong>Abordagem:</strong> Requer produtos e ferramentas adequados; "
                        "recomenda-se serviço técnico.</p>
                        <p><strong>Em Lisboa e Cascais:</strong> Uma vez por ano, antes do verão, "
                        "pode evitar odores, mau desempenho e avarias.</p>
                    </article>
                    <article class="article-task-card">
                        <h3>Recarga de gás refrigerante</h3>
                        <p><strong>Abordagem:</strong> Apenas por técnico habilitado; envolve "
                        "manuseamento de fluidos refrigerantes e verificação de estanquidade.</p>
                        <p><strong>Em Lisboa e Cascais:</strong> Se o aparelho arrefece pouco, não "
                        "tente resolver sozinho — peça diagnóstico.</p>
                    </article>
                    <article class="article-task-card">
                        <h3>Verificação de pressões e carga elétrica</h3>
                        <p><strong>Abordagem:</strong> Profissional, com instrumentação adequada "
                        "ao tipo de gás e modelo do equipamento.</p>
                        <p><strong>Em Lisboa e Cascais:</strong> Incluir na manutenção anual de "
                        "primavera pode detetar fugas antes de avarias maiores.</p>
                    </article>
                </div>

                <h2>Custos de Instalação e Manutenção na Grande Lisboa</h2>
                <p>Os valores publicados online raramente refletem a realidade de cada casa: acesso "
                "à fachada, comprimento da tubagem, potência do equipamento e estado da instalação "
                "elétrica alteram o orçamento. Os intervalos abaixo são <strong>orientativos</strong> "
                "e devem ser confirmados após visita ou descrição do trabalho.</p>
                <h3>Instalação de um split doméstico</h3>
                <p>Para um split standard (potência habitual para quartos ou salas pequenas), com "
                "acesso razoável ao exterior, a instalação costuma situar-se numa faixa que varia "
                "consoante marca, distância entre unidades e trabalhos extra (suportes, furações, "
                "proteções). Peça sempre orçamento por escrito.</p>
                <h3>Manutenção anual</h3>
                <p>Uma revisão técnica completa de um split doméstico em Lisboa pode oscilar entre "
                "valores modestos e montantes mais altos se forem necessárias peças, produtos de "
                "higienização ou deslocação. A <a href="{BASE_URL}/servico-manutencao.html">manutenção "
                "preventiva</a> costuma sair mais barata do que uma reparação de emergência no "
                "agosto.</p>
                <h3>O custo de adiar a manutenção</h3>
                <p>Recargas de gás, substituição de compressor ou reparações elétricas podem custar "
                "significativamente mais do que uma revisão anual. Além do valor financeiro, um "
                "equipamento mal mantido <strong>pode aumentar o consumo</strong> e "
                "<strong>pode encurtar a vida útil</strong> do aparelho.</p>

                <figure class="article-figure">
                    <img src="{IMG_AC}/manutencao-ar-condicionado-checklist.webp"
                         alt="Checklist de manutenção de ar condicionado antes do verão"
                         width="1024" height="1024" loading="lazy" decoding="async">
                    <figcaption>Uma revisão preventiva antes do verão reduz o risco de avarias nos meses de maior calor.</figcaption>
                </figure>

                <h2>Erros Mais Comuns na Instalação e Uso do Split em Lisboa</h2>
                <p>Na instalação e no dia a dia, estes padrões repetem-se com frequência na Grande "
                "Lisboa:</p>
                <ul>
                    <li><strong>Subdimensionar o equipamento.</strong> Um quarto exposto a sul com "
                    "janelas amplas pode precisar de mais capacidade do que a área em m² sugere à "
                    "primeira vista.</li>
                    <li><strong>Má ventilação da unidade exterior.</strong> Instalar em patamar "
                    "fechado ou sem espaço de renovação de ar pode forçar o sistema e aumentar o "
                    "desgaste.</li>
                    <li><strong>Ignorar a drenagem.</strong> O condensado da unidade interior deve "
                    "escoar corretamente; tubagens entupidas ou mal inclinadas causam gotejamentos "
                    "e humidade nas paredes — situações que a nossa equipa de "
                    f'<a href="{BASE_URL}/servico-reparacoes-gerais.html">reparações gerais</a> '
                    "também pode ajudar a resolver.</li>
                </ul>

                <p><strong>Precisa de instalar, limpar ou fazer manutenção ao ar condicionado?</strong> "
                "Fale connosco pelo WhatsApp e peça uma avaliação sem compromisso.</p>
        """,
        "faq": [
            {
                "q": "Qual é o melhor mês para instalar ar condicionado em Lisboa?",
                "a": (
                    "Abril costuma ser um bom mês: a procura ainda não está no pico, há "
                    "disponibilidade de técnicos e as temperaturas permitem testar o equipamento "
                    "antes do calor intenso. Março e maio também são opções sólidas."
                ),
            },
            {
                "q": "Com que frequência devo limpar os filtros do meu split em Lisboa?",
                "a": (
                    "Durante os meses de uso intensivo (junho a setembro para arrefecimento e, "
                    "se usar aquecimento, dezembro a fevereiro), lavar os filtros a cada poucas "
                    "semanas costuma ser adequado. Em zonas com mais pó ou perto do mar, pode "
                    "ser necessário limpar com mais frequência."
                ),
            },
            {
                "q": "A manutenção do ar condicionado é obrigatória por lei em Portugal?",
                "a": (
                    "Em habitações particulares, a manutenção preventiva é sobretudo uma "
                    "recomendação técnica e de garantia. Em edifícios comerciais ou sistemas de "
                    "maior dimensão, podem aplicar-se requisitos legais específicos. Em caso de "
                    "dúvida, confirme com técnico habilitado."
                ),
            },
            {
                "q": "Porque é que o meu split cheira a mofo quando liga?",
                "a": (
                    "O cheiro a mofo costuma indicar humidade e depósitos no evaporador da unidade "
                    "interior — muitas vezes após filtros sujos ou longos períodos sem limpeza "
                    "profunda. Uma higienização técnica resolve na maioria dos casos."
                ),
            },
            {
                "q": "Preciso de autorização do condomínio para instalar um split em Lisboa?",
                "a": (
                    "Na maioria dos casos, sim. A colocação de unidades exteriores em fachadas de "
                    "prédios em regime de condomínio requer aprovação prévia da administração. "
                    "Confirme o regulamento interno antes de avançar."
                ),
            },
            {
                "q": "Qual a diferença entre instalar um split em Cascais e no centro de Lisboa?",
                "a": (
                    "A proximidade ao mar em Cascais e na faixa costeira de Setúbal favorece a "
                    "corrosão das aletas exteriores. Convém equipamentos com proteção adequada e "
                    "revisões mais atentas à unidade exterior."
                ),
            },
            {
                "q": "Vale a pena comprar um split com maior potência do que o necessário?",
                "a": (
                    "Em geral, não. Um split sobredimensionado pode ligar e desligar com demasiada "
                    "frequência, o que pode aumentar o desgaste e o consumo sem melhorar o "
                    "conforto de forma proporcional."
                ),
            },
            {
                "q": "Fazem instalação e manutenção fora de Lisboa?",
                "a": (
                    "Sim. Atendemos a Grande Lisboa e Margem Sul — Cascais, Almada, Setúbal e "
                    "arredores. Contacte-nos para confirmar a sua zona."
                ),
            },
        ],
    },
]
