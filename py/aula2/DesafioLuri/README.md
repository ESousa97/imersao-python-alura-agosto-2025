# Desafio da Luri - Limpeza de Dados de Alunos

Este projeto é um exercício prático de manipulação e limpeza de dados com pandas, criando um dataset fictício de alunos e aplicando técnicas de tratamento de dados.

## Como executar

### Pré-requisitos
```bash
pip install pandas numpy
```

### Execução
```bash
python py/aula2/DesafioLuri/desafio2_luri.py
```

## Saída do programa

```
PS C:\Users\sousa\Projects\imersao-python-alura-agosto-2025> python py/aula2/DesafioLuri/desafio2_luri.py
============================================================
DESAFIO DA LURI - LIMPEZA DE DADOS DE ALUNOS
============================================================

Etapa 1: Criando dataset fictício de alunos...
Dataset criado com 30 alunos.
  Notas nulas: 6
  Idades nulas: 3

==================================================
ANÁLISE DO DATASET INICIAL
==================================================

Informações gerais:
  Total de alunos: 30
  Total de colunas: 4

Primeiras 10 linhas do dataset:
                nome      idade  nota          cidade
0      Amanda Torres  24.367182   6.1        Campinas
1        Diego Costa  34.162143   1.7        São Luís
2          Ana Silva  30.443897   NaN       São Paulo
3      Eduardo Nunes  28.177194   9.5        Campinas
4    Isabela Martins  20.652317   9.7        Campinas
5  Henrique Ferreira  20.651907   8.1  Belo Horizonte
6      Fernanda Cruz  18.987421   3.0       Guarulhos
7    Elena Rodrigues  32.724994   1.0        Curitiba
8       Júlia Campos  28.218955   6.8        Brasília
9       Thiago Gomes  30.037234   NaN       Fortaleza

Tipos de dados:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   nome    30 non-null     object 
 1   idade   27 non-null     float64
 2   nota    24 non-null     float64
 3   cidade  30 non-null     object 
dtypes: float64(2), object(2)
memory usage: 1.1+ KB
None

Estatísticas descritivas:
           idade       nota
count  27.000000  24.000000
mean   24.977152   5.291667
std     4.691029   3.221385
min    18.349936   0.500000
25%    21.104451   2.450000
50%    24.228151   5.750000
75%    28.310227   8.300000
max    34.162143   9.700000

Verificação de valores nulos:
nome      0
idade     3
nota      6
cidade    0
dtype: int64

Problemas identificados:
  idade: 3 valores nulos (10.0%)
  nota: 6 valores nulos (20.0%)

==================================================
PREENCHIMENTO DE VALORES NULOS
==================================================

Preenchendo notas nulas com a média das notas válidas...
  Média das notas válidas: 5.29
  Quantidade de notas nulas: 6
  Notas nulas preenchidas com: 5.3

Preenchendo idades nulas com a mediana das idades válidas...
  Mediana das idades válidas: 24.2
  Quantidade de idades nulas: 3
  Idades nulas preenchidas com: 24.2

Verificação após preenchimento:
nome      0
idade     0
nota      0
cidade    0
dtype: int64
Todos os valores nulos foram preenchidos com sucesso.

==================================================
CONVERSÃO DE TIPOS DE DADOS
==================================================

Tipos de dados antes da conversão:
nome       object
idade     float64
nota      float64
cidade     object
dtype: object

Convertendo coluna 'idade' de float para inteiro...
  Amostra antes da conversão: [24.367182020405163, 34.16214320896857, 30.443897010793886, 28.177194231349624, 20.652316887521422]
  Amostra após a conversão: [24, 34, 30, 28, 20]

Tipos de dados após conversão:
nome       object
idade       int32
nota      float64
cidade     object
dtype: object
Conversão de tipos concluída.

==================================================
FILTRO: ALUNOS ACIMA DA MÉDIA
==================================================

Estatísticas das notas:
  Média geral: 5.29
  Nota mínima: 0.5
  Nota máxima: 9.7
  Mediana: 5.3

Resultados do filtro:
  Total de alunos: 30
  Alunos acima da média: 19
  Percentual acima da média: 63.3%

Alunos com notas acima da média (5.29):
============================================================
 1. Isabela Martins      | Idade: 20 | Nota:  9.7 | Cidade: Campinas
 2. Eduardo Nunes        | Idade: 28 | Nota:  9.5 | Cidade: Campinas
 3. Natália Castro       | Idade: 22 | Nota:  9.4 | Cidade: Fortaleza
 4. Daniela Moura        | Idade: 31 | Nota:  9.2 | Cidade: Guarulhos
 5. Bruno Santos         | Idade: 21 | Nota:  9.1 | Cidade: Brasília
 6. Felipe Lima          | Idade: 24 | Nota:  8.9 | Cidade: Campinas
 7. Henrique Ferreira    | Idade: 20 | Nota:  8.1 | Cidade: Belo Horizonte
 8. Matheus Ribeiro      | Idade: 20 | Nota:  7.8 | Cidade: Goiânia
 9. Júlia Campos         | Idade: 28 | Nota:  6.8 | Cidade: Brasília
10. Sofia Mendes         | Idade: 21 | Nota:  6.6 | Cidade: Rio de Janeiro
11. Amanda Torres        | Idade: 24 | Nota:  6.1 | Cidade: Campinas
12. Gabriela Alves       | Idade: 25 | Nota:  6.0 | Cidade: São Paulo
13. Gustavo Reis         | Idade: 25 | Nota:  5.5 | Cidade: Brasília
14. Leonardo Pinto       | Idade: 26 | Nota:  5.3 | Cidade: Rio de Janeiro
15. João Pereira         | Idade: 22 | Nota:  5.3 | Cidade: São Luís
16. Rafael Araújo        | Idade: 28 | Nota:  5.3 | Cidade: Brasília
17. Ana Silva            | Idade: 30 | Nota:  5.3 | Cidade: São Paulo
18. Otávio Barbosa       | Idade: 32 | Nota:  5.3 | Cidade: Campinas
19. Thiago Gomes         | Idade: 30 | Nota:  5.3 | Cidade: Fortaleza

============================================================
RELATÓRIO FINAL DO DESAFIO
============================================================

Resumo das transformações realizadas:
  1. Dataset criado com 30 alunos fictícios
  2. Valores nulos identificados e tratados:
     • idade: 3 valores nulos preenchidos
     • nota: 6 valores nulos preenchidos
  3. Coluna 'idade' convertida de float para int
  4. Filtro aplicado: alunos acima da média (5.29)

Estatísticas finais:
  Total de alunos no dataset: 30
  Alunos acima da média: 19
  Percentual de destaque: 63.3%
  Nota média geral: 5.29
  Maior nota: 9.7
  Menor nota: 0.5

Top 5 melhores notas:
  1º Isabela Martins: 9.7
  2º Eduardo Nunes: 9.5
  3º Natália Castro: 9.4
  4º Daniela Moura: 9.2
  5º Bruno Santos: 9.1

Distribuição por cidade (Top 5):
  • Campinas: 5 alunos
  • Brasília: 4 alunos
  • Rio de Janeiro: 4 alunos
  • São Luís: 2 alunos
  • São Paulo: 2 alunos

Distribuição por faixa etária:
  • 18-22 anos: 12 alunos
  • 23-27 anos: 9 alunos
  • 28-32 anos: 8 alunos
  • 33+ anos: 1 alunos

Salvando resultados...
  Dataset completo salvo: 'alunos_dataset_completo.csv'
  Alunos destaque salvos: 'alunos_acima_media.csv'

============================================================
DESAFIO CONCLUÍDO COM SUCESSO!
============================================================

Parabéns! Você completou o Desafio da Luri!

Habilidades praticadas:
 - Criação de DataFrames com dados fictícios
 - Identificação e análise de valores nulos
 - Preenchimento de valores ausentes (média/mediana)
 - Conversão de tipos de dados (float → int)
 - Filtragem de dados com condições
 - Análise estatística básica
 - Geração de relatórios estruturados
 - Salvamento de resultados em CSV

Próximos passos sugeridos:
 - Experimente diferentes métodos de preenchimento
 - Crie filtros mais complexos
 - Adicione visualizações gráficas
 - Implemente validações de dados
```

## Resumo do Desafio

### Dataset Criado
- **30 alunos fictícios** com nomes realistas
- **Colunas**: nome, idade, nota, cidade
- **Valores nulos propositais**: 6 notas (20%) e 3 idades (10%)

### Análise Inicial
- **Estatísticas descritivas** completas
- **Identificação de problemas** de qualidade
- **Visualização** dos primeiros registros

### Tratamento de Dados
1. **Notas nulas**: Preenchidas com média (5.3)
2. **Idades nulas**: Preenchidas com mediana (24.2 anos)
3. **Conversão de tipos**: Idade de float64 para int32

### Filtro e Análise
- **Filtro aplicado**: Alunos com notas > média (5.29)
- **Resultado**: 19 alunos (63.3%) acima da média
- **Ranking**: Ordenação por nota decrescente

### Relatórios Gerados
- **Top 5 melhores notas**: Isabela Martins (9.7) liderando
- **Distribuição geográfica**: Campinas com mais alunos (5)
- **Faixas etárias**: Maioria entre 18-22 anos (12 alunos)

### Arquivos Gerados
- `alunos_dataset_completo.csv`: Dataset completo limpo
- `alunos_acima_media.csv`: Apenas alunos destaque

### Habilidades Praticadas
- Criação de dados fictícios
- Tratamento de valores nulos
- Conversão de tipos de dados
- Filtragem condicional
- Análise estatística
- Geração de relatórios
- Persistência de dados


> ✨ **Criado em:** 6 de ago. de 2025