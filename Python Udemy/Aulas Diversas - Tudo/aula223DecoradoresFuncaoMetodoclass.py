# Função decoradora com methodo 


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
        
    # criei ouma função def para informar algo 
    def campeao (self):
        return f" O {self.nome} é o time da inveja o {self.nome} é o time do amor"
        
@adicionar_repr
class Planeta: 
    def __init__(self, nome):
        self.nome = nome

brasil = Time( "Palmeiras")
portugal = Time("Porto")

terra = Planeta ("Terra")
marte = Planeta ("Marte")

print(brasil)
print(portugal)
print(terra)
print(marte)

# print da Def Campeão
print(brasil.campeao())