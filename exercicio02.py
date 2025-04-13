contador = 1
maior = 0
while contador <= 5:
    valor = int(input("Valor --> "))
    if contador == 1 or valor > maior:
        maior = valor
    contador = contador + 1
print(f"maior valor = {maior}")