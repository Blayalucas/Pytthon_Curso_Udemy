# Dataclasses com Propert e Setter 

"""
É um modulo que fornece um decorador e funções para criar classe

_init_(), _repr_(), _eq_() entre outros 
""" 

from dataclasses import dataclass

@dataclass
class Pessoa: 
    nome: str
    idade: int
    sobrenome: str
    
    @property
    def nome_completo(self):
        return f"{self.nome}{self.sobrenome}"


    # Setter Muda o nome de Lucas para Maria Helena
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = "".join(sobrenome)


p1 = Pessoa("Lucas",36,"Blaya")
#p1.nome_completo = 'Maria Helena'
print(p1)
print(p1.nome_completo)
    
    