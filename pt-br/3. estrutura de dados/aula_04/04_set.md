# 🟥 Conjuntos (`set`) em Python

## 📌 O que são?

Um **conjunto** em Python é uma coleção **não ordenada**, **imutável (individualmente)** e **sem elementos duplicados**. Ideal para realizar operações matemáticas como união, interseção e diferença.

```python
# Exemplo de conjunto
numeros = {1, 2, 3, 2, 1}
print(numeros)  # saída: {1, 2, 3}
```

### 🔑 Características principais

* **Não possui ordem** → não é possível acessar elementos por índice.
* **Remove duplicatas automaticamente**.
* Elementos devem ser **imutáveis** (`int`, `str`, `tuple`, etc).

---

## 🗄️ Como criar conjuntos?

```python
# Criando um conjunto diretamente
frutas = {"maçã", "banana", "laranja"}
print(frutas)  # {'maçã', 'banana', 'laranja'}

# Criando um conjunto a partir de uma lista
numeros = set([1, 2, 2, 3, 4, 4, 5])
print(numeros)  # {1, 2, 3, 4, 5}

# Conjunto vazio (importante!)
vazio = set()   # NÃO usar {} → isso cria um dicionário
print(type(vazio))  # <class 'set'>
```

## 🔄 Como percorrer um conjunto?

Mesmo não sendo ordenados, você pode iterar normalmente com for:

```python
animais = {"cachorro", "gato", "papagaio"}

for animal in animais:
    print(animal)
```

---

## 🧰 Principais métodos e operações

| Método               | Descrição                                     |
| -------------------- | --------------------------------------------- |
| `add(x)`             | Adiciona um elemento.                         |
| `remove(x)`          | Remove `x`, se existir (erro se não existir). |
| `discard(x)`         | Remove `x` sem erro caso não exista.          |
| `union(set2)`        | União dos dois conjuntos.                     |
| `intersection(set2)` | Elementos comuns.                             |
| `difference(set2)`   | Elementos que só existem no primeiro.         |
| `issubset(set2)`     | Verifica se é subconjunto.                    |
| `issuperset(set2)`   | Verifica se é superconjunto.                  |

### 🧪 Exemplo prático

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # União → {1, 2, 3, 4, 5, 6}
print(a & b)   # Interseção → {3, 4}
print(a - b)   # Diferença → {1, 2}
```

## ✅ Quando usar?

* Para eliminar **elementos duplicados** de uma lista.
* Quando quiser realizar **operações matemáticas de conjuntos**.
* Quando não importa a ordem dos elementos e você precisa de **alta performance nas buscas**.

---

## 📝 Conclusão

Agora que você aprendeu sobre conjuntos em Python, é hora de testar seu conhecimento!

**Próximo Capítulo : [Compreensão de Listas](../aula_05/compreensao_listas.md)**

### 📝 Exercícios Moderados — Conjuntos (set)

* *Listas de presença*

Crie dois conjuntos representando a presença de alunos em duas turmas. Depois:

```python
turma_manha = {"Carlos", "Ana", "Beatriz"}
todos_manha = {"Carlos", "Ana", "Beatriz", "Pedro", "Lucas"}
```

1. Mostre os alunos que estiveram nas duas turmas (interseção).
2. Liste os alunos que só estiveram em uma das turmas (diferença simétrica).
3. Conte o total de alunos únicos presentes (união).

* *Remoção de duplicatas*

Você tem uma lista de números com valores repetidos: ``numeros = [1, 2, 3, 2, 4, 3, 5, 1, 6]``

1. Converta essa lista em um conjunto para remover duplicatas.
2. Adicione o número 7.
3. Remova o número 3.
4. Mostre o conjunto final.

* *Alunos aprovados*

Suponha dois conjuntos: *aprovados_matematica* e *aprovados_portugues*.

```python
aprovados_matematica = {"Eduardo", "Ana", "Beatriz", "Lucas", "Pedro", "Mariana", "Juliana"}

aprovados_portugues = {"Ana", "Beatriz", "Pedro", "Lucas", "Marcos", "Juliana", "Fernanda"}

```

1. Liste os alunos aprovados em ambas as disciplinas (interseção).
2. Liste os alunos aprovados em pelo menos uma disciplina (união).
3. Liste os alunos aprovados apenas em uma das disciplinas (diferença simétrica).

**[Gabarito](exercicios/README.md)**
