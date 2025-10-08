# 3. Faça um programa que leia uma nota de 0 a 10 e informe se o aluno foi aprovado, reprovado ou se está de recuperação. O critério é:

media_final = float(input("Digite a média do aluno:"))

if media_final >= 7:
    print("Aprovado ✅")
elif 5 <= media_final < 7:
    print("Recuperação ⚠️")
else:
    print("Reprovado ❌")
