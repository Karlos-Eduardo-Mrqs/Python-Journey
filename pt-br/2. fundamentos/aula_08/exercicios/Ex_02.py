# *Maioridade com operador ternário* 1. Faça um programa que leia a idade de uma pessoa e diga: 2. "Maior de idade" se for 18 anos ou mais. 3. "Menor de idade" caso contrário.

idade = int(input("Digite a sua idade:"))
maior_de_idade = "Maior de idade" if idade >= 18 else "Menor de idade"
print(maior_de_idade)