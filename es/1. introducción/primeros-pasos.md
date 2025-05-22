# Primeros Pasos 🐍

Ahora que has configurado tu entorno, ¡podemos empezar a programar en Python!

---

## 📦 Variables

Las variables se utilizan para almacenar información que se puede manipular a lo largo del programa. En Python, crear una variable es sencillo y no requiere definir el tipo de dato (como ocurre en lenguajes como Java o C++).

---

## 🧠 Reglas para nombrar variables

| Regla | Descripción |
| :---------------------------- | :----------------------------------------------------------------------------------- |
| Empieza con una letra o `_` | El nombre debe empezar con una letra (a-z, A-Z) o un guion bajo (`_`). |
| Letras, números y guiones bajos | Después del primer carácter, puede contener letras, números y guiones bajos. |
| No empieza con un número | Las variables **no pueden** empezar con números. |
| Distingue entre mayúsculas y minúsculas | Python distingue entre mayúsculas y minúsculas (`name`, `Name` y `NAME` son diferentes). |
| Evita las palabras reservadas | No uses palabras clave del lenguaje (como `class`, `if`, `for`). |

> **💡 Buenas prácticas:** Usa nombres descriptivos que aclaren qué representa la variable.

---

## ✅ Ejemplos de nombres de variables

| Nombre | Tipo | Nota |
| :------------- | :------- | :----------------------------------- |
| nombre | Válido | Solo minúsculas. |
| for | Inválido | Palabra reservada. |
| Nombre completo | Válido | Uso de mayúsculas y guiones bajos. |
| edad29 | Válido | Puede contener números (no al principio). |
| class | Inválido | Palabra reservada. |
| \_direccion | Válido | Se permite empezar con guiones bajos. |
| 3dad29 | Inválido | No puede empezar con un número. |
| nombre completo | Inválido | No se permiten espacios; use `_`. |

---

## 🔢 Tipos de datos

Python es un lenguaje de tipado dinámico. Esto significa que no es necesario declarar explícitamente el tipo de una variable; se define automáticamente en función del valor asignado.

---

### 📋 Tabla de Tipos de Datos

| Tipo | Descripción | Ejemplo de Código | Ejemplo Real |
| :------ | :------------------------- | :---------------------------------------- | :-------------------------------------------------------- |
| `int` | Enteros. | `age = 30` | Edad de una persona. |
| `float` | Números con decimales. | `height = 1.75` | Altura en metros. |
| `str` | Cadena de texto. | `name = "Carlos"` | Nombre de alguien. |
| `bool` | Verdadero o falso. | `active = True` | ¿Está activo? |
| `list` | Lista ordenada y mutable. | `fruits = ["apple", "banana"]` | Lista de la compra. |
| `tuple` | Lista ordenada e inmutable. | `coordinates = (10, 20)` | Ubicación GPS. *(“Tuple” es el término en inglés para “tupla”)* |
| `dict` | Estructura clave-valor. | `student = {"name": "Ana", "age": 20,}` | Matrícula de estudiante. |

---

### 📚 Explicación rápida

- **`int`** → enteros.
- **`float`** → decimales.
- **`str`** → textos (cadenas).
- **`bool`** → valores lógicos (Verdadero o Falso).
- **`list`** → colecciones mutables.
- **`tuple`** → colecciones inmutables.
- **`dict`** → clave y valor (tipo diccionario).

---

## ✅ Ejemplos prácticos combinados

```python
nombre = "Ana" # str
edad = 25 # int
altura = 1.68 # float
estudiante = True # bool
materias = ["Python", "SQL", "Git"] # lista
coordenadas = (34.5, -120.7) # tupla
perfil = {"nombre": "Ana", "edad": 25} # dict
```

## Comandos de entrada y salida

Aprendamos a interactuar con el usuario mediante la entrada de datos (``input``) y la salida (``print``).

---

## 🔹 Salida de datos: `print()`

El comando `print()` se utiliza para mostrar información en la consola.

Inicio:

```python
print("¡Hola, mundo!")
print("La suma de 2 + 3 es:", 2 + 3)
```

Salida:

```bash
¡Hola, mundo!
La suma de 2 + 3 es: 5
```

## 🔹 Entrada: `input()`

El comando `input()` permite recibir datos del usuario.

Ejemplo:

```python
name = input("Introduce tu nombre: ")
print("Bienvenido", name)
```

El programa se pausará y esperará a que el usuario escriba algo.

Todo lo que se escriba se almacenará como una cadena.

## ⚡ Conversión de Tipos (Conversión)

Para trabajar con números, necesitamos convertir la entrada manualmente mediante funciones de conversión:

```python
age = int(input("Introduce tu edad: "))
height = float(input("Introduce tu altura: "))
```

- **int() :** convierte a entero.
- **float() :** convierte a punto flotante.
- **str() :** convierte a texto (cadena), si es necesario.

---

## 🚀 Conclusión

Estos primeros pasos son fundamentales en tu experiencia con Python. A partir de aquí, ¡ya puedes crear pequeños scripts que reciben datos, procesan información y muestran resultados en pantalla!

> ¡Sigue practicando! Prueba:

- Crea un programa que calcule el promedio de dos calificaciones;
- Crea un registro simple con nombre, edad y ciudad; - Desarrolla un diccionario que contenga nombres, edades, situaciones (estudiando: verdadero) y más;

> 💾 Consejo: ¡Guarda tus pruebas en un archivo como exercicios.py para crear tu propia base de estudio!

> Cada pequeño ejercicio te dará más confianza y te preparará para los siguientes módulos, como estructuras condicionales, repeticiones, funciones y mucho más. 💡🐍

**Siguiente módulo: [Fundamentos del lenguaje](../2.%20fundamentals/readme.md)**