# 📘 Exercícios — Estruturas de Controle (while, break, continue, pass)

Aqui estão alguns exemplos de uso de loops e instruções de controle em Python.

---

## [🔄 Exercício 1 — Contador com while](Ex_01.py)

```python
contador = 0
while True:
    if contador == 20:
        break
    contador += 1
    print(contador)
```

### 📌 Explicação Exercício_01

> O while True cria um loop infinito. O if contador == 20: break interrompe o loop ao chegar em 20.
> Em cada volta, o contador aumenta em 1 e é exibido.

---

## [➕ Exercício 2 — Soma de números até o usuário digitar 0](Ex_02.py)

```python
soma = 0
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero == 0 :
        break
    soma += numero

print(soma)
```

### 📌 Explicação Exercício_02

> O programa pede números repetidamente. Quando o usuário digita 0, o break interrompe o loop.
> Caso contrário, o valor digitado é somado à variável soma.

---

## [🔢 Exercício 3 — Filtro com continue](Ex_04.py)

```python
for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)
```

### 📌 Explicação Exercício_03

> O for percorre os números de 1 a 10. Quando o número for múltiplo de 3, o continue pula para a próxima iteração.
> Assim, apenas os que não são múltiplos de 3 são exibidos.

## [⛔ Exercício 4 — Interromper com break](Ex_04.py)

```python
numeros = []
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero < 0 :
        break
    numeros.append(numero)

print(numeros)
```

### 📌 Explicação Exercício_04

> O usuário digita números que são armazenados na lista numeros. Se digitar um número negativo, o break para o loop. Por fim, a lista é exibida.

---

## [🚩 Exercício 5 — Marcador de pass](Ex_05.py)

```python
for i in range(1, 6):
    print(i if i != 3 else "..")
```

### 📌 Explicação Exercício_05

> O for percorre de 1 a 5. Quando o número for 3, é substituído por "..".
> O pass normalmente é usado como marcador de código vazio, mas aqui foi adaptado para marcar visualmente.

---

**Próximo Capítulo : [Funções](../../aula_12/12_funcoes.md)**
