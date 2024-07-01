# For contador dentro faixa (10)

"""
for i é um contador
in range é uma sacola
então for i in range ()

é contador conta para mim tudo que esta dentro do ()

"""


for c in range(10): # range tem 10 item dentro 
    if c == 2:
        print("c é 2, pulando...")
        continue

    if c == 8:
        print(" i é 8 seu else não executara")
        break # quando chegar até 8 para o programa

# tudo isso é um bloco 

# outro Bloco 

    for i in range(1,3):
        print(c,i)
else: 
    print("For completo com sucesso ")


carros = ["escort", "hb20" , "celta"]

for i in range(len(carros)):  # contador me fala quais item tem dentro da sacola
    print(carros[i]) 