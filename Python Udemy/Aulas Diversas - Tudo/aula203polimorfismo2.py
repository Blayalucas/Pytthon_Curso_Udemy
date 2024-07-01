# Polimorfismo 
"""
Superclasse da Subclasse da Subsubclasse

"""

class Super:
    def hello(self):
        print("Olá, sou a superclasse!")

class Sub (Super): # Sub  recebendo a Super
    def hello(self):
        print("Olá, sou a subclasse!")

class Subsub (Sub): # Subsub recebendo a Sub
    def hello(self):
        print("Olá, sou a subsubclasse!")

teste = Subsub()  # Chamando a Subsub
teste.hello()