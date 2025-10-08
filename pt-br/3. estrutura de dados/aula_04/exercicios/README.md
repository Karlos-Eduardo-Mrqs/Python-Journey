# Exercícios de Conjuntos em Python — Aula 04 (Módulo 3)

Este projeto contém a resolução de exercícios de conjuntos em Python, abordando operações como interseção, diferença, união, remoção de duplicatas e listagem de alunos/aprovados.

---

## [🔹 1. Listando alunos em turmas](EX_01.py)

```py
def listar_turma(set_lista:set,status:str):
    print(status)
    print("--------------------------------------------------")
    for aluno in set_lista:
        print(aluno)
    print("--------------------------------------------------")

turma_manha = {"Carlos", "Ana", "Beatriz"}
todos_manha = {"Carlos", "Ana", "Beatriz", "Pedro", "Lucas"}

lista_alunos_em_todas_as_turmas = turma_manha.intersection(todos_manha)
lista_alunos_somente_na_manha = todos_manha.difference(turma_manha)
qtd_alunos = len(turma_manha.union(todos_manha))

print(f"Temos no total {qtd_alunos} alunos em todas as turmas !")

listar_turma(lista_alunos_em_todas_as_turmas,"Alunos que estão em todas as turmas")
listar_turma(lista_alunos_somente_na_manha,"Alunos que estão somente de manhã")
```

> Explicação:

1. ``intersection`` retorna os alunos que estão em ambas as turmas.
2. ``difference`` retorna os alunos que estão apenas na turma de manhã.
3. ``union`` retorna todos os alunos únicos presentes em todas as turmas, usado para contar o total.
4. ``listar_turma`` percorre e exibe cada aluno do conjunto.

---

## [🔹 2. Removendo duplicatas de uma lista](EX_02.py)

```python
def remover_repeticao(lista:list) -> set:
    lista_nova = set()
    for numero in lista:
        lista_nova.add(numero)
    return lista_nova

def listar_set(set_lista:set,status:str):    
    print(status)
    print("-----------------------------------------------------")
    for numero in set_lista: 
        print(f"Numero : {numero}")
    print("-----------------------------------------------------")

lista_numeros = [1, 2, 3, 2, 4, 3, 5, 1, 6] 
lista_nova = remover_repeticao(lista_numeros)
listar_set(lista_nova,"Lista nova sem repetição ! ")

lista_nova.add(7)
lista_nova.remove(3)

listar_set(lista_nova,"Lista atualizada !")
```

> Explicação:

1. ``remover_repeticao`` converte a lista em um conjunto, eliminando números repetidos automaticamente.
2. ``add()`` adiciona o número 7 ao conjunto.
3. ``remove()`` remove o número 3 do conjunto.
4. ``listar_set`` percorre o conjunto e exibe cada número, garantindo que não haja repetição.

---

## [🔹 3. Aprovados em diferentes matérias](EX_03.py)

```py
def listar_aprovados(lista_aprovados:set,status:str):
    print(status)
    print("--------------------------------------------------")
    for aprovado in lista_aprovados:
        print(aprovado)
    print("--------------------------------------------------")

aprovados_matematica = {"Eduardo", "Ana", "Beatriz", "Lucas", "Pedro", "Mariana", "Juliana"}
aprovados_portugues = {"Ana", "Beatriz", "Pedro", "Lucas", "Marcos", "Juliana", "Fernanda"}

lista_aprovados_em_ambas = aprovados_matematica.intersection(aprovados_portugues)
lista_aprovados_em_portugues = aprovados_portugues.difference(aprovados_matematica)
lista_aprovados_em_matematica = aprovados_matematica.difference(aprovados_portugues)

listar_aprovados(lista_aprovados_em_ambas,"Aprovados em todas as matérias")
listar_aprovados(lista_aprovados_em_portugues,"Aprovados em Português")
listar_aprovados(lista_aprovados_em_matematica,"Aprovados em Matemática")
```

> Explicação:

1. ``intersection`` retorna os alunos aprovados em todas as matérias.
2. ``difference`` retorna os alunos aprovados apenas em uma matéria específica (Matemática ou Português).
3. ``listar_aprovados`` percorre o conjunto e exibe cada aluno.

> Essas operações permitem comparar listas de aprovados e identificar quem foi bem-sucedido em mais de uma disciplina.

**Próximo Capítulo : [Compreensão de listas](../../aula_05/aula_05_compreensao_listas.md)**
