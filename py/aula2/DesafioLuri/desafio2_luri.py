# -*- coding: utf-8 -*-
"""
Desafio da Luri - Limpeza de Dados de Alunos
Exercício prático de manipulação e limpeza de dados com pandas
"""

import pandas as pd
import numpy as np
import random
import warnings

# Configurações para melhor visualização dos dados no terminal
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 50)
warnings.filterwarnings('ignore')

def criar_dataset_alunos():
    """Cria um DataFrame com informações fictícias de alunos"""
    
    print("=" * 60)
    print("DESAFIO DA LURI - LIMPEZA DE DADOS DE ALUNOS")
    print("=" * 60)
    
    print("\nEtapa 1: Criando dataset fictício de alunos...")
    
    # Definindo seed para resultados reprodutíveis
    random.seed(42)
    np.random.seed(42)
    
    nomes = [
        "Ana Silva", "Bruno Santos", "Carla Oliveira", "Diego Costa", "Elena Rodrigues",
        "Felipe Lima", "Gabriela Alves", "Henrique Ferreira", "Isabela Martins", "João Pereira",
        "Larissa Souza", "Matheus Ribeiro", "Natália Castro", "Otávio Barbosa", "Patrícia Dias",
        "Rafael Araújo", "Sofia Mendes", "Thiago Gomes", "Vitória Rocha", "Wesley Cardoso",
        "Amanda Torres", "Carlos Eduardo", "Daniela Moura", "Eduardo Nunes", "Fernanda Cruz",
        "Gustavo Reis", "Helena Porto", "Igor Machado", "Júlia Campos", "Leonardo Pinto"
    ]
    
    cidades = [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Brasília", "Curitiba", "Recife", "Porto Alegre", "Goiânia",
        "Belém", "Guarulhos", "Campinas", "São Luís", "Maceió"
    ]
    
    num_alunos = 30
    
    dados_alunos = {
        'nome': random.sample(nomes, num_alunos),
        'idade': np.random.uniform(18.0, 35.0, num_alunos),
        'nota': np.random.uniform(0, 10, num_alunos),
        'cidade': [random.choice(cidades) for _ in range(num_alunos)]
    }
    
    df_alunos = pd.DataFrame(dados_alunos)
    df_alunos['nota'] = df_alunos['nota'].round(1)
    
    # Introduzindo valores nulos propositalmente
    indices_nulos_nota = random.sample(range(num_alunos), 6)
    indices_nulos_idade = random.sample(range(num_alunos), 3)
    
    df_alunos.loc[indices_nulos_nota, 'nota'] = np.nan
    df_alunos.loc[indices_nulos_idade, 'idade'] = np.nan
    
    print(f"Dataset criado com {num_alunos} alunos.")
    print(f"  Notas nulas: {len(indices_nulos_nota)}")
    print(f"  Idades nulas: {len(indices_nulos_idade)}")
    
    return df_alunos

def analisar_dataset_inicial(df):
    """Analisa o dataset inicial antes da limpeza"""
    
    print("\n" + "=" * 50)
    print("ANÁLISE DO DATASET INICIAL")
    print("=" * 50)
    
    print(f"\nInformações gerais:")
    print(f"  Total de alunos: {len(df)}")
    print(f"  Total de colunas: {len(df.columns)}")
    
    print("\nPrimeiras 10 linhas do dataset:")
    print(df.head(10))
    
    print("\nTipos de dados:")
    print(df.info())
    
    print("\nEstatísticas descritivas:")
    print(df.describe())
    
    print("\nVerificação de valores nulos:")
    valores_nulos = df.isnull().sum()
    print(valores_nulos)
    
    if valores_nulos.sum() > 0:
        print("\nProblemas identificados:")
        for coluna, qtd in valores_nulos[valores_nulos > 0].items():
            percentual = (qtd / len(df)) * 100
            print(f"  {coluna}: {qtd} valores nulos ({percentual:.1f}%)")
    
    return valores_nulos

def preencher_valores_nulos(df):
    """Preenche valores nulos conforme regras do desafio"""
    
    print("\n" + "=" * 50)
    print("PREENCHIMENTO DE VALORES NULOS")
    print("=" * 50)
    
    df_tratado = df.copy()
    
    # Preencher notas nulas com a média das notas válidas
    print("\nPreenchendo notas nulas com a média das notas válidas...")
    media_notas = df_tratado['nota'].mean()
    print(f"  Média das notas válidas: {media_notas:.2f}")
    print(f"  Quantidade de notas nulas: {df_tratado['nota'].isnull().sum()}")
    df_tratado['nota'] = df_tratado['nota'].fillna(media_notas.round(1))
    print(f"  Notas nulas preenchidas com: {media_notas:.1f}")
    
    # Preencher idades nulas com a mediana das idades válidas
    print("\nPreenchendo idades nulas com a mediana das idades válidas...")
    mediana_idades = df_tratado['idade'].median()
    print(f"  Mediana das idades válidas: {mediana_idades:.1f}")
    print(f"  Quantidade de idades nulas: {df_tratado['idade'].isnull().sum()}")
    df_tratado['idade'] = df_tratado['idade'].fillna(mediana_idades)
    print(f"  Idades nulas preenchidas com: {mediana_idades:.1f}")
    
    print("\nVerificação após preenchimento:")
    valores_nulos_final = df_tratado.isnull().sum()
    print(valores_nulos_final)
    
    if valores_nulos_final.sum() == 0:
        print("Todos os valores nulos foram preenchidos com sucesso.")
    
    return df_tratado

def converter_tipos_dados(df):
    """Converte tipos de dados conforme necessário"""
    
    print("\n" + "=" * 50)
    print("CONVERSÃO DE TIPOS DE DADOS")
    print("=" * 50)
    
    print("\nTipos de dados antes da conversão:")
    print(df.dtypes)
    
    df_convertido = df.copy()
    
    print("\nConvertendo coluna 'idade' de float para inteiro...")
    print(f"  Amostra antes da conversão: {df_convertido['idade'].head().tolist()}")
    df_convertido['idade'] = df_convertido['idade'].astype(int)
    print(f"  Amostra após a conversão: {df_convertido['idade'].head().tolist()}")
    
    print("\nTipos de dados após conversão:")
    print(df_convertido.dtypes)
    print("Conversão de tipos concluída.")
    
    return df_convertido

def filtrar_alunos_acima_media(df):
    """Filtra alunos com notas acima da média"""
    
    print("\n" + "=" * 50)
    print("FILTRO: ALUNOS ACIMA DA MÉDIA")
    print("=" * 50)
    
    media_geral = df['nota'].mean()
    print(f"\nEstatísticas das notas:")
    print(f"  Média geral: {media_geral:.2f}")
    print(f"  Nota mínima: {df['nota'].min():.1f}")
    print(f"  Nota máxima: {df['nota'].max():.1f}")
    print(f"  Mediana: {df['nota'].median():.1f}")
    
    alunos_acima_media = df[df['nota'] > media_geral].copy()
    alunos_acima_media = alunos_acima_media.sort_values('nota', ascending=False)
    
    print(f"\nResultados do filtro:")
    print(f"  Total de alunos: {len(df)}")
    print(f"  Alunos acima da média: {len(alunos_acima_media)}")
    print(f"  Percentual acima da média: {(len(alunos_acima_media)/len(df)*100):.1f}%")
    
    print(f"\nAlunos com notas acima da média ({media_geral:.2f}):")
    print("=" * 60)
    for idx, (_, aluno) in enumerate(alunos_acima_media.iterrows(), 1):
        print(f"{idx:2d}. {aluno['nome']:<20} | Idade: {aluno['idade']:2d} | Nota: {aluno['nota']:4.1f} | Cidade: {aluno['cidade']}")
    
    return alunos_acima_media, media_geral

def gerar_relatorio_final(df_original, df_final, alunos_destaque, media_geral):
    """Gera relatório final com as transformações realizadas"""
    
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DO DESAFIO")
    print("=" * 60)
    
    print("\nResumo das transformações realizadas:")
    print(f"  1. Dataset criado com {len(df_original)} alunos fictícios")
    print("  2. Valores nulos identificados e tratados:")
    
    nulos_original = df_original.isnull().sum()
    for coluna, qtd in nulos_original[nulos_original > 0].items():
        print(f"     • {coluna}: {qtd} valores nulos preenchidos")
    
    print("  3. Coluna 'idade' convertida de float para int")
    print(f"  4. Filtro aplicado: alunos acima da média ({media_geral:.2f})")
    
    print("\nEstatísticas finais:")
    print(f"  Total de alunos no dataset: {len(df_final)}")
    print(f"  Alunos acima da média: {len(alunos_destaque)}")
    print(f"  Percentual de destaque: {(len(alunos_destaque)/len(df_final)*100):.1f}%")
    print(f"  Nota média geral: {media_geral:.2f}")
    print(f"  Maior nota: {df_final['nota'].max():.1f}")
    print(f"  Menor nota: {df_final['nota'].min():.1f}")
    
    print("\nTop 5 melhores notas:")
    top5 = df_final.nlargest(5, 'nota')
    for idx, (_, aluno) in enumerate(top5.iterrows(), 1):
        print(f"  {idx}º {aluno['nome']}: {aluno['nota']:.1f}")
    
    print("\nDistribuição por cidade (Top 5):")
    dist_cidades = df_final['cidade'].value_counts().head()
    for cidade, qtd in dist_cidades.items():
        print(f"  • {cidade}: {qtd} alunos")
    
    print("\nDistribuição por faixa etária:")
    df_final['faixa_etaria'] = pd.cut(
        df_final['idade'],
        bins=[17, 22, 27, 32, 40],
        labels=['18-22', '23-27', '28-32', '33+']
    )
    dist_idade = df_final['faixa_etaria'].value_counts().sort_index()
    for faixa, qtd in dist_idade.items():
        print(f"  • {faixa} anos: {qtd} alunos")

def salvar_resultados(df_final, alunos_destaque):
    """Salva os datasets processados em arquivos CSV"""
    
    print("\nSalvando resultados...")
    
    try:
        df_final.to_csv('alunos_dataset_completo.csv', index=False, encoding='utf-8')
        print("  Dataset completo salvo: 'alunos_dataset_completo.csv'")
        
        alunos_destaque.to_csv('alunos_acima_media.csv', index=False, encoding='utf-8')
        print("  Alunos destaque salvos: 'alunos_acima_media.csv'")
    except Exception as e:
        print(f"  Erro ao salvar arquivos: {e}")

def main():
    """Função principal do Desafio da Luri"""
    
    df_alunos = criar_dataset_alunos()
    valores_nulos_inicial = analisar_dataset_inicial(df_alunos)
    df_sem_nulos = preencher_valores_nulos(df_alunos)
    df_convertido = converter_tipos_dados(df_sem_nulos)
    alunos_destaque, media_geral = filtrar_alunos_acima_media(df_convertido)
    gerar_relatorio_final(df_alunos, df_convertido, alunos_destaque, media_geral)
    salvar_resultados(df_convertido, alunos_destaque)
    
    print("\n" + "=" * 60)
    print("DESAFIO CONCLUÍDO COM SUCESSO!")
    print("=" * 60)
    print("""
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
""")
    
    return df_convertido, alunos_destaque

if __name__ == "__main__":
    dataset_final, melhores_alunos = main()
