# Positional - only 

"""
Positional -only  ou / = é um " divisor" para bloquear variaveis 
dentro de uma DEF 

Exemplo: 

def soma (x,y ) - ele vai somar apenas as informações referente a X e y 
ou seja, caso queira mudar as letras durante o codigo vai dar erro.
Com a / você pode bloquear o x e y e utilizar outras letras variais

def soma (x,y \ a,b) agora podemos usar mais informações dentro do Def

"""

def soma(a,b, /, x,y): 
    print(a + b + y + x )

soma(1, 2, 3, 9 ) # 15 

