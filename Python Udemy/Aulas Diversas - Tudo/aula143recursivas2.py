# recursa 

"""
Recursiva  no fatorial

# 5 = 5*4*3*2*1 = 120
# 3 = 3*2*1 = 6
# 4 = 4*3*2*1 = 24

Fatorial de um numero qualquer será 
essa formula: 

n * fatorial (n-1) vai fazer um loop sempre

exemplo:

fat(3) = 3 * fatorial(2) 
fat(2) = 2 * fatorial(1)
fat(1) = 1

"""
# # Caso base ou forma basica
def fatorial (n):
    if n == 0 or n == 1:  # Caso base ou forma basica
        return 1
# Caso Geral 
    return n * fatorial (n-1)  # formula para todos os numeros

print(fatorial(0))
print(fatorial(1))
print(fatorial(4))
print(fatorial(5))
print(fatorial(20))
print(fatorial(82))