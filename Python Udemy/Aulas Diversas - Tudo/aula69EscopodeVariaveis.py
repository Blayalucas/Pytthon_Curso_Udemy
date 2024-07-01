# Escopo de Variavel 

"""
A variavel que está no programa principal ela pode ser usada 
em todas as partes seja dentro do def ou fora do def.
"""
# Exemplo

def teste(b):
    b += 4  # 5 vai ganhar + 4 ou seja será 9 
    c = 2 # aqui será apenas 2 
    print(f"A dentro vale {a}") # O a esta no programa principal, mas pode ser usada em toda parte
    print(f"A dentro vale {b}") # Já b e c pode apenas ser usada dentro do DEF
    print(f"A dentro vale {c}") # ou seja, o que dentro do Def e def o que esta fora pode ser usada em tudo

a = 5
teste(a)

# Vai ate o caderno na aula 69 para aprender