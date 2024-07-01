# Field em python 

"""
field é uma função em python que retorna o que "Nos Pedimos" 

neste exemplo pedimos para o Y e Z seja reprentado como falso, 
ou seja, não aparece no terminal.

15 e 25

"""

from dataclasses import dataclass, field, fields

@dataclass
class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr = False, default=10)
    t: int = 20
    

c = C (10, 15,20)
print(c)

# print(fields(c)) - isso mostrar todo o comando tin tin tin no terminal 