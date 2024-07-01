# Json em Dump 

"""
Podemos usar nossa classe e criarmos um Dump (jogar o arquivo para fora )
    
"""

import json
from pprint import pprint
from typing import TypedDict


# 2 Passo - Criar uma classe com todas as informações e descriminando cada coisa
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None
    
# 1 Passo - Criar um Json 
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
# 3 Passo = Receber a Classe
Movies: Movie = json.loads(string_Json)
print(Movies)

movie_dump = json.dumps(Movies, ensure_ascii=False,indent=2)
print(movie_dump)