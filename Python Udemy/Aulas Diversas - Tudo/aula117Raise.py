# Raise 

"""
Formas de GERAR excessões na linguagem python 

é usada bastante em biblioteca

"""
def soma(a, b):
    if a < 0 or b < 0:
        raise ValueError("A e B não pode ser negativos")
    
    return a + b

print(soma(10, -2))

#  raise ValueError("A e B não pode ser negativos")
#  ValueError: A e B não pode ser negativos
