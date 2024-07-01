# Notas em exceptions


class MeuError( Exception):
    ...
    
def levantar():
    exception_ = MeuError ("a","b","c")
    exception_.add_note("Olha o nota 1")
    raise exception_

try:
    levantar()
except (MeuError,ZeroDivisionError) as error:  # criamos uma variavel dentro do except
    print(error.__class__.__name__)
    print(error.args)
    print()
