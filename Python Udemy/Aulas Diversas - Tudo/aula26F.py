# """
# Formatação basica de strings
# s - string
# d - int
# f - float
#.<número de digitos >f
# x ou X - Hexadecimal 
# (Caractere) (><^) ( quantidade)
# > - Esquerda 
# < - Direita 
# ^ - Centro 
# Sinal - + ou - 
# Ex. : 0 > 100, .1f
# Conversion flags - !r !s !a
# """
variavel = "ABC"
print (f"{variavel}")
print(f"{variavel: >10}.")
print(f"{variavel: <10}.")
print(f"{variavel: ^10}.")
print(f"{10000.4873648123746:, .1f}")

# Ou seja você pode utilizar espaçamentos contando casas 
# (para o lado direito, esquerdo e centro)
