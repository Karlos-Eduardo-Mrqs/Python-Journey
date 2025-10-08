# 📝 Exercícios — Módulo 2: Operadores condicionais em Python

Este documento reúne os exercícios da Aula 04, com soluções comentadas e explicações práticas. O objetivo é compreender o uso dos operadores de verificação em Python, aplicando-os em situações do dia a dia para comparações de identidade e pertencimento de objetos.

---

## [🔹 Exercício 01 — Identidade de Objetos (``is`` / ``is not``)](Ex_01.py)

**Objetivo:** Verificar se duas variáveis apontam para o mesmo objeto na memória.

```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print("lista1 é lista2?:", lista1 is lista2)

lista3 = lista1
print("lista1 é lista3?:", lista1 is lista3)
```

> ➡️ **``is`` verifica se duas variáveis apontam para o mesmo objeto na memória.**
> >➡️ **``is not`` retorna o inverso, ou seja, ``True`` se não forem o mesmo objeto.**
> > >➡️ Mesmo que ``lista1`` e ``lista2`` tenham o mesmo conteúdo, são objetos diferentes → ``lista1 is lista2`` é ``False``.
> > > >➡️ Quando atribuimos ``lista3 = lista1``, ambas as variáveis referenciam o mesmo objeto → ``lista1 is lista3`` é ``True`` e ``lista1 is not lista3`` é ``False``.

---

## [🔹 Exercício 02 — Pertencimento em uma Lista (``in`` / ``not in``)](Ex_02.py)

**Objetivo:** Verificar se um elemento digitado pelo usuário está presente em uma lista de frutas.

```python
frutas = ["maçã", "banana", "laranja", "uva", "pera"]

item = input("Digite o nome de uma fruta: ").lower()

print(f"O item está na lista?: {item in frutas}")
print(f"O item não está na lista?: {item not in frutas}")
```

> ➡️ Usa ``in`` para checar presença do item e ``not in`` para checar ausência.
> > ➡️ Retorna ``True`` ou ``False`` de acordo com a existência do elemento na ``lista``.

---

## 📌 Conclusão

Nesta aula, exploramos **os operadores de verificação**, aprendendo a:

- Usar ``is`` e ``is not`` para identificar se duas variáveis compartilham o mesmo objeto

- Aplicar ``in`` e ``not in`` para verificar pertencimento de elementos em sequências

- Diferenciar igualdade de ``valor (==)`` de identidade de objeto ``(is)``

> **💡 Dica: Sempre que for necessário comparar conteúdo, use ==. Para verificar referência de memória, use is ou is not.**

**Próximo Capítulo : [Resumo Geral dos Operadores em Python](../../aula_05/05_resumo_operadores.md)**
