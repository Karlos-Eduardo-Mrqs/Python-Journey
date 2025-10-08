# Operadores de Membros 04: Crie um programa que pergunte ao usuário por um item e verifique se esse item está em uma

lista_compras = ["arroz", "feijão", "leite", "pão", "açúcar"]

item = input("Digite um item para verificar na lista de compras: ")

print("Obs.: True = Verdadeiro e False = Falso ")

print("O item está na lista? ", item in lista_compras)
print("O item não está na lista? ", item not in lista_compras)
