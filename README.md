# Análise Socioeconômica de Natal/RN

Esta aplicação Streamlit demonstra uma análise interativa dos dados socioeconômicos dos bairros de Natal/RN, utilizando visualizações com Plotly e recursos de filtragem dinâmica.

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone este repositório:
```sh
git clone git@github.com:VictorNGomes/Streamlit-Introduction.git
cd Streamlit-Introduction
```

2. Crie um ambiente virtual:
```sh
python -m venv env
```

3. Ative o ambiente virtual:

**No Linux/macOS**:
```sh
source env/bin/activate
```

**No Windows**:
```sh
.\env\Scripts\activate
```

4. Instale as dependências necessárias:
```sh
pip install streamlit pandas plotly numpy
```

## Executando a Aplicação

Com o ambiente virtual ativado, execute:

```sh
streamlit run streamlit_app.py
```

A aplicação abrirá automaticamente em seu navegador padrão no endereço `http://localhost:8501`.

## Funcionalidades

- Visualização espacial dos bairros de Natal/RN
- Filtros por região e indicadores socioeconômicos
- Análise estatística por bairro e região
- Gráficos interativos usando Plotly
- Comparações entre regiões da cidade

## Estrutura do Projeto

```
Streamlit-Introduction/
├── README.md
├── .gitignore
├── streamlit_app.py
└── env/
```

## Dados

A aplicação utiliza dados socioeconômicos dos bairros de Natal/RN, incluindo:
- Renda mensal por pessoa
- Rendimento nominal médio
- População total
- Distribuição espacial dos bairros

## Dependências Principais

- streamlit
- pandas
- plotly
- numpy