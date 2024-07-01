# Função Decoradora class com Função repr 

"""
A ideia da decorador classe com função repr é fazer uma 
função DEF que recebe uma class e dentro dessa função 
tem outro Def com self e o padrão basico do repr
    
"""


# Passo 1 = Função Def que recebe a class e dentro outra função DEf com self
def adicionar_repr(cls):
    def meu_repr(self): 
        class_name = self.__class__.__name__    # Atributos 
        class_dict = self.__dict__
        class_repr = f"{class_name}({class_dict})"
        return class_repr
    cls.__repr__  = meu_repr   # Class repr recebe Def Self
    return cls # retorna class


@adicionar_repr
class Time: 
    def __init__(self, nome):
        self.nome = nome
        
        
@adicionar_repr
class Planeta: 
    def __init__(self, nome):
        self.nome = nome

brasil = Time( "Brasil")
portugal = Time("Portugal")

terra = Planeta ("Terra")
marte = Planeta ("Marte")

print(brasil)
print(portugal)
print(terra)
print(marte)