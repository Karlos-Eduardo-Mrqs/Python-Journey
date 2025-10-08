# 🔁 Exercícios de Estruturas de Repetição em Python

Este material apresenta exemplos práticos de como utilizar loops (for e while), bem como instruções especiais como break, continue e list comprehensions no Python.

Cada exercício é acompanhado de uma breve explicação do que o código faz.

---

## [1. 📊 Contar de 1 a 10 usando for](Ex_01.py)

```python
for i in range(1, 11):
    print(i, "..")
```

> 🔹 O for percorre um intervalo definido por range(1, 11), imprimindo os números de 1 a 10. ➡️ Ideal para contagens simples.

---

## [2. ⏳ Contador com while](Ex_02.py)

```python
contador = 0
while contador != 20:
    contador += 2
    print(contador, '..')
```

> 🔹 O while repete enquanto a condição for verdadeira.
> Neste caso, soma +2 até atingir 20, exibindo os números pares entre 2 e 20. ➡️ Bom para laços baseados em condições.

---

## [3. ➕ Soma de uma lista com for](Ex_03.py)

```python
numeros = [8,7,9,8,5,5,6,10,4,5,8,2,3]
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma dos numeros da lista : {soma}")
```

> 🔹 O for percorre cada elemento da lista e acumula os valores em soma. ➡️ Útil para operações acumulativas.

---

## [4. 🛑 Busca com break](Ex_04.py)

```python
lista_numeros = []
while True:
    numero = int(input("Digite um numero inteiro:"))
    if numero == 0:
        break    
    lista_numeros.append(numero)

if len(lista_numeros) == 0:
    print("A lista está vazia !")

for index, numero in enumerate(lista_numeros):
    print(f"indice : {index} | numero : {numero}")
```

> 🔹 O while True cria um loop infinito, interrompido apenas quando o usuário digita 0 (comando break). ➡️ Muito usado em programas que esperam entradas do usuário.

---

## [5. ⚖️ Filtrar pares com continue](Ex_05.py)

```python
numeros = [i for i in range(1, 11)]
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero, "..")
```

> 🔹 O continue faz o loop ignorar os ímpares, imprimindo apenas os números pares de 1 a 10. ➡️ Excelente para pular condições indesejadas.

---

## 6. 🧮 Compreensão de listas (List Comprehension)

```python
numeros = [i ** 2 for i in range(1, 11)]
print(numeros)
```

> 🔹 Cria uma lista com os quadrados de 1 a 10 em uma única linha de código. ➡️ Sintaxe compacta e eficiente para criar listas transformadas.

---

**Próximo Capítulo : [Loopings Contáveis](../../aula_10/10_loopings_contaveis.md)**
