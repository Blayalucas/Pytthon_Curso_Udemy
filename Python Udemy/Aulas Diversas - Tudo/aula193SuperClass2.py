# Super Classe 2 

"""
Entendo a Super Classe 

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



c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()