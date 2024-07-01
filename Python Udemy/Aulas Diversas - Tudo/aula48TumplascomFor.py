# tumplas com For 

lanches = ("Hamburguer", "Suco", "Pizza", "Pudin" )

# para cada comida in lanche
for comida in lanches: # for repeti até que todos os lanches seja comidos
    print(f"Eu vou comer {comida}")



# ou pode fazer colocar posicao e inumerar

lanches = ("Hamburguer", "Suco", "Pizza", "Pudin" )
for pos, comida in enumerate(lanches):
    print(f"Eu vou comer {comida} na posicão {pos}")
print("Comi para caramba")

# ou fazer contador

for c in range (0,len[lanches]):
    print(f"Eu vou comer {lanches [c]}  na posição[c]")
print("Comi para caramba")