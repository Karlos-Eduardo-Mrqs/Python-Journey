# 5. Crie um programa que leia três números e imprima o maior número entre eles, utilizando estruturas condicionais.

num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))
num_3 = float(input("Digite o terceiro numero:"))

if num_1 > num_2 and num_1 > num_3:
    maior = (f"O numero {num_1} é maior")
    print(f"O numero {num_2} é o meio | O numero {num_3} é menor" if num_2 > num_3 else f"O numero {num_3} é o meio | O numero {num_2} é menor")
elif num_2 > num_1 and num_2 > num_3:
    print(f"O numero {num_2} é maior")
    print(f"O numero {num_1} é o meio | O numero {num_3} é menor" if num_1 > num_3 else f"O numero {num_3} é o meio | O numero {num_1} é menor")
elif num_3 > num_1 and num_3 > num_2:
    print(f"O numero {num_3} é maior")
    print(f"O numero {num_2} é o meio | O numero {num_1} é menor" if num_2 > num_1 else f"O numero {num_1} é o meio | O numero {num_2} é menor")
else:
    print("Os números sao iguais")