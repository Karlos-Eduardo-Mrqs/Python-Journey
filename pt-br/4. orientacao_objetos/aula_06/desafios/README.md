# Exercício de Sobrecarga de Operadores — Aula 06 (Módulo 4)

Este projeto demonstra como usar métodos especiais para definir o comportamento de objetos em operações como soma, comparação e indexação.

---

## [🔹 1. Classe Retangulo com operadores personalizados](EX_01.py)

```py
class Retangulo:
    def __init__(self,largura:float,altura:float):
        self.largura = largura
        self.altura = altura
    
    def __str__(self) -> str:
        return f"A área do retângulo = {self.largura * self.altura}"
    
    def __eq__(self, outro) -> bool:
        if isinstance(self,Retangulo):
            return (self.largura * self.altura) == (outro.largura * outro.altura)
        return False

    def __add__(self, outro):
        # Mantemos a largura do primeiro retângulo e calculamos a altura necessária
        if isinstance(outro, Retangulo):
            nova_area = (self.largura * self.altura) + (outro.largura * outro.altura)
            nova_altura = nova_area / self.largura
            return Retangulo(self.largura, nova_altura)
        return NotImplemented

# Testando a classe
r1 = Retangulo(4, 5)
r2 = Retangulo(2, 10)
r3 = Retangulo(4, 5)

print(r1)
print(r2)

# Verificando igualdade
print(r1 == r2)
print(r1 == r3)

# Somando retângulos
r4 = r1 + r2
print(r4)
print(r4.largura * r4.altura)
```

> 🧠 Explicação

- ``__str__()`` — Representação em texto

1. Permite personalizar o que será exibido ao usar ``print(objeto)``.
2. Aqui, exibe a área calculada do retângulo.

- ``__eq__()`` — Comparação de igualdade (==)

1. Compara dois retângulos verificando se suas áreas são iguais.
2. O uso de ``isinstance()`` garante que só haja comparação entre objetos Retangulo.

- ``__add__()`` — Soma de objetos (+)

1. Permite somar dois retângulos combinando suas áreas.
2. Mantém a largura do primeiro e ajusta a altura proporcionalmente.
3. Retorna um novo objeto Retangulo resultante da soma.

- Exemplo prático

1. r1 e r2 possuem a mesma área (20), então ``r1 == r2 → True``.
2. ``r4 = r1 + r2`` gera um novo retângulo com área total de 40.

### ✅ Conceitos aplicados

1. *Sobrecarga de operadores:* redefinição de comportamentos padrões (``==, +, print()``).
2. *Criação de novos objetos* a partir de operações.
3. *Encapsulamento de lógica* matemática dentro da classe.
4. Verificação de tipo com ``isinstance()`` para evitar erros de tipo.

---

## [🔹 2. Classe ListaPersonalizada simulando listas nativas](EX_02.py)

```py
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
```

> 🧠 Explicação

- ``__getitem__()`` — acesso por índice (``objeto[i]``)

1. Permite acessar elementos da lista personalizada como uma lista comum.

- ``__setitem__()`` — atribuição por índice (``objeto[i] = valor``)

1. Permite alterar elementos diretamente pelo índice.

- ``__delitem__()`` — exclusão (``del objeto[i]``)

1. Remove um item da lista com a palavra-chave ``del``.

- ``__contains__()`` — operador ``in``

1. Permite verificar se um valor está contido na lista (``valor in objeto``).

- ``__len__()`` — função ``len()``

1. Retorna o tamanho da lista personalizada, assim como listas nativas.

### ✅ Conceitos aplicados

1. *Protocolo de sequência do Python* (implementando métodos que imitam listas).
2. *Encapsulamento de listas* internas (``self.itens``).
3. *Interface customizada* que torna a classe compatível com comportamentos nativos (``len(), in, []``).
4. *Alta flexibilidade:* a classe pode evoluir com validações ou restrições específicas, mantendo a sintaxe familiar das listas.

---

## 💡 Conclusão

Esses dois desafios mostram como o Python permite transformar classes comuns em objetos altamente expressivos, parecidos com tipos nativos, ao usar métodos especiais (dunder methods). Com eles, é possível:

1. ✅ Personalizar comparações
2. ✅ Controlar operações matemáticas
3. ✅ Criar estruturas de dados próprias
4. ✅ Tornar o código mais intuitivo e legível

**Próximo Capítulo : [Em breve](..)**
