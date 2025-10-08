# 📝 Exercícios — Módulo 2: Operadores em Python

Este documento reúne os exercícios da Aula 01, com soluções e explicações breves. O objetivo é compreender como funcionam os operadores.

---

## [🔹 Exercício 01 — Operadores Aritméticos](Ex_01.py)

**Objetivo:** Criar um programa que receba dois números e realize as operações básicas de soma, subtração, multiplicação, divisão e exponenciação.

```python
num_1 = int(input("Digite o primeiro numero inteiro:"))
num_2 = int(input("Digite o segundo numero inteiro:"))

print(num_1," + ", num_2 ," = ", num_1 + num_2)
print(num_1," - ", num_2 ," = ", num_1 - num_2)
print(num_1," * ", num_2 ," = ", num_1 * num_2)
print(num_1," / ", num_2 ," = ", num_1 / num_2)
print(num_1," // ", num_2 ," = ", num_1 // num_2)
print(num_1," % ", num_2 ," = ", num_1 % num_2)
print(num_1," ** ", num_2 ," = ", num_1 ** num_2)
```

> ➡️ Mostra todas as operações básicas de forma clara, incluindo divisão inteira // e módulo %.

---

## [🔹 Exercício 02 — Operadores Relacionais](Ex_02.py)

**Objetivo:** Comparar a idade de duas pessoas e verificar quem é mais velho (ou se possuem a mesma idade).

```python
primeira_idade = int(input("Digite a idade da primeira pessoa:"))
segunda_idade = int(input("Digite a idade da segunda pessoa:"))

print("A primeira idade é maior?", primeira_idade > segunda_idade)
print("A segunda idade é maior?", segunda_idade > primeira_idade)
print("As duas idades são iguais?", primeira_idade == segunda_idade)
```

> ➡️ Os operadores relacionais retornam valores booleanos (True ou False).

---

## [🔹 Exercício 03 — Operadores Lógicos](Ex_03.py)

**Objetivo:** Verificar se um número está dentro de uma faixa de valores usando and e or.

```python
numero = int(input("Digite um número inteiro: "))

entre_10_e_20 = numero >= 10 and numero <= 20
fora_do_limite = numero < 10 or numero > 20

print("O número está entre 10 e 20?", entre)
print("O número está fora dessa faixa?", fora)
```

> ➡️ ``and`` exige que as duas condições sejam verdadeiras; ``or`` exige apenas uma.

---

## [🔹 Exercício 04 — Operadores de Membros](Ex_04.py)

**Objetivo:** Conferir se um item fornecido pelo usuário está presente em uma lista de compras.

```python
lista_compras = ["arroz", "feijão", "leite", "pão", "açúcar"]

item = input("Digite um item: ").lower()

print("O item está na lista?", item in lista_compras)
print("O item não está na lista?", item not in lista_compras)
```

> ➡️ O operador in verifica a presença de um elemento; not in verifica a ausência.

---

## [🔹 Exercício 05 — Operadores Bit a Bit](Ex_05.py)

**Objetivo:** Manipular os bits de um número para entender como eles alteram o valor.

```python
num = int(input("Digite um número inteiro: "))

print("Número em binário: ", bin(num))
print("AND (&) com 1:", num & 1)
print("OR (|) com 1:", num | 1)
print("XOR (^) com 1:", num ^ 1)
print("NOT (~):", ~num)
print("Shift Left (<< 1):", num << 1)
print("Shift Right (>> 1):", num >> 1)
```

> ➡️ Mostra como os operadores de bits (&, |, ^, ~, <<, >>) funcionam, alterando a representação binária do número.

---

**Próximo Capítulo : [Operadores de Cálculo](../../aula_02/02_operadores_calculo.md)**
