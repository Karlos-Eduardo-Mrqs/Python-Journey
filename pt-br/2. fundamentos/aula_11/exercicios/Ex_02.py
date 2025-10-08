# Soma de números até o usuário digitar 0 Leia números do usuário em um loop while e some-os até que seja digitado 0.

soma = 0
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero == 0 :
        break
    soma += numero

print(soma)