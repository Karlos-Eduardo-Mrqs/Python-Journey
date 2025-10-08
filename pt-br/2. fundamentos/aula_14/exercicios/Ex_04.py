def produto(nome, preco, quantidade):
    print(f"Produto: {nome} | Preço: {preco} | Quantidade: {quantidade}")

# Chamando com argumentos posicionais
produto("Caderno", 15.5, 3)

# Chamando com argumentos nomeados (ordem trocada)
produto(quantidade=2, nome="Caneta", preco=2.75)
