# CSV. DictWinter

"""
Com essa Comando podemos escrever colunas e criar um dicionario, 
ou seja, um " Json dentro da Listas [] " estilo excel"

"""

# 1 Passo - Chamar e importar biblioteca 
import csv
from pathlib import Path

# 2 Passo - Criar um caminho caminho no PC 
CAMINHO_CSV = Path(__file__).parent / 'aula271DictWinter.csv'

# 3 Passo - Criar uma Instancia com lista e dicionario 
lista_clientes = [
    {'Nome': 'Lucas Blaya ', 'Endereço': 'Vila Formosa'},
    {'Nome': 'Pedro Cardoso ', 'Endereço': 'R. X, "1000"'},
    {'Nome': 'Maria Bonita', 'Endereço': 'Av. Drumont , 3A'},
]

# 4 passo - abrir o arquivo em forma de 'W' e criar coluna e dados 
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()


# 5 Passo - Fazer um for 
    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)