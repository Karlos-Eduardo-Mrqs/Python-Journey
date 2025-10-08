# - **Busca com `break`** 
# Crie um programa que receba uma lista e pare de percorrê-la assim que encontrar o número 0.

lista_numeros = []
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero == 0:
        break    
    lista_numeros.append(numero)

if len(lista_numeros) == 0:
    print("A lista está vazia !")

for index, numero in enumerate(lista_numeros):
    print(f" indice : {index} | numero : {numero}")