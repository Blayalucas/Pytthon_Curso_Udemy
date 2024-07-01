
# Media Idade " while"

""""
Faça um programa para ler a media de idades usando While
quantidade de alunos
"""

qtd = int(input("Quantidade de Alunos: "))
i = 0 # contador iniciara apartir do Zero 
soma = 0 # iniciara apartir do Zero 

while i < qtd:
    idade = int(input("Digite a idade : "))
    soma_idade = soma_idade + idade 
    i += 1   # loop
media = soma_idade / qtd
print(f" A Média das idades é: {media:,.2f}")