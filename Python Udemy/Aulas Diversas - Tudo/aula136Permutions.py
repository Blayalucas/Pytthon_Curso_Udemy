# Permutação - Ordem importa

""""
Ela basicamente é um combinação,porém informa todos os nomes 
aleatoriamente combinados.

"""

from itertools import combinations, permutations

def print_iter(interator):
    print(*list(interator))


pessoas = [
    'joão', 'Joana','Luiz','Leticia',
]
Camisetas = [
    'pretas', 'branca',
]

print("Combination") # identificar o que combination 
print_iter(combinations(pessoas,2)) # Chamando a combinations de pessoas em grupo de 2
print("Permutation")
print_iter(permutations(pessoas,2))

