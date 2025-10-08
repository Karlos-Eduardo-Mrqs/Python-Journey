# 🟩 Listas (`list`) em Python  

As listas são uma das estruturas de dados mais usadas em Python. Elas armazenam coleções **ordenadas** de elementos e podem ser modificadas a qualquer momento.

## ✅ Criando listas

Você pode criar uma lista usando colchetes `[]` e separando os elementos com vírgulas.

```python
# Lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Lista mista
mistura = [1, "texto", True, 3.14]
```

## 🔍 Como acessar os itens ?

```python
print(frutas[0])    # 'maçã'
print(frutas[-1])   # 'laranja' (último item)
```

## ✏️ Como mudar um item

```python
frutas[1] = "uva"
print(frutas)  # ['maçã', 'uva', 'laranja']
```

## 🧰 Métodos mais usados

| Método      | O que faz                             |
| ----------- | ------------------------------------- |
| `append()`  | Adiciona um item ao final da lista    |
| `insert()`  | Insere um item em uma posição         |
| `remove()`  | Remove a primeira ocorrência do valor |
| `pop()`     | Remove e retorna item por índice      |
| `clear()`   | Remove todos os itens da lista        |
| `sort()`    | Ordena os itens da lista              |
| `reverse()` | Inverte a ordem da lista              |
| `len()`     | Retorna o número de itens             |

### 💻 Exemplos Práticos

> 🔖 ``append()``

```python
frutas = ["maçã", "banana"]
frutas.append("laranja")
print(frutas)  # ['maçã', 'banana', 'laranja']
```

> 🔖 ``insert()``

```python
frutas = ["maçã", "laranja"]
frutas.insert(1, "banana")
print(frutas)  # ['maçã', 'banana', 'laranja']
```

> 🔖 ``remove()``

```python
frutas = ["maçã", "banana", "laranja"]
frutas.remove("banana")
print(frutas)  # ['maçã', 'laranja']
```

> 🔖 ``pop()``

```python
frutas = ["maçã", "banana", "laranja"]
item = frutas.pop(1)
print(item)    # 'banana'
print(frutas)  # ['maçã', 'laranja']
```

> 🔖 ``clear()``

```python
frutas = ["maçã", "banana", "laranja"]
frutas.clear()
print(frutas)  # []
```

> 🔖 ``sort()``

```python
frutas = ["banana", "maçã", "laranja"]
frutas.sort()
print(frutas)  # ['banana', 'laranja', 'maçã']
```

> 🔖 ``reverse()``

```python
frutas = ["banana", "maçã", "laranja"]
frutas.reverse()
print(frutas)  # ['laranja', 'maçã', 'banana']

> 🔖 ``len()``

```python
frutas = ["maçã", "banana", "laranja"]
print(len(frutas))  # 3
```

---

### 🔁 Como usar for com listas

Você pode percorrer todos os itens de uma lista usando um for.

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta) # maçã, banana , laranja 

```

---

## ✅ Conclusão

As listas são um dos pilares da programação em Python.Elas permitem armazenar, organizar e manipular coleções de dados de forma fácil e poderosa. Depois desta seção, você já é capaz de:

- Criar listas com diferentes tipos de dados;
- Acessar e modificar elementos;
- Usar métodos úteis ``como append()``, ``pop()``, ``sort()`` e muitos outros;
- Percorrer listas com ``for``;
- Resolver desafios práticos com listas!

> ➡️ Dominar listas é essencial para seguir com temas mais avançados como estruturas de repetição, funções e até manipulação de arquivos e dados!
> Agora que você conhece bem essa estrutura, experimente criar seus próprios programas com listas e veja na prática como elas podem facilitar a sua vida como programador(a) Python. 💡🐍

**Próximo Capítulo : [Tuplas](../aula_02/02_tuplas.md)**

### 📝 Exercícios — Listas

- *Lista de números*

1. Crie uma lista com os números de 1 a 10.
2. Mostre o 1º e o último número.
3. Substitua o número 5 por 50.
4. Exiba a lista final.

- *Controle de estoque*

1. Crie uma lista chamada estoque com os itens: "arroz", "feijão", "macarrão".
2. Adicione "açúcar" ao final.
3. Insira "sal" na 2ª posição.
4. Remova "feijão".
5. Mostre o estoque atualizado.

- *Notas de alunos*

1. Crie uma lista com as notas [7.5, 8.0, 6.0, 9.0, 10.0].
2. Calcule e exiba a média.
3. Mostre a maior e a menor nota.

**[Gabarito](exercicios/README.md)**
