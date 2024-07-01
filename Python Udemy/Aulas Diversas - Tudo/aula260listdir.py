# Listdir

"""
Navegar por caminhos 
"""
import os 

caminho = r"'C:\\Users\\blaya\\OneDrive\\Área de Trabalho"

for item in os.listdir(caminho):
    print(item)