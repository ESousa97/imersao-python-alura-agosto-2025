# -*- coding: utf-8 -*-
"""
Análise de Dados com Pandas - Adaptado para execução local
Baseado na Aula 1 - Imersão dados com Python Alura
"""

import pandas as pd
import numpy as np
import warnings

# Configurações para melhor visualização dos dados no terminal
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
pd.set_option('display.width', None)        # Ajustar largura automaticamente
pd.set_option('display.max_colwidth', 50)  # Limitar largura máxima das colunas
warnings.filterwarnings('ignore')            # Ignorar avisos para evitar poluição no output

def main():
    """Função principal para executar a análise dos dados de salários em Data Science"""
    
    print("=== ANÁLISE DE DADOS: SALÁRIOS EM DATA SCIENCE ===\n")
    
    # Carregando os dados diretamente da URL
    print("Carregando dados...")
    try:
        df = pd.read_csv(
            "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
        )
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return
    
    # Exibir informações básicas sobre o dataset
    print("\nINFORMAÇÕES BÁSICAS DO DATASET")
    print("=" * 50)
    
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
    
    linhas, colunas = df.shape
    print(f"\nDimensão do dataset:")
    print(f"  Linhas: {linhas:,}")
    print(f"  Colunas: {colunas}")
    
    print("\nInformações gerais do dataset:")
    print(df.info())
    
    print("\nEstatísticas descritivas das colunas numéricas:")
    print(df.describe())
    
    print("\nNomes originais das colunas:")
    print(list(df.columns))
    
    # Renomear colunas para português para facilitar entendimento
    print("\nRenomeando colunas para português...")
    print("=" * 50)
    
    novos_nomes = {
        'work_year': 'ano',
        'experience_level': 'senioridade',
        'employment_type': 'contrato',
        'job_title': 'cargo',
        'salary': 'salario',
        'salary_currency': 'moeda',
        'salary_in_usd': 'usd',
        'employee_residence': 'residencia',
        'remote_ratio': 'remoto',
        'company_location': 'empresa',
        'company_size': 'tamanho_empresa'
    }
    
    df.rename(columns=novos_nomes, inplace=True)
    print("Colunas renomeadas com sucesso!")
    print(f"Novas colunas: {list(df.columns)}")
    
    # Analisar os valores únicos em categorias importantes
    print("\nAnálise das categorias:")
    print("=" * 50)
    
    print("\nNível de senioridade:")
    print(df['senioridade'].value_counts())
    print("""
Legenda:
  SE = Senior (Sênior)
  MI = Mid (Pleno)
  EN = Entry (Júnior)
  EX = Executive (Executivo)
""")
    
    print("\nTipo de contrato:")
    print(df['contrato'].value_counts())
    print("""
Legenda:
  FT = Full-time (Integral)
  PT = Part-time (Parcial)
  CT = Contract (Contrato)
  FL = Freelance (Freelancer)
""")
    
    print("\nRegime de trabalho (percentual remoto):")
    print(df['remoto'].value_counts())
    print("""
Legenda:
  0 = Presencial
  50 = Híbrido
  100 = Remoto
""")
    
    print("\nTamanho da empresa:")
    print(df['tamanho_empresa'].value_counts())
    print("""
Legenda:
  L = Large (Grande)
  M = Medium (Média)
  S = Small (Pequena)
""")
    
    # Padronizar nomes das categorias para termos em português simples
    print("\nPadronizando nomes das categorias...")
    print("=" * 50)
    
    senioridade_map = {
        'SE': 'senior',
        'MI': 'pleno',
        'EN': 'junior',
        'EX': 'executivo'
    }
    df['senioridade'] = df['senioridade'].replace(senioridade_map)
    
    contrato_map = {
        'FT': 'integral',
        'PT': 'parcial',
        'CT': 'contrato',
        'FL': 'freelancer'
    }
    df['contrato'] = df['contrato'].replace(contrato_map)
    
    tamanho_empresa_map = {
        'L': 'grande',
        'M': 'media',
        'S': 'pequena'
    }
    df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa_map)
    
    remoto_map = {
        0: 'presencial',
        50: 'hibrido',
        100: 'remoto'
    }
    df['remoto'] = df['remoto'].replace(remoto_map)
    
    print("Categorias padronizadas com sucesso!")
    
    # Mostrar dataset após as transformações
    print("\nDataset após as transformações:")
    print("=" * 50)
    
    print("\nPrimeiras 5 linhas:")
    print(df.head())
    
    print("\nEstatísticas das variáveis categóricas:")
    print(df.describe(include='object'))
    
    # Responder algumas perguntas de negócio com base nos dados
    print("\nRespostas para perguntas de negócio:")
    print("=" * 50)
    
    # Nível de senioridade mais comum
    senioridade_mais_comum = df['senioridade'].mode()[0]
    freq_senioridade = df['senioridade'].value_counts().iloc[0]
    perc_senioridade = df['senioridade'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"1. Nível de senioridade mais comum: {senioridade_mais_comum.capitalize()}")
    print(f"   Frequência: {freq_senioridade:,} ({perc_senioridade:.1f}%)")
    
    # Tipo de contrato mais frequente
    contrato_mais_comum = df['contrato'].mode()[0]
    freq_contrato = df['contrato'].value_counts().iloc[0]
    perc_contrato = df['contrato'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n2. Tipo de contrato mais frequente: {contrato_mais_comum.capitalize()}")
    print(f"   Frequência: {freq_contrato:,} ({perc_contrato:.1f}%)")
    
    # Cargo mais frequente
    cargo_mais_comum = df['cargo'].mode()[0]
    freq_cargo = df['cargo'].value_counts().iloc[0]
    perc_cargo = df['cargo'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n3. Cargo mais frequente: {cargo_mais_comum}")
    print(f"   Frequência: {freq_cargo:,} ({perc_cargo:.1f}%)")
    
    # País com mais profissionais
    pais_mais_profissionais = df['residencia'].mode()[0]
    freq_pais_profs = df['residencia'].value_counts().iloc[0]
    perc_pais_profs = df['residencia'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n4. País com mais profissionais: {pais_mais_profissionais}")
    print(f"   Frequência: {freq_pais_profs:,} ({perc_pais_profs:.1f}%)")
    
    # País com mais empresas
    pais_mais_empresas = df['empresa'].mode()[0]
    freq_pais_emp = df['empresa'].value_counts().iloc[0]
    perc_pais_emp = df['empresa'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n5. País com mais empresas: {pais_mais_empresas}")
    print(f"   Frequência: {freq_pais_emp:,} ({perc_pais_emp:.1f}%)")
    
    # Regime de trabalho mais comum
    regime_mais_comum = df['remoto'].mode()[0]
    freq_regime = df['remoto'].value_counts().iloc[0]
    perc_regime = df['remoto'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n6. Regime de trabalho mais comum: {regime_mais_comum.capitalize()}")
    print(f"   Frequência: {freq_regime:,} ({perc_regime:.1f}%)")
    
    # Tamanho de empresa mais comum
    tamanho_mais_comum = df['tamanho_empresa'].mode()[0]
    freq_tamanho = df['tamanho_empresa'].value_counts().iloc[0]
    perc_tamanho = df['tamanho_empresa'].value_counts(normalize=True).iloc[0] * 100
    
    print(f"\n7. Tamanho de empresa mais comum: {tamanho_mais_comum.capitalize()}")
    print(f"   Frequência: {freq_tamanho:,} ({perc_tamanho:.1f}%)")
    
    # Informações sobre salários
    print("\nInformações salariais (em USD):")
    print("=" * 50)
    
    print(f"Salário médio: ${df['usd'].mean():,.2f}")
    print(f"Salário mediano: ${df['usd'].median():,.2f}")
    print(f"Salário mínimo: ${df['usd'].min():,.2f}")
    print(f"Salário máximo: ${df['usd'].max():,.2f}")
    
    # Salvando o dataset processado em arquivo CSV (opcional)
    try:
        df.to_csv('salarios_processados.csv', index=False, encoding='utf-8')
        print("\nArquivo 'salarios_processados.csv' salvo com sucesso.")
    except Exception as e:
        print(f"\nAviso: Não foi possível salvar o arquivo. Motivo: {e}")
    
    print("\nAnálise concluída com sucesso!")
    print("=" * 50)
    
    return df

# Executa a análise somente se o script for rodado diretamente
if __name__ == "__main__":
    df_final = main()
