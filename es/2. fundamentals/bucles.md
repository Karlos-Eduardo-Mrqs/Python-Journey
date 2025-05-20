# ⚙️ Estructuras de repetición en Python

Las estructuras de repetición permiten que un bloque de código se ejecute varias veces, en función de una condición o de un número específico de iteraciones. Son esenciales para automatizar tareas repetitivas y procesar grandes volúmenes de datos de manera eficiente.

## 📌 ¿Por qué son importantes?

- Permiten automatizar tareas repetitivas;
- Facilitan el tratamiento de las recogidas de datos;
- Hacen que el código sea más compacto y fácil de entender;

## 🔷 Principales tipos de repetición

### 🔹 para

La estructura for se utiliza para iterar sobre una secuencia (como una lista, una tupla, una cadena o un rango de números). Es ideal para cuando sabes el número de iteraciones que quieres realizar.

> ✅ Sintaxis:

```python
for item in sequencia:
# bloque de código
```

> 📌 Ejemplo de uso: Iterar sobre una lista de números e imprimir cada uno.

```python
números = [1, 2, 3, 4, 5]
for numero in números:
imprimir (número)
```

### 🔷 mientras

La estructura while ejecuta un bloque de código mientras una condición sea verdadera. Es útil cuando el número de iteraciones no se conoce de antemano.

> ✅ Sintaxis:

```python
while condición:
# bloque de código
```

> 📌 Ejemplo de uso: Imprimir números del 1 al 5 con while.

```python
contar = 1
while contador <= 5:
    imprimir(contador)
    contador += 1
```

## 🔹 break, continue, and pass

Estas declaraciones cambian el comportamiento predeterminado de los bucles como for y while.

### 🔸 break

La declaración break se utiliza para detener un bucle prematuramente. Cuando Python encuentra una interrupción, sale inmediatamente del bucle y continúa ejecutando el código después del bucle.

> 📌 Example of use with break:

```python
number = 0
for number in range(10):
    print(number) # 0, 1 , 2 , 3 , 4 , 5
if number == 5:
    break # Stops the loop when the number is 5
print(number)
```

### 🔸 continue

La declaración continue hace que el bucle omita la iteración actual y pase directamente a la siguiente iteración, sin ejecutar el resto del código dentro del bucle para la iteración actual.

> 📌 Ejemplo de uso con continue:

```python
number = 0
for number in range(10):
    print(number) # 0 , 1 , 2 , 3 , 4 , 6 , 7 , 8, 9
if number == 5:
    continue # Skip the iteration when the number is 5
print(number)

```

### 🔸 pass

La declaración de pase es un marcador de posición. Es útil cuando necesitas una estructura de control, como un if o un bucle, pero no quieres que suceda nada dentro de esa estructura, o si estás desarrollando el código y quieres dejar una parte abierta sin errores.

> 📌 Ejemplo de uso con pase:

```python
number = 0
for number in range(5):
print(number) # 0 , 1 , 2 , 3 , 4
if number == 3:
pass # Do nothing when number is 3
print(number)
```

## 🔷 Iteration Functions

### 🔹 range()

La función range() se utiliza para generar una secuencia de números, muy útil en bucles for. Puede recibir hasta tres argumentos: inicio, parada y paso.

> ✅ Sintaxis:

```python
start:1 # starting value (inclusive).
stop: 10 # ending value (exclusive).
step: 1 # increment value (optional).

range(start, stop, step)
```

> 📌 Ejemplo de uso con range(): Crea una secuencia de números del 0 al 9.

```python
for i in range(10):
    print(i)
📌 Usage example with range(): Create a sequence with an increment of 2.
```

```python
for i in range(0, 10, 2):
    print(i)
```

### 🔹 enumerate()

La función enumerate() agrega un contador automático a un iterable, devolviendo una tupla con el índice y el valor.

> ✅ Sintaxis:

```python
enumerate(iterable)
```

> 📌 Ejemplo de uso con enumerate(): iterar sobre una lista y obtener el índice y el valor.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
print(f"Index {index}: {fruit}")
```

### 🔹 zip()

La función zip() combina dos o más iterables y devuelve una secuencia de tuplas. Cada tupla contiene los elementos correspondientes de los iterables.

> ✅ Sintaxis:

```python
zip(iterable1, iterable2, ...)
```

> 📌 Ejemplo de uso de zip(): Combina dos listas e itera sobre ellas.

```python
names = ["John", "Mary", "Carlos"]
ages = [25, 30, 22]
for name, age in zip(names, ages):
print(f"{name} is {age} years old")
```

### 🔹 Comprensión de listas

Las listas por comprensión proporcionan una forma compacta y eficiente de crear listas a partir de otras colecciones o secuencias, utilizando una sintaxis más simple que los bucles tradicionales. Además, es especialmente útil cuando quieres aplicar una transformación simple a cada elemento de una lista o filtrarlos con una condición.

> ✅ Sintaxis:

```python
[expression for item in iterable if condition]
```

> 📌 Ejemplo de uso:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]
```

---

## 🚀 Conclusión

Las estructuras de repetición son esenciales para automatizar tareas y trabajar con grandes volúmenes de datos en Python. Con ellos, puedes repetir acciones en función de condiciones (`while`) o recorrer secuencias de forma eficiente (`for`), además de controlar el flujo de ejecución con `break`, `continue` y `pass`.

Si también dominas herramientas como `range()`, `enumerate()`, `zip()` y las listas por comprensión, harás que tu código sea más limpio, más elegante y más potente.

## 📝 Ejercicios de repetición

1. **Contar del 1 al 10 usando `for`**
Cree un programa que utilice un bucle `for` para imprimir los números del 1 al 10.

2. **Contador con `while`**
Crea un programa que cuente del 0 al 20, saltando de 2 en 2, usando `while`.

3. **Suma de una lista**
Utilice `for` para agregar todos los elementos de una lista de números enteros.

4. **Buscar con `break`**
Cree un programa que reciba una lista y deje de recorrerla tan pronto como encuentre el número 0.

5. **Filtrar pares con `continue`**
Recorra una lista e imprima sólo los números pares, usando `continue` para ignorar los impares.

6. **Comprensión de listas**
Crea una nueva lista con los cuadrados de los números del 1 al 10 usando comprensión de listas.

## 🔧 Consejos para la práctica:

- **Utiliza `for` cuando sabes cuántas veces necesitas repetir algo.**
- **Utilice `while` cuando la repetición depende de una condición.**
- **Explora funciones como `range()`, `enumerate()` y `zip()` para hacer que tus bucles sean más potentes.**
- **Practica la lectura y la escritura de listas por comprensión: harán que tu código sea más claro y expresivo.**

> ¡Ahora es tu turno! 🐍 ¡Practica con los ejercicios, prueba variaciones de los ejemplos y continúa evolucionando en el mundo de la programación con Python!