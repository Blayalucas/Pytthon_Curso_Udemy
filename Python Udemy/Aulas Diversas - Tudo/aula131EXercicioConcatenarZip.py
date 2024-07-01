# Concatenar 2 Lista usando zip

""""
Exercicio - Unir lista 

"""



lista_1 = ["Salvador", "São Paulo", "Rio de Janeiro", " Minas Gerais"]
lista_2 = ["BA", "SP", "RJ", "MG","RO"]

for list in zip(lista_1,lista_2):
    print(list)