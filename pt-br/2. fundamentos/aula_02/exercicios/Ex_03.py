# - Leia o valor de um empréstimo, a taxa de juros e o número de meses. 1. Calcule o valor total a pagar com juros simples: 2. ``total = valor + (valor * taxa * meses)`` 3. Mostre o resultado.

valor_emprestimo = float(input("Qual foi o valor do emprestimo ?:"))
taxas_juros = float(input("Qual foi o valor da taxa ?:"))
meses = int(input("Quantos meses ?:"))
total = valor_emprestimo + (valor_emprestimo * taxas_juros * meses)
print(f"O total a pagar após {meses} meses : R$ {total:.2f}")