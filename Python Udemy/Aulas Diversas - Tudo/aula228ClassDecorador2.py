# Classe Decoradora continuação 

"""

    
"""


# Passo 1 - Fazer uma classe inserindo um multiplicador

class Multiplicar: 
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10
        
    
    def __call__(self,*args,**kwds):
        resultado = self.func (*args,**kwds)
        return resultado + self.multiplicador 
        

# Passo 2 - Chamar o Decorador 
@Multiplicar 
def soma (x,y):
    return x + y

# Chamar a Instancia 
resultado = soma (2,4)
print(resultado)
