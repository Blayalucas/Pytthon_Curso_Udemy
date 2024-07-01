# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# Passo 1 - Importar as Bibiotecas 
from datetime import datetime

from dateutil.relativedelta import relativedelta


# Passo 2 - Criar as Instancias "Variaveis"
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

# Passo 3 - Criar um as Condições
data_parcelas = []  
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

# Passo 4 - criar numero de parcelas mensais com o valor a ser pago por parcela  
numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

# Passo 5 - Criar um loop mês a mês
for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

# Passo 6 - Criar um Print para o usuario 
print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
    
)

