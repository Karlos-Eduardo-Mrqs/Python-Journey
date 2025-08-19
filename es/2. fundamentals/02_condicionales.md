# ⚙️ Estructuras condicionales en Python

Las estructuras condicionales permiten que su código tome decisiones basadas en condiciones específicas. De esta manera, puedes crear programas que se comporten de manera diferente según las entradas y las situaciones.

## 📌 ¿Por qué son importantes?

- Verificar valores y ejecutar comandos específicos;
- Define diferentes flujos de ejecución;
- Crear validaciones y procesamiento de datos;
- Mejorar la lógica y dinámica del programa;

## 🔷 Principales tipos de condicionales

### 🔹 if, elif y else

La estructura más básica y común para tomar decisiones en Python. Permite ejecutar diferentes bloques de código en función de una o más condiciones.

> ✅ Sintaxis:

```python
if condicion1:
# bloque de código si la condición1 es verdadera
elif condicion2:
# bloque de código si la condición1 es falsa y la condición2 es verdadera
else:
# bloque de código si todas las condiciones anteriores son falsas
```

> 📌 Ejemplo de uso: Comprobar si un número es positivo, negativo o cero.

```python
if número > 0:
    print("Número positivo")
    número elif < 0:
    print("Número negativo")
else:
    print("Cero")
```

### 🔹 Condicionales anidados

Son estructuras if dentro de otras estructuras if. Permiten comprobar condiciones dependientes o jerárquicas, profundizando en la lógica de decisión.

> ✅ Sintaxis:

```python
if condición1:
    if condición2:
        # bloquear si ambas condiciones son verdaderas
    else:
        # bloquear si la condición1 es verdadera y la condición2 es falsa
else:
    # bloquear si la condición1 es falsa
```

> 📌 Ejemplo de uso: Validar dos condiciones vinculadas, como calificación y asistencia.

```python
if calificación >= 7: # Si la calificación es mayor o igual a siete, avanza en el algoritmo
    if frecuencia >= 75: # Si la frecuencia es mayor o igual al 75% se aprobará
        imprimir("Aprobado")
    else:
        print("Reprobado por falta de asistencia")
else:
    print("Reprobado por calificación")
```

### 🔹 Operador ternario

Una forma compacta de escribir condiciones simples en una sola línea. Ideal cuando quieres asignar valores o devolver expresiones cortas de forma elegante.

> ✅ Sintaxis:

```python
valor_si_es_verdadero si condición de lo contrario valor_si_es_falso 
```

> 📌 Ejemplo de uso:

```python
estado = "Aprobado" si la calificación >= 7 de lo contrario "Reprobado" # Si la calificación es mayor o igual a siete, el estado será aprobado, de lo contrario el estado será reprobado
```

### 🔹 Match case (valid in Python 3.10+)

Es la estructura introducida en Python 3.10 para reemplazar el switch en otros lenguajes. Permite comparar un valor con múltiples "casos", haciendo que el código sea más limpio y organizado para múltiples decisiones basadas en el mismo valor.

> ✅ Sintaxis:

```python
match variable de coincidencia:
    case valor de caso1:
        # bloque de código para el valor1
    case valor de caso2:
        # bloque de código para valor2
    case_:
        # bloque predeterminado (equivalente a "predeterminado")
```

**El carácter _ (guión bajo) representa el caso "predeterminado", que se ejecutará si no se cumple ninguna de las condiciones anteriores.**

> 📌 Ejemplo de uso:

```python
color = "rojo"

match color:
    case "rojo":
        print("Color elegido: Rojo")
    case "azul":
        print("Color elegido: Azul")
    case "vierde":
        print("Color elegido: Verde")
    caso_:
        print("Color no reconocido")
```

---

## 🚀 Conclusión

Las declaraciones condicionales en Python son herramientas poderosas que permiten que su código tome decisiones basadas en condiciones dinámicas.

Son esenciales para controlar el flujo de tu programa, haciéndolo flexible y adaptable a diferentes entradas y situaciones. Al comprender cómo usar if, elif, else, declaraciones condicionales anidadas, el operador ternario y match case, tendrá un conjunto sólido de herramientas para manejar cualquier tipo de situación condicional.

## 📝 Ejercicios condicionales

1. **Comprueba si el número es positivo, negativo o cero.**
Implemente un programa que lea un número e imprima si es positivo, negativo o cero.

2. **Clasificación por edad**
Crea un programa que lea la edad de una persona y la clasifique como:

- Niño (0 a 12 años)
- Adolescente (13 a 17 años)
- Adulto (18 a 64 años)
- Personas mayores (65 años o más)

3. **Comprobación de calificaciones**

Crear un programa que lea una calificación del 0 al 10 e informe si el estudiante aprobó, reprobó o está recuperando. Los criterios son:

- Aprobado: calificación >= 7
- Recuperado: 5 <= grado < 7
- Suspendido: calificación < 5

4. **Calculadora simple**

Cree un programa que lea dos números y un operador matemático (+, -, *, /). El programa debe realizar la operación correspondiente entre los dos números y mostrar el resultado.

5. **Mayor que tres números**

Cree un programa que lea tres números e imprima el número más grande entre ellos, utilizando estructuras condicionales.

## 🔧 Consejos para la práctica

- **Validación de la entrada del usuario:**
Utilice condicionales para validar las entradas de datos, como los cálculos de descuento basados ​​en la edad o la categoría del cliente.

- **Casos múltiples:**
Utilice la combinación de mayúsculas y minúsculas en sistemas que involucran múltiples casos, lo que hará que su código sea más organizado y legible.

> ¡Ahora es el momento de poner en práctica lo aprendido! ✨🐍 ¡Sigue explorando, resolviendo desafíos y mejorando tus habilidades en Python!

**Seguiente archivo : [bluces](03_bucles.md)**
