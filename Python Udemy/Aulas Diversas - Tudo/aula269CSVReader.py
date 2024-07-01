# CSV.Reader

"""
Retorna um objeto leitor do  csvfile fornecido. 

"""
import csv
from pathlib import Path

# 1 Passo - Abrir um caminho 

CAMINHO_CSV = Path(__file__).parent / 'aula269CSVReader.csv'

# 2 Passo - abrir um arquivo, com formarto de leitura "r"

with open(CAMINHO_CSV,'r') as arquivo:
    leitor = csv.reader( arquivo)
    
    
    print(next(leitor))
    
# 3 Passo - criar um laço (For)

    for linha in leitor:
        print(linha)

