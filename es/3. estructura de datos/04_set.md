# 🟥 Conjuntos (`set`) en Python

## 📌 ¿O qué?

Un **conjunto** en Python es una colección **no ordenada**, **imutável (individualmente)** y **sem elementos duplicados**. Ideal para realizar operaciones matemáticas como unión, interseção y diferencia.

```python
# Ejemplo de conjunto
numeros = {1, 2, 3, 2, 1}
print(numeros) # dijo: {1, 2, 3}
```

## 🔑 Características principales

* **Não possui ordem** → não é possível acessar elementos por índice.
* **Eliminar duplicados automáticamente**.
* Los elementos deben ser **imutáveis** (`int`, `str`, `tuple`, etc.).

## 🧰 Principios métodos y operaciones

| Método | Descripción |
| -------------------- | --------------------------------------- |
| `añadir(x)` | Addicion um elemento. |
| `eliminar(x)` | Elimine `x`, si existe (error se não existe). |
| `descartar(x)` | Elimine `x` sin error si no existe. |
| `unión(conjunto2)` | União dos dos conjuntos. |
| `intersección(conjunto2)` | Elementos comunes. |
| `diferencia(conjunto2)` | Elementos que sí existen en el primer momento. |
| `issubconjunto(conjunto2)` | Verifique que sea un subconjunto. |
| `issuperset(set2)` | Verifica que sea superconjunto. |

### 🧪 Ejemplo práctico

```python
un = {1, 2, 3, 4}
segundo = {3, 4, 5, 6}

print(a | b) # Unión → {1, 2, 3, 4, 5, 6}
print(a & b) # Intersección → {3, 4}
print(a - b) # Diferencia → {1, 2}
```

## ✅ ¿Cuándo usar?

* Para eliminar **elementos duplicados** de una lista.
* Cuando quiera realizar **operações matemáticas de conjuntos**.
* Quando não importa a ordem dos elementos y você precisa de **alta performance nas buscas**.

---

## 📝 Conclusión

Ahora que aprendes sobre conjuntos en Python, ¡es hora de probar tu conocimiento!

✅ **Desafíos sugeridos:**

1. Crie dois conjuntos representando listas de presencia de dos turmas e calcule:

* Quem compareceu em ambas as turmas (interseção).
* Quem compareceu apenas em uma das turmas (diferencia).
* O total de alunos únicos presentes (união).

2. Utilice `add()` para insertar nuevos todos en las listas de presencia y `remove()` para corregir otras opciones.

3. Experimente con los métodos `issubset()` y `issuperset()`:

* Llora un conjunto `turma_A_manha = {"Carlos", "Ana"}`;
* Llora un conjunto `todos_manha = {"Carlos", "Ana", "Pedro"}`;
* Verifique que `turma_A_manha` sea un subconjunto de `todos_manha` con `issubset()`;
* Verifique que `todos_manha` sea un superconjunto de `turma_A_manha` con `issuperset()`;

> Praticar com situações do dia a dia ajuda a entender melhor o uso real dessa estrutura poderosa.

---

**Next Module [object orientation](../4.%20orientacion_objetos/README.md) or go to [bonus](bonus.md)**
