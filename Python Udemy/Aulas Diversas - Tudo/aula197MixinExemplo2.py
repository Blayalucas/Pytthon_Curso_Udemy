# Mixin 
# Parte 2 

from log import logPrintmixin

class Eletronico:
    def __init__(self,nome):
        self._nome = nome 
        self._ligado = False 
        
    
    def ligar (self):
        if not _ligado:
            self._ligado = True
        
        
    def desligado (self):
        if not _ligado:
            self._ligado = False
    
class Smartphone(Eletronico, logPrintmixin):
    def ligar(self):
        super().ligar()
        
        if self._ligado: 
            self._ligado = False
            
            
        
    def desligar(self):
        super().desligar()
        