# Sales Management System & Dashboard (Streamlit + Plotly)

*[Leia em Português](#sistema-de-gestão-e-dashboard-de-vendas-streamlit--plotly)*

An interactive web application built with Python and Streamlit for registering sales transactions and monitoring real-time commercial performance. The system persists records in a CSV database using Pandas and renders dynamic KPIs and charts with Plotly Express.

## Technologies Used

* **Python 3**
* **Streamlit** (Interactive Web UI, Sidebar Form & Layout Management)
* **Pandas** (CSV Data Persistence & Tabular Manipulation)
* **Plotly Express** (Interactive Bar and Pie Charts)

## Project Structure

* `main.py`: Core application script containing the sidebar sales registration form, CSV persistence logic, interactive data table, and analytics dashboard.
* `vendas.csv`: Sales dataset storing transaction date, salesperson, product, quantity, and total value.
* `requirements.txt`: Project dependencies list.

## Features

* **Sales Registration:** Sidebar form with input validation for date, salesperson (`Ana`, `Bruno`, `Carla`), product (`Notebook`, `Celular`, `Fone`), quantity, and total amount.
* **Real-Time Persistence:** Automatically appends new transactions to `vendas.csv` and updates the interface immediately.
* **Performance Dashboard:** Displays total revenue KPI, stacked bar chart of revenue by salesperson and product, and pie chart of product revenue share.

## How to Run

1. Install the dependencies:

    pip install -r requirements.txt

2. Start the Streamlit web server:

    streamlit run main.py

---

# Sistema de Gestão e Dashboard de Vendas (Streamlit + Plotly)

*[Read in English](#sales-management-system--dashboard-streamlit--plotly)*

Aplicação web interativa desenvolvida com Python e Streamlit para cadastro de vendas e acompanhamento de desempenho comercial em tempo real. O sistema salva os registros em uma base CSV utilizando Pandas e exibe indicadores dinâmicos e gráficos interativos com Plotly Express.

## Tecnologias Utilizadas

* **Python 3**
* **Streamlit** (Interface Web Interativa, Formulário Lateral e Gerenciamento de Layout)
* **Pandas** (Persistência de Dados em CSV e Manipulação Tabular)
* **Plotly Express** (Gráficos Interativos de Barras e Pizza)

## Estrutura do Projeto

* `main.py`: Script principal contendo o formulário lateral de cadastro de vendas, lógica de gravação no CSV, tabela interativa e dashboard analítico.
* `vendas.csv`: Base de dados armazenando data, vendedor, produto, quantidade e valor total das vendas.
* `requirements.txt`: Lista de dependências do projeto.

## Funcionalidades

* **Cadastro de Vendas:** Formulário lateral com validação de entrada para data, vendedor (`Ana`, `Bruno`, `Carla`), produto (`Notebook`, `Celular`, `Fone`), quantidade e valor total.
* **Persistência em Tempo Real:** Grava automaticamente cada nova venda no arquivo `vendas.csv` e atualiza a tela imediatamente.
* **Dashboard Gerencial:** Exibe o indicador de faturamento total, gráfico de barras empilhadas por vendedor/produto e gráfico de pizza com a participação de cada produto na receita.

## Como Executar

1. Instale as dependências:

    pip install -r requirements.txt

2. Inicie o servidor web do Streamlit:

    streamlit run main.py
