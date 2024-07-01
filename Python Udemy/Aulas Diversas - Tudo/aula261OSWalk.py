# Os.walk     

"""
é uma função que permite percorrer uma estrutura de diretórios de 
maneira recursiva, ou seja vai entrar pasta por pasta gerando uma sequencia de Tuplas 

tres elemtos existem: O diretorio (root), lista de Subdiretórios ( dirs)
e uma lista dos arquivos de diretórios atual ( files)
"""   


import os 

caminho = os.path.join ("/Users", "blaya", "OneDrive", "Área de Trabalho")

for root, dirs, files in os.walk (caminho):
    print(caminho)
                        