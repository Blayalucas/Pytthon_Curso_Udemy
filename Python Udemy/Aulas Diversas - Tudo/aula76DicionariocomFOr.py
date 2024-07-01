# Dicionario com o for 

"""
pessoas = {'nome':"Gustavo", 'sexo':"M", 'idade':"22"}
for k, v in pessoas.items():
    print(k,v)

# Ele irá contar ou informar tudo que tem na sacola(items)


"""

estado = dict ()  # dicionario {}
brasil = list () # lista []
for c in range (0,3):  
    estado["UF"] = str(input("Nome do Estado: "))
    estado["Sigla"] = str(input("Sigla Federativa: "))
    brasil.append(estado.copy()) # brasil"list" vai receber a copia de tudo que foi digitado pelo usuario
for e in brasil:
    for v in e.items():   
        print(v) 