# Interactive Help == ajuda interativa
# Docstrins == faz anotações do passo do seu projeto


def contador(i=0,f=0,p=0):
    c = i
    while c <= f:
        print(f"{c}", end = "..")
        c += p
    print("Fim")

contador(2,10,2)

