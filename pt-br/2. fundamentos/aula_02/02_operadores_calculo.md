# 🔹 Operadores de Cálculo ➕✖️➗📝

Os operadores de cálculo em Python englobam:

*Aritméticos* → usados para realizar operações matemáticas básicas.

*De Atribuição* → permitem armazenar valores e atualizar variáveis de forma prática.

*Bit a Bit (Bitwise)* → realizam operações diretamente sobre os bits dos números.

---

## 🧮 Operadores Aritméticos

> Realizam operações matemáticas entre valores numéricos.

| Operador | Descrição       | Exemplo          |
| -------- | --------------- | ---------------- |
| `+`      | Adição          | `2 + 3` → `5`    |
| `-`      | Subtração       | `10 - 4` → `6`   |
| `*`      | Multiplicação   | `6 * 7` → `42`   |
| `/`      | Divisão (float) | `10 / 4` → `2.5` |
| `//`     | Divisão inteira | `10 // 4` → `2`  |
| `%`      | Módulo (resto)  | `10 % 4` → `2`   |
| `**`     | Potência        | `2 ** 3` → `8`   |

### 📌 Exemplo dos aritméticos

```python
a = 15
b = 4

print(a + b)   # 19
print(a - b)   # 11
print(a * b)   # 60
print(a / b)   # 3.75
print(a // b)  # 3
print(a % b)   # 3
print(a ** b)  # 50625
```

---

## 📝 Operadores de Atribuição

> Permitem atribuir valores a variáveis e atualizar seu conteúdo em uma única instrução.

| Operador | Equivalente               | Exemplo                  |
| -------- | ------------------------- | ------------------------ |
| `=`      | Atribuição simples        | `x = 10` → `x = 10`      |
| `+=`     | Soma e atribui            | `x += 5` → `x = x + 5`   |
| `-=`     | Subtração e atribui       | `x -= 3` → `x = x - 3`   |
| `*=`     | Multiplica e atribui      | `x *= 2` → `x = x * 2`   |
| `/=`     | Divide e atribui          | `x /= 4` → `x = x / 4`   |
| `//=`    | Divisão inteira e atribui | `x //= 3` → `x = x // 3` |
| `%=`     | Módulo e atribui          | `x %= 2` → `x = x % 2`   |
| `**=`    | Exponenciação e atribui   | `x **= 3` → `x = x ** 3` |

### 📌 Exemplo de atribuição

```python
x = 10
x += 5   # agora x vale 15
x *= 2   # agora x vale 30
x -= 4   # agora x vale 26
print(x) # saída: 26
```

---

## ⚙️ Operadores Bit a Bit (Bitwise)

> Trabalham diretamente com os bits que compõem os números inteiros. São muito usados em programação de baixo nível, redes e otimizações.

| Operador | Descrição               | Exemplo (`a = 6, b = 3`) | Resultado |     |     |
| -------- | ----------------------- | ------------------------ | --------- | --- | --- |
| `&`      | AND bit a bit           | `a & b`                  | `2`       |     |     |
| `\`       | OR bit a bit           | `a \ b`               | ``7`` |   |   |
| `^`      | XOR (OU exclusivo)      | `a ^ b`                  | `5`       |     |     |
| `~`      | NOT (inversão dos bits) | `~a`                     | `-7`      |     |     |
| `<<`     | Desloca bits à esquerda | `a << 1`                 | `12`      |     |     |
| `>>`     | Desloca bits à direita  | `a >> 1`                 | `3`       |     |     |

### 📌 Exemplo dos bitwise

```python
a = 6   # 110 em binário
b = 3   # 011 em binário

print(a & b)   # 2  -> 010
print(a | b)   # 7  -> 111
print(a ^ b)   # 5  -> 101
print(~a)      # -7 -> inversão dos bits
print(a << 1)  # 12 -> 1100
print(a >> 1)  # 3  -> 011
```

---

## 📌 Conclusão

**Os operadores aritméticos** permitem realizar cálculos matemáticos.

**Os operadores de atribuição** tornam o código mais limpo ao atualizar valores diretamente.

Já **os operadores bit a bit** oferecem maior controle sobre os dados em nível binário, sendo muito úteis em contextos como programação de baixo nível, criptografia e manipulação de sinais.

> 👉 Esses três grupos de operadores são fundamentais em Python e aparecem em diferentes tipos de programas — desde exercícios iniciais até aplicações complexas.

**Próximo Capítulo: [Operadores Condicionais](../aula_03/03_operadores_condicionais.md)**

---

## 📝 Exercícios - Operadores de Cálculo ➕✖️➗

### Cálculo de Média e Diferença

1. Leia três números do usuário.
2. Mostre a média dos números.
3. Mostre a diferença entre o maior e o menor número.

### Leia um número e mostre seu quadrado, seu cubo e sua raiz quadrada (use para exponenciação)

### Leia o valor de um empréstimo, a taxa de juros e o número de meses

1. Calcule o valor total a pagar com juros simples:
2. ``total = valor + (valor * taxa * meses)``
3. Mostre o resultado.

### Leia a base e a altura de um retângulo

1. Calcule e mostre a ``área (base * altura)``.
2. Calcule e mostre o ``perímetro (2 * (base + altura))``.

**[Gabarito](exercicios/README.md)**
