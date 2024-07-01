# Polimorfismo 

"""
É a capacidade do programa identificar e saber qual metodo com nome iguais 
está sendo usado o da Superclasse ou Subclasse.
O objeto tem capacidade de assumir diversar formas ( polimorfismo)

Exemplo: 

Vamos criar a classe Superclasse e uma Subclasse que tem apenas um método, 
o hello(). Instanciamos ( função ) um objeto e chamamos  esse método.

"""
# Super Classe ( passo 1) 
class Super:
    def hello(self): # função - Metodo Hello 
        print("Olá, sou a superclasse!")
        
# Subclasse ( passo 2)
class Sub (Super): # Subclasse recebendo a super classe 
    def hello(self): # função - metodo
        print("Olá, sou a subclasse!")

teste = Sub()   # chamando o Metodo Subclasse ( neste caso) - ( passo 3 )
teste.hello()