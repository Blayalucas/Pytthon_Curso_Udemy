# GROUPBY - Agrupar Valotes (itertools)

"""
O groupby vai agrupar os dados para permitir que você execute 
operações para cada grupo criado.Esse método divide os dados com base na 
coluna e/ou condição desejada em grupos e aplica a função 
desejada nesse grupo, combinando o resultado em uma única saída.

OBS: Os dados " OBJETOS" dentro da Variavel precisa esta 
no MINIMO organizados - ATENTAR ISSO

SORTED para deixar organizado - coloca tudo em ordem 

Caso não esteja faz um groupby(sorted(alunos))

"""

from itertools import groupby


alunos = ['a','a','a','a','b','c',]   
grupos = groupby(alunos)


for chaves, grupo in grupos:  # chaves vai colocar uma [] e deixar organizadinho
    print(chaves)
    print(list(grupo))  # list vai ler o objetos em ordem de lista

    