# NA Pratica (desempacotador)

"""
Sempre criar o programa principal ( para criar depois a def)
"""
def dobra (lista):
    pos = 0 
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


# Programa Principal 
valores = [3,5,4,8,7,2]
dobra(valores)
print(valores)