# Time dateutil.relativedelta

"""
O tipo relativodelta foi projetado para ser aplicado a uma data e hora existente e 
pode " SUBSTITUIR" e " ACRESCENTAR" componentes específicos 
dessa data e hora ou representar um intervalo de tempo.

Essa função é melhor que datime pois tem um monte de items dentro dela

"""

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


fmt = "%d/%m/%Y"
data_inicio = datetime.strptime("05/03/1958", fmt)
data_fim = datetime.strptime("24/06/1987",fmt)
#delta = timedelta(days= 10, hours=2)
delta = relativedelta( data_fim, data_inicio)

print(data_fim + delta)
print (data_fim + relativedelta(seconds=59,days=8,months=10))