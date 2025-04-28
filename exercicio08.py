valor = int(input("Informe um valor inteiro e positivo --> "))
total_de_divisores = 0
if valor <= 0:
    print("O valor deve ser inteiro e positivo")
else:
    for cont in range(1,  valor + 1):
        if valor % cont == 0:
            total_de_divisores += 1
    if total_de_divisores == 2:
        print(f'{valor} é primo')
    else:
        print(f'{valor} não é primo')
                   