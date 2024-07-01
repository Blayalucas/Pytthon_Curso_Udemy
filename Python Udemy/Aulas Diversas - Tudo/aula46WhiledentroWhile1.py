
qtd_linhas = 5 
qtd_colunas = 5

linha = 1 # contador 
coluna = 1 # Contador
while linha <= qtd_linhas: 
    while coluna <= qtd_colunas: # isso igual uma engrenagem grande e uma pequena
        coluna += 1 # loop do while de dentro " coluna"
        print(f"{linha=} {coluna=}")
    linha += 1  # loop do while de fora "linha"
print("Fim")