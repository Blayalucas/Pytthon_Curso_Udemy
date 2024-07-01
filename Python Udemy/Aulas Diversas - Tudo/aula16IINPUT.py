# A palvra input coleta dados do usuario e pode fazer perguntas 
# A palavra input só retorna para str ou seja palavras não números 
# para fazer ela retornar um numero devemos colocar a pala int antes do input

# exemplo de pergunta sem numeros 

input("Qual seu nome? ") 

nome = input("Qual seu nome? ")
print(f" O seu nome é {nome}")

# exemplo de pergunta com  numeros com o int

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
print(numero_1 + numero_2)