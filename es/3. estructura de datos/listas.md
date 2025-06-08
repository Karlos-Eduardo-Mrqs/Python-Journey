# 🟩 Listas (`list`) en Python

Las listas son una de las estructuras de datos más utilizadas en Python. Almacenan colecciones **ordenadas** de elementos y pueden modificarse en cualquier momento.

## ✅ Creación de listas

Puedes crear una lista utilizando corchetes `[]` y separando los elementos con comas.

```python
# Lista de frutas
frutas = ["manzana", "plátano", "naranja"]

# Lista mixta
mezcla = [1, "texto", True, 3.14]
```

## 🔍 ¿Cómo acceder a los elementos?

```python
print(frutas[0])    # 'manzana'
print(frutas[-1])   # "naranja" (último elemento)
```

## ✏️ Cómo cambiar un elemento

```python
frutas[1] = "uva"
print(frutas)  # ["manzana", "uva", "naranja"]
```

## 🧰 Métodos más utilizados

| Método      | Qué hace                             |
| ----------- | ------------------------------------- |
| `append()`  | Añade un elemento al final de la lista    |
| `insert()`  | Inserta un elemento en una posición         |
| `remove()`  | Elimina la primera aparición del valor |
| `pop()`     | Elimina y devuelve el elemento por índice      |
| `clear()`   | Elimina todos los elementos de la lista        |
| `sort()`    | Ordena los elementos de la lista              |
| `reverse()` | Invierte el orden de la lista              |
| `len()`     | Devuelve el número de elementos             |

### 💻 Ejemplos prácticos

> 🔖 ``append()``

```python
frutas = ["manzana", "plátano"]
frutas.append("naranja")
print(frutas)  # ["manzana", "plátano", "naranja"]
```

> 🔖 ``insert()``

```python
frutas = ["manzana", "naranja"]
frutas.insert(1, "plátano")
print(frutas)  # ["manzana", "plátano", "naranja"]
```

> 🔖 ``remove()``

```python
frutas = ["manzana", "plátano", "naranja"]
frutas.remove("plátano")
print(frutas)  # ["manzana", "naranja"]
```

> 🔖 ``pop()``

```python
frutas = ["manzana", "plátano", "naranja"]
item = frutas.pop(1)
print(item)    # "plátano"
print(frutas)  # ["manzana", "naranja"]
```

> 🔖 ``clear()``

```python
frutas = ["manzana", "plátano", "naranja"]
frutas.clear()
print(frutas)  # []
```

> 🔖 ``sort()``

```python
frutas = ["plátano", "manzana", "naranja"]
frutas.sort()
print(frutas)  # ["plátano", "naranja", "manzana"]
```

> 🔖 ``reverse()``

```python
frutas = ["plátano", "manzana", "naranja"]
frutas.reverse()
print(frutas)  # ["naranja", "manzana", "plátano"]

> 🔖 ``len()``

```python
frutas = ["manzana", "plátano", "naranja"]
print(len(frutas))  # 3
```

### 🔁 Cómo usar for con listas

Puedes recorrer todos los elementos de una lista usando un for.

```python
frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(fruta) # manzana, plátano , naranja 

```

---

# ✅ Conclusión

Las listas son uno de los pilares de la programación en Python. Permiten almacenar, organizar y manipular colecciones de datos de forma fácil y potente.

Después de esta sección, ya eres capaz de:

- Crear listas con diferentes tipos de datos;
- Acceder y modificar elementos;
- Usar métodos útiles como append(), pop(), sort() y muchos otros;
- Recorrer listas con for;
- ¡Resolver retos prácticos con listas!

Ahora que conoces bien esta estructura, prueba a crear tus propios programas con listas y comprueba en la práctica cómo pueden facilitarte la vida como programador Python. 💡🐍

> ➡️ Dominar las listas es esencial para continuar con temas más avanzados como estructuras de repetición, funciones e incluso manipulación de archivos y datos.

## 🧪 ¡Reto!

Intenta hacerlo tú mismo:

1. Crea una lista con 5 nombres.
2. Ordena la lista.
3. Elimina el tercer nombre.
4. Añade 2 nombres nuevos.
5. Muestra el resultado final con print().

**Seguiente archivo [Tuplas](./tuplas.md)**