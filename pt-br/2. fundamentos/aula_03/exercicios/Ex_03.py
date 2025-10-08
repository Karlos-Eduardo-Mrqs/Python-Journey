# Leia um número inteiro. 1. Mostre se ele é positivo, negativo ou zero. 2. Indique também se é par ou ímpar.

numero = int(input("Digite um numero inteiro:"))
print("Obs. : True = Verdadeiro e False = Falso")
print(f"O numero é positivo ? : {numero >= 0}")
print(f"O numero é negativo ? : {numero < 0}")
print(f"O numero é zero ? : {numero == 0}")
print(f"O numero é par ? : {numero % 2 == 0}")
print(f"O numero é impar ? : {numero % 2 == 1}")
