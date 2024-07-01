# Non Local 2

def concatenar (string_inicial):
    valor_final  = string_inicial   # Def concatenar

    def interna(valor_a_Cancatenar):
        return valor_final               # def interna (que não executa nada) 
    return interna                          

c = concatenar('a')   # variavel vai concatenar o a
print(c("b"))   # print apenas variavel c
print(c("c"))   # print apenas variavel c
print(c("d"))   # print apenas variavel c