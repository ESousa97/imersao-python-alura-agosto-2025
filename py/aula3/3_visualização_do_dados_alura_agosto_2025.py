# -*- coding: utf-8 -*-
"""
Globo Salarial por País (com rotação automática)
-------------------------------------------------

O script:
1) Carrega o dataset público de salários.
2) Limpa e cria a coluna 'regiao'.
3) Agrega salário médio por país (amostra mínima).
4) Gera um globo (projeção ortográfica) em Plotly com rotação automática suave.

Dependências:
    pip install pandas numpy plotly
"""

from pathlib import Path
from datetime import datetime
import logging
import warnings
import webbrowser

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio


# -------------------------------------------------------------------------
# Configurações básicas
# -------------------------------------------------------------------------

DEFAULT_DATA_URL = (
    "https://raw.githubusercontent.com/guilhermeonrails/"
    "data-jobs/refs/heads/main/salaries.csv"
)

pio.templates.default = "plotly_white"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("globo-salarial")
warnings.filterwarnings("ignore")


# -------------------------------------------------------------------------
# Mapeamentos
# -------------------------------------------------------------------------

COLUMN_MAPPING = {
    "work_year": "ao",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "usd",
    "employee_residence": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "company_size": "tamanho_empresa",
}

ISO2_TO_ISO3 = {
    "US": "USA", "BR": "BRA", "GB": "GBR", "DE": "DEU", "FR": "FRA", "ES": "ESP", "PT": "PRT",
    "CA": "CAN", "AU": "AUS", "IN": "IND", "NL": "NLD", "IT": "ITA", "PL": "POL", "AR": "ARG",
    "MX": "MEX", "JP": "JPN", "CN": "CHN", "KR": "KOR", "RU": "RUS", "TR": "TUR", "IE": "IRL",
    "SE": "SWE", "NO": "NOR", "DK": "DNK", "FI": "FIN", "CH": "CHE", "BE": "BEL", "AT": "AUT",
    "IL": "ISR", "AE": "ARE", "SG": "SGP", "ZA": "ZAF", "NZ": "NZL", "CL": "CHL", "CO": "COL",
    "PE": "PER", "UY": "URY", "HR": "HRV", "SI": "SVN", "LU": "LUX",
}

COUNTRY_NAMES_PT = {
    "US": "Estados Unidos", "BR": "Brasil", "GB": "Reino Unido", "DE": "Alemanha", "FR": "França",
    "ES": "Espanha", "PT": "Portugal", "CA": "Canadá", "AU": "Austrália", "IN": "Índia",
    "NL": "Países Baixos", "IT": "Itália", "PL": "Polônia", "AR": "Argentina", "MX": "México",
    "JP": "Japão", "CN": "China", "KR": "Coreia do Sul", "RU": "Rússia", "TR": "Turquia",
    "IE": "Irlanda", "SE": "Suécia", "NO": "Noruega", "DK": "Dinamarca", "FI": "Finlândia",
    "CH": "Suíça", "BE": "Bélgica", "AT": "Áustria", "IL": "Israel",
    "AE": "Emirados Árabes Unidos", "SG": "Singapura", "ZA": "África do Sul",
    "NZ": "Nova Zelândia", "CL": "Chile", "CO": "Colômbia", "PE": "Peru", "UY": "Uruguai",
    "HR": "Croácia", "SI": "Eslovênia", "LU": "Luxemburgo",
}


# -------------------------------------------------------------------------
# Pipeline mínimo
# -------------------------------------------------------------------------

def load_and_prepare(data_source: str | Path = DEFAULT_DATA_URL,
                     min_samples_per_country: int = 5) -> pd.DataFrame:
    """
    Carrega o dataset e produz a tabela pronta para o mapa.

    Retorna um DataFrame com:
        iso3, nome_pais, regiao, salario_medio, total_registros, salario_formatado
    """
    logger.info("Carregando dados de: %s", data_source)
    df = pd.read_csv(data_source)

    # Renomeia colunas para português (só as que usaremos aqui)
    df = df.rename(columns=COLUMN_MAPPING)

    # Mantém apenas colunas necessárias
    df = df[["usd", "residencia"]].dropna().copy()

    # Filtra registros válidos
    df = df[df["usd"] > 0].copy()

    # Mapeia residência -> região
    americas = {"US", "CA", "BR", "AR", "MX", "CL", "CO", "PE", "UY"}
    europe = {"GB", "DE", "FR", "ES", "PT", "IT", "NL", "PL", "SE", "NO", "DK", "FI", "CH", "BE", "AT", "IE"}
    asia_pacific = {"IN", "JP", "CN", "KR", "SG", "AU", "NZ"}
    mea = {"IL", "AE", "ZA", "TR"}

    def to_region(cc: str) -> str:
        if cc in americas:
            return "Américas"
        if cc in europe:
            return "Europa"
        if cc in asia_pacific:
            return "Ásia-Pacífico"
        if cc in mea:
            return "Oriente Médio/África"
        return "Outros"

    df["residencia"] = df["residencia"].astype(str)
    df["regiao"] = df["residencia"].map(to_region)

    # Agrega por país
    agg = (
        df.groupby("residencia", observed=True)["usd"]
        .agg(salario_medio="mean", total_registros="size")
        .reset_index()
    )

    # Amostra mínima
    agg = agg.query("total_registros >= @min_samples_per_country").copy()

    # ISO3 e nomes
    agg["iso3"] = agg["residencia"].map(ISO2_TO_ISO3)
    agg = agg.dropna(subset=["iso3"]).copy()

    agg["nome_pais"] = agg["residencia"].map(COUNTRY_NAMES_PT).fillna(agg["residencia"])
    agg["salario_formatado"] = agg["salario_medio"].apply(lambda x: f"US$ {int(x):,}".replace(",", "."))

    # Junta a região
    regions = df[["residencia", "regiao"]].drop_duplicates()
    agg = agg.merge(regions, on="residencia", how="left")

    # Ordenação apenas para consistência visual
    agg = agg.sort_values("salario_medio", ascending=False).reset_index(drop=True)

    logger.info("Países incluídos no mapa: %d", len(agg))
    return agg


# -------------------------------------------------------------------------
# Visualização com rotação automática
# -------------------------------------------------------------------------

def build_salary_globe(map_df: pd.DataFrame) -> go.Figure:
    """
    Constrói o globo (projeção ortográfica) com rotação automática suave.
    """
    # Choropleth principal
    choropleth = go.Choropleth(
        locations=map_df["iso3"],
        z=map_df["salario_medio"],
        colorscale="Viridis",
        colorbar_title="Salário Médio (USD)",
        text=map_df["nome_pais"],
        hovertemplate=(
            "<b>%{text}</b><br>"
            "Região: %{customdata[0]}<br>"
            "Salário médio: %{customdata[1]}<br>"
            "Registros: %{customdata[2]}<extra></extra>"
        ),
        customdata=np.column_stack([
            map_df["regiao"],
            map_df["salario_formatado"],
            map_df["total_registros"],
        ]),
        marker_line_color="rgba(255,255,255,0.6)",
        marker_line_width=0.5,
    )

    # Frames variando a rotação longitudinal (lon)
    frames = []
    for lon in range(0, 361, 2):  # passo pequeno para rotação suave
        frames.append(
            go.Frame(
                name=f"rot_{lon}",
                layout=dict(
                    geo=dict(
                        projection=dict(
                            type="orthographic",
                            rotation=dict(lon=lon, lat=0)
                        )
                    )
                )
            )
        )

    # Figura com layout inicial e frames
    fig = go.Figure(
        data=[choropleth],
        layout=go.Layout(
            title={
                "text": (
                    "Globo Salarial por País"
                    f"<br><sub>Salário médio em USD | Atualizado em {datetime.now().strftime('%d/%m/%Y %H:%M')}</sub>"
                ),
                "x": 0.5,
                "xanchor": "center",
            },
            geo=dict(
                projection=dict(type="orthographic", rotation=dict(lon=0, lat=0)),
                showframe=False,
                showcoastlines=True,
                showcountries=True,
                countrycolor="rgba(120,120,120,0.5)",
                oceancolor="rgba(230,240,255,1.0)",
                showocean=True,
                landcolor="rgba(240,240,240,1.0)",
                bgcolor="white",
            ),
            margin=dict(l=20, r=20, t=80, b=20),
            # Botão opcional de controle manual; autoplay será feito no HTML
            updatemenus=[{
                "type": "buttons",
                "showactive": False,
                "x": 0.5, "xanchor": "center",
                "y": 1.08, "yanchor": "top",
                "buttons": [{
                    "label": "Reproduzir",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": 50, "redraw": True},
                        "transition": {"duration": 0},
                        "fromcurrent": True,
                        "mode": "immediate"
                    }]
                }]
            }]
        ),
        frames=frames
    )

    return fig


# -------------------------------------------------------------------------
# Execução
# -------------------------------------------------------------------------

def main():
    """
    Gera o globo e abre automaticamente no navegador com autoplay ativo.
    Observação: o autoplay contínuo roda uma vez. Para loop infinito,
    é necessário um pequeno script JS adicional (posso fornecer se quiser).
    """
    df_map = load_and_prepare(DEFAULT_DATA_URL, min_samples_per_country=5)
    fig = build_salary_globe(df_map)

    # Salva HTML com autoplay da animação
    out = Path(f"globo_salarial_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
    pio.write_html(
        fig,
        file=out,
        include_plotlyjs="cdn",
        auto_play=True,  # inicia a animação automaticamente
        config={"displaylogo": False, "responsive": True}
    )
    logger.info("Arquivo gerado: %s", out.resolve())

    # Abre no navegador padrão
    webbrowser.open(out.resolve().as_uri(), new=2)


if __name__ == "__main__":
    main()
