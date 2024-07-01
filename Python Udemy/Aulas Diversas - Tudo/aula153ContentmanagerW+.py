# Content Manager W+

"""
O Comando W + escrever mais dentro do arquivinho 
enconding = "utf-8" para corrigir erros
"""

caminhos_arquivo = "C:\\Users\\blaya\\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula153.txt' # nomeio como quiser com .txt

with open(caminhos_arquivo, "w+", enconding = "utf-8") as arquivo: # comando W+ 
    arquivo.write("Linha1\n") 
    arquivo.write("Linha2\n")
    arquivo.seek(0,0)  # move o curso dentro do arquivo "importante"
    print(arquivo.read())
