# 📝 Exercícios — Módulo 2: Condicionais aninhadas em Python

Este repositório reúne os exercícios da Aula 08 do Módulo 2, voltados para condicionais aninhadas em Python. O objetivo é fortalecer a compreensão do uso das estruturas ``if, elif e else`` em situações do dia a dia, aplicando lógica de programação para resolver problemas práticos.

---

## Exercício_01 — Mês do ano

**Objetivo:** Ler um número de 1 a 12 e exibir o mês correspondente. Caso o número não esteja no intervalo, exibir "Mês inválido".

### [1ª Opção (usando match case)](Ex_01_pt1.py)

```python
mes = int(input("Digite o numero de um mes:"))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Não existe esse mês")
```

### [2ª Opção (usando lista e índice)](Ex_01_pt2.py)

```python
lista_dos_meses = ["...","Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
mes = int(input("Digite o numero de um mes:"))

if mes >= 1 and mes <= 12:
    print(f"O mês que você digitou é {lista_dos_meses[mes]}")
else:
    print("Não existe")
```

> Explicação:
> > Na 1ª versão, usamos o ``match case`` para associar diretamente cada número ao seu mês. É mais didático e detalhado, mas gera bastante repetição de código.
> > > Na 2ª versão, usamos uma lista onde a posição corresponde ao número do mês. Assim, o programa fica mais enxuto e fácil de expandir.

---

## [Exercício_02 — Maioridade (operador ternário)](Ex_02.py)

**Objetivo:** Ler a idade de uma pessoa e informar se ela é maior ou menor de idade usando operador ternário.

```python
idade = int(input("Digite a sua idade:"))
maior_de_idade = "Maior de idade" if idade >= 18 else "Menor de idade"
print(maior_de_idade)
```

> Explicação:
No exemplo, a condição idade >= 18 é avaliada:
> > Se ``True``, a variável ``maior_de_idade`` recebe ``"Maior de idade"``.
> > > Se ``False``, recebe ``"Menor de idade"``.

Em seguida, imprimimos a variável, mostrando diretamente o resultado da decisão.

---

## [Exercício_03 — Sistema de Notas com condicionais](Ex_03.py)

**Objetivo:** Implemente um programa que leia uma letra de conceito (A, B, C, D ou F) para exibir a mensagem correspondente

```python
media_final = float(input("Digite a média entre (0 até 10):"))
 
if media_final <= 4:
    print("O aluno é Classe F !")
elif media_final <= 5 and media_final <= 5.9:
    print("O aluno é Classe E !") 
elif media_final >= 6 and media_final <= 6.9:
    print("O aluno é Classe D !")
elif media_final >= 7 and media_final <= 7.9:
    print("O aluno é Classe C !")
elif media_final >= 8 and media_final <= 8.9:
    print("O aluno é Classe B !")
elif media_final >= 9 and media_final <= 10:
    print("O aluno é Classe A !")

```

> Explicação:
    1. O Python verifica as condições de cima para baixo.
    2. Assim que uma condição True é encontrada, o respectivo bloco é executado e todas as demais condições são ignoradas.
    3. Essa estrutura garante que cada média seja classificada em apenas uma faixa.

*Obs.:* Não há necessidade de else final, mas poderia ser usado para capturar valores inválidos (ex.: médias negativas ou acima de 10).

---

## [Exercício_04 — Categoria de IMC](Ex_04.py)

**Objetivo:** Crie um programa que leia o peso e a altura de uma pessoa e calcule o IMC.

```python
print("Calculadora de Indice de Massa Corporal")

altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))
IMC = peso / (altura ** 2)

if IMC <= 18.5:
    print("Você está: ABAIXO DO PESO")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Você está: PESO NORMAL")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Você está: SOBREPESO")
elif IMC >= 30:
    print("Você está: OBESIDADE")
```

**Explicação:**
Cada IMC será classificado em apenas uma categoria:
    1. *Faixa 1:* IMC ≤ 18.5 → Abaixo do peso
    2. *Faixa 2:* 18.5 ≤ IMC ≤ 24.9 → Peso normal
    3. *Faixa 3:* 25 ≤ IMC ≤ 29.9 → Sobrepeso
    4. *Faixa 4:* IMC ≥ 30 → Obesidade

---

**Próximo Capítulo : [Loopings](../../aula_09/09_loopings.md)**
