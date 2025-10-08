# Filtro com continue Use um loop while para ler números de 1 a 10 e imprimir apenas os múltiplos de 3

for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)
