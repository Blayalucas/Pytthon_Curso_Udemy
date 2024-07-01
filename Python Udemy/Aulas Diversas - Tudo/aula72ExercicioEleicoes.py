# Eleições com DEf 

"""
Crie um programa que tenha uma função chamada VOTO
que ira receber o parametro Ano de nascimento 
"""

def voto (ano):
    if ano >= 18:
        print(f"A sua idade é {ano} seu voto é OPCIONAL")
    elif ano <= 100: 
        print(f"A sua idade é {ano} seu voto é OBRIGATÓRIO")
    else: 
        print("Seu voto foi NEGADO")

voto = int(input("Digite o ano de seu nascimento: "))