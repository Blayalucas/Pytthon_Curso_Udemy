# Raise 2 

# Exemplo

def não_aceita_zero (d):
    if d == 0:
        raise ZeroDivisionError (" Você está tentando dividir por 0 ")
    return True

def divide(n,d):
    não_aceita_zero (d)
    return n/d

print(divide(8,0))