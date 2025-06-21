# 🟥 Conjuntos (`set`) em Python

## 📌 O que são?

Um **conjunto** em Python é uma coleção **não ordenada**, **imutável (individualmente)** e **sem elementos duplicados**. Ideal para realizar operações matemáticas como união, interseção e diferença.

```python
# Exemplo de conjunto
numeros = {1, 2, 3, 2, 1}
print(numeros)  # saída: {1, 2, 3}
```

## 🔑 Características principais

* **Não possui ordem** → não é possível acessar elementos por índice.
* **Remove duplicatas automaticamente**.
* Elementos devem ser **imutáveis** (`int`, `str`, `tuple`, etc).

## 🧰 Principais métodos e operações

| Método               | Descrição                                     |
| -------------------- | --------------------------------------------- |
| `add(x)`             | Adiciona um elemento.                         |
| `remove(x)`          | Remove `x`, se existir (erro se não existir). |
| `discard(x)`         | Remove `x` sem erro caso não exista.          |
| `union(set2)`        | União dos dois conjuntos.                     |
| `intersection(set2)` | Elementos comuns.                             |
| `difference(set2)`   | Elementos que só existem no primeiro.         |
| `issubset(set2)`     | Verifica se é subconjunto.                    |
| `issuperset(set2)`   | Verifica se é superconjunto.                  |

### 🧪 Exemplo prático

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # União → {1, 2, 3, 4, 5, 6}
print(a & b)   # Interseção → {3, 4}
print(a - b)   # Diferença → {1, 2}
```

## ✅ Quando usar?

* Para eliminar **elementos duplicados** de uma lista.
* Quando quiser realizar **operações matemáticas de conjuntos**.
* Quando não importa a ordem dos elementos e você precisa de **alta performance nas buscas**.

---

## 📝 Conclusão

Agora que você aprendeu sobre conjuntos em Python, é hora de testar seu conhecimento!

✅ **Desafios sugeridos:**

1. Crie dois conjuntos representando listas de presença de duas turmas e calcule:

   * Quem compareceu em ambas as turmas (interseção).
   * Quem compareceu apenas em uma das turmas (diferença).
   * O total de alunos únicos presentes (união).

2. Use `add()` para inserir novos alunos nas listas de presença e `remove()` para corrigir ausências.

3. Experimente os métodos `issubset()` e `issuperset()`:

   * Crie um conjunto `turma_A_manha = {"Carlos", "Ana"}`
   * Crie um conjunto `todos_manha = {"Carlos", "Ana", "Pedro"}`
   * Verifique se `turma_A_manha` é subconjunto de `todos_manha` com `issubset()`
   * Verifique se `todos_manha` é superconjunto de `turma_A_manha` com `issuperset()`

> Praticar com situações do dia a dia ajuda a entender melhor o uso real dessa estrutura poderosa.

---

**Próximo Módulo [orientação de objetos](../4.%20orientacao_objetos/readme.md) ou vá para o [bônus](./bonus.md)**