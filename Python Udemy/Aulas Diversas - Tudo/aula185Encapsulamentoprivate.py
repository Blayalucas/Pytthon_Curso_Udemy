# Encapsulamento Private

"""
O metodo private é realizado com Dois underline 

è feito dentro da classe tambem

"""
class Foo:
    def __init__(self):
        self.__private = "Isso é private"
        
        
        
    def metodo_public(self):
        self.__private  # posso colocar ele dentro do publico como privado 
        self.__metodo_private()
        return "metodo_public"
    
  
    def __metodo_private(self):  # posso criar um Def para ele 
        print("__metodo_private")
        return "__metodo_private"

# variavel da Classe
f = Foo()
print(f.metodo_public())


