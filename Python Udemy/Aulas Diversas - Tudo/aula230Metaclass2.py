"""
Metaclasses são magias mais profunda do que 99% dos usuarios
deveriam se aprofundar. Se você quer saber se precisa delas, 
não precisa (as pessoas que realmente precisam delas sabem com 
certeza que precisa dela e não precisam de uma explicação sobre 
o porquê)


"""

# Class Mãe Meta  que cria as classes = Formula Basica 
class Meta(type):
    def __new__ (mcs,name,base,dct ): 
        print("Metaclass New")
        cls = super().__new__(mcs,name,base,dct )
        return cls
    
    
# Aqui nesse exemplo Pessoa é a " class  Filha  " da meta 
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

# Aqui é o Init da Class Filha 
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

