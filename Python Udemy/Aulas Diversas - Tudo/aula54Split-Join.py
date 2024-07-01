# . split, join e strip são métodos muito úteis da str

"""
analise de Str. 

São elas 
"""

frase = "Quando surge o alviverde imponente"
print(len(frase));  # comprimento da frase 
print(frase.count("a")); # Contador de Letras na frase
print(frase.find("m")); # Conta quantas vezes ele encontra a palavra
print("Quando" in frase); # ele informa se a palavra esta na frase
print(frase.replace("Quando" ,"enquanto")); # substitui a palavra por outra
print(frase.upper()); # deixa as palavras em Maiusculo
print(frase.lower()); # deixa as palavras em Minusculo
print(frase.title()); # deixa as PRIMEIRAS palavras em Minusculo
print(frase.strip()); # ela corta os espaço da frase 
print(frase.lstrip()); # ela corta os espaço da frase lado esquerdo
print(frase.rstrip()); # ela corta os espaço da frase lado direito
print(frase.split()); # Coloca a frase em listas ["Quando," Surge" , "o","alviverde", "imponente" ]
print("-".join(frase)); # coloca traço em cada Palavra Q-u-a-n-d-o



