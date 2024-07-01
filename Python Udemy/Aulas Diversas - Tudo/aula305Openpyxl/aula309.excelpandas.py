# Gerando uma planilha excel com Pandas 

"""
De um modo pratico e simples 
    
"""
# importando a biblioteca 
import pandas as pd 

# criando instancia com Json e tuplas

carros = {
    "Marca":["Fiat","Chevrolet","Ford"],
    "Modelo": ["Marea","Onix","Escort"],
    "Ano": ["1999","2021","1995"]
    
}

# chamando a instancia 
dataframe = pd.DataFrame(carros)
dataframe. to_excel(' ./carros.xlxs')

