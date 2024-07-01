# Json Loads + pprint

"""
Loads convert uma str em python para "Strings", ou seja, 
convert tudo em python para Json e para isso ocorrer 
você import o pprint para o VScode 

"""

import json
from pprint import pprint

# 1 Passo - criar uma Variavel "com comentário" e jogar o arquivo dentro  
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

# 2 Passo - uma Instância que recebe todo a Strings
Movies = json.loads(string_Json)
pprint(Movies)