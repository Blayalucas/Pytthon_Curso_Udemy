# Try except com variavel 

"""
Você pode criar uma variavel dentro do exception
para mostrar o erro "real"

# usando o (as) variavel

"""

try: 
    a = 18
    b = 0
    c = a /b
except SyntaxError as v:  # criei uma variavel para o erro 
    print(v)
