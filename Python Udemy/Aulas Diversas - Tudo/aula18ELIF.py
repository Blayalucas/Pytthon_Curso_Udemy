# if / se  - Sempre será a primeira condição 
# elif / se não se  - Sempre será a segunda condição (precisa do if)
# else / se não - Sempre será terceira ou a "ultima  opção" atrelada a elif (precisa do if) 

# OBS: olhar os dois : no fim da variavel 

# Entendendo o if elif e  else 

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = True

if condicao1: 
    print("Codigo para Condição 1")
elif condicao2:
    print("Codigo para Condição 2")
elif condicao3:
    print("Codigo para Condição 3")
elif condicao4:
    print("Codigo para Condição 4")
else: 
    print( "Nenhuma condição foi realizada")

# Caso o sistema encontre uma condição verdadeira 
# Ele pula para a proxima fase outro if

condicao5 = False
Condicao6 = True
condicao7 = False

if condicao5: 
    print("Codigo para Condição 5")
elif Condicao6:
    print("Codigo para Condição 6")
elif condicao7:
    print("Codigo para Condição 7")
else: 
    print( "nenhuma condição foi realizada")