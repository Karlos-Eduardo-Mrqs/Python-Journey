# 🟨 Diccionarios (`dict`) en Python

## 📌 ¿O qué?

Un **dicionário** es una estructura de dados que armazena pares de **chave → valor**. Es una colección **mutável**, **desordenada** (até o Python 3.6) e **indexada por chave**, no por posición.

```python
# Ejemplo de diccionario
aluno = {"nome": "Carlos", "idade": 20, "curso": "Python"}
print(aluno["nombre"]) # saída: Carlos
```

## 🔑 Características principales

* As **chaves são únicas**.
* Os **valores podem ser de cualquier tipo**.
* Como chaves normalmente son `str`, `int`, o `tuple` imutáveis.

## 🧰 Principios métodos y operaciones

| Método | Descripción |
| ----------- | -------------------------------------------------- |
| `dict[clave]` | Acessa o valor da chave `key`. |
| `obtener (clave)` | Retorna o valor da chave ou `None` no existe. |
| `claves()` | Retorna todas las chaves. |
| `valores()` | Retorna todos los valores. |
| `elementos()` | Retorna os pares (chave, valor). |
| `actualizar()` | Atualiza con nuevos pares. |
| `pop(tecla)` | Retire o par com a chave dada. |

### 🧪 Ejemplo práctico

```python
libro = { 
"título": "Python Básico", 
"autor": "João Silva", 
"año": 2025
}

# Acceder al título del libro
print(libro["título"])

# Agregar nuevo par, número de páginas
libro["páginas"] = 300

# Atualizar el valor del año
libro["ano"] = 2024

# Iterar sobre el diccionario
para chave, valor en livro.items(): 
print(f"{chave}: {valor}")
```

## ✅ ¿Cuándo usar?

* Quando você precisa **asociar um dado a uma chave significativa**.
* Para **armazenar atributos de un objeto**, como en un catastro.

---

## 📝 Conclusión

Ahora que entiendes cómo funcionan los diccionarios en Python, ¡es hora de practicar!

✅ **Desafíos sugeridos:**

1. Grite un diccionario que represente una película, con información como título, director, año y género.
2. Actualizar los valores, agregar nuevos pares y eliminar una llave.
3. Percorra os itens com um for e exiba todas as informações de forma formatada.

> Praticar é a melhor forma de consolidar o aprendizado! Pruebe diferentes combinaciones, explore los métodos y abuse de print() para observar los resultados.

**Próximo archivo [Set](./set.md)**
