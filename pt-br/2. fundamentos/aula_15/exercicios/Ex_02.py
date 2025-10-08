def comprar(valor):
    valor_local = 500
    print(f"Valor da variável local : {valor_local}")
    return valor_local - valor

valor_usuario = 150.45
print(f"Valor usuario {valor_usuario:.2f} X Valor local {comprar(valor_usuario)}")