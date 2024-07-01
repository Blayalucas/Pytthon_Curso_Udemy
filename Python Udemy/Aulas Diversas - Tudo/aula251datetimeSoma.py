# Datetime Soma 

"""
A função Python timedelta() está presente na biblioteca datetime, 
que geralmente é usada para calcular diferenças em datas e também pode 
ser usada para manipulações de datas em Python.
É uma das maneiras mais fáceis de realizar manipulações de datas.


"""
# Podemos  criar datas e fazer contas ( +,-,*,/)


from datetime import datetime, timedelta

fmt = "%d/%m/%Y"
data_inicio = datetime.strptime("05/03/1958", fmt)
data_fim = datetime.strptime("24/06/1987",fmt)

print( data_fim - data_inicio)


