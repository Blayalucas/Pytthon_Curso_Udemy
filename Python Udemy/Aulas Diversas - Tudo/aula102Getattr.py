# Dir, hasattr , getattr em python

"""
O getattr é um " rastreiado" ou " buscador" dentro da class um atributo 

"""


class Student:    # Fiz uma classe student  e inseri informações
  marks = 88
  name = 'Sheeran'

person = Student()   # variavel que recebe a class ()

name = getattr(person, 'name')  #  variavel , localizador dentro da class
print(name)         

marks = getattr(person, 'marks') #  variavel , localizador dentro da class
print(marks)

# Output: Sheeran
#         88