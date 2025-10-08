# Verificar se um elemento digitado pelo usuário está presente em uma lista de frutas.frutas = ["maçã", "banana", "laranja", "uva", "pera"]

frutas = ["maçã", "banana", "laranja", "uva", "pera"]

item = input("Digite o nome de uma fruta: ").lower()

print(f"O item está na lista?: {item in frutas}")
print(f"O item não está na lista?: {item not in frutas}")