pessoas = [
    {"nome": "Carlos", "idade": 25},
    {"nome": "Victor", "idade": 30},
    {"nome": "Beatriz", "idade": 22}
]

ordenacao_idade = sorted(pessoas, key = lambda pessoa: pessoa["idade"])
print(ordenacao_idade)