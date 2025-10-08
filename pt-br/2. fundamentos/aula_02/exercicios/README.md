# 📝 Exercícios — Módulo 2: Operadores de cálculo em Python

Este documento reúne os exercícios da Aula 02, com soluções e explicações breves. O objetivo é compreender como funcionam os operadores aritméticos e operadores de atribuição no Python, aplicados em cálculos do dia a dia.

---

## [🔹 Exercício 01 — Média e Diferença entre Números](Ex_01.py)

**Objetivo:** Ler três números do usuário, calcular a média e a diferença entre o maior e o menor número.

```python
num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))

media = (num_1 + num_2 + num_3) / 3
print(f"A média dos numeros: {media:.2f}")

numeros = [num_1, num_2, num_3]
print(f"A diferença entre {max(numeros)} e {min(numeros)}: {max(numeros) - min(numeros)}")
```

> ➡️ Aplica operadores de soma, divisão e funções ``max()`` e ``min()`` para calcular resultados a partir de entradas do usuário.

---

## [🔹 Exercício 02 — Quadrado, Cubo e Raiz Quadrada](Ex_02.py)

**Objetivo:** Ler um número e mostrar o seu quadrado, cubo e raiz quadrada.

```python
num = float(input("Digite um numero: "))

print(f"O quadrado de {num} = {num ** 2}")
print(f"O cubo de {num} = {num ** 3}")
print(f"A raiz quadrada de {num} = {num ** 0.5:.2f}")
```

> ➡️ Demonstra o uso do operador de exponenciação ** para calcular potência e raiz quadrada.

---

## [🔹 Exercício 03 — Cálculo de Juros Simples](Ex_03.py)

**Objetivo:** Ler o valor de um empréstimo, a taxa de juros e o número de meses, e calcular o valor total a pagar.

```python
valor_emprestimo = float(input("Qual foi o valor do emprestimo?: "))
valor_taxa = float(input("Qual foi o valor da taxa?: "))
meses = int(input("Quantos meses?: "))

total = valor_emprestimo + (valor_emprestimo * valor_taxa * meses)
print(f"O total a pagar após {meses} meses: R$ {total:.2f}")
```

> ➡️ Aplica operadores de multiplicação e soma para calcular juros simples sobre o valor inicial.

---

## [🔹 Exercício 04 — Área e Perímetro de um Retângulo](Ex_04.py)

**Objetivo:** Ler a base e a altura de um retângulo e calcular a área e o perímetro.

```python
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"A área do retângulo: {area}")
print(f"O perímetro do retângulo: {perimetro}")
```

> ➡️ Utiliza operadores de multiplicação e adição para calcular medidas geométricas simples.

---

## 📌 Resumo da Aula

Nesta aula, aplicamos operadores aritméticos e de atribuição para resolver problemas práticos de cálculo, como médias, potências, juros e geometria. Esses exercícios ajudam a consolidar conceitos fundamentais e a construir uma base sólida para problemas mais complexos em Python.

**Próximo capítulo : [Operadores Condicionais](../../aula_03/03_operadores_condicionais.md)**
