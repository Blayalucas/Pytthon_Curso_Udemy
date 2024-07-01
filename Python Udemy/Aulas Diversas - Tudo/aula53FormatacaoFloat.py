"""
Formatação de numeros Flutuantes
Double-precision float-point format IEEE 754

# round é uma função para colocar casas descimais
print(round(variavel, numero casa descimal))

print(round(numero_3,2)) # exemplo

"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f"{numero_3:,.2f}")
print(round(numero_3,2))
    
