# 1. Faça um programa que leia um ano; 2. verifique se ele é bissexto ou não bissexto. 3. um ano é bissexto se for divisível por 4. 4. Não é divisível por 100, exceto se também for divisível por 400.

ano_usuario = int(input("Digite um ano:"))

if (ano_usuario % 4 == 0 and ano_usuario % 100 != 0) or (ano_usuario % 400 == 0):
    print("O ano é bissexto ! ")
else :
    print("O ano não é bissexto !")