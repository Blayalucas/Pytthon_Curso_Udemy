# Super Classe 3 com MRO

"""
Entendo a Super Classe 

#     A             ou seja, a Classe Mãe A passa para B e C 
#   /   \           o ideal é só fazer A ate C o de fica complicado
#  B --- C
#   \   /
#     D                 MRO basicamente chama tudo para o D 



"""

class A:
    atributo_a = "Eu"
    def metodo (self):
        print('A')
        
        
class B(A):
    atributo_b = "Sou"
    
    
    def metodo (self):
        print('B')
        

class C(B):
    atributo_c = "Lucas"
    
    def metodo (self):
        super(C ,self ).metodo()  # Chamando o Super do metodo C dentro do B
        print('C')


print(C.mro()) # MRO chama tudo paradentro do C