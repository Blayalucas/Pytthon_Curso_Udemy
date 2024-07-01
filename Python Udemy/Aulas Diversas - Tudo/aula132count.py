# count é um iterador sem Fim (itertools)

# intertools é metodo que não vem no python precisa importa-los

"""
Python List count() é uma função embutida em Python 
que retorna a contagem de quantas vezes um determinado objeto 
ocorre em uma List . A função count() 
é usada para contar os elementos de uma lista e também de uma string.

O Count é um interator infinito

"""
from itertools import count

contador = count()   # Ele conta e se fazer um next ele vai contar infinitamente
print(next(contador))