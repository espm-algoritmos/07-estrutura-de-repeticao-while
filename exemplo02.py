''' programa exemplo para imprimir no terminal os
    números de 1 até 20
    
    programa para ler dois valores informados pelo usuário. O 
    programa deve imprimir todos os números entre o primeiro e o segundo
    valor
    
    programa para imprimir apenas os números pares entre os dois valores que o usuário
    digitou. A impressão deve incluir os extremos.
'''

valor1 = int(input("Informe o valor inicial: "))
valor2 = int(input("Informe o valor final: "))
contador = valor1
while contador <= valor2:    
    if contador % 2 == 0:
        print(f'{contador}')
    contador = contador + 1
    