# Filtrar pares com continue 
# Percorra uma lista de 1 a 10 e imprima apenas os números pares, utilizando continue para ignorar os ímpares.

numeros = [i for i in range(1,11)]
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero,"..")