class ListaPersonalizada:
    def __init__(self, itens=None):
        if itens is None:
            itens = []
        self.itens = itens

    def __getitem__(self, index):
        return self.itens[index]

    def __setitem__(self, index, valor):
        self.itens[index] = valor

    def __delitem__(self, index):
        del self.itens[index]

    def __contains__(self, valor):
        return valor in self.itens

    def __len__(self):
        return len(self.itens)

lista = ListaPersonalizada([10, 20, 30])

print(lista[1])    # 20
lista[1] = 99
print(lista[1])    # 99
del lista[0]
print(lista.itens) # [99, 30]
print(len(lista))  # 2
print(99 in lista) # True
