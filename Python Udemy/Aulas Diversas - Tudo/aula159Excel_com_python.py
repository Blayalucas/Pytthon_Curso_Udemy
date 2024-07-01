# Para baixar uma planilha no Python

"""
Primeiro Passo: import pandas as pd
Segundo Passo: criar uma variavel = pd.read_csv("arquivo.csv")

"""
import pandas as pd

tabela = pd.read_csv("arquivo.csv") 

# Somando a coluna de vendas da planilha
Total_vendas = tabela["Vendas"].sum()