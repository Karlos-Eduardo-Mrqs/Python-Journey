# Sistema de Notas com Match Case. 1. Implemente um programa que leia uma letra de conceito (A, B, C, D ou F) e use match case para exibir a mensagem correspondente: 2. A → "Excelente"; B → "Bom"; C → "Regular"; D → "Ruim"; F → "Reprovado" 3. Outro valor → "Conceito inválido"

media_final = float(input("Digite a média entre (0 até 10):"))
 
if media_final <= 4:
    print("O aluno é Classe F !")
elif media_final <= 5 and media_final <= 5.9:
    print("O aluno é Classe E !") 
elif media_final >= 6 and media_final <= 6.9:
    print("O aluno é Classe D !")
elif media_final >= 7 and media_final <= 7.9:
    print("O aluno é Classe C !")
elif media_final >= 8 and media_final <= 8.9:
    print("O aluno é Classe B !")
elif media_final >= 9 and media_final <= 10:
    print("O aluno é Classe A !")
