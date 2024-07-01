# Mapeamento de list comprehension

produtos = [
    {'nome': "P1", 'preco' : 20},
    {'nome': "P2", 'preco' : 40},
    {'nome': "P3", 'preco' : 80},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto ['preco'] > 20 else {**produto}  for produto in produtos
]

print(*novos_produtos)