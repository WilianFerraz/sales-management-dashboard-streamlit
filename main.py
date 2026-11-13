import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Sistema de Vendas", layout="wide")
st.write("# Sistema de Vendas")

# Load sales dataset
tabela = pd.read_csv("vendas.csv")

# Sidebar registration form
st.sidebar.write("## Cadastrar venda")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", min_value=1, step=1)
valor = st.sidebar.number_input("Valor Total (R$)", min_value=0.01, step=50.0)
botao = st.sidebar.button("Cadastrar venda")

# Persist new sale record to CSV
if botao:
    nova_venda = [str(data), vendedor, produto, int(quantidade), float(valor)]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv("vendas.csv", index=False)
    st.sidebar.success("Venda cadastrada com sucesso!")

# Display registered sales table
st.write("## Vendas cadastradas")
st.dataframe(tabela, use_container_width=True)

# Interactive Analytics Dashboard
st.write("## Dashboard")
soma = tabela["valor"].sum()
st.metric("Faturamento Total", f"R$ {soma:,.2f}")

col1, col2 = st.columns(2)

with col1:
    grafico = px.bar(
        tabela,
        x="vendedor",
        y="valor",
        color="produto",
        title="Faturamento por Vendedor e Produto"
    )
    st.plotly_chart(grafico, use_container_width=True)

with col2:
    grafico2 = px.pie(
        tabela,
        names="produto",
        values="valor",
        title="Participação nas Vendas por Produto"
    )
    st.plotly_chart(grafico2, use_container_width=True)
