# Metaclasse 3 

# Class Meta - Formula Basica 
class Meta(type):
    def __new__ (mcs,name,base,dct ): 
        print("Metaclass New")
        cls = super().__new__(mcs,name,base,dct )
        return cls
    
    
# Classe " Filha da Meta " Pessoa 
class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    
    def __call__(self, *args, **kwargs ):
        instancia = super().__call__(*args,**kwargs)
        print(" Olá")
        return instancia

# INit da Filha 
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome
        
    def falar(self):
        print(" Falando...")
        
        
p1 = Pessoa ("Lucas")
p1.falar( )
