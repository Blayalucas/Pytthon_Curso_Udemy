# __New__ & __Init__

"""
O __init__ inicia uma classe ( Um programa)
O __new__ele cria um novo metodo 
"""

class A: 
    def __init__(self):
        print(" Eu sou o Init")
        
    def __repr__(self):
        return "A"
        
a = A()


"""
O __new__ele cria um novo metodo 
"""

class B: 
    def __new__(cls):
        return super().__new__(cls)