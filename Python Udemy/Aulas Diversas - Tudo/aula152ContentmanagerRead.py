# Content Manager Read

"""
O Comando Write permite escrever dentro do arquivinho 
enconding = "utf-8" para corrigir erros
"""

caminhos_arquivo = "C:\\Users\\blaya\\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula152.txt' # nomeio como quiser com .txt

with open(caminhos_arquivo, "w", enconding = "utf-8") as arquivo:
    arquivo.write("Linha1\n") # para pular uma linha \n
    arquivo.write("Linha2\n")



# Para ler o arquivo 

with open(caminhos_arquivo, "r") as arquivo: # coloco a letra r 
    print(arquivo.read())