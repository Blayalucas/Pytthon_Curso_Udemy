#Combinations, Permutstions e Product - Intertools
# Combinação - Ordem não importa - iterável = tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores unicos 

"""
Combinations faz combinações entre objetos dentro da variaveis

como é um itertools precisa importa-lo

OBS : A maioria dos itertools é interator.

"""
from itertools import combinations

def print_iter(interator):
    print(*list(interator))


pessoas = [
    'joão', 'Joana','Luiz','Leticia',
]
Camisetas = [
    'pretas', 'branca',
]

print_iter(combinations(pessoas,2)) # Chamando a combinations de pessoas em grupo de 2


