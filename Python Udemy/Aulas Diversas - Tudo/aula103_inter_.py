# Generator expression, Iterables e Iterators
"""
Iterables ou "_iter_" no Python é iteravel 
um tipo de objeto que possibilita a ação de repetição sobre seus elementos, 
como listas e strings.

No Python, um objeto é considerado iterável se ele implementa 
o método __iter__, permitindo, por exemplo, que um loop FOR seja 
executado sobre ele.

OBS: Se ela for iteravel da para fazer um for NÂO É iterador

Podemos fazer o seguinte comando. 
"""


lista = [0,1,2,3,4,5]

print(hasattr(lista, '_iter_'))  # localizando um _iter_ dentro da lista

for c in lista:    # contando o que tem na lista
    print(c)

lista = [0,1,2,3,4,5]
lista = iter(lista)
print(hasattr(lista, '_next')) 

