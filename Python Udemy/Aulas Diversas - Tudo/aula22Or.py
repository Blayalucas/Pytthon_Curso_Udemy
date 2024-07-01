# Operador Lógico "or"
# or - Qualquer condição verdadeira avaliada 
# toda a expressão como verdadeira.
# se qualquer valor for considerado verdadeiro
# a expressão inteira será avaliada naquele valor 

entrada = input(" [E]ntrar [S]air: ")
senha_digitada = input ("Senha numérica:  " )
senha_permitida = "123456"

# recapitulando todo codigo com ()  o python le de dentro para fora
# ou seja primeiro le ou soma os parente para depois ler as demais 
# neste caso abaixo ele está lendo (entrada == "E" or entrada == "e") - primeira expressão
# para então ler o resto : and senha_digitada == senha_permitida: - segunda expressão

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")

else: 
    print("Sair")

# outro exemplo de avaliação de curto circuito 

senha = input("Senha: ") or "sem senha" 
print(senha)


