
# asdict e astuple em Dataclass

"""
Asdict converte para um discionario 
astuple converte em um tupla

"""

from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome : str
    

p1 = Pessoa ("Lucas", "Blaya")
print(asdict(p1))  
print(astuple(p1))