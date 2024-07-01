# Argparse 

"""
Descobre se o usuario passou um argumento. " elemento" 

"""

from argparse import ArgumentParser

parser = ArgumentParser ()

parser.add_argument('--basic')

args = parser.parse_args ()

if args.basic is None: 
    print("Você não passou argumentos")
    
else: 
    print(args.basic)

