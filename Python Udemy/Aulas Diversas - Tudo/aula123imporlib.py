# importLib /singleton

"""
Quando importo um modulo o python já salva na memoria

O python só importa 1 vez para carregar ele novamente faz 

import imporlib
"""
import importlib

import aula122Modularização

for i in range(10):
    importlib.reload(aula122Modularização)
    print(i)



