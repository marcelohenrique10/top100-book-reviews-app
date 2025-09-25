import streamlit as st
import pandas as pd
import plotly.express as px

#Transformar página em widescreen
st.set_page_config(layout="wide")

#importando os arquivos csv
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

book_title_page = "Top 100 Bestselling Book Reviews on Amazon" 
st.title(book_title_page)

#Fazendo slide de max e min valor
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

#Variável maior preço com slider do stremlit dentro da side bar
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
#O filtro que faz o slider de preço selecionar os livros de acordo com o preço
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

#Mostra o slider na tela
df_books

#Criando os gráficos
fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

#divide em duas colunas
colun1 , colun2 = st.columns(2)
colun1.plotly_chart(fig)
colun2.plotly_chart(fig2)