# _dict_ exemplo 

"""
Neste caso ele esta pegando a informação passada na variavel 

ou seja, Carla referente ao nome, idade não foi informada e altura criada


"""

class Pessoa: 
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento (self):
        return Pessoa.ano_atual - self.idade


# retornando o _dict_    
p1 = Pessoa("Carla", 1.86)

print(p1.__dict__)
# {'nome': 'Carla', 'idade': 1.86}
        