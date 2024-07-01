# Operadores Logicos 
# and (e) or (ou) not (não)
# and - todas as condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso, 
# a expressão inteira será avaliada naquele valor 
# são considerados false ( que você já viu )
# 0 0 0 '' False 
# também existe o tipo NONE que é 
# usado para apresentar um não valor 

# exemplo: 

entrada = input(" [E]ntrar [S]air: ")
senha_digitada = input ("Senha numérica:  " )
senha_permitida = "123456"

# OBS:  o if só vai dar certo se for  TRUE "Entrar" se não vai dar Sair
# a expressão and serve para dar continuidade no 
# programa ou seja uma nova condição


if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")

else: 
    print("Sair")

# Se o usuario digitar qualquer número sem ser o 123456 vai cair no sair


print (True and True and True)   # o python vai printar o resuldado verdadeiro 

print( True and False and True)  # o python considera o resuldado Falso 
# ou seja se aparecer 1 False e tiver 10 True
# # o python considera sempre Falso

# Essa parada no python da o nome de "Avaliação de curto circuito"




