# Content Manager Writelines

"""
O Comando W + escrever varias linhas  dentro do arquivinho 
enconding = "utf-8" para corrigir erros
"""

caminhos_arquivo = "C:\\Users\\blaya\\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula154.txt' # nomeio como quiser com .txt

with open(caminhos_arquivo, "w+", enconding = "utf-8") as arquivo: # comando W+ 
    arquivo.writelines(
        ("Olá Mundo\n", "Hoje eu acordei Feliz\n")
    )
    arquivo.seek(0,0)  # move o curso dentro do arquivo "importante"
    print(arquivo.read())
