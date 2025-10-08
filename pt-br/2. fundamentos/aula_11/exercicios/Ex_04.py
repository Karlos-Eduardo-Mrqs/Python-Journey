# Interromper com break Crie um loop que leia números do usuário e pare quando o número for negativo.

numeros = []
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero < 0 :
        break
    numeros.append(numero)

print(numeros)