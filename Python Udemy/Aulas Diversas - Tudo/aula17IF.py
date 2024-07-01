# if / se  - Sempre será a primeira condição 
# elif / se não se  - Sempre será a segunda condição 
# else / se não - Sempre será terceira opção atrelada a elif
# OBS: Essas 3 requer uma condição ou seja uma pergunta 

# Ao todo será 6 regras

# exemplo

entrada = input (' Você quer "entrar" ou "sair"? ')

if entrada == "entrar":
    print("Você entrou no sistema")
elif entrada == "sair":
    print("Você saiu do sistema")
else:
    print("Você não digitou entrar ou sair")