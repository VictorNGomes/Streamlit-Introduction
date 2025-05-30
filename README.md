# Streamlit Data Visualization Examples

This repository contains examples of interactive data visualizations using Streamlit. The examples demonstrate various Streamlit features including basic elements, interactive widgets, Plotly visualizations, layout containers, and data filtering.

## Prerequisites

- Python 3.12 or later
- pip (Python package installer)

## Installation

1. Clone this repository:
```sh
git clone git@github.com:VictorNGomes/Streamlit-Introduction.git
cd <repository-folder>
```

2. Create a virtual environment:
```sh
python -m venv env
```

3. Activate the virtual environment:

**On Linux/macOS**:
```sh
source env/bin/activate
```

**On Windows**:
```sh
.\env\Scripts\activate
```

4. Install required packages:
```sh
pip install streamlit pandas plotly numpy
```

## Running the Examples

After activating the virtual environment, you can run any of the example scripts using:

```sh
streamlit run <script-name>.py
```

Available examples:

- Basic Elements:
```sh
streamlit run exemplo1_elementos_basicos.py
```

- Interactive Widgets:
```sh 
streamlit run exemplo2_widgets_interativos.py
```

- Plotly Visualization:
```sh
streamlit run exemplo3_plotly_visualizacao.py
```

- Layout Containers:
```sh
streamlit run exemplo4_layout_containers.py
```

- Data Filtering:
```sh
streamlit run exemplo5_filtros_dados_reais.py
```

The app will open automatically in your default web browser at `http://localhost:8501`.

## Structure

- `exemplo1_elementos_basicos.py`: Demonstrates basic Streamlit text and formatting elements
- `exemplo2_widgets_interativos.py`: Shows interactive widgets like buttons, selectors, and input fields
- `exemplo3_plotly_visualizacao.py`: Examples of interactive data visualization using Plotly
- `exemplo4_layout_containers.py`: Demonstrates layout options and containers
- `exemplo5_filtros_dados_reais.py`: Shows how to implement data filters using real data

## Data

The examples use socioeconomic data from Natal/RN, Brazil. The data is loaded directly from a GitHub repository during runtime.

## Requirements

Main dependencies:
- streamlit
- pandas
- plotly
- numpy