"""
While  crescente e descrescente com if e elif
"""

while True:
    x = int(input("Digite um numero inteiro : "))
    y = int(input("Digite outro numero inteiro "))
    if x > y:
        x = x + 1
        print("Descrecente")
    elif x < y :
        y = y = 1 
        print("Crescente")