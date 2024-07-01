# Quando você criar as variaveis e for escrever o texto
# escreva ele a frase texto enfim 
# por linha colocando as variantes e o texto com "" no inicio e fim
# exempo: f"Você {acordo} hoje e abriu a {janela} que tem {altura:.2f}"
# essa f  na frente da frase significa que você pode colocar 
# as variaveis em  chaves{} e esse :.2f significa que vc pode colocar 
# 2 casas decimais  para fazer altura, peso, tamanho etc. 

# ou seja "f-strings" é {} na variaveis e 
# :.2f duas casas descimais nas continhas exemplo: 1.80 

nome = "Luiz Otávio"
altura = 1.80
peso = 95
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f"{nome} tem {altura:.2f} de altura,"
linha_2 = f"pesa {peso} quilos e seu imc é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)