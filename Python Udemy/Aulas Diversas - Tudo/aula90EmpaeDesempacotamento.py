# Empacotamento e desempacotamento de dicionário

# Você pode pegar peças internas dentro do dicionario

"""
utilizando parametros onde a vale 'nome ' e o b "Aline " ou seja, 
adjetivo e sujeito
"""

pessoas = {'Nome':"Aline",
'Sobrenome': "Souza",
}

a, b = pessoas.values()
print(a,b)

a, b = pessoas.items()
print(a,b)

a, b = pessoas.keys()
print(a,b)



