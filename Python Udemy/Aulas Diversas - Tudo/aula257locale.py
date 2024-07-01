# Locale Internacionale 

"""
Faz com que o codigo mude para sua localidade "tradutor"

"""

import calendar 
import locale

# Mudar tudo dentro do codigo - cada palavra/informação para o meu idioma 
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

print(calendar.calendar(2024))