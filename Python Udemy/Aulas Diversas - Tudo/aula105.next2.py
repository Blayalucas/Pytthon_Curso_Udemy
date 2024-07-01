# Iterators

"""
iterator ou next a função dele " objetivo" é entregar o proximo valor

ou seja, ele pula de casa em casa buscando dentro do iterable

ele sabe o começo mas não sabe o final 

# se tiver no primeiro elemento ele entrega o primeiro elemento

"""

iterable = ['Eu', 'tenho', '_iter_']

iterator = iterable.__iter__()  # pode fazer iterator = iter(iterable)
# iterator = iter(iterable)  # mesma coisa

print(next(iterator))




