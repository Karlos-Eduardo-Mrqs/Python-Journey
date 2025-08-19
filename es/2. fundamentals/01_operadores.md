# 🔢 Operadores en Python

Los operadores son símbolos que se utilizan para realizar operaciones con variables y valores. Python tiene varios tipos de operadores.

## 🔹 Aritmética ➕➖✖️➗

> **Los operadores aritméticos se utilizan para realizar operaciones matemáticas, como sumar, restar, multiplicar y dividir valores.**
> Son útiles en cualquier situación donde sea necesario realizar cálculos, ya sea sumar la edad de los usuarios, calcular descuentos o multiplicar valores en un carrito de compras.

| 🧮 Operador | 📝 Descripción | 💡Ejemplo |
|------------|--------------|------------|
| `+` | Adición | `2 + 3` → `5` |
| `-` | Resta | `5 - 2` → `3` |
| `*` | Multiplicación | `4 * 2` → `8` |
| `/` | División | `10/2` → `5.0` |
| `//` | División de enteros | `10 // 3` → `3` |
| `%` | Módulo (resto) | `10 % 3` → `1` |
| `**` | Poder | `2 ** 3` → `8` |

## 🔹 Relacional (Comparación) 🔎

> **Estos operadores comparan dos valores y devuelven un resultado booleano (``Verdadero`` o ``Falso``).**
> Son esenciales en estructuras de decisión, como el ``si``, ya que nos ayudan a saber si algo es mayor que, menor que, igual a o diferente de otro valor.

| 🔁Operador | 🤔 Significado | 💡Ejemplo |
|------------|----------------|----------------|
| `==` | Igual | `5 == 5` → `Verdadero` |
| `!=` | No igual | `5 != 3` → `Verdadero` |
| `>` | Mayor que | `4 > 2` → `Verdadero` |
| `<` | Menos de | `2 < 1` → `Falso` |
| `>=` | Mayor o igual que | `4 >= 4` → `Verdadero` |
| `<=` | Menor o igual que | `3 <= 5` → `Verdadero` |

## 🔹 Lógico 🔗

> **Los operadores lógicos se utilizan para combinar expresiones booleanas.**
> Son muy útiles cuando queremos comprobar múltiples condiciones al mismo tiempo. Por ejemplo: comprobar si un usuario ha iniciado sesión y tiene permisos de administrador.

### 📘 Tabla de verdad

> **Una tabla de verdad muestra todas las combinaciones posibles de valores lógicos (Verdadero o Falso) para una operación dada.**
> Es esencial comprender el comportamiento de operadores como y, o y no.

| A | B | A y B | A o B | no A |
|---|---|----------|---------|--------|
| ✅ | ✅ | ✅ | ✅ | ❌ |
| ✅ | ❌ | ❌ | ✅ | ❌ |
| ❌ | ✅ | ❌ | ✅ | ✅ |
| ❌ | ❌ | ❌ | ❌ | ✅ |

> **✅: ``Verdadero`` | ❌: ``Falso``**

### 🔹 Ejemplos 🔗

| 🔣Operador | 💬 Ejemplo | 🎯 Resultado |
|--------------|------------|--------------|
| `and` | Verdadero y falso |`Falso` |
| `or` | `Verdadero o Falso` | `Verdadero` |
| `not` | `no es cierto` | `Falso` |

**Consejo🔎:**

- ``or`` -> solo devuelve Verdadero si ambos son ``Verdadero``.
- ``and`` -> devuelve ``Verdadero`` si al menos uno es ``Verdadero``.
- ``not`` -> 🔁 invierte el valor

> 📌 El operador `not` solo depende de un valor (unario), a diferencia de `and` y `or`, que comparan dos valores.

## 🔹 Operadores de identidad 🆔

> Se utiliza para comprobar si dos variables apuntan al mismo objeto en la memoria, y no solo si tienen el mismo valor.

| Operador | Descripción | Ejemplo | Resultado |
|----------|-----------|----------|-----------|
| `in` | Devuelve "Verdadero" si las variables hacen referencia al mismo objeto en la memoria | `a in b` | `Verdadero` o `Falso` |
| `not in` | Devuelve "Verdadero" si los objetos son **diferentes** | `a no es b` | `Verdadero` o `Falso` |

> **💡 Sugerencia: a == b compara los valores, mientras que a es b compara si son el mismo objeto en la memoria.**

### Ejemplo 🆔

```python
a = [1, 2]
segundo = un
c = [1, 2]
print(a in b) # Verdadero → a y b son el mismo objeto
print(a not in c) # Falso → a y c tienen el mismo contenido, pero son objetos diferentes
```

## 🔹 Operadores de Membresía 🔎📦

> Se utiliza para probar si un valor existe dentro de una secuencia, como listas, cadenas o diccionarios.

| Operador | Descripción | Ejemplo | Resultado |
|----------|----------|---------|----------|
| `in` | Devuelve "Verdadero" si el valor está presente | `'a' in 'Carlos'` | `True` |
| `no in` | Devuelve "Verdadero" si el valor **no** está presente | `5 no in [1,2,3]` | `True` |

### Ejemplo 🔎📦

```python
frutas = ['manzana', 'plátano']
print('banana' en frutas) # Verdadero
print('naranja' no está en frutas) # Verdadero
print("uva" en frutas) # Falso
```

## 🔹 Operadores bit a bit 🧠⚙️

> Operan directamente sobre bits, siendo útil en programación de bajo nivel, redes, criptografía o manipulación de permisos binarios.

| 🔢 Operador | 📛 Nombre | 💬 Descripción |
|--------------|---------|---------------|
| `&` | Y | Devuelve 1 si **ambos** bits son 1 |
| `OR` | O | Devuelve 1 si **cualquier** bit es 1 |
| `^` | XOR | Devuelve 1 si los bits son **diferentes** |
| `~` | NO | Invierte todos los bits |
| `<<` | Desplazamiento a la izquierda | Desplaza bits hacia la izquierda |
| `>>` | Desplazamiento a la derecha | Desplaza bits hacia la derecha |

### Ejemplo 🧠⚙️

```python
a = 5 # binario: 0101
b = 3 # binario: 0011
imprimir(a & b) # 1 → 0001 (0101 y 0011)
imprimir(a | b) # 7 → 0111 (0101 | 0011)
```

## 🔹 Tarea 📝

> **Sirven para almacenar valores en variables.** Además del clásico ``=``, existen operadores que realizan una operación y actualizan el valor de la variable, como ``+=``, ``-=``, etc. Esto hace que el código sea más limpio y directo.

| 🔢 Operador | 🟰 Equivalente |
|----------|-------------|
| `=` | Asignación sencilla |
| `+=` | Agrega y asigna |
| `-=` | Resta y asignaciones |
| `*=` | Multiplicaciones y asignaciones |
| `/=` | Divisiones y asignaciones |
| `//=` | Realiza divisiones y asignaciones de números enteros |
| `%=` | Realiza el módulo (recordatorio) y asigna |
| `**=` | Realiza exponenciaciones y asignaciones |

---

## ⚖️ Precedencia de operadores

El orden que utiliza Python para resolver expresiones:

1. Paréntesis `()`
2. `**` Exponenciación
3. `+`, `-` (unario)
4. `*`, `/`, `//`, `%`
5. `+`, `-` (binario)
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `>`, `<`, `>=`, `<=`, `es`, `en`
11. `not`
12. `and`
13. `or`
14. `=`, `+=`, `-=`, etc.

---

## 🚀 Conclusión

Los operadores de Python son herramientas esenciales para realizar operaciones y comparar datos eficientemente. Con esta descripción general, podrás realizar desde cálculos aritméticos simples hasta manipulación avanzada de datos con operadores lógicos, bit a bit y de asignación.

**Para seguir avanzando en tu aprendizaje, te sugerimos algunos ejercicios**:

- *Operadores aritméticos:* Crea un programa que realice las cuatro operaciones matemáticas con los números proporcionados por el usuario.

- *Operadores relacionales:* Desarrolla un sistema que compare las edades de dos personas e indique quién es mayor.

- *Operadores lógicos:* Implementa una función que compruebe si un número está entre dos valores (usando `y` y `or`).

- *Operadores miembro:* Crea un programa que solicite al usuario un artículo y compruebe si está en una lista de la compra.

- *Operadores bit a bit:* Intenta manipular los bits de un número y observa cómo cambia su valor.

**🔍 Consejo:** La práctica constante es clave para consolidar tu comprensión de los operadores. Con el tiempo, ¡se integrarán de forma natural en tu código!

**💡 Próximos pasos:** Una vez que domines los operadores, explora cómo usarlos en estructuras condicionales y de bucle. ¡Esto te permitirá escribir programas más dinámicos e interesantes!

> Dominar los operadores te da control total sobre cómo tu programa toma decisiones y transforma datos. ¡Esta es la base para crear sistemas inteligentes y eficientes!

**Seguiente Archivo : [condicionales](02_condicionales.md)**
