# Content Manager - open com Modos "modulos"

"""
Em Python existe comandos ou modos para abrir e manusear arquivo são eles:

Open() para abrir o arquivo
close() e obrigatorio criar um fechamento 

r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binario)
t (modo texto), + (leitura e escrita)

OBS: O + tem o puder de fazer o modo leitura e escrita juntos 

Exemplo: 
r+ você vai ler todo texto
w+ vc vai pode escrever 
enconding = "utf-8"

"""
caminhos_arquivo = "C:\\Users\\blaya\OneDrive\\Área de Trabalho\\Arquivo_Python\\"
caminhos_arquivo += 'aula148.txt' # nomeio como quiser com .txt

arquivo = open(caminhos_arquivo, "w") # criando um arquivo novo dentro da pasta


arquivo.close()  # fechamento de arquivo 
