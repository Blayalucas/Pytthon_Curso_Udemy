# Problema dos parametros mutáveis em Python 

"""
Caso for criar uma Lista em DEF Fazer isso SEMPRE

def XXX (nome, lista=None):
    if lista is None: 
        Lista = []
    Lista.append (nome)
    return Lista 

Deste modo posso acrescentar nome na lista sem erro. 
"""

def adiciona_clientes (nome, lista=None):
    if lista is None: 
        lista = []
    lista.append (nome)
    return lista 

# Duas Lista

cliente1 = adiciona_clientes ("Luiz")
adiciona_clientes ("Joana", cliente1)



cliente2 = adiciona_clientes ("Helena")
adiciona_clientes ("Bruna", cliente2)

print(cliente1)
print(cliente2)