# Groupby com biblioteca pandas 

"""


"""

import pandas as pd


# Criando variavel com informações usar tuplas () depois biblioteca dentro 
tecnologia   = ({
    'Curso':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'taxa' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duração':['30dias','50dias','55dias','40dias','60dias','35dias','30dias','50dias','40dias'],
    'Desconto':[1000,2300,1000,1200,2500,None,1400,1600,0]
})

# variavel chamando pandas com classe DataFrame para "deixa em ordem igual excel"
df = pd.DataFrame(tecnologia)
print(df)