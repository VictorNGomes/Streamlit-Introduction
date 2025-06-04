"""
Aplicação Principal - Análise Socioeconômica de Natal/RN

Este é o aplicativo principal que demonstra uma análise completa dos dados socioeconômicos
dos bairros de Natal/RN. O objetivo é mostrar como criar uma aplicação Streamlit completa
que integra diferentes elementos:
- Visualizações interativas com Plotly
- Filtros dinâmicos por região e indicadores
- Análises estatísticas
- Layout responsivo e organizado
- Manipulação de dados com Pandas

Autor: Victor Gomes
Data: Junho 2024
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Análise Socioeconômica de Natal/RN",
    page_icon="📊",
    layout="wide"
)

# Título e descrição
st.title("📊 Análise Socioeconômica dos Bairros de Natal/RN")
st.markdown("""
Esta aplicação demonstra como transformar análises de dados estáticas em visualizações interativas usando Streamlit e Plotly.
Baseado na análise exploratória de dados socioeconômicos dos bairros de Natal/RN.
""")

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    # Carrega o dataset contendo informações socioeconômicas dos bairros de Natal/RN
    df = pd.read_csv('https://raw.githubusercontent.com/igendriz/DCA3501-Ciencia-Dados/main/Dataset/Bairros_Natal_v01.csv')
    
    # Remove linhas com quaisquer valores ausentes (NaN)
    df = df.dropna()
    
    # Corrige nomes específicos de bairros para padronização (sem acentos ou espaços)
    df.loc[0, "bairro"] = 'ns_apresentacao'   # Nossa Senhora da Apresentação
    df.loc[34, "bairro"] = 'ns_nazare'        # Nossa Senhora de Nazaré
    df.loc[32, "bairro"] = 'c_esperanca'      # Cidade da Esperança
    
    # Remove a coluna 'Unnamed: 0', gerada automaticamente pelo salvamento anterior do CSV
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns='Unnamed: 0')
    
    return df

# Carrega os dados
df_natal = carregar_dados()

# Sidebar para filtros
st.sidebar.header("Filtros")

# Filtro por região
regioes = ["Todas"] + sorted(df_natal["regiao"].unique().tolist())
regiao_selecionada = st.sidebar.selectbox("Selecione a Região:", regioes)

# Filtro por indicador socioeconômico
indicadores = {
    "Renda Mensal por Pessoa (R$)": "renda_mensal_pessoa",
    "Rendimento Nominal Médio (sal. mín.)": "rendimento_nominal_medio",
    "População Total": "populacao"
}
indicador_selecionado = st.sidebar.selectbox("Selecione o Indicador:", list(indicadores.keys()))
coluna_indicador = indicadores[indicador_selecionado]

# Filtro por limiar de rendimento
if coluna_indicador in ["renda_mensal_pessoa", "rendimento_nominal_medio"]:
    min_valor = float(df_natal[coluna_indicador].min())
    max_valor = float(df_natal[coluna_indicador].max())
    limiar = st.sidebar.slider(
        "Limiar de Rendimento:",
        min_valor, max_valor,
        (min_valor + max_valor) / 2  # valor padrão
    )

# Aplicar filtros
if regiao_selecionada != "Todas":
    df_filtrado = df_natal[df_natal["regiao"] == regiao_selecionada.lower()]
else:
    df_filtrado = df_natal.copy()

# Layout principal com duas colunas
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Visualização Espacial dos Bairros")
    
    # Preparação dos dados para visualização espacial
    x = df_filtrado['x'] / 1e3   # Coordenada X convertida para quilômetros
    y = df_filtrado['y'] / 1e3   # Coordenada Y convertida para quilômetros
    
    # Dicionário com cores atribuídas para cada região
    cores_regiao = {
        'norte': 'blue',
        'sul': 'green',
        'leste': 'orange',
        'oeste': 'red'
    }
    
    # Criar figura Plotly para visualização espacial
    fig_espacial = go.Figure()
    
    # Adicionar pontos para cada região
    for regiao, grupo in df_filtrado.groupby('regiao'):
        tamanho = grupo[coluna_indicador]
        
        # Ajustar escala de tamanho conforme o indicador
        if coluna_indicador == "populacao":
            tamanho = tamanho / 150
        elif coluna_indicador == "rendimento_nominal_medio":
            tamanho = tamanho * 50
        else:  # renda_mensal_pessoa
            tamanho = tamanho / 20
        
        fig_espacial.add_trace(go.Scatter(
            x=grupo['x'] / 1e3,
            y=grupo['y'] / 1e3,
            mode='markers+text',
            marker=dict(
                size=tamanho,
                color=cores_regiao.get(regiao, 'gray'),
                opacity=0.8,
                line=dict(width=1, color='black')
            ),
            text=grupo['bairro'],
            textposition="top center",
            name=regiao.capitalize(),
            hovertemplate=(
                "<b>%{text}</b><br>" +
                f"Região: {regiao.capitalize()}<br>" +
                f"{indicador_selecionado}: %{{customdata}}<br>" +
                "Coordenada X: %{x:.2f} km<br>" +
                "Coordenada Y: %{y:.2f} km"
            ),
            customdata=grupo[coluna_indicador]
        ))
    
    # Configurações do layout
    fig_espacial.update_layout(
        title=f"Distribuição Espacial por {indicador_selecionado}",
        xaxis_title="Coordenada X (km)",
        yaxis_title="Coordenada Y (km)",
        legend_title="Região",
        height=600,
        hovermode='closest'
    )
    
    # Exibir o gráfico
    st.plotly_chart(fig_espacial, use_container_width=True)

with col2:
    st.subheader("Análise por Bairro")
    
    # Gráfico de barras para o indicador selecionado
    fig_barras = px.bar(
        df_filtrado.sort_values(by=coluna_indicador, ascending=False),
        x="bairro",
        y=coluna_indicador,
        color="regiao",
        title=f"{indicador_selecionado} por Bairro",
        labels={"bairro": "Bairro", coluna_indicador: indicador_selecionado},
        height=600
    )
    
    # Ajustar layout
    fig_barras.update_layout(
        xaxis_tickangle=-45,
        xaxis_title="Bairro",
        yaxis_title=indicador_selecionado
    )
    
    # Exibir o gráfico
    st.plotly_chart(fig_barras, use_container_width=True)

# Seção adicional para estatísticas
st.subheader("Estatísticas Descritivas")

# Estatísticas por região
if regiao_selecionada != "Todas":
    st.write(f"Estatísticas para a região **{regiao_selecionada}**:")
else:
    st.write("Estatísticas por região:")

# Calcular estatísticas por região
stats_regiao = df_natal.groupby('regiao')[coluna_indicador].agg(['mean', 'min', 'max', 'count']).reset_index()
stats_regiao.columns = ['Região', 'Média', 'Mínimo', 'Máximo', 'Quantidade de Bairros']

# Formatar valores numéricos
if coluna_indicador != "populacao":
    stats_regiao['Média'] = stats_regiao['Média'].round(2)
    stats_regiao['Mínimo'] = stats_regiao['Mínimo'].round(2)
    stats_regiao['Máximo'] = stats_regiao['Máximo'].round(2)
else:
    stats_regiao['Média'] = stats_regiao['Média'].round(0).astype(int)
    stats_regiao['Mínimo'] = stats_regiao['Mínimo'].round(0).astype(int)
    stats_regiao['Máximo'] = stats_regiao['Máximo'].round(0).astype(int)

# Exibir tabela de estatísticas
st.dataframe(stats_regiao, use_container_width=True)

# Adicionar um gráfico de comparação entre regiões
st.subheader("Comparação entre Regiões")

fig_comparacao = px.bar(
    stats_regiao,
    x='Região',
    y='Média',
    color='Região',
    title=f"Média de {indicador_selecionado} por Região",
    labels={"Média": f"Média de {indicador_selecionado}"},
    text_auto=True
)

st.plotly_chart(fig_comparacao, use_container_width=True)

# Rodapé com informações
st.markdown("---")
st.markdown("""
**Fonte dos dados:** IBGE (dados adaptados para fins didáticos)  
**Aplicação desenvolvida com:** Streamlit e Plotly  
**Contexto:** Aula de Ciência de Dados - Visualização Interativa
""")
