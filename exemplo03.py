
resposta = "sim"
while resposta == "sim":
    valor = int(input("Digite um valor inteiro --> "))
    contador = 0
    while contador <= 10:
        resultado = valor * contador
        print(f"{valor} * {contador} = {resultado}" )
        contador = contador + 1
        print()
    resposta = input("Deseja imprimir outra tabuada (sim ou não): ")
    