# datetime.strptime('DATA', 'FORMATO')

"""
Documentação de como criar datas 

https://docs.python.org/3/library/datetime.html

OBS: OLhar as diretives no final da tela. 

"""

from datetime import datetime

data_str_data = "1987-06-24"
data_str_fmt = "%Y-%m-%d"

data = datetime.strptime(data_str_data,data_str_fmt)
print (data)