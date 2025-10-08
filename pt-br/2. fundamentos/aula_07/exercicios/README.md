# 📝 Exercícios — Módulo 2: Condicionais aninhadas em Python

Este documento reúne os exercícios da Aula 07, com soluções comentadas e explicações práticas.
O objetivo é praticar o uso de estruturas condicionais (``if elif else``), aplicando-as em problemas reais e situações comuns de lógica de programação.

---

## [🔹 Exercício 02 — Controle de Velocidade e Multa](Ex_02.py)

*Objetivo:* Verificar se a velocidade de um carro está dentro do limite de 80 km/h e calcular multa quando necessário.

```python
velocidade_carro = float(input("Qual foi a velocidade do carro ?:"))

if velocidade_carro <= 80.0:
    print("Dentro do limite")
elif velocidade_carro > 80.0:
    multa = (velocidade_carro - 80) * 5.00
    print(f"Você será multado por R$ {multa:.2f}")
```

> ➡️ Se a velocidade for até 80 km/h, o programa informa que está dentro do limite.
> > ➡️ Se for maior que 80 km/h, calcula a multa de R$ 5,00 por km excedente.

---

## [🔹 Exercício 03 — Jogo do Número Secreto](Ex_03.py)

**Objetivo:** Criar um jogo simples de adivinhação, onde o usuário tenta descobrir um número secreto.

```python
import random 

numero_aleatorio = random.randint(0,10)
numero_usuario = int(input("Digite um numero inteiro entre 0 até 10:"))

if numero_usuario > numero_aleatorio :
    print("Você errou ! O numero é menor que o digitado")
elif numero_usuario < numero_aleatorio:
    print("Você errou ! O numero é maior que o digitado")
else:
    print("Você acertou !")

print(f"O numero secreto é {numero_aleatorio}")
```

> ➡️ O programa gera um número aleatório entre 0 e 10.
> > ➡️ Quando o usuário digitar:

1. **Se digitar um número maior**, o programa avisa que o secreto é menor.
2. **Se digitar um número menor**, avisa que o secreto é maior.
3. **Se acertar**, exibe mensagem de sucesso.

---

## [🔹 Exercício 04 — Verificação de Ano Bissexto](Ex_04.py)

**Objetivo:** Determinar se um ano é bissexto ou não.

```python
ano_usuario = int(input("Digite um ano:"))

if (ano_usuario % 4 == 0 and ano_usuario % 100 != 0) or (ano_usuario % 400 == 0):
    print("O ano é bissexto ! ")
else :
    print("O ano não é bissexto !")
```

> ➡️ Um ano é bissexto se for: Divisível por 4 e não divisível por 100 ou divisível por 400.
> > ➡️ Caso contrário, não é bissexto.

---

**Próximo Capítulo : [Operador Ternário e Match Case](../../aula_08/08_condicionais_match_case_ternario.md)**
