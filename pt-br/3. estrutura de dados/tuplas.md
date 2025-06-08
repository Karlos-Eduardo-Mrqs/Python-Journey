
# 🟨 Tuplas (`tuple`) em Python

As tuplas são outra estrutura de dados importante em Python. Elas são muito parecidas com listas, mas com uma diferença fundamental: **são imutáveis**, ou seja, depois de criadas, seus valores **não podem ser alterados**.

---

## ✅ Criando tuplas

Você pode criar uma tupla usando parênteses `()` e separando os elementos com vírgulas:

```python
# Tupla de frutas
frutas = ("maçã", "banana", "laranja")

# Tupla mista
mistura = (1, "texto", True, 3.14)
```

> 💡 Dica: Os parênteses são opcionais! Você pode declarar uma tupla apenas separando os elementos por vírgulas:

```python
numeros = 1, 2, 3
```

---

## 🔎 Como acessar os itens?

Assim como nas listas, você acessa os elementos da tupla por meio de **índices**, começando do zero:

```python
print(frutas[0])    # 'maçã'
print(frutas[-1])   # 'laranja' (último item)
```

> ✅ Índices negativos também funcionam, assim como em listas.

---

## 🚫 Tuplas são imutáveis

Como as tuplas são **imutáveis**, tentar alterar um elemento gera erro:

```python
frutas[1] = "uva"  # TypeError
```

**Isso vai gerar um erro!** Se precisar modificar, converta a tupla para lista:

```python
lista_frutas = list(frutas)
lista_frutas[1] = "uva"
frutas = tuple(lista_frutas)
```

---

## 🧰 Métodos úteis

Por serem imutáveis, as tuplas possuem menos métodos que listas. Os mais usados são:

| Método    | Função                                                |
|-----------|--------------------------------------------------------|
| `index()` | Retorna o índice do primeiro valor encontrado.         |
| `count()` | Conta quantas vezes um valor aparece.                  |
| `len()`   | Retorna o número de itens.                             |

---

## 💻 Exemplos práticos

🔖 `index()`

```python
numeros = (10, 20, 30, 20)
print(numeros.index(30))  # Saída: 2
```

🔖 `count()`

```python
numeros = (10, 20, 30, 20)
print(numeros.count(20))  # Saída: 2
```

🔖 `len()`

```python
numeros = (1, 2, 3, 4)
print(len(numeros))  # Saída: 4
```

---

## 🔁 Iterando com `for`

Tuplas são iteráveis, ou seja, podem ser percorridas com o laço `for`:

```python
cores = ("vermelho", "azul", "verde")

for cor in cores:
    print(cor)
```

Ou se quiser exibir tudo em uma linha:

```python
print(", ".join(cores))  # Saída: vermelho, azul, verde
```

---

## 📦 Desempacotamento de tuplas

Tuplas permitem uma forma prática de atribuir valores a várias variáveis de uma vez:

```python
ponto = (10, 20)
x, y = ponto

print(x)  # 10
print(y)  # 20
```

---

## ✅ Conclusão

Tuplas são ideais quando você precisa armazenar dados que **não devem ser modificados**, como:

- Coordenadas;
- Datas;
- Registros fixos.

Ao final deste conteúdo, você já é capaz de:

- Criar tuplas com diferentes tipos de dados;
- Acessar elementos com índices positivos e negativos;
- Entender a diferença entre mutabilidade e imutabilidade;
- Utilizar métodos como `index()`, `count()` e `len()`;
- Percorrer tuplas com o laço `for`;
- Aplicar o desempacotamento de tuplas.

> ➡️ Tuplas são simples, rápidas e seguras. Saber quando usá-las é essencial para escrever código eficiente e bem estruturado.

Agora que você entende bem **listas** e **tuplas**, vamos seguir com **conjuntos (`set`)** e **dicionários (`dict`)**. Continue estudando! 💪🐍
