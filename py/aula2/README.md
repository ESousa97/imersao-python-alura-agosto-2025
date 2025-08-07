# Aula 2 - Preparação e Limpeza de Dados

Este projeto realiza preparação e limpeza de dados, focando no tratamento de valores nulos e conversão de tipos de dados, baseado na Aula 2 da Imersão Python da Alura (Agosto 2025).

## Como executar

### Pré-requisitos
```bash
pip install pandas numpy
```

### Execução
```bash
python py/aula2/aula_2_imersão_dados_com_python_alura_agosto_2025.py
```

## Saída do programa

```
PS C:\Users\sousa\Projects\imersao-python-alura-agosto-2025> python py/aula2/aula_2_imersão_dados_com_python_alura_agosto_2025.py
======================================================================
AULA 2 - PREPARAÇÃO E LIMPEZA DOS DADOS
======================================================================
=== CARREGANDO E PREPARANDO DADOS INICIAIS ===

Carregando dados...
Dados carregados com sucesso!

Renomeando colunas para português...
Padronizando categorias...
Dados preparados com sucesso!

=== VERIFICAÇÃO DE VALORES NULOS ===
==================================================

Verificando valores nulos por coluna:
ano                10
senioridade         0
contrato            0
cargo               0
salario             0
moeda               0
usd                 0
residencia          0
remoto              0
empresa             0
tamanho_empresa     0
dtype: int64

Encontradas 1 coluna(s) com valores nulos:
  • ano: 10 nulos (0.01%)

Valores únicos na coluna 'ano':
  [2025.   nan 2024. 2022. 2023. 2020. 2021.]

Visualizando linhas com valores nulos:
Total de linhas com valores nulos: 10

Primeiras linhas com valores nulos:
       ano senioridade  contrato              cargo  salario moeda     usd residencia      remoto empresa tamanho_empresa
5588   NaN      senior  integral    Product Manager   184500   USD  184500         US  presencial      US           media
59692  NaN       pleno  integral           Engineer   110000   USD  110000         DE  presencial      DE           media
59710  NaN      junior  integral     Data Scientist   208800   USD  208800         US  presencial      US           media
59759  NaN      senior  integral  Software Engineer   135000   USD  135000         US  presencial      US           media
59789  NaN      senior  integral           Engineer   112000   USD  112000         US  presencial      US           media

=== DEMONSTRAÇÃO DE MÉTODOS DE PREENCHIMENTO ===
============================================================

Exemplo 1: Preenchimento de salários com média e mediana

DataFrame original:
      nome   salario
0   Eloise    4000.0
1   Enoque       NaN
2   Carlos    5000.0
3   Victor       NaN
4  Edvaldo  100000.0

Após preenchimento:
      nome   salario  salario_media  salario_mediana
0   Eloise    4000.0        4000.00           4000.0
1   Enoque       NaN       36333.33           5000.0
2   Carlos    5000.0        5000.00           5000.0
3   Victor       NaN       36333.33           5000.0
4  Edvaldo  100000.0      100000.00         100000.0

Estatísticas:
  Média: 36333.33
  Mediana: 5000.00

Exemplo 2: Preenchimento com Forward Fill (ffill)

DataFrame original:
       Dia  Temperatura
0  Segunda         30.0
1    Terça          NaN
2   Quarta          NaN
3   Quinta         28.0
4    Sexta         27.0
5   Sábado         32.0
6  Domingo         36.0

Após Forward Fill:
       Dia  Temperatura  Preenchido_ffill
0  Segunda         30.0              30.0
1    Terça          NaN              30.0
2   Quarta          NaN              30.0
3   Quinta         28.0              28.0
4    Sexta         27.0              27.0
5   Sábado         32.0              32.0
6  Domingo         36.0              36.0

Exemplo 3: Preenchimento com Backward Fill (bfill)

Após Backward Fill:
       Dia  Temperatura  Preenchido_bfill
0  Segunda         30.0              30.0
1    Terça          NaN              28.0
2   Quarta          NaN              28.0
3   Quinta         28.0              28.0
4    Sexta         27.0              27.0
5   Sábado         32.0              32.0
6  Domingo         36.0              36.0

Exemplo 4: Preenchimento com valor específico

DataFrame original:
      nome               Cidade
0   Eloise            São Paulo
1   Enoque                  NaN
2   Carlos                Belém
3   Victor                  NaN
4  Edvaldo  Rio Grande do Norte

Após preenchimento:
      nome               Cidade    Cidade_preenchida
0   Eloise            São Paulo            São Paulo
1   Enoque                  NaN        Não informado
2   Carlos                Belém                Belém
3   Victor                  NaN        Não informado
4  Edvaldo  Rio Grande do Norte  Rio Grande do Norte

=== LIMPEZA DOS DADOS ===
==============================

Dados antes da limpeza:
  Total de linhas: 133,349
  Total de colunas: 11

Removendo linhas com valores nulos...

Dados após limpeza:
  Total de linhas: 133,339
  Total de colunas: 11
  Linhas removidas: 10

Verificando valores nulos após limpeza:
ano                0
senioridade        0
contrato           0
cargo              0
salario            0
moeda              0
usd                0
residencia         0
remoto             0
empresa            0
tamanho_empresa    0
dtype: int64
Todos os valores nulos foram removidos com sucesso.

=== CONVERSÃO DE TIPOS DE DADOS ===
========================================

Tipos de dados antes da conversão:
ano                float64
senioridade         object
contrato            object
cargo               object
salario              int64
moeda               object
usd                  int64
residencia          object
remoto              object
empresa             object
tamanho_empresa     object
dtype: object

Convertendo coluna 'ano' de float para int...

Tipos de dados após conversão:
ano                 int64
senioridade        object
contrato           object
cargo              object
salario             int64
moeda              object
usd                 int64
residencia         object
remoto             object
empresa            object
tamanho_empresa    object
dtype: object

Visualizando os dados após conversão:
    ano senioridade  contrato               cargo  salario moeda     usd residencia      remoto empresa tamanho_empresa
0  2025      senior  integral  Solutions Engineer   214000   USD  214000         US      remoto      US           media
1  2025      senior  integral  Solutions Engineer   136000   USD  136000         US      remoto      US           media
2  2025       pleno  integral       Data Engineer   158800   USD  158800         AU  presencial      AU           media
3  2025       pleno  integral       Data Engineer   139200   USD  139200         AU  presencial      AU           media
4  2025      junior  integral       Data Engineer    90000   USD   90000         US  presencial      US           media

=== SALVANDO DADOS LIMPOS ===
===================================
Dados limpos salvos em 'dados_limpos_aula2.csv'.

Resumo dos dados salvos:
  Linhas: 133,339
  Colunas: 11
  Memória usada: 68.38 MB

======================================================================
RESUMO DA AULA 2 - PREPARAÇÃO E LIMPEZA DOS DADOS
======================================================================

Nesta aula você aprendeu:

1. Verificação de Valores Nulos:
   • Como identificar e quantificar dados ausentes
   • Visualizar padrões e linhas com valores nulos

2. Métodos de Tratamento de Dados Ausentes:
   • Preenchimento com média, mediana e valores específicos
   • Forward Fill e Backward Fill para preenchimento sequencial
   • Remoção de linhas com dados ausentes

3. Limpeza e Preparação dos Dados:
   • Exclusão de dados incompletos
   • Conversão de tipos de dados para análise correta

4. Persistência dos Dados:
   • Salvamento do dataset limpo para uso posterior

Os dados estão agora prontos para análises mais avançadas!
```

## Resumo dos Conceitos Abordados

### Preparação dos Dados
- **Carregamento**: Importação do dataset de salários
- **Renomeação**: Tradução das colunas para português
- **Padronização**: Normalização das categorias

### Identificação de Problemas
- **Valores nulos**: 10 registros com ano nulo (0.01%)
- **Tipos incorretos**: Coluna 'ano' como float64

### Métodos de Preenchimento Demonstrados
1. **Média/Mediana**: Para dados numéricos
2. **Forward Fill (ffill)**: Propaga último valor válido
3. **Backward Fill (bfill)**: Usa próximo valor válido
4. **Valor específico**: Para categorias ('Não informado')

### Limpeza Aplicada
- **Remoção**: 10 linhas com valores nulos eliminadas
- **Conversão**: Tipo 'ano' convertido para int64
- **Validação**: Verificação da integridade dos dados

### Resultados Finais
- **Dataset limpo**: 133,339 registros válidos
- **Arquivo gerado**: dados_limpos_aula2.csv
- **Memória utilizada**: 68.38 MB


> ✨ **Criado em:** 6 de ago. de 2025