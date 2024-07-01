# Select com Python e importando itens no SQL 

"""
O Select * From envia dados "itens"  que estão na aula 320 " Main" para o SQL
    
"""

# Biblioteca e realizando link na aula 320 "Main"

import sqlite3

from aula320SQLITE_com_SQL import DATABASE_FILE,TABLE_NAME

# Conectando as bases 

connection = sqlite3.connect(DATABASE_FILE)
cursor = connection.cursor()

# Executando a Tabela com PYTHON
cursor.execute(f'SELECT * From {TABLE_NAME}')

# For Loop para adicionar cada linha em python no SQL

for row in cursor.fetchall():
    _id, name, weight = row
    print(-_id,name,weight)
    

# Fechamento do Sistema ( obrigatório sempre fechar)

cursor.close()
connection.close()


# OBS: Para Deletar tudo basta trocar Select * From por Delete From

"""
OBS: Para realizar atualização na Tabela basta: 
 f'UPDATE {TABLE_NAME}'
 'SET  name="Qualquer" '
 ' WHERE id = 50'

"""
