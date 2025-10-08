#    1. Leia três números do usuário. 2. Mostre a média dos números. 3. Mostre a diferença entre o maior e o menor número.
num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))
num_3 = float(input("Digite o terceiro numero:"))

media = (num_1+num_2+num_3)/3
print(f"A média dos numeros :{media:.2f}")
numeros = [num_1,num_2,num_3]

print(f"A diferenca entre {max(numeros)} e {min(numeros)} :  {max(numeros) - min(numeros)}")