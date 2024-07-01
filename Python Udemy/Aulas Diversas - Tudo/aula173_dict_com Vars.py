# O vars substitui o _dict_




class Pessoa:
    def __init__(self, nome, idade, altura):

        """Método construtor da classe Pessoa"""

        self.nome = nome
        self.idade = idade
        self.altura = altura


# retornando o _dict_ com com metodo vars
pessoa1 = Pessoa('Fulano', 32, 1.86)  

print(vars(pessoa1))