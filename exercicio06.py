from math import sqrt

n = int(input("Informe o valor n maior que zero: "))
y = 0
x = 1

if n <= 0:
    print("valor de n deve ser MAIOR QUE zero")
else:
    while x <= n:
        y = y + x / sqrt(x)
        x += 1
    print(f"y = {y}")