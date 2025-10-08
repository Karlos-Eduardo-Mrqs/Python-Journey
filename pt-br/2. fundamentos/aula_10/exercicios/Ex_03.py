# Use ``list comprehension`` para criar uma nova lista apenas com os nomes que começam com a letra ``"A"``.

nomes = ["Ana", "João", "Amanda", "Carlos", "André", "Beatriz"]

for nome in nomes:
    if nome[0] == "A":
        print(nome,"..")
