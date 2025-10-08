#  Exercício 2: Somando listas com ``zip()`` 
# Use ``zip()`` para criar uma nova lista chamada somas que contenha a soma dos elementos nas mesmas posições.

lista1 = [10, 20, 30]
lista2 = [1, 2, 3]

for list1, list2 in zip(lista1,lista2):
    soma = list1 + list2

print(f"A soma das listas é {soma}")