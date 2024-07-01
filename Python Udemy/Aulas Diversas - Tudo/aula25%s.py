# """
# Interpolação básica de strings 
# s - string 
# d e i - int
# f - float
# x e X Hexadecimal (ABCDEF0123456789)
# Casa decimais :,.2f
# """

nome = "Lucas"
preco = 1000.95897643
variavel = "%s, o preço é R$%.2f" %(nome, preco)
print (variavel)

# Você pode substituir a variavel colocando 
# % e identificando se é uma str ou float ou int
# neste caso nome é uma str então %s
# preço é um float %. quantas casa decimais %.2f por ser um float
# termina o codigo usando "" e declara as variaveis 
# % (nome, preco)

