
# 🟨 Tuplas ``(tuple)`` en Python

Las tuplas son otra estructura de datos importante en Python. Son muy similares a las listas, pero con una diferencia fundamental: **son inmutables**, es decir, una vez creadas, sus valores **no se pueden modificar**.

---

## ✅ Creación de tuplas

Puedes crear una tupla utilizando paréntesis `()` y separando los elementos con comas:

```python
# Tupla de frutas
frutas = ("manzana", "plátano", "naranja")

# Tupla mixta
mezcla = (1, "texto", True, 3.14)
```

> 💡 Consejo: ¡Los paréntesis son opcionales! Puedes declarar una tupla simplemente separando los elementos con comas:

```python
números = 1, 2, 3
```

---

## 🔎 ¿Cómo acceder a los elementos?

Al igual que en las listas, puedes acceder a los elementos de la tupla mediante **índices**, comenzando desde cero:

```python
print(frutas[0])    # "manzana"
print(frutas[-1])   # "naranja" (último elemento)
```

> ✅ Los índices negativos también funcionan, al igual que en las listas.

---

## 🚫 Las tuplas son inmutables

Como las tuplas son **inmutables**, intentar modificar un elemento genera un error:

```python
frutas[1] = "uva"  # TypeError
```

**Esto generará un error!** Si necesitas modificarlo, convierte la tupla en una lista:

```python
lista_frutas = list(frutas)
lista_frutas[1] = "uva"
frutas = tuple(lista_frutas)
```

---

## 🧰 Métodos útiles

Al ser inmutables, las tuplas tienen menos métodos que las listas. Los más utilizados son:

| Método    | Función                                                |
|-----------|--------------------------------------------------------|
| `index()` | Devuelve el índice del primer valor encontrado.         |
| `count()` | Cuenta cuántas veces aparece un valor.                  |
| `len()`   | Devuelve el número de elementos.                             |

---

## 💻 Ejemplos prácticos

🔖 `index()`

```python
números = (10, 20, 30, 20)
print(números.index(30))  # Salida: 2
```

🔖 `count()`

```python
números = (10, 20, 30, 20)
print(números.count(20))  # Salida: 2
```

🔖 `len()`

```python
números = (1, 2, 3, 4)
print(len(números))  # Salida: 4
```

---

## 🔁 Iterando con `for`

Las tuplas son iterables, es decir, se pueden recorrer con el bucle `for`:

```python
colores = ("rojo", "azul", "verde")

for color in colores:
    print(color)
```

O si quieres mostrar todo en una línea:

```python
print(", ".join(colores))  # Salida: rojo, azul, verde
```

---

## 📦 Desempaquetado de tuplas

Las tuplas permiten una forma práctica de asignar valores a varias variables a la vez:

```python
punto = (10, 20)
x, y = punto

print(x)  # 10
print(y)  # 20
```

---

## ✅ Conclusión

Las tuplas son ideales cuando necesitas almacenar datos que **no deben modificarse**, como:

- Coordenadas;
- Fechas;
- Registros fijos.

Al final de este contenido, ya serás capaz de:

- Crear tuplas con diferentes tipos de datos;
- Acceder a elementos con índices positivos y negativos;
- Entender la diferencia entre mutabilidad e inmutabilidad;
- Utilizar métodos como `index()`, `count()` y `len()`;
- Recorrer tuplas con el bucle `for`;
- Aplicar el desempaquetado de tuplas.

> ➡️ Las tuplas son sencillas, rápidas y seguras. Saber cuándo utilizarlas es esencial para escribir código eficiente y bien estructurado.

Ahora que ya entiendes bien las **listas** y las **tuplas**, vamos a continuar con los **conjuntos (`set`)** y los **diccionarios (`dict`)**. ¡Sigue estudiando! 💪🐍