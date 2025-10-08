# Exercícios de Listas em Python — Aula 01 (Módulo 3)

Este projeto contém a resolução de exercícios básicos de listas em Python, incluindo manipulação de números, controle de estoque e notas de alunos. Abaixo está uma explicação detalhada de cada exercício e do código utilizado.

---

## [🔹 1. Lista de Números](EX_01.py)

```py

lista_num = [num for num in range(0,11)]
print(f"Primeiro número é:{lista_num[0]}")
indice_num5 = lista_num.index(5)
lista_num[indice_num5] = 50
print(lista_num)
```

> Explicação:

1. ``[num for num in range(0,11)]`` cria uma lista com números de 0 a 10.
2. ``lista_num[0]`` acessa o primeiro elemento da lista.
3. ``lista_num.index(5)`` encontra a posição do número 5 na lista.
4. ``lista_num[indice_num5] = 50`` substitui o número 5 por 50.
5. ``print(lista_num)`` exibe a lista final atualizada.

---

## [🔹 2. Controle de Estoque](EX_02.py)

```py

lista_itens = ["arroz","feijao","macarrao"]
lista_itens.append("açucar")
lista_itens.insert(1,"sal")
lista_itens.remove("feijao")
print(lista_itens)
```

> Explicação:

1. ``append("açucar")`` adiciona o item "açúcar" ao final da lista.
2. ``insert(1, "sal")`` insere "sal" na posição 1 (segunda posição).
3. ``remove("feijao")`` remove o item "feijão" da lista.
4. ``print(lista_itens)`` mostra a lista final de estoque.

---

## [🔹 3. Notas de Alunos](EX_03.py)

```py
lista_notas = [7.5,8.0,6.0,9.0,10.0]
media = sum(lista_notas) / len(lista_notas)
maior_nota = max(lista_notas)
menor_nota = min(lista_notas)

print(f"Média: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
```

> Explicação:

1. ``sum(lista_notas) / len(lista_notas)`` calcula a média das notas.
2. ``max(lista_notas)`` encontra a maior nota.
3. ``min(lista_notas)`` encontra a menor nota.
4. ``print(f"...")`` exibe os resultados formatados.

---

**Próximo Capítulo : [Tuplas](../../aula_02/02_tuplas.md)**
