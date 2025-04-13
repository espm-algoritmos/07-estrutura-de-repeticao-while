contador = 1
maior = float('-inf')
while contador <= 3:
    valor = int(input("Valor --> "))
    if valor > maior:
        maior = valor
    contador = contador + 1
print(f"maior valor = {maior}")