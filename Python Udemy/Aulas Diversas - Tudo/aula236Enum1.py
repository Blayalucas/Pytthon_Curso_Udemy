# Enum 

"""
Resumidamente é numeração de alguma coisa, ela tem membros e valores  sempre 
constante não tem fim

Exemplo: 

farol_verde = 1
farol_amarelo = 2 
farol_vermelho = 3

E são representados pelo seguintes comandos:

membro = Classe(valor),Classe["chave"]
chave = Classe.chave.name
valor = Classe.chave.value

"""
import enum

class Season(enum.Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
 
# print o nome da classe +  instacia 
print(Season.SPRING)
 
# print o nome da instancia 
print(Season.SPRING.name)
 
# print o valor da instancia 
print(Season.SPRING.value)
 
# print o type da classe
print(type(Season.SPRING))
 
# print da repr da classe + instancia com o valor incluso tambem 
print(repr(Season.SPRING))
 
# print todas as instacia em formato de list
print(list(Season))