# Args Parse

"""


    
"""

# Argparse 

"""
Descobre se o usuario passou um argumento. " elemento" 

"""

from argparse import ArgumentParser

parser = ArgumentParser ()

parser.add_argument('--basic',
                    help = "Mostra Olá Mundo", 
                    type = str,
                    metavar = 'STRING',
                    default= "Olá mundo",
                    required= False,
                    nargs='+' # inserir mais valores
                                
)

args = parser.parse_args ()

if args.basic is None: 
    print("Você não passou argumentos")
    
else: 
    print(args.basic)