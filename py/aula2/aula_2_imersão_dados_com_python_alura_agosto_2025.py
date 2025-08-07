# -*- coding: utf-8 -*-
"""
Aula 2 - Preparação e Limpeza de Dados - Adaptado para execução local
Baseado na Imersão Python Alura - Agosto 2025
"""

import pandas as pd
import numpy as np
import warnings

# Configurações para melhor visualização dos dados no terminal
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
pd.set_option('display.width', None)        # Ajusta a largura da tela automaticamente
pd.set_option('display.max_colwidth', 50)  # Limitar largura máxima das colunas
warnings.filterwarnings('ignore')            # Ignorar avisos para manter a saída limpa

def carregar_e_preparar_dados():
    """Carrega os dados e realiza preparação inicial (similar à Aula 1)"""
    
    print("=== CARREGANDO E PREPARANDO DADOS INICIAIS ===\n")
    
    print("Carregando dados...")
    try:
        df = pd.read_csv(
            "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
        )
        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None
    
    print("\nRenomeando colunas para português...")
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
    
    print("Padronizando categorias...")
    
    senioridade = {'SE': 'senior', 'MI': 'pleno', 'EN': 'junior', 'EX': 'executivo'}
    df['senioridade'] = df['senioridade'].replace(senioridade)
    
    contrato = {'FT': 'integral', 'PT': 'parcial', 'CT': 'contrato', 'FL': 'freelancer'}
    df['contrato'] = df['contrato'].replace(contrato)
    
    tamanho_empresa = {'L': 'grande', 'S': 'pequena', 'M': 'media'}
    df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
    
    mapa_trabalho = {0: 'presencial', 100: 'remoto', 50: 'hibrido'}
    df['remoto'] = df['remoto'].replace(mapa_trabalho)
    
    print("Dados preparados com sucesso!")
    
    return df

def verificar_valores_nulos(df):
    """Verifica a presença e quantidade de valores nulos no DataFrame"""
    
    print("\n=== VERIFICAÇÃO DE VALORES NULOS ===")
    print("=" * 50)
    
    print("\nVerificando valores nulos por coluna:")
    valores_nulos = df.isnull().sum()
    print(valores_nulos)
    
    colunas_com_nulos = valores_nulos[valores_nulos > 0]
    
    if len(colunas_com_nulos) > 0:
        print(f"\nEncontradas {len(colunas_com_nulos)} coluna(s) com valores nulos:")
        for coluna, qtd in colunas_com_nulos.items():
            percentual = (qtd / len(df)) * 100
            print(f"  • {coluna}: {qtd:,} nulos ({percentual:.2f}%)")
        
        for coluna in colunas_com_nulos.index:
            print(f"\nValores únicos na coluna '{coluna}':")
            valores_unicos = df[coluna].unique()
            print(f"  {valores_unicos}")
        
        print(f"\nVisualizando linhas com valores nulos:")
        linhas_com_nulos = df[df.isnull().any(axis=1)]
        print(f"Total de linhas com valores nulos: {len(linhas_com_nulos):,}")
        print("\nPrimeiras linhas com valores nulos:")
        print(linhas_com_nulos.head())
        
        return colunas_com_nulos, linhas_com_nulos
    else:
        print("\nNenhum valor nulo encontrado no DataFrame.")
        return None, None

def demonstrar_metodos_preenchimento():
    """Exemplifica diferentes formas de preencher valores nulos"""
    
    print("\n=== DEMONSTRAÇÃO DE MÉTODOS DE PREENCHIMENTO ===")
    print("=" * 60)
    
    print("\nExemplo 1: Preenchimento de salários com média e mediana")
    df_salarios = pd.DataFrame({
        'nome': ["Eloise", "Enoque", "Carlos", "Victor", "Edvaldo"],
        'salario': [4000, np.nan, 5000, np.nan, 100000]
    })
    
    print("\nDataFrame original:")
    print(df_salarios)
    
    df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
    df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
    
    print("\nApós preenchimento:")
    print(df_salarios)
    
    print("\nEstatísticas:")
    print(f"  Média: {df_salarios['salario'].mean():.2f}")
    print(f"  Mediana: {df_salarios['salario'].median():.2f}")
    
    print("\nExemplo 2: Preenchimento com Forward Fill (ffill)")
    df_temperaturas = pd.DataFrame({
        'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
        'Temperatura': [30, np.nan, np.nan, 28, 27, 32, 36]
    })
    
    print("\nDataFrame original:")
    print(df_temperaturas)
    
    df_temperaturas['Preenchido_ffill'] = df_temperaturas['Temperatura'].ffill()
    
    print("\nApós Forward Fill:")
    print(df_temperaturas[['Dia', 'Temperatura', 'Preenchido_ffill']])
    
    print("\nExemplo 3: Preenchimento com Backward Fill (bfill)")
    df_temperaturas2 = pd.DataFrame({
        'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
        'Temperatura': [30, np.nan, np.nan, 28, 27, 32, 36]
    })
    
    df_temperaturas2['Preenchido_bfill'] = df_temperaturas2['Temperatura'].bfill()
    
    print("\nApós Backward Fill:")
    print(df_temperaturas2[['Dia', 'Temperatura', 'Preenchido_bfill']])
    
    print("\nExemplo 4: Preenchimento com valor específico")
    df_cidades = pd.DataFrame({
        'nome': ["Eloise", "Enoque", "Carlos", "Victor", "Edvaldo"],
        'Cidade': ['São Paulo', np.nan, 'Belém', np.nan, 'Rio Grande do Norte']
    })
    
    print("\nDataFrame original:")
    print(df_cidades)
    
    df_cidades['Cidade_preenchida'] = df_cidades['Cidade'].fillna('Não informado')
    
    print("\nApós preenchimento:")
    print(df_cidades)

def limpar_dados(df, colunas_com_nulos):
    """Remove linhas que possuem valores nulos"""
    
    print("\n=== LIMPEZA DOS DADOS ===")
    print("=" * 30)
    
    print(f"\nDados antes da limpeza:")
    print(f"  Total de linhas: {len(df):,}")
    print(f"  Total de colunas: {len(df.columns)}")
    
    print("\nRemovendo linhas com valores nulos...")
    df_limpo = df.dropna()
    
    print(f"\nDados após limpeza:")
    print(f"  Total de linhas: {len(df_limpo):,}")
    print(f"  Total de colunas: {len(df_limpo.columns)}")
    print(f"  Linhas removidas: {len(df) - len(df_limpo):,}")
    
    print("\nVerificando valores nulos após limpeza:")
    valores_nulos_final = df_limpo.isnull().sum()
    print(valores_nulos_final)
    
    if valores_nulos_final.sum() == 0:
        print("Todos os valores nulos foram removidos com sucesso.")
    
    return df_limpo

def converter_tipos_dados(df_limpo):
    """Converte tipos de dados para os formatos adequados"""
    
    print("\n=== CONVERSÃO DE TIPOS DE DADOS ===")
    print("=" * 40)
    
    print("\nTipos de dados antes da conversão:")
    print(df_limpo.dtypes)
    
    print("\nConvertendo coluna 'ano' de float para int...")
    df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('int64'))
    
    print("\nTipos de dados após conversão:")
    print(df_limpo.dtypes)
    
    print("\nVisualizando os dados após conversão:")
    print(df_limpo.head())
    
    return df_limpo

def salvar_dados_limpos(df_limpo):
    """Salva o DataFrame limpo em arquivo CSV"""
    
    print("\n=== SALVANDO DADOS LIMPOS ===")
    print("=" * 35)
    
    try:
        nome_arquivo = 'dados_limpos_aula2.csv'
        df_limpo.to_csv(nome_arquivo, index=False, encoding='utf-8')
        print(f"Dados limpos salvos em '{nome_arquivo}'.")
        
        print("\nResumo dos dados salvos:")
        print(f"  Linhas: {len(df_limpo):,}")
        print(f"  Colunas: {len(df_limpo.columns)}")
        print(f"  Memória usada: {df_limpo.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
    except Exception as e:
        print(f"Aviso: Não foi possível salvar o arquivo. Motivo: {e}")

def main():
    """Função principal - Aula 2: Preparação e Limpeza dos Dados"""
    
    print("=" * 70)
    print("AULA 2 - PREPARAÇÃO E LIMPEZA DOS DADOS")
    print("=" * 70)
    
    # Etapa 1: Carregar e preparar dados iniciais
    df = carregar_e_preparar_dados()
    if df is None:
        return
    
    # Etapa 2: Verificar valores nulos
    colunas_com_nulos, linhas_com_nulos = verificar_valores_nulos(df)
    
    # Etapa 3: Demonstrar métodos de preenchimento
    demonstrar_metodos_preenchimento()
    
    # Etapa 4: Limpar dados removendo linhas com valores nulos, se existirem
    if colunas_com_nulos is not None:
        df_limpo = limpar_dados(df, colunas_com_nulos)
    else:
        print("\nDados já estão limpos, não há necessidade de remoção.")
        df_limpo = df.copy()
    
    # Etapa 5: Converter tipos de dados para adequar o DataFrame
    df_limpo = converter_tipos_dados(df_limpo)
    
    # Etapa 6: Salvar dados limpos em arquivo CSV
    salvar_dados_limpos(df_limpo)
    
    print("\n" + "=" * 70)
    print("RESUMO DA AULA 2 - PREPARAÇÃO E LIMPEZA DOS DADOS")
    print("=" * 70)
    print("""
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
""")
    
    return df_limpo

# Executa o script somente se for chamado diretamente
if __name__ == "__main__":
    df_final = main()
