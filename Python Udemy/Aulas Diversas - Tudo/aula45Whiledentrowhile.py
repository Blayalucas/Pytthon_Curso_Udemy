# While dentro de While 

qtd_linhas = 5 
qtd_colunas = 5

linha = 1 # contador 
coluna = 1 # Contador
while linha <= qtd_linhas: 
    while coluna <= qtd_colunas: # isso igual uma engrenagem grande e uma pequena
        print(f"{linha=} {coluna=}")
        coluna += 1 # loop do while de dentro 
    linha += 1  # loop do while de fora 
print("Fim")