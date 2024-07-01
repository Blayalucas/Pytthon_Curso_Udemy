# Abspath         

"""
É um caminho absoluto que trás o arquivo da raiz até aqui 
no Vs Code __file__ fazendo tudo em letras maiusculas

"""
import json
import os

# 1 Passo - Criar o Caminho do arquivo

NOME_ARQUIVO = 'aula267.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
        
    )
        
)

print(__file__)
# caso queira saber o nome da pasta fazer: print(os.path.dirname(__file__))

# 2 Passo - Criar um Json
string_Json = '''

{
    "title": "Velozes e Furiosos ",
    "original_title": "Fast & Furious ",
    "is_movie": true,
    "imdb_rating": 6.8,
    "year": 2001,
    "characters": ["Toreto", "Letty", "Brian", "Mia", "Han", "Roman"],
    "budget": null
    
}
'''

# 3 Passo - Chamar o arquivo em modo de escrita 'W'

with open (CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivos:
    json.dump(string_Json, arquivos, ensure_ascii=False,indent=2)
    
    
# 4 Passo - Abrir o arquivo em formato { biblioteca } em leitura "R"
with open (CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivos:
    filme_do_json = json.load(arquivos)
    print(filme_do_json)