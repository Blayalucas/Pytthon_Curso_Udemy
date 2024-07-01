# _init_

"""
Todas as classes DEF possuem uma função chamada __init__(), 
que sempre é executada quando a classe está sendo iniciada.

Use a função __init__() para atribuir valores 

Crie uma classe chamada Person e crie uma DEF com __init__() 

para atribuir valores para nome e idade

"""

class Person:
  def __init__(self, name, age):   # Def tem init 
    self.name = name  # chamando o self do nome
    self.age = age

p1 = Person("John", 36)  # p1 vai receber person e seus adjetivos

print(p1.name)
print(p1.age)