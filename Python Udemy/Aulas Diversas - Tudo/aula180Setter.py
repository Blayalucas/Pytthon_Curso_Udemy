# Setter 

"""
Setters : Estes são os métodos usados no recurso OOPS 
que ajuda a definir o valor de atributos privados em uma classe

OBS: se você ve um self._cor é que o programador pediu para nã pudar nada ali.
"""


class Caneta:                  
    def __init__(self, cor):
        # private protected
        self.cor = cor 
        
        
    
    @property 
    def cor (self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print("Estou no Setter")
        self._cor = valor
        

caneta = Caneta("Azul")
caneta.cor = "Rosa"

print(caneta.cor)
