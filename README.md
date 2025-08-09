# Análise de Dados de Salários em Data Science - Imersão Python Alura

**Transformando Dados Brutos em Insights Acionáveis e Visualizações Interativas.**

---

## Abstract (Resumo Técnico)

Este projeto representa uma implementação compreensiva de um pipeline de análise de dados, desenvolvido como parte da Imersão Python da Alura. O trabalho aborda o problema de extrair inteligência de mercado a partir de um dataset público sobre salários na área de Ciência de Dados. A metodologia adotada segue um fluxo de trabalho canônico em projetos de dados, iniciando com uma Análise Exploratória de Dados (EDA) para compreender a estrutura, qualidade e características intrínsecas do dataset. Subsequentemente, o projeto avança para uma fase crítica de pré-processamento e limpeza, onde são aplicadas técnicas para tratamento de valores ausentes, padronização de categorias e conversão de tipos de dados, garantindo a integridade e a consistência dos dados para análises futuras. A culminação do projeto é a criação de uma visualização de dados avançada e interativa — um globo 3D gerado com a biblioteca Plotly — que mapeia a distribuição geográfica dos salários médios em escala global. A principal contribuição deste repositório é servir como um recurso educacional e um artefato de portfólio, demonstrando de forma prática e sequencial as etapas fundamentais de um ciclo de vida de projeto de dados, desde a ingestão e limpeza até a comunicação de resultados através de visualizações impactantes.

## Badges Abrangentes


![Linguagem Principal](https://img.shields.io/github/languages/top/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge&logo=python&logoColor=white)


![Licença](https://img.shields.io/github/license/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge&color=blue)


![Issues Abertas](https://img.shields.io/github/issues/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge&logo=github)


![Pull Requests](https://img.shields.io/github/issues-pr/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge&logo=github)


![Último Commit](https://img.shields.io/github/last-commit/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge&logo=git)


![Tamanho do Repositório](https://img.shields.io/github/repo-size/ESousa97/imersao-python-alura-agosto-2025?style=for-the-badge)


## Sumário (Table of Contents)

1.  [Introdução e Motivação](#introdução-e-motivação)
2.  [Arquitetura do Sistema](#arquitetura-do-sistema)
3.  [Decisões de Design Chave](#decisões-de-design-chave)
4.  [✨ Funcionalidades Detalhadas](#-funcionalidades-detalhadas-com-casos-de-uso)
5.  [🛠️ Tech Stack Detalhado](#️-tech-stack-detalhado)
6.  [📂 Estrutura Detalhada do Código-Fonte](#-estrutura-detalhada-do-código-fonte)
7.  [📋 Pré-requisitos Avançados](#-pré-requisitos-avançados)
8.  [🚀 Guia de Instalação e Configuração Avançada](#-guia-de-instalação-e-configuração-avançada)
9.  [⚙️ Uso Avançado e Exemplos](#️-uso-avançado-e-exemplos)
10. [API Reference](#-api-reference-se-aplicável)
11. [🧪 Estratégia de Testes e Qualidade de Código](#-estratégia-de-testes-e-qualidade-de-código)
12. [🚢 Deployment Detalhado e Escalabilidade](#-deployment-detalhado-e-escalabilidade)
13. [📜 Licença e Aspectos Legais](#-licença-e-aspectos-legais)
14. [👥 Equipe Principal e Colaboradores Chave](#-equipe-principal-e-colaboradores-chave)
15. [❓ FAQ (Perguntas Frequentes)](#-faq-perguntas-frequentes)
16. [📞 Contato e Suporte](#-contato-e-suporte)

## Introdução e Motivação

No cenário tecnológico atual, a área de Ciência de Dados se consolidou como um dos campos mais dinâmicos e de maior crescimento. Compreender as tendências de remuneração, os níveis de senioridade mais demandados e a distribuição geográfica das oportunidades é crucial tanto para profissionais que buscam se posicionar no mercado quanto para empresas que desejam atrair talentos. No entanto, os dados brutos disponíveis publicamente, embora valiosos, frequentemente se apresentam de forma não estruturada, com inconsistências, valores ausentes e em formatos que não permitem a extração direta de insights.

Este projeto nasceu da necessidade de transpor essa barreira, aplicando um processo metodológico de análise de dados para transformar um conjunto de dados brutos em conhecimento acionável. Desenvolvido no contexto da **Imersão Python da Alura**, o projeto serve como uma jornada prática através das etapas essenciais do trabalho de um analista ou cientista de dados.

A motivação central é dupla:
1.  **Educacional:** Prover um exemplo claro, documentado e reprodutível de um pipeline de dados, demonstrando as melhores práticas no uso de ferramentas como `pandas` para manipulação e `plotly` para visualização. O projeto é estruturado em "aulas", refletindo uma progressão pedagógica do simples para o complexo.
2.  **Prática:** Gerar análises e visualizações concretas que respondem a perguntas de negócio relevantes sobre o mercado de trabalho em Data Science. O resultado final não é apenas código, mas também artefatos de dados (CSVs limpos) e uma visualização interativa que comunica os achados de forma eficaz.

O projeto se diferencia por não apenas aplicar técnicas, mas por documentar o "porquê" por trás de cada etapa, desde a tradução de colunas para facilitar a compreensão até a escolha de estratégias específicas para tratamento de dados e a seleção de uma biblioteca de visualização que favorece a interatividade e o engajamento do usuário.

## Arquitetura do Sistema

A arquitetura do projeto não se configura como um sistema de software tradicional com serviços em tempo real, mas sim como um **Pipeline de Processamento de Dados em Lotes (Batch Data Pipeline)**. A estrutura é sequencial e modular, onde cada estágio consome o artefato do estágio anterior, processa-o e gera um novo artefato, enriquecendo os dados a cada passo.

O fluxo de dados pode ser visualizado através do seguinte diagrama:

```mermaid
graph TD
    A[🌐 Fonte de Dados Externa<br>(CSV Bruto no GitHub)] --> B{Estágio 1: Análise Exploratória<br>(py/aula1/aula_1.py)};
    
    subgraph "Pipeline Principal"
        direction LR
        B -- Gera --> C[📊 Artefato 1<br>(salarios_processados.csv)];
        C -- Consumido por --> D{Estágio 2: Limpeza e Preparação<br>(py/aula2/aula_2.py)};
        D -- Gera --> E[🧹 Artefato 2<br>(dados_limpos_aula2.csv)];
        E -- Consumido por --> F{Estágio 3: Visualização<br>(py/aula3/3_visualização.py)};
        F -- Gera --> G[🌍 Artefato Final<br>(Globo Interativo - HTML)];
    end

    subgraph "Processo Paralelo (Desafio)"
        direction LR
        H[💡 Geração de Dados Fictícios] --> I{Desafio Luri<br>(py/aula2/DesafioLuri/desafio2_luri.py)};
        I -- Gera --> J[📄 CSVs de Alunos];
    end

    style A fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#4ECDC4,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#A8E6CF,stroke:#333,stroke-width:2px,color:#333
    style C fill:#FFE66D,stroke:#333,stroke-width:1px
    style E fill:#FFE66D,stroke:#333,stroke-width:1px
    style B fill:#45B7D1,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#45B7D1,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#45B7D1,stroke:#333,stroke-width:2px,color:#fff
    style I fill:#B8A9FF,stroke:#333,stroke-width:2px,color:#fff
```

### Detalhamento dos Componentes:

*   **Fonte de Dados Externa:** Um arquivo CSV bruto hospedado em um repositório público no GitHub, servindo como ponto de partida único e imutável para o pipeline.
*   **Estágio 1 (Aula 1 - Análise Exploratória):** Este script Python é responsável pela ingestão dos dados brutos. Suas tarefas incluem:
    *   Carregamento do CSV para um DataFrame `pandas`.
    *   Análise inicial (dimensões, tipos de dados, estatísticas descritivas).
    *   Renomeação das colunas para o português, melhorando a legibilidade.
    *   Padronização inicial de valores categóricos.
    *   Geração do primeiro artefato (`salarios_processados.csv`), uma versão mais limpa e compreensível dos dados.
*   **Estágio 2 (Aula 2 - Limpeza e Preparação):** Consome o artefato do Estágio 1. Suas responsabilidades são:
    *   Identificação e análise de valores nulos (`NaN`).
    *   Aplicação de uma estratégia de limpeza (neste caso, remoção das linhas com dados nulos via `dropna()`).
    *   Conversão de tipos de dados para formatos mais adequados (ex: `float` para `int`).
    *   Geração do segundo artefato (`dados_limpos_aula2.csv`), que representa o dataset pronto para análise e visualização.
*   **Estágio 3 (Aula 3 - Visualização):** A fase final do pipeline, que consome o dataset limpo. Suas funções são:
    *   Agregação dos dados (cálculo do salário médio por país).
    *   Enriquecimento geográfico (mapeamento de códigos de país ISO2 para ISO3).
    *   Geração da visualização interativa com `plotly`.
    *   Produção do artefato final, um arquivo HTML autocontido que pode ser aberto em qualquer navegador.
*   **Processo Paralelo (Desafio da Luri):** Um módulo autocontido que demonstra técnicas de limpeza de dados em um cenário diferente. Ele gera seus próprios dados fictícios, aplica métodos de imputação (preenchimento de nulos com média/mediana) e salva seus próprios resultados, servindo como um exercício complementar.

## Decisões de Design Chave

1.  **Estrutura Dual: Notebooks e Scripts (`.ipynb` vs `.py`):**
    *   **Decisão:** Manter duas estruturas de código paralelas: uma no diretório `notebook/` e outra no `py/`.
    *   **Justificativa:** Esta abordagem atende a dois públicos e propósitos distintos. Os **Jupyter Notebooks** (`.ipynb`) são ideais para o ensino e a exploração. Eles permitem a execução de código em células, a visualização imediata de outputs (DataFrames, gráficos) e a intercalação de texto explicativo em Markdown, tornando o processo de aprendizado mais interativo e didático. Os **scripts Python** (`.py`), por outro lado, são otimizados para automação e reprodutibilidade. Eles podem ser executados a partir da linha de comando, integrados em pipelines maiores (ex: Airflow, cron jobs) e versionados de forma mais limpa, representando uma "versão de produção" da análise.

2.  **Pipeline Sequencial com Artefatos Intermediários:**
    *   **Decisão:** Cada "aula" ou estágio do projeto gera um arquivo CSV intermediário que serve como entrada para o próximo estágio.
    *   **Justificativa:** Essa arquitetura desacopla as etapas do pipeline. Permite a inspeção, depuração e validação dos dados em cada fase. Se uma etapa falhar, as anteriores não precisam ser reexecutadas. Além disso, os artefatos (`salarios_processados.csv`, `dados_limpos_aula2.csv`) são valiosos por si só, podendo ser utilizados para outras análises ou compartilhados.

3.  **Escolha de `Plotly` para Visualização Final:**
    *   **Decisão:** Utilizar a biblioteca `plotly` para a visualização principal do projeto, em detrimento de bibliotecas mais tradicionais como `matplotlib` ou `seaborn` (que também estão presentes nos `requirements`).
    *   **Justificativa:** O objetivo da Aula 3 era criar uma visualização de alto impacto e interativa. `Plotly` se destaca na geração de gráficos interativos baseados em HTML/JavaScript, que permitem ao usuário final explorar os dados (zoom, rotação, hover). A projeção de globo ortográfico é uma funcionalidade avançada que comunica a natureza global dos dados de forma muito mais eficaz do que um mapa 2D estático.

4.  **Estratégia de Tratamento de Nulos: Remoção vs. Imputação:**
    *   **Decisão:** No pipeline principal (Aula 2), os poucos registros com valores nulos foram removidos (`dropna()`). No "Desafio da Luri", os valores nulos foram preenchidos (imputados) com a média ou mediana.
    *   **Justificativa:** Esta foi uma decisão pedagógica deliberada para demonstrar dois cenários comuns. No dataset principal, a quantidade de dados nulos era ínfima (<0.01%), tornando a remoção uma abordagem segura e simples que não introduz viés significativo. No desafio, com um dataset fictício e uma proporção maior de nulos (10-20%), a imputação foi usada para ilustrar técnicas de preenchimento e preservar o tamanho da amostra, uma situação comum em datasets menores ou com muitos dados faltantes.

## ✨ Funcionalidades Detalhadas (com Casos de Uso)

### 1. Análise Exploratória e Padronização (Aula 1)
*   **Propósito:** Realizar a primeira inspeção nos dados brutos para entender sua estrutura e realizar uma padronização inicial.
*   **Funcionalidades:**
    *   **Carregamento de Dados:** Ingestão de dados a partir de uma URL remota.
    *   **Diagnóstico do DataFrame:** Exibição de informações vitais como número de linhas/colunas, tipos de dados por coluna e contagem de valores não nulos.
    *   **Análise Estatística:** Geração de estatísticas descritivas (média, mediana, desvio padrão, etc.) para colunas numéricas.
    *   **Tradução e Renomeação:** Conversão dos nomes das colunas do inglês para o português para facilitar a análise e a compreensão.
    *   **Padronização Categórica:** Mapeamento de abreviações (ex: `SE`, `MI`, `EN`) para termos descritivos (`senior`, `pleno`, `junior`) e valores numéricos (`0`, `50`, `100`) para categorias (`presencial`, `hibrido`, `remoto`).
*   **Caso de Uso:** Um analista de dados recebe um novo dataset. Antes de qualquer análise profunda, ele executa este script para obter um "raio-x" completo dos dados, identificar inconsistências iniciais e criar uma versão de trabalho mais limpa e intuitiva, salva como `salarios_processados.csv`.

### 2. Limpeza de Dados e Conversão de Tipos (Aula 2)
*   **Propósito:** Garantir a qualidade e a integridade dos dados, preparando-os para análises e modelagem.
*   **Funcionalidades:**
    *   **Detecção de Nulos:** Varredura sistemática do dataset para identificar e quantificar valores ausentes (`NaN`) em cada coluna.
    *   **Remoção de Nulos:** Aplicação da estratégia de exclusão de linhas que contêm qualquer valor nulo, resultando em um dataset completo.
    *   **Conversão de Tipos:** Ajuste dos tipos de dados para formatos mais apropriados e eficientes em termos de memória (ex: conversão da coluna `ano` de `float64` para `int64` após a remoção dos nulos).
*   **Caso de Uso:** Após a exploração inicial, o analista percebe que a coluna `ano` contém valores nulos, o que a força a ser do tipo `float`. Para realizar operações de séries temporais ou agrupamentos por ano, ele executa este script para limpar os dados e converter a coluna para um tipo inteiro, salvando o resultado final em `dados_limpos_aula2.csv`.

### 3. Desafio de Limpeza de Dados (Desafio da Luri)
*   **Propósito:** Exercício prático e autocontido para treinar técnicas de limpeza e manipulação de dados em um ambiente controlado.
*   **Funcionalidades:**
    *   **Criação de Dataset Fictício:** Geração programática de um DataFrame de alunos com dados simulados, incluindo a introdução intencional de valores nulos.
    *   **Imputação de Dados:** Preenchimento de valores nulos na coluna `nota` com a média e na coluna `idade` com a mediana das respectivas colunas.
    *   **Filtragem e Análise:** Seleção de alunos com notas acima da média e geração de um relatório final com estatísticas e rankings.
*   **Caso de Uso:** Um estudante de ciência de dados quer praticar suas habilidades com `pandas`. Ele executa este script para vivenciar um ciclo completo de limpeza de dados, desde a criação de um problema até a sua solução, comparando os dados antes e depois do tratamento.

### 4. Visualização Geográfica Interativa (Aula 3)
*   **Propósito:** Comunicar os insights sobre a distribuição salarial de forma visualmente impactante e interativa.
*   **Funcionalidades:**
    *   **Agregação de Dados por País:** Cálculo do salário médio em USD e da contagem de registros para cada país presente no dataset.
    *   **Enriquecimento Geográfico:** Mapeamento dos códigos de país de duas letras (ISO 3166-1 alpha-2) para o formato de três letras (alpha-3), necessário para o `plotly`.
    *   **Geração de Globo 3D:** Construção de um mapa coroplético projetado em um globo ortográfico, onde a cor de cada país representa seu salário médio.
    *   **Hover Interativo Personalizado:** Configuração de tooltips que aparecem ao passar o mouse sobre um país, exibindo informações detalhadas como nome do país, região, salário médio formatado e número de registros na amostra.
    *   **Animação de Rotação:** Implementação de uma animação que rotaciona o globo automaticamente, permitindo a visualização de todos os continentes sem interação manual.
*   **Caso de Uso:** Um gerente de produto ou um recrutador quer entender rapidamente onde estão os maiores polos de talentos e quais regiões oferecem os maiores salários em Data Science. Ele abre o arquivo HTML gerado por este script e explora o globo interativo, girando-o e passando o mouse sobre os países de interesse para obter insights imediatos.

## 🛠️ Tech Stack Detalhado

A seleção de tecnologias para este projeto foi orientada pela eficiência, poder de análise e padrões da indústria de Ciência de Dados com Python.

| Categoria | Tecnologia | Versão Específica | Propósito no Projeto | Justificativa da Escolha |
| :--- | :--- | :--- | :--- | :--- |
| **Análise de Dados** | **Python** | 3.9+ | Linguagem principal para toda a lógica de script e processamento. | Ecossistema maduro e robusto para Ciência de Dados, com vasta disponibilidade de bibliotecas. |
| **Análise de Dados** | **Pandas** | >=1.5.0 | Estrutura de dados central (DataFrame) para manipulação, limpeza e análise. | Padrão de fato da indústria para manipulação de dados tabulares em Python. Oferece alta performance e uma API expressiva. |
| **Análise de Dados** | **NumPy** | >=1.21.0 | Suporte para operações numéricas eficientes e arrays multidimensionais. | Biblioteca fundamental para computação científica em Python, da qual o Pandas depende. Usada para cálculos e manipulação de dados numéricos. |
| **Análise de Dados** | **SciPy** | >=1.7.0 | Utilizada para funções estatísticas e científicas mais avançadas. | Embora seu uso seja implícito em algumas funções de alto nível, sua presença garante acesso a um conjunto vasto de algoritmos científicos. |
| **Visualização** | **Plotly** | >=5.0.0 | Geração da visualização final, o globo 3D interativo. | Escolhida por sua capacidade de criar gráficos interativos e de alta qualidade (D3.js) que podem ser facilmente exportados para HTML. |
| **Visualização** | **Matplotlib** | >=3.5.0 | Biblioteca base para visualizações estáticas (usada em notebooks). | Ferramenta fundamental e versátil para plotagem em Python. Serve como base para outras bibliotecas como o Seaborn. |
| **Visualização** | **Seaborn** | >=0.11.0 | Criação de gráficos estatísticos estáticos e visualmente atraentes. | Fornece uma interface de alto nível para Matplotlib, simplificando a criação de gráficos informativos e esteticamente agradáveis. |
| **Ambiente Dev.** | **Jupyter** | >=1.0.0 | Ambiente de notebook para desenvolvimento exploratório e educacional. | Ferramenta essencial para análise interativa, permitindo a combinação de código, visualizações e texto em um único documento. |
| **Ambiente Dev.** | **IPython** | >=7.0.0 | Shell interativo avançado que potencializa os notebooks Jupyter. | Oferece funcionalidades como autocompletar, introspecção e uma rica experiência de computação interativa. |

## 📂 Estrutura Detalhada do Código-Fonte

A organização do repositório foi projetada para ser lógica e escalável, separando claramente o código de exploração (notebooks) do código de execução (scripts), bem como os dados de entrada e saída de cada etapa.

```
imersao-python-alura-agosto-2025-main/
├── notebook/                  # Contém os Jupyter Notebooks para exploração e ensino.
│   ├── Aula_1_Imersão_dados_com_Python_Alura_Agosto_2025.ipynb
│   ├── Aula_2_Preparação_e_limpeza_dos_dadosAlura_Agosto_2025.ipynb
│   └── Aula_3_Visualização_do_Dados_Alura_Agosto_2025.ipynb
│
├── py/                        # Contém os scripts Python (.py) prontos para execução.
│   ├── aula1/                 # Módulo da Aula 1: Análise Exploratória.
│   │   ├── aula_1_imersão_dados_com_python_alura_agosto_2025.py
│   │   ├── requirements.txt   # Dependências específicas da Aula 1.
│   │   ├── README.md          # Documentação do módulo da Aula 1.
│   │   └── salarios_processados.csv # Artefato de saída da Aula 1.
│   │
│   ├── aula2/                 # Módulo da Aula 2: Limpeza de Dados.
│   │   ├── aula_2_imersão_dados_com_python_alura_agosto_2025.py
│   │   ├── requirements.txt   # Dependências específicas da Aula 2.
│   │   ├── README.md          # Documentação do módulo da Aula 2.
│   │   ├── dados_limpos_aula2.csv # Artefato de saída da Aula 2.
│   │   └── DesafioLuri/       # Sub-módulo para o desafio complementar.
│   │       ├── desafio2_luri.py
│   │       ├── README.md
│   │       ├── alunos_dataset_completo.csv # Saídas do desafio.
│   │       └── alunos_acima_media.csv
│   │
│   └── aula3/                 # Módulo da Aula 3: Visualização.
│       ├── 3_visualização_do_dados_alura_agosto_2025.py
│       ├── requirements.txt   # Dependências específicas da Aula 3.
│       ├── README.md          # Documentação do módulo da Aula 3.
│       └── demo.png           # Imagem de exemplo da visualização gerada.
│
└── README.md                  # Este arquivo de documentação principal.
```

### Filosofia da Estrutura:
*   **Separação de Interesses:** O diretório `notebook/` é para o "laboratório", onde as ideias são testadas e o processo é explicado passo a passo. O diretório `py/` é a "fábrica", contendo código otimizado para ser executado de forma autônoma.
*   **Modularidade:** Cada "aula" é tratada como um módulo autocontido dentro do diretório `py/`, com suas próprias dependências, documentação e artefatos. Isso facilita o entendimento e a execução de cada parte do projeto isoladamente.
*   **Dados como Artefatos:** Os arquivos `.csv` gerados não são tratados como dados temporários, mas como artefatos versionados que marcam a conclusão bem-sucedida de uma etapa do pipeline.

## 📋 Pré-requisitos Avançados

Para replicar o ambiente de desenvolvimento e executar todos os scripts deste projeto, os seguintes componentes são necessários:

*   **Python:** Versão `3.9` ou superior.
*   **pip:** Gerenciador de pacotes do Python, geralmente incluído na instalação do Python.
*   **Ambiente Virtual (Recomendado):** Ferramentas como `venv` (nativa do Python) ou `conda` são fortemente recomendadas para isolar as dependências do projeto e evitar conflitos com outros pacotes do sistema.
*   **Git:** Sistema de controle de versão para clonar o repositório.
*   **Navegador Web Moderno:** Necessário para visualizar o arquivo HTML interativo gerado pela Aula 3 (ex: Chrome, Firefox, Edge).

## 🚀 Guia de Instalação e Configuração Avançada

Siga os passos abaixo para configurar o projeto em sua máquina local.

1.  **Clonar o Repositório:**
    Abra um terminal e execute o seguinte comando para clonar o projeto:
    ```bash
    git clone https://github.com/ESousa97/imersao-python-alura-agosto-2025.git
    ```

2.  **Navegar para o Diretório do Projeto:**
    ```bash
    cd imersao-python-alura-agosto-2025
    ```

3.  **Criar e Ativar um Ambiente Virtual (Recomendado):**
    *   **No Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    *   **No macOS / Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    Após a ativação, seu prompt de comando deverá exibir `(.venv)` no início.

4.  **Instalar as Dependências:**
    O projeto está estruturado em módulos, cada um com seu próprio `requirements.txt`. A abordagem recomendada é instalar as dependências de cada aula conforme você as executa. Para uma instalação completa de todas as dependências do projeto de uma vez, você pode executar os seguintes comandos:
    ```bash
    pip install -r py/aula1/requirements.txt
    pip install -r py/aula2/requirements.txt
    pip install -r py/aula3/requirements.txt
    ```
    *Nota: Pode haver pacotes duplicados entre os arquivos, mas o `pip` gerenciará isso de forma eficiente.*

5.  **Verificar a Instalação:**
    A instalação está completa. Você está pronto para executar os scripts de análise, conforme detalhado na seção [Uso Avançado e Exemplos](#️-uso-avançado-e-exemplos).

## ⚙️ Uso Avançado e Exemplos

Cada script foi projetado para ser executado de forma independente a partir da raiz do repositório.

### Executando a Aula 1: Análise Exploratória
Este script irá carregar os dados brutos, processá-los e salvar o arquivo `salarios_processados.csv` no diretório `py/aula1/`.
```bash
python py/aula1/aula_1_imersão_dados_com_python_alura_agosto_2025.py
```
**Output Esperado:** O terminal exibirá um relatório detalhado da análise exploratória, incluindo as primeiras linhas do dataset, estatísticas, contagens de categorias e, ao final, uma mensagem de sucesso confirmando a gravação do arquivo CSV.

### Executando a Aula 2: Limpeza de Dados
Este script utiliza o artefato da Aula 1 (assumindo que ele exista), realiza a limpeza e salva o arquivo `dados_limpos_aula2.csv` no diretório `py/aula2/`.
```bash
python py/aula2/aula_2_imersão_dados_com_python_alura_agosto_2025.py
```
**Output Esperado:** O terminal mostrará a verificação de valores nulos antes e depois da limpeza, o processo de conversão de tipos e uma mensagem de confirmação da gravação do novo arquivo CSV.

### Executando o Desafio da Luri (Aula 2)
Este é um script autocontido que gera seus próprios dados e saídas.
```bash
python py/aula2/DesafioLuri/desafio2_luri.py
```
**Output Esperado:** O terminal apresentará um relatório completo do desafio, desde a criação do dataset fictício até a análise final, salvando dois novos arquivos CSV no diretório `py/aula2/DesafioLuri/`.

### Executando a Aula 3: Visualização Interativa
Este script utiliza o artefato da Aula 2, realiza as agregações e gera o globo interativo.
```bash
python py/aula3/3_visualização_do_dados_alura_agosto_2025.py
```
**Output Esperado:** Após a execução, uma **nova aba ou janela do seu navegador padrão será aberta automaticamente**, exibindo o globo 3D interativo. O terminal mostrará logs do processo. O arquivo `globo_salarial.html` será salvo na raiz do projeto.

## API Reference (se aplicável)

Não aplicável a este projeto. O projeto consiste em uma suíte de scripts para processamento em lote e não expõe nenhuma API (Application Programming Interface) para consumo externo.

## 🧪 Estratégia de Testes e Qualidade de Código

Dado o caráter educacional e exploratório do projeto, uma suíte de testes automatizados formais (utilizando frameworks como `pytest` ou `unittest`) não foi implementada. A validação e a garantia de qualidade foram realizadas através de outras abordagens:

*   **Validação por Inspeção:** Cada script gera saídas detalhadas no console (`print` statements, `df.info()`, `df.head()`), permitindo a verificação manual da correção das transformações em cada etapa.
*   **Validação de Artefatos:** Os arquivos CSV intermediários gerados por cada aula servem como pontos de verificação. A inspeção manual desses arquivos (por exemplo, abrindo-os em um editor de planilhas ou carregando-os em um notebook separado) confirma que a etapa foi concluída com sucesso.
*   **Testes Visuais:** A saída da Aula 3 é uma visualização. A validação consiste em verificar se o globo é renderizado corretamente, se a interatividade (hover, rotação) funciona como esperado e se os dados exibidos são consistentes com a análise.
*   **Reprodutibilidade:** Os scripts são determinísticos. Executá-los múltiplas vezes com a mesma fonte de dados de entrada produzirá exatamente os mesmos artefatos de saída, garantindo a consistência.

### Proposta de Melhoria Futura (Testes Formais)
Para evoluir o projeto para um nível de produção, uma estratégia de testes formais poderia ser implementada:
*   **Testes Unitários:** Utilizando `pytest`, poderíamos criar testes para funções puras, como as de mapeamento e padronização de categorias.
*   **Testes de Integração:** Testar o pipeline de ponta a ponta, executando os scripts em sequência e validando os artefatos finais contra um resultado esperado (ex: verificar o schema e o número de linhas de um CSV de saída).
*   **Testes de Dados (Great Expectations):** Implementar uma ferramenta como a Great Expectations para definir "contratos de dados" e validar a qualidade dos DataFrames em cada etapa (ex: garantir que uma coluna não tenha nulos, que seus valores estejam dentro de um intervalo esperado, etc.).

## 🚢 Deployment Detalhado e Escalabilidade

Embora o projeto seja uma coleção de scripts locais, seus artefatos e sua lógica podem ser implantados e escalados.

### Deployment dos Artefatos
*   **Visualização Interativa (`globo_salarial.html`):** Sendo um arquivo HTML autocontido, ele pode ser facilmente hospedado em qualquer serviço de hospedagem de sites estáticos:
    *   **GitHub Pages:** Ideal para projetos hospedados no GitHub. Bastaria configurar o repositório para servir arquivos de uma branch específica (ex: `gh-pages`).
    *   **Netlify / Vercel:** Oferecem um processo de deploy simples via drag-and-drop ou integração contínua com o repositório Git.
*   **Dados Processados (`.csv`):** Os arquivos CSV limpos podem ser armazenados em soluções de armazenamento de dados para consumo por outras ferramentas (ex: BI, outras análises):
    *   **Cloud Storage:** Amazon S3, Google Cloud Storage, Azure Blob Storage.
    *   **Data Warehouse:** Google BigQuery, Snowflake, Amazon Redshift.

### Escalabilidade do Pipeline
Para executar este pipeline em produção (por exemplo, para processar dados que chegam diariamente), a seguinte arquitetura poderia ser adotada:
*   **Containerização:** Empacotar os scripts Python e suas dependências em um **container Docker**. Isso garante um ambiente de execução consistente e isolado. Um `Dockerfile` seria criado para este fim.
*   **Orquestração de Workflow:** Utilizar uma ferramenta de orquestração de pipelines de dados como **Apache Airflow** ou **Prefect**.
    *   Cada script (`aula_1.py`, `aula_2.py`, etc.) se tornaria uma `Task` em um `DAG` (Directed Acyclic Graph).
    *   O orquestrador gerenciaria a execução sequencial, o tratamento de falhas, as tentativas e o agendamento (ex: rodar o pipeline toda noite).
*   **Computação Escalável:** Em vez de rodar em uma máquina local, os containers Docker poderiam ser executados em serviços de nuvem escaláveis, como **AWS Fargate**, **Google Cloud Run** ou um cluster **Kubernetes**, permitindo o processamento de volumes de dados muito maiores.

## 📜 Licença e Aspectos Legais

Este projeto é distribuído sob os termos da **Licença MIT**.

Isso significa que você tem total liberdade para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do software, desde que o aviso de direitos autorais e esta permissão sejam incluídos em todas as cópias ou partes substanciais do software.

Para mais detalhes, consulte o arquivo [LICENSE](./LICENSE) no repositório.

## 👥 Equipe Principal e Colaboradores Chave

*   **Autor Principal:** [Enoque Sousa](https://www.linkedin.com/in/enoque-sousa-bb89aa168/)
*   **Conceito e Inspiração:** O projeto foi desenvolvido com base nos materiais e desafios propostos durante a **Imersão Python da Alura (Agosto 2025)**, um agradecimento especial aos instrutores e à comunidade Alura.

## ❓ FAQ (Perguntas Frequentes)

1.  **P: Por que existem arquivos `.ipynb` e `.py` com lógicas semelhantes?**
    **R:** Eles servem a propósitos diferentes. Os notebooks (`.ipynb`) são para exploração, aprendizado e documentação interativa, ideais para apresentar o processo passo a passo. Os scripts Python (`.py`) são para automação e execução em ambientes de produção, representando a versão final e otimizada da análise.

2.  **P: Executei o script da Aula 3, mas nenhuma visualização apareceu. O que pode ter acontecido?**
    **R:** O script da Aula 3 foi projetado para abrir automaticamente uma nova aba no seu navegador padrão para exibir o globo. Verifique se o seu navegador não bloqueou o pop-up. Além disso, um arquivo chamado `globo_salarial.html` deve ter sido criado na raiz do projeto; você pode abri-lo manualmente no navegador.

3.  **P: Posso usar os arquivos `.csv` gerados nos meus próprios projetos?**
    **R:** Sim. Os arquivos `salarios_processados.csv` e `dados_limpos_aula2.csv` são artefatos do pipeline e contêm os dados em estágios de limpeza progressivos. Sinta-se à vontade para usá-los como ponto de partida para suas próprias análises.

4.  **P: Por que a Aula 2 remove os dados nulos (`dropna`) em vez de preenchê-los?**
    **R:** A decisão foi baseada na quantidade de dados nulos, que era extremamente pequena (menos de 0.01% do dataset). Nesses casos, a remoção é uma abordagem simples e segura que não impacta significativamente a análise. O "Desafio da Luri", em contrapartida, foi criado especificamente para demonstrar como preencher (imputar) dados nulos quando eles são mais prevalentes.

## 📞 Contato e Suporte

*   **Relatório de Bugs e Sugestões de Features:** A forma preferencial de contato é através da abertura de uma **[Issue no GitHub](https://github.com/ESousa97/imersao-python-alura-agosto-2025/issues)**. Isso permite que a comunidade acompanhe e participe da discussão.
*   **Contato Profissional:** Para outras questões, você pode entrar em contato com o autor através do [LinkedIn](https://www.linkedin.com/in/enoque-sousa-bb89aa168/).


> ✨ **Criado em:** 5 de ago. de 2025 às 20:00
