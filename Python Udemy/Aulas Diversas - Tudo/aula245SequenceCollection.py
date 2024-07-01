# Sequence Collection

"""

"""
from collections.abc import Sequence


class MyList:
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
        
    
    def append(self, value):
        self._data[self._index] = value
        self._index += 1
        
        
lista = MyList ()
lista.append("Maria")
lista.append("Carlos")
print(lista._data)
        
        