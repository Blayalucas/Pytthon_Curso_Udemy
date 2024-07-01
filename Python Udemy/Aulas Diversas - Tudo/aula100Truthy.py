# Valores Truthy e Falsy, tipos mutáveis e Imutáveis 
# Mutáveis [] {} set()
# imutáveis () "" 0.0.0 None False range (0,10)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = " "
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range (0)

def falsy (valor):
    return "False" if not valor else "truthy"


print(f"Teste", falsy ("Teste"))
print(f"{lista =}", falsy (lista))
print(f"{dicionario =}", falsy (dicionario))
print (f"{conjunto=}", falsy (conjunto))
print (f"{tupla=}", falsy (tupla))
print (f"{string=}", falsy (string))
print (f"{inteito=}", falsy (inteito))
print (f"{flutuante=}", falsy (flutuante))
print (f"{nada=}", falsy (nada))
print (f"{falso=}", falsy (falso))
print (f"{intervalo=}", falsy (intervalo))