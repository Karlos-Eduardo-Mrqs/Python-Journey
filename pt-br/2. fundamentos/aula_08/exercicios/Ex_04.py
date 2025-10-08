# Categoria de IMC 1. Crie um programa que leia o peso e a altura de uma pessoa e calcule o IMC. 
# 2. Classifique de acordo com a tabela: Menor que 18.5 → Abaixo do peso; Entre 18.5 e 24.9 → Peso normal; Entre 25.0 e 29.9 → 
# Sobrepeso; 30.0 ou mais → Obesidade;

print("Calculadora de Indice de Massa Corporal")

altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))
IMC = peso / (altura ** 2)

if IMC <= 18.5:
    print("Você está: ABAIXO DO PESO")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Você está: PESO NORMAL")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Você está: SOBREPESO")
elif IMC >= 30:
    print("Você está: OBESIDADE")