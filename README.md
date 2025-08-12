# 📊 Statistical data analysis dashboard using Python


## 🇧🇷 Sobre o Projeto

Essa é uma aplicação desenvolvida em **Python** utilizando **Streamlit** para construção de um dashboard interativo de análise salarial na área de dados.  

O projeto utiliza uma base de dados em formato `.csv` contendo informações sobre profissionais da área de dados ao redor do mundo, abrangendo diferentes anos, níveis de senioridade, tipos de contrato, tamanhos de empresa e cargos.  

Os dados foram tratados com **Pandas** e visualizados por meio de gráficos interativos criados com **Plotly**.  

🔗 **[Acesse a demonstração online aqui](https://data-python-dashboard-2025.streamlit.app/)**  

No dashboard é possível:  
- Filtrar por ano, senioridade, tipo de contrato, tamanho da empresa e cargo.  
- Visualizar métricas como salário médio, mediana, salário máximo, total de registros e cargo mais frequente.  
- Analisar as 10 maiores médias salariais por cargo.  
- Explorar a distribuição de salários ao longo dos anos.  
- Observar a proporção de modalidades de trabalho (remoto, presencial, híbrido).  
- Ver a média salarial por país em um mapa-múndi interativo.  
- Consultar a base de dados detalhada.  

---

### 📦 Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

### 📚 Bibliotecas

As dependências do projeto estão listadas no arquivo `requirements.txt`. Entre as principais:  

- `streamlit`  
- `pandas`  
- `plotly`  

---

### 📝 Instruções

#### ⚙️ Requisitos

Antes de iniciar, certifique-se de ter os seguintes recursos instalados:  

- Python 3.10+  
- Git  
- pip (gerenciador de pacotes Python)  

---

#### 🚀 Instalação

1. **Clone o repositório**:

```bash
git clone https://github.com/andre-ribeiro93/data-python-dashboard.git
cd data-python-dashboard
```

2. **Crie e ative um ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

---

#### ▶️ Executando o projeto

```bash
streamlit run app.py
```

O dashboard será iniciado em:  
[http://localhost:8501](http://localhost:8501)  

---

## 🇺🇸 About the Project

This is an application developed in **Python** using **Streamlit** to build an interactive salary analysis dashboard for the data field.  

The project uses a `.csv` dataset containing information about data professionals worldwide, covering different years, seniority levels, contract types, company sizes, and job positions.  

The data was processed with **Pandas** and visualized through interactive charts built with **Plotly**.  

🔗 **[Access the live demo here](https://data-python-dashboard-2025.streamlit.app/)**  

In the dashboard, you can:  
- Filter by year, seniority, contract type, company size, and job position.  
- View metrics such as average salary, median salary, maximum salary, total records, and most frequent job position.  
- Analyze the top 10 highest average salaries by job title.  
- Explore the salary distribution over the years.  
- See the proportion of work modalities (remote, on-site, hybrid).  
- Check the average salary by country on an interactive world map.  
- Browse the detailed dataset.  

---

### 📦 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

### 📚 Libraries

Project dependencies are listed in the `requirements.txt` file. Main ones include:  

- `streamlit`  
- `pandas`  
- `plotly`  

---

### 📝 Instructions

#### ⚙️ Requirements

Before starting, make sure you have the following installed:  

- Python 3.10+  
- Git  
- pip (Python package manager)  

---

#### 🚀 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/andre-ribeiro93/data-python-dashboard.git
cd data-python-dashboard
```

2. **Create and activate a virtual environment** (optional but recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

#### ▶️ Running the project

```bash
streamlit run app.py
```

The dashboard will start at:  
[http://localhost:8501](http://localhost:8501)  

---

### 📷 Preview

<div align="center">
  <img width="80%" src="/assets/preview.png" alt="Dashboard preview">
</div>