# - *Mês do ano (com match case)* 1. Faça um programa que leia um número de 1 a 12 e informe o mês correspondente usando match case. 2. Exemplo: 1 → Janeiro, 2 → Fevereiro, etc. 3. Caso o número não esteja no intervalo, exiba "Mês inválido".

mes = int(input("Digite o numero de um mes:"))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Não existe esse mês")