# Sys.Argv

"""

esse modulo SYS ARGV informa o local exato onde estamos trabalhando, 
dentro do Computador, numero de elementos que possui o local " Pasta"
fazendo um LEN e fazendo STR podemos criar uma Lista para saber a " Raiz"
do local. 
    
"""
  
import sys 
  
# Passo 1 : Mostrar o local da pasta com SYS.ARGV
print("Este é o nome da pasta :", 
       sys.argv[0]) 

# Passo 2: Saber o numero de elementos que contem a pasta com um LEN
print("Numero de elementos que contem a pasta:", 
       len(sys.argv)) 

# Passo 3 - Caso queira excluir os elementos na pasta faz um Len menos a quantidade do elemento. 
print("Numero de elementos que excluido na pasta :", 
      (len(sys.argv)-1)) 

# Passo 4 - Criar uma Lista exata onde o local se encontra fazendo um STR
print("Uma Lista  exata do local onde a pasta está ", 
       str(sys.argv)) 