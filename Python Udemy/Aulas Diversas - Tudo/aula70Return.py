# Retorno de Valores - return

"""
O return é tipo um loop de variaveis, ou seja 
se no programa principal tiver 4 ou 10 variais vai sempre retornar e da
resultado
"""
# exemplo 
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s  # loop 

variavel1 = somar(3,2,5) # vai somar essa resultado 10
variavel2 = somar (1,7) # resultado 8
variavel3 = somar (4) # resultado 4

print(f"Os resultados são: {variavel1},{variavel2} e {variavel3}.")