# Fazer um programa que contenha 
"""
Colete o CPF:
Colete a soma dos 9 primeiro digito
Multiplique cada um dos valores 
resto da divisão

Se o resultado anterior for maior que 9:
    resultado é 0 
Contrario disso: 
    
"""
cpf = int and float(input("Digite o número do seu CPF: "))
soma_CPF =  cpf + cpf
mult_10 = soma_CPF * 10
div_resto = mult_10 % 11
print(soma_CPF)
print(mult_10)
print(div_resto)
if div_resto > 9:
    print("Resultado é 0")
else: 
    print(" Resultado é o valor da Conta")



