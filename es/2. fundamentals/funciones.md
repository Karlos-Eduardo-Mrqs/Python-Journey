# 🧰 Funciones en Python

Las funciones son bloques de código reutilizables que se pueden llamar para realizar una tarea específica. Ayudan a que el código sea más organizado, modular y fácil de entender.

## 📌 ¿Por qué utilizar funciones?

- **Reutilización de código:** evita repetir el mismo código varias veces.
- **Modularización:** organiza el código en bloques lógicos e independientes.
- **Mejor legibilidad y facilidad de mantenimiento:** hace que sea más fácil entender y cambiar el código.

## 🔹 Declaración de función con def

Para crear una función, utilizamos la palabra clave def, seguida del nombre de la función, paréntesis y dos puntos. El cuerpo de la función está sangrado.

> ✅ Sintaxis:

```python
def funcione_nombre(parameters):
    # function code
    return value
```

> 📌 Ejemplo de uso: Función simple que imprime un saludo.

```python
def saludo():
    print("¡Hola, bienvenido!")

saludo() # Output: Hello, welcome!
```

## 🔷 Parámetros y argumentos

Los parámetros son las variables enumeradas en la declaración de la función. Los argumentos son los valores que se pasan a la función cuando se llama.

> 📌 Ejemplo de uso:

```python
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Carlos") # Salida: ¡Hola, Carlos!
```

## 🔷 Argumentos predeterminados y con nombre

En Python, podemos hacer que los parámetros sean opcionales asignándoles valores predeterminados. También podemos especificar valores por nombre, lo que permite cambiar el orden de los argumentos y aumenta la legibilidad del código.

### Parámetros con valores predeterminados

Los parámetros con valores predeterminados le permiten definir un valor "automático" para un parámetro, en caso de que no se especifique en la llamada de función. Esto hace que el parámetro sea opcional y evita errores al llamar a la función con menos argumentos.

> ✅ Sintaxis:

```python
def nombre_función(parámetro1=valor1, parámetro2=valor2):
#código
```

> 📌 Usage example:

```python
def greeting(name="User"):
print(f"Hello, {name}!")

greeting() # Output: Hello, User!
greeting("Anna") # Output: Hello, Anna!
```

#### 📘 Explicación

En el ejemplo anterior, la función de saludo se definió con un valor predeterminado de "Usuario" para el parámetro de nombre. Entonces, si el usuario no pasa ningún argumento, se utilizará automáticamente "Usuario".

### Argumentos con nombre

Los argumentos con nombre le permiten pasar valores especificando el nombre del parámetro. Esto hace que la llamada de función sea más clara y le permite cambiar el orden de los argumentos sin afectar la lógica.

> 📌 Ejemplo de uso:

```python
def saludo(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

saludo(edad=25, nombre="Carlos") # Salida: Hola, Carlos. Tienes 25 años.
```

#### 📘 Explicación

Incluso si la edad viene antes del nombre en la llamada de función, funciona correctamente porque se nombraron los argumentos. Esto es útil para funciones con muchos parámetros o cuando queremos que el código sea más legible.

## 🔷 regresar

La declaración de retorno se utiliza para devolver un valor de una función. Cuando una función encuentra un retorno, finaliza la ejecución y devuelve el valor especificado.

> ✅ Sintaxis:

```python
def suma(a, b): 
    return a+b
```

> 📌 Ejemplo de uso:

```python
def suma(a, b):
    return a+b

resultado = suma(3, 5)
print(resultado) # Salida: 8
```

## 🔷 Functions with Multiple Returns

In Python, a function can return more than one value at once. These values ​​are returned as a tuple (even if you don't see the parentheses) and can be unpacked into separate variables.

> ✅ Syntax

```python
def function_name():
    return value1, value2, ..., valueN
```

> 📌 Example explained

```python
def operations(a, b):
    sum = a + b
    product = a * b
    return sum, product # returns two values
```

### 💡 Consejo útil

Puedes mezclar argumentos posicionales y con nombre, pero los argumentos posicionales deben ir antes que los nombrados. Esto garantiza la claridad en la lectura y evita errores al llamar a la función. Ejemplo:

```python
def datos_personales(nombre, edad, ciudad="Desconocido"):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

datos_personales("Ana", 30, ciudad="Sao Paulo")
```

## 🔹 Alcance de la variable

El alcance de una variable determina dónde se puede acceder a ella. Hay dos tipos de ámbito en Python:

- **Ámbito local:🚩** Variables definidas dentro de una función, accesibles solo dentro de esa función.

- **Ámbito global:🌐** Variables definidas fuera de cualquier función, accesibles en cualquier lugar del código.

> 📌 Ejemplo de uso del alcance:

```python
global_variable = "¡Soy global!"

def ejemplo():
    local_variable = "¡Soy local!"
    print(global_variable) # Acceder a la variable global
    print(local_variable) # Acceder a la variable local

ejemplo()
# print(variable_local) # ¡Error! No se puede acceder a variables locales fuera de la función. ```
```

## 🔷 Funciones anónimas con Lambda

Las funciones anónimas, o funciones lambda, son funciones pequeñas, sin nombre, que generalmente se utilizan para operaciones simples que se pueden realizar en una sola línea. Son muy útiles en funciones como map(), filter() y sorted().

> ✅ Sintaxis:

```python
variable = lambda argumentos: expresión
```

> 📌 Ejemplo de uso:

```python
suma = lambda x, y : x + y
print(suma(3, 5)) # Salida: 8
```

## Conclusión 🚀

Las funciones de Python son bloques de código reutilizables que le permiten organizar y modularizar su programa, haciéndolo más legible, eficiente y fácil de mantener. Son esenciales para reducir la repetición de código y facilitar la creación de programas escalables.

Al comprender cómo definir y llamar funciones, cómo pasar parámetros y devolver valores, podrá crear soluciones más sofisticadas y elegantes. Además, las funciones pueden tener parámetros predeterminados, variables y devolver múltiples valores, lo que aumenta aún más su flexibilidad.

## 📝 Ejercicios de funciones

1. **Función suma**
Crea una función que recibe dos números como parámetros y devuelve su suma.

2. **Función promedio**
Crea una función que recibe una lista de números y devuelve el promedio de estos números.

3. **Función factorial**
Implementar una función que calcule el factorial de un número.

4. **Función de comprobación de números primos**
Crea una función que determine si un número dado es primo.

5. **Función de conteo de caracteres**
Crea una función que cuente el número de ocurrencias de un carácter en una cadena.

## 🔧 Consejos para la práctica:

- **Modularización del código:**
Divida su código en pequeñas funciones, cada una responsable de una tarea específica, para facilitar el mantenimiento y la reutilización.

- **Funciones recursivas:**
Intente crear funciones recursivas para problemas que puedan dividirse en subproblemas más pequeños, como calcular factorial o resolver problemas de búsqueda y clasificación.

> ¡Ahora es el momento de poner en práctica lo aprendido! ✨🐍 ¡Sigue explorando y creando tus propias funciones para resolver problemas cotidianos y mejorar tus habilidades en Python!