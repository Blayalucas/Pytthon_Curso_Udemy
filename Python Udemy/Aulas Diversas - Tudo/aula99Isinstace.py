# isinstace

"""
OBS: Importante sempre manter os dados em padrão
Se tiver uma lista de numeros deixa só numeros 
se tiver string deixa string e assim deixar tudo padronizado

Se deixar misturado pode ser ruim

# insistance é uma função

"""

lista = [
    "a", 1, 1.1, True, [0,1,2], (1,2),
    {0,1} , {"Nome" : "Luiz"},

]
for item in lista:
    print(item, isinstance (item, set))