# 📝 Exercícios — Módulo 2: Estruturas Condicionais em Python

Este documento reúne exercícios práticos da Aula 06 — Estruturas Condicionais, abordando decisões com ``if``, ``elif`` e ``else``.
O objetivo é fixar a lógica de comparação e tomada de decisão, aplicando-a em situações do dia a dia.

---

## [🔹 Exercício 01 — Verificar se o número é positivo, negativo ou zero](Ex_01.py)

**Objetivo:** Ler um número e verificar sua classificação em relação a zero.

```python
numero = int(input("Digite um numero:"))
if numero < 0:
    print(f"O número {numero} é negativo")
elif numero > 0:
    print(f"O número {numero} é positivo") 
else:
    print("O número é 0")
```

> Explicação
> > Se o número for menor que 0, é negativo.
> > > Se for maior que 0, é positivo.
> > > > Caso não seja nenhum dos dois, só pode ser igual a 0.

---

## [🔹 Exercício 02 — Classificação de idades](Ex_02.py)

**Objetivo:** Ler a idade de uma pessoa e classificá-la em faixas etárias.

```python
idade = int(input("Digite a sua idade:"))

if idade > 0:
    if idade <= 12:
        print("O usuario é uma Criança.")
    elif idade <= 17:
        print("O usuario é um Adolescente.")
    elif idade <= 64:
        print("O usuario é um Adulto.")
    elif idade >= 65:
        print("O usuario é um idoso.")
else:
    print("Idade invalida !")
```

> Explicação:
Aqui, utilizamos comparações encadeadas para organizar a idade em faixas etárias:

1. Criança (até 12 anos).
2. Adolescente (13 a 17 anos).
3. Adulto (18 a 64 anos).
4. Idoso (65 anos ou mais).

---

## [🔹 Exercício 03 — Verificação de notas](Ex_03.py)

**Objetivo:** Ler uma media (0 a 10) e informe se o aluno foi aprovado, reprovado ou se está de recuperação.

```python
media_final = float(input("Digite a média do aluno:"))

if media_final >= 7:
    print("Aprovado ✅")
elif 5 <= media_final < 7:
    print("Recuperação ⚠️")
else:
    print("Reprovado ❌")
```

> Explicação:
O programa avalia a média do aluno e decide sua situação escolar:

1. Média maior ou igual a 7 → aprovado.
2. Média entre 5 e 7 → recuperação.
3. Média menor que 5 → reprovado.

> Esse tipo de estrutura condicional é comum em sistemas acadêmicos.

---

## [🔹 Exercício 04 — Calculadora simples](Ex_04.py)

**Objetivo:** Implementar uma calculadora básica que leia dois números e um operador matemático (``+``, ``-``, ``*``, ``/``).

```python
simbolos = ["+","-","*","X","/"]

num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))

print("+ : Soma")
print("- : Subtracao")
print("X ou * : Multiplicacao")
print("/ : Divisão")
simbolo_usuario = input("Digite um dos simbolos acima:")

if simbolo_usuario in simbolos:
    match simbolo_usuario:
        case "+":
            print(f"{num_1} + {num_2} = {num_1 + num_2}")
        case "-":
            print(f"{num_1} - {num_2} = {num_1 - num_2}")
        case "X" | "*":
            print(f"{num_1} X {num_2} = {num_1 * num_2}")
        case "/":
            if num_2 != 0:
                print(f"{num_1} / {num_2} = {num_1 / num_2}")
            else:
                print("Divisao nao permitida !")
else:   
    print("Nao ha como fazer essa operacao !")
```

> Explicação:
Este exercício simula uma calculadora básica. O usuário escolhe a operação e o programa executa com base no símbolo digitado:

1. ``+`` soma;
2. ``-`` subtração;
3. ``*`` ou ``X`` multiplicação;
4. ``/`` divisão;

> Também foi incluída uma validação importante: a divisão por zero não é permitida, então o programa avisa caso isso aconteça.

---

## Exercício 05 — Maior de três números

**Objetivo:** Encontrar o maior número entre três valores informados.

### [1ª Opção **(função ``sort()``)**](Ex_05_pt1.py)

```python
num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))
num_3 = float(input("Digite o terceiro numero:"))

if num_1 == num_2 == num_3:
    print("Os numeros sao iguais")

numeros = [num_1,num_2,num_3]
numeros.sort()
maior,meio,menor = numeros[0], numeros[1], numeros[2]

print(f"Ordem Crescente : {maior} , {meio} , {menor}")
print(f"Ordem Decrescente : {menor} , {meio} , {maior}")
```

### [2ª Opção **(condicionais + operador ternário)**](Ex_05_pt2.py)

```python
num_1 = float(input("Digite o primeiro numero:"))
num_2 = float(input("Digite o segundo numero:"))
num_3 = float(input("Digite o terceiro numero:"))

if num_1 > num_2 and num_1 > num_3:
    maior = (f"O numero {num_1} é maior")
    print(f"O numero {num_2} é o meio | O numero {num_3} é menor" if num_2 > num_3 else f"O numero {num_3} é o meio | O numero {num_2} é menor")
elif num_2 > num_1 and num_2 > num_3:
    print(f"O numero {num_2} é maior")
    print(f"O numero {num_1} é o meio | O numero {num_3} é menor" if num_1 > num_3 else f"O numero {num_3} é o meio | O numero {num_1} é menor")
elif num_3 > num_1 and num_3 > num_2:
    print(f"O numero {num_3} é maior")
    print(f"O numero {num_2} é o meio | O numero {num_1} é menor" if num_2 > num_1 else f"O numero {num_1} é o meio | O numero {num_2} é menor")
else:
    print("Os números sao iguais")
```

> Explicação:
> > Na primeira versão, todas as comparações são feitas com condicionais.
> > > Na segunda, o Python organiza a lista automaticamente com sort() e o maior número fica na posição [0].

---

**Próximo Capítulo : [Condicionais Aninhadas](../../aula_07/07_condicionais_aninhadas.md)**
