# 📌 Resumo Geral dos Operadores em Python

Python oferece diferentes tipos de operadores para cálculos, comparações, combinações lógicas e verificações. A tabela abaixo traz um resumo de cada categoria:

| Categoria             | Operadores                        | Exemplo               | Resultado    |     |
| --------------------- | --------------------------------- | --------------------- | ------------ | --- |
| **Aritméticos** ➕➖✖️➗ | `+  -  *  /  //  %  **`           | `5 + 2`               | `7`          |     |
| **Atribuição** 📝     | `=  +=  -=  *=  /=  //=  %=  **=` | `x = 5; x += 2`       | `7`          |     |
| **Bit a Bit** ⚡       | ``\ & ^  \ ~  <<  >> \``           | `6 & 3`      | `2`  | |
| **Relacionais** 🔎    | `==  !=  >  <  >=  <=`            | `5 > 3`               | `True`       |     |
| **Lógicos** 🔗        | `and  or  not`                    | `(5 > 3) and (2 < 4)` | `True`       |     |
| **Identidade** 🆔     | `is  is not`                      | `a is b`              | `True/False` |     |
| **Pertencimento** 📦  | `in  not in`                      | `'a' in 'carro'`      | `True`       |     |

## ⚖️ Precedência dos Operadores

A ordem que o Python segue para avaliar expressões

| Nível | Operadores                                   | Descrição                                          |              |
| ----- | -------------------------------------------- | -------------------------------------------------- | ------------ |
| 1     | `()`                                         | Parênteses — avalia primeiro                       |              |
| 2     | `**`                                         | Exponenciação                                      |              |
| 3     | `+`, `-` (unário)                            | Mais e menos unário, ex.: `-5`, `+3`               |              |
| 4     | `*`, `/`, `//`, `%`                          | Multiplicação, divisão, divisão inteira, módulo    |              |
| 5     | `+`, `-` (binário)                           | Adição e subtração normais                         |              |
| 6     | `<<`, `>>`                                   | Shift à esquerda e à direita (bit a bit)           |              |
| 7     | `&`                                          | AND bit a bit                                      |              |
| 8     | `^`                                          | XOR bit a bit                                      |              |
| 9     | `\`                             | OR bit a bit  |  |
| 10    | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in` | Operadores relacionais, identidade e pertencimento |              |
| 11    | `not`                                        | Negação lógica                                     |              |
| 12    | `and`                                        | Conjunção lógica                                   |              |
| 13    | `or`                                         | Disjunção lógica                                   |              |
| 14    | `=`, `+=`, `-=`, `*=`, `/=`, etc.            | Atribuição e atribuições compostas                 |              |

**Proximo Capítulo: [Condicionais](../aula_06/06_condicionais.md)**
