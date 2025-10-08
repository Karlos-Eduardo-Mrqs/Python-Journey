# - *Mês do ano (com match case)* 1. Faça um programa que leia um número de 1 a 12 e informe o mês correspondente usando match case. 2. Exemplo: 1 → Janeiro, 2 → Fevereiro, etc. 3. Caso o número não esteja no intervalo, exiba "Mês inválido".

lista_dos_meses = ["...","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
mes = int(input("Digite o numero de um mes:"))

if mes >= 1 and mes <= 12:
    print(f"O mês que você digitou é {lista_dos_meses[mes]}")
else:
    print("Não existe")