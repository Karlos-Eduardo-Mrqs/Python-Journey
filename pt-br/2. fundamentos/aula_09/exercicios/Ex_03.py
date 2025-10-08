# - **Soma de uma lista** 
# Utilize um `for` para somar todos os elementos de uma lista de números inteiros. A lista é ``numeros = [8,7,9,8,5,5,6,10,4,5,8,2,3]``

numeros = [8,7,9,8,5,5,6,10,4,5,8,2,3]
soma = 0
for numero in numeros:
    soma += numero

print(f"A soma dos numeros da lista : {soma}")