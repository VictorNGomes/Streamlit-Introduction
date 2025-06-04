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

## Descrição dos Arquivos

### Aplicação Principal
- `streamlit_app.py`: Aplicação principal que implementa a análise socioeconômica completa dos bairros de Natal/RN, incluindo visualizações interativas, filtros e estatísticas.

### Exemplos Didáticos
- `examples/exemplo1_elementos_basicos.py`: Demonstração dos elementos básicos do Streamlit como texto, markdown, títulos e layouts simples.
- `examples/exemplo2_widgets_interativos.py`: Exemplo completo de widgets interativos como botões, sliders, inputs e seletores.
- `examples/exemplo3_plotly_visualizacao.py`: Demonstração de diferentes tipos de visualizações usando Plotly.
- `examples/exemplo4_layout_containers.py`: Exemplos de uso de containers e organização de layout.
- `examples/exemplo5_filtros_dados_reais.py`: Implementação de filtros interativos com dados reais.

## Executando a Aplicação

Com o ambiente virtual ativado, execute:

```sh
streamlit run streamlit_app.py
```

Para executar os exemplos:
```sh
streamlit run examples/exemplo1_elementos_basicos.py
streamlit run examples/exemplo2_widgets_interativos.py
streamlit run examples/exemplo3_plotly_visualizacao.py
streamlit run examples/exemplo4_layout_containers.py
streamlit run examples/exemplo5_filtros_dados_reais.py
```

A aplicação abrirá automaticamente em seu navegador padrão no endereço `http://localhost:8501`.

## Estrutura do Projeto

```
Streamlit-Introduction/
├── README.md
├── .gitignore
├── streamlit_app.py
├── examples/
│   ├── exemplo1_elementos_basicos.py
│   ├── exemplo2_widgets_interativos.py
│   ├── exemplo3_plotly_visualizacao.py
│   ├── exemplo4_layout_containers.py
│   └── exemplo5_filtros_dados_reais.py
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