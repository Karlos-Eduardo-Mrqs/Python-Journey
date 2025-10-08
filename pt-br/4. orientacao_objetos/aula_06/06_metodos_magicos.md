# 🧩 Métodos Mágicos em Python

Nesta aula, você aprenderá sobre os métodos mágicos (ou dunder methods) em Python — funções especiais que começam e terminam com dois underscores, usadas para personalizar o comportamento de classes e objetos.

Eles tornam seus objetos mais naturais de usar, permitindo sobrecarregar operadores, controlar representações e até gerenciar comportamento interno de coleções.

## 🧠 Conceito

Métodos mágicos são funções internas que o Python chama automaticamente em certas situações:

- ``__init__()``→ chamado ao criar um objeto.
- ``__str__()`` → define a representação textual do objeto.
- ``__repr__()`` → representação oficial do objeto (usado pelo ``repr()`` ou no console).

- ``__add__()`` → permite usar + com objetos.
- ``__sub__()`` → permite usar - com objetos.
- ``__len__()`` → retorna o tamanho do objeto (usado com len()).

- ``__getitem__()`` → permite acessar itens com índice obj[i].
- ``__setitem__()`` → permite atribuir valores com índice obj[i] = valor.
- ``__delitem__()`` → permite deletar itens com índice del obj[i].

- ``__contains__()`` → usado pelo operador in.
- ``__iter__()`` e ``__next__()`` → permitem que o objeto seja iterável.

> 🔹 Eles não precisam ser chamados diretamente; o Python chama automaticamente quando você usa operadores ou funções correspondentes.

---

## 🧪 Exemplos Práticos

### 1️⃣ Representação do Objeto

```py
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

    def __repr__(self):
        return f"Pessoa('{self.nome}', {self.idade})"

p = Pessoa("Ana", 25)
print(p)      # Chama __str__: Ana, 25 anos
print(repr(p)) # Chama __repr__: Pessoa('Ana', 25)
```

### 2️⃣ Operadores Matemáticos

```py
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __sub__(self, outro):
        return Ponto(self.x - outro.x, self.y - outro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Ponto(2, 3)
p2 = Ponto(4, 1)

print(p1 + p2)  # (6, 4)
print(p1 - p2)  # (-2, 2)
```

### 3️⃣ Controle de Comprimento

```py
class Time:
    def __init__(self, jogadores):
        self.jogadores = jogadores

    def __len__(self):
        return len(self.jogadores)

time = Time(["Lucas", "Ana", "Pedro"])
print(len(time))  # 3
```

### 4️⃣ Iteráveis e Indexação

```py
class Fib:
    def __init__(self, n):
        self.n = n
        self.seq = [0, 1]

    def __getitem__(self, i):
        while i >= len(self.seq):
            self.seq.append(self.seq[-1] + self.seq[-2])
        return self.seq[i]

f = Fib(10)
print(f[5])  # 5
print(f[8])  # 21
```

### 5️⃣ Checagem de Pertinência

```py
class Grupo:
    def __init__(self, membros):
        self.membros = membros

    def __contains__(self, nome):
        return nome in self.membros

grupo = Grupo(["Ana", "Pedro", "Lucas"])
print("Ana" in grupo)    # True
print("Beatriz" in grupo) # False
```

---

## 🧭 Conclusão

Métodos mágicos tornam suas classes flexíveis e poderosas, permitindo que objetos se comportem como tipos nativos do Python:

1. Sobrecarregando operadores (``+``, ``-``, ``*``, ``==``);
2. Controlando representações (``__str__``, ``__repr__``);
3. Tornando objetos iteráveis e indexáveis (``__iter__``, ``__getitem__``);
4. Permitindo verificações de pertinência (``in``).

> 💡 Dica: Sempre que quiser que sua classe se comporte naturalmente com operadores e funções nativas do Python, use métodos mágicos!

**Próximo Capítulo : [Em breve](..)**

---

### 🚀 Desafios

- Crie uma classe *Retangulo* com:

1. atributos largura e altura;
2. métodos mágicos ``__str__()``, ``__eq__()`` e ``__add__()``;
3. ``__eq__()`` retorna True se dois retângulos têm a mesma área;
4. ``__add__()`` retorna um retângulo cuja área é a soma das áreas dos dois;

- Crie uma classe *ListaPersonalizada* que:

1. armazena elementos internamente;
2. implementa ``__getitem__``, ``__setitem__``, ``__delitem__`` e ``__len__()``;
3. teste indexação, atribuição, deleção e len().
4. Experimente adicionar ``__contains__()`` em *ListaPersonalizada* para checar se um valor está presente usando in.
