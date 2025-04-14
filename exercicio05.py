n = int(input("Informe o valor n maior que zero: "))
y = 0
denominador = 1

if n <= 0:
    print("valor de n deve ser MAIOR QUE zero")
else:
    while denominador <= n:
        y = y + 1 / denominador
        denominador = denominador + 1
    print(f"y = {y}")