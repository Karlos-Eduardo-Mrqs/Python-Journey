# 1. Crie um programa que leia um número digitado pelo usuário e compare com um número secreto definido no código. 2. Se o usuário acertar, exiba "Você acertou!". 3. Caso contrário, diga se o número é maior ou menor que o secreto.
import random 

numero_aleatorio = random.randint(0,10)
numero_usuario = int(input("Digite um numero inteiro entre 0 até 10:"))

if numero_usuario > numero_aleatorio :
    print("Você errou ! O numero é menor que o digitado")
elif numero_usuario < numero_aleatorio:
    print("Você errou ! O numero é maior que o digitado")
else:
    print("Você acertou !")

print(f"O numero secreto é {numero_aleatorio}")