# os.path.getsize 

"""
os.path.getsize() O método em Python é usado para verificar o tamanho do caminho especificado. 
Ele retorna o tamanho do caminho especificado em bytes. 
O método gera OSError se o arquivo não existir ou estiver de alguma forma inacessível.

"""

    
# import modulo
import os

# caminho
path = "C://Users//blaya//OneDrive//Área de Trabalho//Curso_Python_Udemy"

# tamanho do caminho   
pathsize = os.path.getsize(path)

# Print the size (in bytes)
# of specified path 
print("Tamanho do Bytes", pathsize)