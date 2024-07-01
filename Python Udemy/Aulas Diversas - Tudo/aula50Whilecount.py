# While com contador - count

frase = " O Rato esta no Buraco para comer queijo"

i = 0 # contador
qtd_apareceu_mais_vezes = 0 # vai iniciar com 0
letra_apareceu_mais_vezes_atual = " "


while  i < len(frase):  # contador menor que a frase 
    letra_atual = frase [i]  # letra atual vai receber a frase inteira com o contador
    qtd_letra = frase.count(letra_atual) # vai receber contador cada palavra
    
    if qtd_apareceu_mais_vezes < letra_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = letra_apareceu_mais_vezes_atual  # condição 
        letra_apareceu_mais_vezes_atual = letra_atual
    
    i += 1  # loop de uma volta

print(
    "A letra que apareceu mais vezes foi"
    f"{letra_apareceu_mais_vezes_atual} que apareceu"
    f"{qtd_apareceu_mais_vezes} X"
)