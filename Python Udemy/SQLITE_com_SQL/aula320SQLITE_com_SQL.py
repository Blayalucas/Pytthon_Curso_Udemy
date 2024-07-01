# SQLite3 com SQL e DBeaver

"""
O SQLite3 é uma biblioteca semelhante ao Json porém melhorado, entretanto, 
"limitado" é para uso de poucos usuario  

Dica importante: 

Vá no terminar e faça o seguinte comando para criar um DBLITE3: 

python aula320SQLite_com_SQL/aula320SQLite_com_SQL.py

"""

# Biblioteca 
import sqlite3

from pathlib import Path

# Abrindo a pasta e criando um caminho até o arquivo X 

ROOT_DIR = Path(__file__).parent

# Nome da Pasta 
DATABASE_NAME = "db.SQlite3"
# Arquivo localizado
DATABASE_FILE = ROOT_DIR / DATABASE_NAME
TABLE_NAME = "Customers"

# Conectando o sistema com o arquivo 

connection = sqlite3.connect(DATABASE_FILE)

# Cursor para selecionar ou apagar coisas no sistema

cursor = connection.cursor ()

# Limpando a Tabela 

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
    
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name=  "{TABLE_NAME}"'
    
)

connection.commit()
# SQL com DBveaver ( criando Colunas)
"""
Vá no windows abra o DBeaver:
novo arquivo e clique em dblite3 e localize o arquivo criado na pasta e conecte

com aspas simples 
"""

cursor.execute(
    f'Create Table if not exists {TABLE_NAME}'
    '('
    
    'ID Integer Primary Key AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    
    ')'
)

# Commit para dentro o DBeaver 

connection.commit() # print

# Registrar Valores na Tabela com instancia e cursor
sql = (
    f"INSERT INTO {TABLE_NAME}" 
    "(name, weight)"
    "VALUES"
    "(?,?)"
    
)
cursor.executemany(sql,[["Lucas Mendonca", 69], ["Ariani", 58],["Daniel", 75]]) # itens 
connection.commit()
print(sql)

# Fechamento do Sistema ( obrigatório sempre fechar)

cursor.close ()
connection.close()



