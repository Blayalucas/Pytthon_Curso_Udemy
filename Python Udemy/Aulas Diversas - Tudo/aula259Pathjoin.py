# os.path     

"""
os.path é um modulo que fornece funções para trabalhar com caminho de arquivos 

# os.path join: ele junta todos os arquivo em um unico arquivo. 

'pasta1\\pasta2\\arquivo.txt'  - ou seja o caminho dentro do windows

# os.path.split: coloca uma tupla  (diretório, arquivo).

os.path.split(''pasta1\\pasta2\\arquivo.txt'')

# os.path.exists: verifica se um caminho especificado existe.

OBS: LEMBRE-SE Sempre usar a Barra Duplas no WINDOWS

"""

import os 


# Passo 1 - criando um caminho qualquer - join
caminho = os.path.join ('C:\\Users\\blaya\\OneDrive\\Área de Trabalho')
print(caminho)

# Passo 2 - dividindo arquivo em  (diretório, arquivo) - coloca " "
print(os.path.split(caminho))

# Passo 3 - Verifica se o caminho existe - True ou False

print(os.path.exists(caminho))
