# API post 

"""
API post = Fazer um envio para o site 

atraves do site replit: https://replit.com/

"""
# Importando Pandas, flask e o jsonify
import pandas as pd
from flask import Flask, jsonify

#criando um app Flask - OBRIGATÓRIO SEMPRE
app = Flask(__name__)


# Construindo as Funcionalidades
# HomePage
@app.route('/home')
def homepage():
  return 'Essa é minha primeira Homepage de API no Ar'


# Enviando o total de vendas " formato" Json "jsonify"
@app.route('/PegarVendas')
def pegarvendas():
  tabela = pd.read_csv('arquivo.csv')
  total_vendas = tabela['Vendas'].sum()
  resultado_total = {'total_vendas': total_vendas}
  return jsonify(resultado_total)


# Rodando a API com parametro " Direto com link da minha Home"
app.run(host='0,0,0,0')


#Baixando a Planilha CSV para o Python
#tabela = pd.read_csv("arquivo.csv")
# Somando a Coluna de vendas da planilha
#Total_vendas = tabela["Vendas"].sum()



