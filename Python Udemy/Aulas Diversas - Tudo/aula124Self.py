# Self 

"""
O self parâmetro é SEMPRE referência uma instância atual da classe 
e é usado como complemennto  para chamar as variáveis.

Não precisa ser nomeado self, você pode chamar como quiser, 
mas tem que ser o primeiro parâmetro de qualquer função da classe:

# OBS : Pode ser qualquer nome é o primeira variavel do DEF

Aqui usamos o nome dados

"""

class Person:
  def __init__(dados, name, age):    # primeira variavel é um self aqui é dados
    dados.name = name
    dados.age = age

  def myfunc(dados):
    print("Olá meu nome é  " + dados.name)

p1 = Person("John", 36)
p1.myfunc()