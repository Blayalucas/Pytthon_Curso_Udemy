# Empacotamento e desempacotamento de dicionário

#** faz com que tenhamos 1 dicionário apenas ( junta tudo)

pessoa = {'nome':"Aline",
'Sobrenome': "Souza",
}

dados_pessoa = { 'idade' : 16 , 
'altura' : 1.6

}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)
