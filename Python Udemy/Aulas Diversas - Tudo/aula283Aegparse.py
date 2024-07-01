# ArgParse

"""
O argparse descobrirá como analisá-los em sys.argv. 
O módulo argparse também gera automaticamente mensagens de ajuda e uso. 
O módulo também emitirá erros quando os usuários fornecerem argumentos inválidos ao programa.
"""

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("--basic")
args = parser.parse_args()
print(args)

if args.basic is None: 
    print(" Você não passou o argumento b.")

else: 
    print(args.basic)