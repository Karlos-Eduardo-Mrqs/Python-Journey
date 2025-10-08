# 1. Crie duas listas lista1 e lista2 com os mesmos valores [1, 2, 3]. 2. Verifique se lista1 e lista2 são o mesmo objeto usando is.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print("lista1 é lista2?:", lista1 is lista2)

lista3 = lista1
print("lista1 é lista3?:", lista1 is lista3)
print("lista1 não é  lista3?:", lista1 is not lista3)