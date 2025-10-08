# Exercício 1: Tabuada personalizada
# Peça para o usuário digitar um número inteiro e imprima a tabuada desse número de 1 a 10.

numero = int(input("Digite um numero inteiro:"))
for i in range(1,11):
    print(f"{numero} X {i} = {numero * i} ")