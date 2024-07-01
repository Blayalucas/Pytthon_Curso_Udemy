# kWARGS é o args porém melhor ( pois deixa Organizado)

#**kwargs - é um dicionario

def calcular_imposto(valor,**impostos):  # O valor primeiro, depois **Kwargs com tudo dentro
   total_imposto = 0  # contador apartir do 0
   print(impostos)
   return total_imposto


print(calcular_imposto (valor = 1000,ir = 0.275,iss = 0.05,csll = 0.0375,pis = 0.03 )) # descriminei cada parametro