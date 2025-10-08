# Crie um programa que pergunte duas notas e diga se o aluno foi aprovado (média >= 7).

primeira_nota = float(input("1ª nota:"))
segunda_nota = float(input("2ª nota:"))
media = (primeira_nota + segunda_nota)/2
print("Obs. : True = Verdadeiro e False = Falso")
print(f"A media do aluno : {media:.1f}")
print(f"Entao, o aluno passo ?: {media >= 7}")