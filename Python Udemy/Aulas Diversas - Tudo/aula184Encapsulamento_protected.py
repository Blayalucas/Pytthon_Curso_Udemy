# Encapsulamento Protected

"""
protected = uma underline _underline 

Sempre precisa fazer dentro da classe _init_

Jamais chamar o Print

mas pode chamar uma variavel da classe

"""
class Foo:
    def __init__(self):
        self.public = "Isso é publico"  
        self._protected = "Isso é protegido"
        
        
        self._metodo_protected()  # sempre dentro do init ( jamais fora)
        
        
    def _metodo_protected(self):
        print("_metodo_protected")
        return "_metodo_protected"

# variavel da Classe
f = Foo()