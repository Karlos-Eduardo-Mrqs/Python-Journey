# 1. Implemente um programa que leia um número e imprima se ele é positivo, negativo ou zero.

numero = int(input("Digite um numero:"))

if numero < 0:
    print(f"O número {numero} é negativo")
elif numero > 0:
    print(f"O número {numero} é positivo") 
else:
    print("O número é 0")