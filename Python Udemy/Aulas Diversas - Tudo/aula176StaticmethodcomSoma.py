# Staticmethod ()

"""
A staticmethod()função interna retorna 
um método estático para uma determinada função.

"""
class Calculator:

  def add_numbers(num1, num2):
    return num1 + num2

# convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(5, 7)
print('Sum:', sum)