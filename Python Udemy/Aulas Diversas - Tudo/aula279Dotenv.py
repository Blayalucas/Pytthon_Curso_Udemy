# Modulo Dontev 

"""
É um modulo que fica na raiz do Computador, para chamarmos necessitamos
criar um arquivo .env igual um arquivo .csv na base do VScode

Olhar o arquivo das aulas

"""

import os 

from dotenv import load_dotenv #type: ignore

load_dotenv()

print(os.getenv('BD_PASSWORD'))

