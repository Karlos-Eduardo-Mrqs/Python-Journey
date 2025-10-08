# 🔢 Loopings Contáveis em Python

Os loopings contáveis são aqueles em que sabemos exatamente quantas vezes o código deve ser executado.
Em Python, usamos a estrutura for para esse tipo de repetição.

---

## 🔹 for

``A estrutura for`` é usada para iterar sobre uma sequência (como uma lista, tupla, string ou intervalo de números). Ela é ideal para quando você sabe o número de iterações que deseja realizar.

> ✅ Sintaxe:

```python
for item in sequencia:
    # bloco de código
```

> 📌 Exemplo de uso: Iterar sobre uma lista de números e imprimir cada um.

```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

## 🔷 Funções de iteração

### 🔹 ``range()``

A função ``range()`` é usada para gerar uma sequência de números, muito útil em loops for. Ela pode receber até três argumentos: ``start``, ``stop`` e ``step``.

> ✅ Sintaxe:

```python

range(start, stop, step)
```

1. ``start``: valor inicial (inclusivo);
2. ``stop``: valor final (exclusivo);
3. ``step``: incremento (opcional).

> 📌 Exemplo de uso com ``range()``:

```python

for i in range(10):
    print(i)  # números de 0 a 9

for i in range(0, 10, 2):
    print(i)  # números pares: 0, 2, 4, 6, 8
```

### 🔹 ``enumerate()``

A função ``enumerate()`` adiciona um contador automático a um iterável, retornando uma tupla com o índice e o valor.

> ✅ Sintaxe:

```python
enumerate(iteráveis)
```

> 📌 Exemplo:

```python
frutas = ["maçã", "banana", "cereja"]
for index, fruta in enumerate(frutas):
    print(f"Índice {index}: {fruta}")
```

### 🔹 ``zip()``

A função ``zip()`` combina dois ou mais iteráveis, retornando uma sequência de tuplas. Cada tupla contém os elementos correspondentes dos iteráveis.

> ✅ Sintaxe:

```python
zip(iterável1, iterável2, ...)
```

> 📌 Exemplo:

```python
nomes = ["João", "Maria", "Carlos"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
```

---

## 🔹 Compreensão de Listas (List Comprehensions)

A compreensão de listas oferece uma forma compacta e eficiente de criar listas a partir de outras coleções ou sequências.
É muito útil para aplicar transformações ou filtros em listas.

> ✅ Sintaxe:

```python
[expressao for item in iteravel]
```

> 📌 Exemplo:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = [numero**2 for numero in numeros]
print(quadrados)  # Saída: [1, 4, 9, 16, 25]
```

---

## ✅ Conclusão

Os loopings contáveis em Python, representados principalmente pelo for, são fundamentais quando sabemos exatamente quantas vezes queremos repetir uma ação. Com o auxílio de funções como ``range()``, ``enumerate()`` e ``zip()``, além das compreensões de listas, conseguimos escrever códigos mais simples, claros e eficientes.

Esses recursos são amplamente utilizados no dia a dia da programação, desde tarefas básicas, como percorrer listas de números, até aplicações mais complexas, como processamento de grandes volumes de dados.

**Próximo Capítulo: [Loopings Não Contaveis](../aula_11/11_loopings_nao_contaveis.md)**

---

## Exercícios da aula 10

### Tabuada personalizada

Peça para o usuário digitar um número inteiro e imprima a tabuada desse número de 1 a 10.

### Somando listas com ``zip()``

Dadas duas listas de mesmo tamanho:

```python
lista1 = [10, 20, 30]
lista2 = [1, 2, 3]
```

Use ``zip()`` para criar uma nova lista chamada somas que contenha a soma dos elementos nas mesmas posições.

### Filtrar nomes com list comprehension

Dada a lista:

```python
nomes = ["Ana", "João", "Amanda", "Carlos", "André", "Beatriz"]
```

Use ``list comprehension`` para criar uma nova lista apenas com os nomes que começam com a letra ``"A"``.

### Contador regressivo

Utilize ``range()`` para imprimir uma contagem regressiva de 10 até 1.

### Iterar com índice usando ``enumerate()``

Dada a lista de tarefas:

```python

tarefas = ["Lavar a louça", "Estudar Python", "Fazer exercícios", "Ler um livro"]
```

Use ``enumerate()`` para imprimir as tarefas com numeração a partir de 1:

**[Gabarito](exercicios/README.md)**
