# 4. Crie um programa que leia dois números e um operador matemático (+, -, *, /). O programa deve executar a operaçao correspondente entre os dois números e mostrar o resultado.
simbolos = ["+","-","*","X","/"]

num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))

print("+ : Soma")
print("- : Subtracao")
print("X ou * : Multiplicacao")
print("/ : Divisão")
simbolo_usuario = input("Digite um dos simbolos acima:")

if simbolo_usuario in simbolos:
    match simbolo_usuario:
        case "+":
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        case "-":
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
        case "X" | "*":
            print(f"{num_1} X {num_2} = {num_1 * num_2}")
        case "/":
            if num_2 != 0:
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
            else:
                print("Divisao nao permitida !")
else:   
    print("Nao ha como fazer essa operacao !")