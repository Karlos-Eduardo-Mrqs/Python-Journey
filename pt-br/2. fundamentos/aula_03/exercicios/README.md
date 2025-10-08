# 📝 Exercícios — Módulo 2: Operadores condicionais em Python

Este documento reúne os exercícios da Aula 03, com soluções comentadas e explicações práticas. O objetivo é compreender o uso dos operadores condicionais em Python, aplicando-os em situações do dia a dia para verificação de condições, comparações e decisões lógicas.

---

## [🔹 Exercício 01 — Verificação de Idade para Carteira de Motorista](Ex_01.py)

**Objetivo:** Pedir a idade do usuário e informar se ele pode tirar a carteira de motorista (idade >= 18).

```python
idade = int(input("Digite a idade do usuário: "))
print("Obs.: True = Verdadeiro e False = Falso")
print(f"O usuário pode dirigir?: {idade >= 18}")
```

> ➡️ O operador >= compara se a idade é maior ou igual a 18.
> > ➡️ O resultado da comparação é booleano (True ou False).
> > > ➡️ A f-string f"" permite inserir diretamente o resultado da comparação na mensagem exibida.

---

## [🔹 Exercício 02 — Verificação de Aprovação do Aluno](Ex_02.py)

**Objetivo:** Perguntar duas notas do aluno, calcular a média e informar se ele foi aprovado (média >= 7).

```python
primeira_nota = float(input("1ª nota: "))
segunda_nota = float(input("2ª nota: "))

media = (primeira_nota + segunda_nota) / 2
print("Obs.: True = Verdadeiro e False = Falso")
print(f"A média do aluno: {media:.1f}")
print(f"Então, o aluno passou?: {media >= 7}")
```

> ➡️ Calcula a média usando operadores aritméticos.
> > ➡️ O operador >= é usado para comparar se a média é suficiente para aprovação.
> > > ➡️ A f-string f"" com :.1f formata a média com uma casa decimal.

---

## [🔹 Exercício 03 — Número Positivo/Negativo e Par/Ímpar](Ex_03.py)

**Objetivo:** Ler um número inteiro e mostrar:

1. Se ele é positivo, negativo ou zero.
2. Se ele é par ou ímpar.

```python
numero = int(input("Digite um número inteiro: "))

print("Obs.: True = Verdadeiro e False = Falso")
print(f"O número é positivo?: {numero >= 0}")
print(f"O número é negativo?: {numero < 0}")
print(f"O número é zero?: {numero == 0}")
print(f"O número é par?: {numero % 2 == 0}")
print(f"O número é ímpar?: {numero % 2 == 1}")
```

> ➡️ Usa operadores relacionais (>=, <, ==) para verificar condições numéricas.
> > ➡️ Usa o operador módulo % para verificar se o número é divisível por 2 (par ou ímpar).
> > > ➡️ Retorna True ou False, mostrando o resultado de cada condição.

---

## 📌 Resumo da Aula

Nesta aula, aplicamos operadores condicionais para resolver problemas práticos:

- Comparações com ``>=  <= <  >  ==``
- Combinações de condições com ``and``
- Verificação de resultados booleanos (``True`` ou ``False``)
- Uso de ``f-strings`` para exibir resultados de forma clara e formatada

> ➡️ Esses exercícios ajudam a consolidar a lógica de decisão em Python e preparam para estruturas condicionais mais avançadas (if, elif, else).

**Próximo Capítulo : [Operadores de Verificação](../../aula_04/04_operadores_verificacao.md)**
