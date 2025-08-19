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

### 🔁 Como usar for com listas

Você pode percorrer todos os itens de uma lista usando um for.

```python
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta) # maçã, banana , laranja 

```

---

## ✅ Conclusão

As listas são um dos pilares da programação em Python. Elas permitem armazenar, organizar e manipular coleções de dados de forma fácil e poderosa.

Depois desta seção, você já é capaz de:

- Criar listas com diferentes tipos de dados;
- Acessar e modificar elementos;
- Usar métodos úteis como append(), pop(), sort() e muitos outros;
- Percorrer listas com for;
- Resolver desafios práticos com listas!

> ➡️ Dominar listas é essencial para seguir com temas mais avançados como estruturas de repetição, funções e até manipulação de arquivos e dados!
> Agora que você conhece bem essa estrutura, experimente criar seus próprios programas com listas e veja na prática como elas podem facilitar a sua vida como programador(a) Python. 💡🐍

## 🧪 Desafio!

Tente fazer sozinho:

1. Crie uma lista com 5 nomes.
2. Ordene a lista.
3. Remova o 3º nome.
4. Adicione 2 novos nomes.
5. Mostre o resultado final com print().

**Próximo arquivo [Tuplas](02_tuplas)**