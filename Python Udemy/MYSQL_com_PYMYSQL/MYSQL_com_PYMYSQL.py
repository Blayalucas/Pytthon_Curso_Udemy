# Mysql usando PYMYSQL

# Biblioteca
import dotenv
import pymysql
import os

# Instância 
TABLE_NAME = "EXEMPLO_LUCAS"

# Carregando o Dotenv
dotenv.load_dotenv()



# Conectando PymySQL com os. environ
connection = pymysql.connect(
    host= os.environ['MYSQL_HOST'],
    user= os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database= os.environ['MYSQL_DATABASE'],
    
)



# Conectando cursor para inserção de SQL
with connection:
    with connection.cursor() as cursor:
        #SQL Aqui dentro de forma simples 
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'ID INT NOT NULL AUTO_INCREMENT, '
            'NOME VARCHAR (50) NOT NULL, '
            'IDADE INT NOT NULL, '
            'PRIMERY KEY (ID)'
            
            ')'
                
        )
    connection.commit()    
    
# Conectando Outro Cursor 

    with connection.cursor() as cursor:
        #SQL Simples com parentes 
        sql= (
            'INSERT INTO {TABLE_NAME} '
            '(Nome,Idade)' 
            'VALUES'
            '(%s,%s) '
        ) 
        
        # SQL com Jason 
        sql2 = (
            {"name": "Sahah","Age": 33,},
            {"name": "Julia","Age": 74,},
            {"name": "Rose","Age": 53,},
            
        )
        
        
        result= cursor.executemany(sql,sql2) # executemany executa tudo
        print(sql,sql2)    
        print(result)
        
        
    connection.commit()    

