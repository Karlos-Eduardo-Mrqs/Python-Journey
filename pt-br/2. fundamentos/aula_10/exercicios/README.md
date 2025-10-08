# 📘 Exercícios Práticos — Estruturas de Repetição e Funções de Iteração

Aqui temos exemplos de como usar loops, funções de iteração e list comprehension em Python.

---

## [🔢 Exercício 1 — Tabuada personalizada](Ex_01.py)

```python
numero = int(input("Digite um numero inteiro:"))
for i in range(1,11):
    print(f"{numero} X {i} = {numero * i}")
```

### 📌 Explicação Exercício_01

> O usuário digita um número. O for percorre de 1 até 10.
> Em cada iteração, imprime a multiplicação (tabuada) do número escolhido.

---

## [➕ Exercício 2 — Somando listas com zip()](Ex_02.py)

```python
lista1 = [10, 20, 30]
lista2 = [1, 2, 3]

somas = [a + b for a, b in zip(lista1, lista2)]
print(somas)
```

### 📌 Explicação Exercício_02

> zip(lista1, lista2) combina os elementos de mesma posição. Exemplo: (10,1), (20,2), (30,3).
> Usamos list comprehension para somar cada par.

---

## [🔤 Exercício 3 — Filtrar nomes com list comprehension](Ex_03.py)

```python
nomes = ["Ana", "João", "Amanda", "Carlos", "André", "Beatriz"]
nomes_com_a = [nome for nome in nomes if nome[0] == "A"]
print(nomes_com_a)
```

### 📌 Explicação Exercício_03

> Percorre a lista de nomes. Mantém apenas os que começam com a letra "A".

---

## [⏳ Exercício 4 — Contagem regressiva com range()](Ex_04.py)

```python
for i in range(10, 0, -1):
    print(i)
```

### 📌 Explicação Exercício_04

> range(10, 0, -1) → começa em 10, vai até 1, diminuindo de 1 em 1. O último valor (0) não é incluído.

---

## [📝 Exercício 5 — Enumerar tarefas com enumerate()](Ex_05.py)

```python
tarefas = ["Lavar a louça", "Estudar Python", "Fazer exercícios", "Ler um livro"]

for indice, tarefa in enumerate(tarefas, start=1):
    print(f"{indice} : {tarefa}")
```

### 📌 Explicação Exercício_05

> enumerate(lista, start=1) retorna índice + item da lista. O parâmetro start=1 faz a contagem começar em 1 (e não em 0).

---

**Próximo Capítulo : [Loopgins Não Contaveis](../../aula_11/11_loopings_nao_contaveis.md)**
