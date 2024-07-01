# _dict_ 

"""
_dict_ é um dicionario que retorna as informações dentro do DEF 
def __init__(self, nome, idade, altura)

porém precisa de uma variavel da classe com as informações

neste exemplo retorna fulano, 32, 1.86

"""

class Pessoa:
    def __init__(self, nome, idade, altura):

        """Método construtor da classe Pessoa"""

        self.nome = nome
        self.idade = idade
        self.altura = altura


# retornando o _dict_
pessoa1 = Pessoa('Fulano', 32, 1.86)  

print(pessoa1.__dict__)