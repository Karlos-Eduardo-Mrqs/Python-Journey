# 1. Implemente um programa que leia a velocidade de um carro. 2. Se for até 80 km/h, exiba "Dentro do limite". 3. Se for maior, calcule a multa de R$5,00 por km acima do limite e mostre o valor.

velocidade_carro = float(input("Qual foi a velocidade do carro ?:"))
if velocidade_carro <= 80.0:
    print("Dentro do limite")
elif velocidade_carro > 80.0:
    multa = (velocidade_carro - 80) * 5.00
    print(f"Você será multado por R$ {multa:.2f}")