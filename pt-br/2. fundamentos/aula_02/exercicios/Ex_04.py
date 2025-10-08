# - Leia a base e a altura de um retângulo. 1. Calcule e mostre a ``área (base * altura)``. 2. Calcule e mostre o ``perímetro (2 * (base + altura))``.

base = float(input("Digite a base do retângulo:"))
altura = float(input("Digite a altura do retângulo:"))
area = base * altura
perimetro = (2* (base + altura))

print(f"A area do retangulo : {area:.2f}")
print(f"O perimetro do retangulo : {perimetro:.2f}")