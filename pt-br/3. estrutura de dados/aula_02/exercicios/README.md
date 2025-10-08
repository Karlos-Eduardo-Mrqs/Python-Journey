# Exercícios de Tuplas em Python — Aula 02 (Módulo 3)

Este projeto contém a resolução de exercícios básicos de tuplas em Python, incluindo contagem de elementos, desempacotamento e conversão de listas em tuplas. Abaixo está uma explicação detalhada de cada exercício e do código utilizado.

---

## [🔹 1. Contando elementos em uma tupla](EX_01.py)

```py
tupla_numeros = (1,2,3,2,4,2,5)
cont_2 = tupla_numeros.count(2)

print(f"A tupla tem {len(tupla_numeros)} numeros.")
print(f"A tupla tem o numero 2 aparecendo {cont_2} vezes.")
```

> Explicação:

1. ``tupla_numeros.count(2)`` retorna quantas vezes o número 2 aparece na tupla.
2. ``len(tupla_numeros)`` retorna a quantidade total de elementos da tupla.
3. ``print(f"...")`` exibe os resultados, mostrando o tamanho da tupla e a contagem do número 2.

---

## [🔹 2. Desempacotamento de tuplas](EX_02.py)

```py
coordenadas = (15,30)
eixo_x, eixo_y = coordenadas
print(f"Eixo X:{eixo_x} e Eixo Y:{eixo_y}")
```

> Explicação:

1. ``coordenadas = (15,30)`` cria uma tupla com dois valores.
2. ``eixo_x, eixo_y`` = coordenadas realiza o desempacotamento, atribuindo o primeiro valor a eixo_x e o segundo a eixo_y.
3. ``print(f"...")`` exibe os valores separados dos eixos X e Y.

---

## [🔹 3. Convertendo lista em tupla](EX_03.py)

```py
lista_compras = ["arroz", "feijão", "açúcar"]
lista_compras = tuple(lista_compras)
print(lista_compras)
```

> Explicação:

1. lista_compras é inicialmente uma lista de itens.
2. ``tuple(lista_compras)`` converte a lista em uma tupla.
3. ``print(lista_compras)`` mostra a tupla final.

## 🔹 4. Tentativa de alterar elementos de uma tupla

```py
cores = ("azul", "verde", "vermelho")
cores[1] = "amarelo"
```

> Explicação:

1. Tuplas são imutáveis, ou seja, seus elementos não podem ser alterados depois de criados.
2. Ao tentar executar cores[1] = "amarelo", o Python gera um TypeError:
3. ``TypeError: 'tuple' object does not support item assignment``
4. Para modificar valores, é necessário criar uma nova tupla ou converter para lista, alterar e reconverter para tupla.

**Próximo Capítulo : [Dicionários](../../aula_03/03_dicionarios.md)**
