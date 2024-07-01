# Dir, hasattr , getattr em python

"""
O hassattr é um " rastreiado" ou " buscador dentro do programa ao dar print
se existe tal informação 
"""

class person:    # Fiz uma classe person e inseri informações 
    age = 23
    name = "Adam"

person = person ()  # variavel que irá receber tupla "person" 

print("person`s age:", hasattr(person, "Age")) # person Age existe dentro da classe?
print("person`s salario:", hasattr(person, "Salario")) # person salario existe dentro da classe?