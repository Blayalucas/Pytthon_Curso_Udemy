# Try com except e com Else e Finally


# exemplo try le para mim
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
    
# se tiver errado escreve na tela XXXXX
except: 
    print("Infelizmente temos um problema")

# se der Certo print else
else:
    print(" o resultado é {r:.2f}")