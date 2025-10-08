# Operadores Lógicos 03: Verifique se um número está entre dois valores (usando and e or).

numero = float(input("Digite um numero:"))

entre_10_e_20 = numero >= 10 and numero <= 20
fora_do_limite = numero < 10 or numero > 20

print("Obs.: True = Verdadeiro e False = Falso ")

print("O número está entre 10 e 20? ", entre_10_e_20)
print("O número está fora da faixa 10 a 20? ", fora_do_limite)
