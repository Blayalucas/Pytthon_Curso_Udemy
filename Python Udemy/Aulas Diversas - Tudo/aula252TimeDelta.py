# Datetime Soma 

"""
A Função Timedelta () e para acrescentar dias, horas ma data.

"""

from datetime import datetime, timedelta

fmt = "%d/%m/%Y"
data_inicio = datetime.strptime("05/03/1958", fmt)
data_fim = datetime.strptime("24/06/1987",fmt)
delta = timedelta(days= 10, hours=2)


print(data_fim + delta )
