# Criando uma agenda SQLite3

"""
O SQLite3 é um gerenciador de Banco de Dados, utilizado em telefones Celulares

Criando e fazendo em 8 passos: 

# Passo 1 - importando o SQLite3
# Passo 2 - Fazendo conexão para abrir o arquivos "agenda" utilizando .db
# Passo 3 - criando um cursor com conexão - para receber e enviar dados "API de trafego" 
# Passo 4 - Cursor execute - para enviar os dados que quero usando aspas triplas 
- SQlite utiliza como boa pratica """  """ e criando e inserindo tabela 
para guardar NOMES e TELEFONES - "create table com values"
# Passo 5 - Commitando todas as informações da agenda para o sistema
# Passo 6 - Fechando o cursor para NÂO recebimento e envio de dados
# Passo 7 - print("Agenda criada com sucesso")
# Passo 8 - Fechando a conexão

"""
# importando o SQLite3
import sqlite3 

# Fazendo conexão para abrir o arquivos "agenda" utilizando .db
conexao = sqlite3.connect("agenda.db")

# criando um cursor com conexão - para receber e enviar dados "API de trafego" 
cursor = conexao.cursor()

# Cursor execute - para enviar os dados que quero  e criando e inserindo tabela 
#para guardar NOMES e TELEFONES de cada informação

cursor.execute("""criando  tabela agenda (nome text, telefone text)""") # criando tabela
cursor.execute("""inserindo informações na agenda (nome, telefone) dados (?,?)""", ("Bruna", 99999999)) # inserindo dados

# Commitando todas as informações  da agenda para o sistema
conexao.commit()

#Fechando o cursor para Não recebimento e envio de dados
cursor.close

# Print Agenda criada
print("Agenda criada com sucesso")

#Fechando a conexão
conexao.close

