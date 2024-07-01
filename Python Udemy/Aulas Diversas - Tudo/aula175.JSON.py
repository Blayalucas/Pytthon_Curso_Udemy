# json

"""
Json é uma estrutura de Dados para enviar ou transportar dados. 
vem em formato de "um dicionario" {}

podemos pedi algo no site ou enviar atraves do json 

ou criar um arquivo em formato JSON {}

"""
import json

# Criando arquivo da aula 
CAMINHO_ARQUIVO = "aula.174.json"

# Criando Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
# Variavel pessoa e variavel lista db com Vars

p1 = Pessoa ("João", 33)
p2 = Pessoa ("Carlos", 18)
p3 = Pessoa ( "Ana", 22)
bd = [vars(p1),vars(p2),vars(p3)]

"""
Manipulação do Json no novo arquivo co "w" escrita
jogando ele no novo arquivo com DUMP 

ensure_ascii= False (uni os arquivos de uma pagina a outra)
indent 2 (indenta os arquivos corretamente) as duas paginas
"""
def fazendo_dump ():
    with open(CAMINHO_ARQUIVO, "w") as arquivos:
        print("Fazendo Dump")
        json.dump(bd, arquivos, ensure_ascii=False, indent=2)
    
