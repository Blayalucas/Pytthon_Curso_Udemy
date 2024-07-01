# Def com if - par ou impar 

def par(n=0): # se não passar nenhum numero ele é 0
    if n % 2 == 0: # se o numero divido por 2 é igual a 0
        return True 
    else: 
        return False
    

num = int(input("Digite um numero: "))
print(par(num))