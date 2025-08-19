# 🌀 Bonus: Comprensiones de Listas en Python

## 📌 ¿Qué es una comprensión?

Una **comprensión** es una forma concisa de crear nuevas secuencias (como listas, conjuntos o diccionarios) aplicando una expresión a cada elemento de un iterable.

Ayuda a que tu código sea **más limpio, más corto y, a menudo, más legible**.

```python
# Manera tradicional
cuadricula = []
for i in range(5):
    cuadricula.append(i * i)

# Con compreensão de lista
cuadricula = [i * i for i in range(5)]
```

---

## 🧩 Comprensión de listas — Sintaxis

```python
[expresión para elemento en iterable si condición]
```

* `expresión`: qué se desea hacer con cada elemento
* `elemento`: cada elemento del iterable
* `condición` (opcional): filtrar los elementos a incluir

### ✅ Ejemplos

```python
# Todos los números pares entre 0 ... 10
evens = [x for x in range(11) if x % 2 == 0]

# Los números al cuadrado hasta el número 6
cuadricula = [x**2 for x in range(1, 6)]

# Convierte la lista de palabras y las convierte en palabras en mayúsculas
palabras = ["python", "rocks"]
palavras_mayusculas = [palabras.upper() for palabra in palabras]
```

---

## 🔄 Conjunto Comprensiones y Diccionarios

### Conjunto

```python
tamano = {len(palabra) for palabra in ["hello", "world", "hi"]}
```

### Diccionario

```python
numeros_al_cuadricula = {x: x**2 for x in range(1, 6)}
print(numeros_al_cuadricula)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🧪 ¡Hora del reto!

Intenta resolver estos problemas usando comprensiones:

1. Crea una lista de los primeros 10 múltiplos de 3.

2. Construye un conjunto de caracteres únicos (sin espacios) a partir de una oración.

3. Crea un diccionario que asigne los números del 1 al 5 a su factorial.

---

## 🎯 ¿Por qué usar comprensiones?

* Escribe código más limpio y expresivo
* Evita texto repetitivo innecesario
* Transformaciones más fáciles de identificar rápidamente

Pero recuerda: **no sacrifiques la legibilidad por la concisión**. Si se vuelve demasiado complejo, un bucle regular podría ser mejor.

---

> 🚀 Dominar las comprensiones hará que tu código Python sea más rápido de escribir y más fácil de leer. ¡Una pequeña inversión para una mayor claridad!

**Siguiente módulo [orientacion_objetos](../4.%20orientacion_objetos/README.md)**
