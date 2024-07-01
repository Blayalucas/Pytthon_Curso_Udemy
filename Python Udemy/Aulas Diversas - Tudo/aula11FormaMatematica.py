# OBS: Parentes sempre será executados primeiro. 

# 1. (n + n) - Parentes primeiro 
# 2. **  - Exponensiação
# 3. * / // % - Multiplicação, divisão, divisão inteiro e resto
# 4. + - adição e subtração

conta_1 = 1 + 1 ** 5 + 5 #7
conta_1 = (1 +1) ** (5 + 5) # 1024
conta_1 = (1 + int (0.5 + 0.5)) ** (5 + 5) # 1024
print (conta_1)
