# Content Manager With + Open + as 

"""
Com o comando With + Open + as posso criar um arquivo 
abri-lo e fecha-lo e se quiser escrever posso 

"""

caminhos_arquivo = "C:\\Users\\blaya\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula150.txt' # nomeio como quiser com .txt

with open(caminhos_arquivo, "w", enconding = "utf-8") as arquivo:
    print("Olá Mundo")
