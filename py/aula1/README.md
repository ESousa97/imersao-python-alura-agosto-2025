# Análise de Dados - Salários em Data Science - Aula 1

Este projeto realiza uma análise exploratória de dados sobre salários na área de ciência de dados, baseado na Aula 1 da Imersão Python da Alura (Agosto 2025).

## Como executar

### Pré-requisitos
```bash
pip install -r requirements.txt
```

### Execução
```bash
python py/aula_1_imersão_dados_com_python_alura_agosto_2025.py
```

## Saída do programa

```
PS C:\Users\sousa\Projects\imersao-python-alura-agosto-2025> python py/aula_1_imersão_dados_com_python_alura_agosto_2025.py
=== ANÁLISE DE DADOS: SALÁRIOS EM DATA SCIENCE ===

Carregando dados...
Dados carregados com sucesso!

INFORMAÇÕES BÁSICAS DO DATASET
==================================================

Primeiras 5 linhas do dataset:
   work_year experience_level employment_type           job_title  salary salary_currency  salary_in_usd employee_residence  remote_ratio company_location company_size
0     2025.0               SE              FT  Solutions Engineer  214000             USD         214000                 US           100               US            M
1     2025.0               SE              FT  Solutions Engineer  136000             USD         136000                 US           100               US            M
2     2025.0               MI              FT       Data Engineer  158800             USD         158800                 AU             0               AU            M
3     2025.0               MI              FT       Data Engineer  139200             USD         139200                 AU             0               AU            M
4     2025.0               EN              FT       Data Engineer   90000             USD          90000                 US             0               US            M

Dimensão do dataset:
  Linhas: 133,349
  Colunas: 11

Informações gerais do dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 133349 entries, 0 to 133348
Data columns (total 11 columns):
 #   Column              Non-Null Count   Dtype
---  ------              --------------   -----
 0   work_year           133339 non-null  float64
 1   experience_level    133349 non-null  object
 2   employment_type     133349 non-null  object
 3   job_title           133349 non-null  object
 4   salary              133349 non-null  int64
 5   salary_currency     133349 non-null  object
 6   salary_in_usd       133349 non-null  int64
 7   employee_residence  133349 non-null  object
 8   remote_ratio        133349 non-null  int64
 9   company_location    133349 non-null  object
 10  company_size        133349 non-null  object
dtypes: float64(1), int64(3), object(7)
memory usage: 11.2+ MB
None

Estatísticas descritivas das colunas numéricas:
           work_year        salary  salary_in_usd   remote_ratio
count  133339.000000  1.333490e+05  133349.000000  133349.000000
mean     2024.358770  1.632833e+05  157617.272098      20.905669
std         0.680627  2.173860e+05   74288.363097      40.590044
min      2020.000000  1.400000e+04   15000.000000       0.000000
25%      2024.000000  1.060200e+05  106000.000000       0.000000
50%      2024.000000  1.470000e+05  146206.000000       0.000000
75%      2025.000000  1.990000e+05  198000.000000       0.000000
max      2025.000000  3.040000e+07  800000.000000     100.000000

Nomes originais das colunas:
['work_year', 'experience_level', 'employment_type', 'job_title', 'salary', 'salary_currency', 'salary_in_usd', 'employee_residence', 'remote_ratio', 'company_location', 'company_size']

Renomeando colunas para português...
==================================================
Colunas renomeadas com sucesso!
Novas colunas: ['ano', 'senioridade', 'contrato', 'cargo', 'salario', 'moeda', 'usd', 'residencia', 'remoto', 'empresa', 'tamanho_empresa']

Análise das categorias:
==================================================

Nível de senioridade:
senioridade
SE    77241
MI    40465
EN    12443
EX     3200
Name: count, dtype: int64

Legenda:
  SE = Senior (Sênior)
  MI = Mid (Pleno)
  EN = Entry (Júnior)
  EX = Executive (Executivo)


Tipo de contrato:
contrato
FT    132563
CT       394
PT       376
FL        16
Name: count, dtype: int64

Legenda:
  FT = Full-time (Integral)
  PT = Part-time (Parcial)
  CT = Contract (Contrato)
  FL = Freelance (Freelancer)


Regime de trabalho (percentual remoto):
remoto
0      105312
100     27718
50        319
Name: count, dtype: int64

Legenda:
  0 = Presencial
  50 = Híbrido
  100 = Remoto


Tamanho da empresa:
tamanho_empresa
M    129561
L      3574
S       214
Name: count, dtype: int64

Legenda:
  L = Large (Grande)
  M = Medium (Média)
  S = Small (Pequena)


Padronizando nomes das categorias...
==================================================
Categorias padronizadas com sucesso!

Dataset após as transformações:
==================================================

Primeiras 5 linhas:
      ano senioridade  contrato               cargo  salario moeda     usd residencia      remoto empresa tamanho_empresa
0  2025.0      senior  integral  Solutions Engineer   214000   USD  214000         US      remoto      US           media
1  2025.0      senior  integral  Solutions Engineer   136000   USD  136000         US      remoto      US           media
2  2025.0       pleno  integral       Data Engineer   158800   USD  158800         AU  presencial      AU           media
3  2025.0       pleno  integral       Data Engineer   139200   USD  139200         AU  presencial      AU           media
4  2025.0      junior  integral       Data Engineer    90000   USD   90000         US  presencial      US           media

Estatísticas das variáveis categóricas:
       senioridade  contrato           cargo   moeda residencia      remoto empresa tamanho_empresa
count       133349    133349          133349  133349     133349      133349  133349          133349
unique           4         4             390      26        102           3      95               3
top         senior  integral  Data Scientist     USD         US  presencial      US           media
freq         77241    132563           17314  126140     119579      105312  119641          129561

Respostas para perguntas de negócio:
==================================================
1. Nível de senioridade mais comum: Senior
   Frequência: 77,241 (57.9%)

2. Tipo de contrato mais frequente: Integral
   Frequência: 132,563 (99.4%)

3. Cargo mais frequente: Data Scientist
   Frequência: 17,314 (13.0%)

4. País com mais profissionais: US
   Frequência: 119,579 (89.7%)

5. País com mais empresas: US
   Frequência: 119,641 (89.7%)

6. Regime de trabalho mais comum: Presencial
   Frequência: 105,312 (79.0%)

7. Tamanho de empresa mais comum: Media
   Frequência: 129,561 (97.2%)

Informações salariais (em USD):
==================================================
Salário médio: $157,617.27
Salário mediano: $146,206.00
Salário mínimo: $15,000.00
Salário máximo: $800,000.00

Arquivo 'salarios_processados.csv' salvo com sucesso.

Análise concluída com sucesso!
==================================================
```

## Resumo dos Resultados

### Dataset
- **Registros**: 133,349 profissionais
- **Período**: 2020-2025
- **Colunas**: 11 variáveis

### Principais Insights
- **Perfil dominante**: Profissional Senior (57.9%) com contrato integral (99.4%)
- **Cargo mais comum**: Data Scientist (13.0%)
- **Localização**: Estados Unidos concentra 89.7% dos profissionais e empresas
- **Trabalho**: Presencial ainda é predominante (79.0%)
- **Empresas**: Médio porte representa 97.2% das empresas

### Salários (USD)
- **Média**: $157,617
- **Mediana**: $146,206
- **Amplitude**: $15,000 - $800,000

## Arquivos gerados
- `salarios_processados.csv`: Dataset limpo e processado
