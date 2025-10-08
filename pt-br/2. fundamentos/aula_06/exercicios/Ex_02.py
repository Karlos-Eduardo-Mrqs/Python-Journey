# 2. Crie um programa que leia a idade de uma pessoa e classifique-a como: Criança (0 a 12 anos); Adolescente (13 a 17 anos) ; Adulto (18 a 64 anos) ; Idoso (65 anos ou mais)

idade = int(input("Digite a sua idade:"))

if idade > 0:
    if idade <= 12:
        print("O usuario é uma Criança.")
    elif idade <= 17:
        print("O usuario é um Adolescente.")
    elif idade <= 64:
        print("O usuario é um Adulto.")
    elif idade >= 65:
        print("O usuario é um idoso.")
else:
    print("Idade invalida !")
