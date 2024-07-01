# Classmethod

"""
Classe com metodo ou classmethod "CLS"

è um metodo para criar classes

"""

class Pessoa:
    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    @classmethod
    def methodo_de_class(cls):
        print("Hey")
        
    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)
    
p1 = Pessoa ("João, 34")
p2 = Pessoa.criar_com_50_anos("Helena")

print(p2.nome,p2.idade)