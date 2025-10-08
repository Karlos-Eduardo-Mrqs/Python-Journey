# 5. Crie um programa que leia três números e imprima o maior número entre eles, utilizando estruturas condicionais.

num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))
num_3 = float(input("Digite o terceiro numero:"))

if num_1 == num_2 == num_3:
    print("Os numeros sao iguais")

numeros = [num_1,num_2,num_3]
numeros.sort()
maior,meio,menor = numeros[0], numeros[1], numeros[2]

print(f"Ordem Crescente : {maior} , {meio} , {menor}")
print(f"Ordem Decrescente : {menor} , {meio} , {maior}")