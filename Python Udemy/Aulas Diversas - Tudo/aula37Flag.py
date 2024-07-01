# """"
# Flag ( Bandeira) - Marcar um local 
# None = não valor ( o None é bastante usado com is )
# exemplo : variavel is None
# exemplo: variavel is not 
# is e is not = é ou não é ( tipo, valor, identidade)
# id = Identidade 
# """"

v1 = "a"
v2 = "a"
print(id(v1))
print(id(v2))

condicao = False 
passou_no_if = None

if condicao: 
    print("Faça algo")
else: 
    print ("Não faça algo")