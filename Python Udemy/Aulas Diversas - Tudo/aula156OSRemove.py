# |os.remove ou unlink - apaga os arquivos

"""
Para apagar tudo 
importo o OS
"""
import os

caminhos_arquivo = "C:\\Users\\blaya\\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula156.txt' # nomeio como quiser com .txt

with open(caminhos_arquivo, "w+", enconding = "utf-8" ) as arquivo: # comando W+ 
    arquivo.writelines(
        ("Olá Mundo\n", "Hoje eu acordei Feliz\n", "Treinei e estudei\n")
    )
    arquivo.seek(0,0)  # move o curso dentro do arquivo "importante"
    print(arquivo.readlines())

# para remover arquivo serve um ou outro 
os.remove(caminhos_arquivo)

os.unlink(caminhos_arquivo)

# para renomear o arquivo 

os. rename(caminhos_arquivo, " Aula1000.txt")
