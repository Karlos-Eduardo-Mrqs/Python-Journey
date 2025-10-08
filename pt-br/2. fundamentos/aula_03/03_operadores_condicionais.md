# 🔹 Operadores Condicionais 🔎

Os operadores condicionais em Python permitem comparar valores e combinar expressões booleanas.

Eles são essenciais para tomar decisões dentro do código, como determinar se um usuário pode acessar um recurso ou se um número atende a determinada condição.

## 🔹 Relacionais

> Usados para comparar valores, retornando ``True`` ou ``False``.

| 🔁 Operador | 🤔 Significado | 💡 Exemplo        |
| ----------- | -------------- | ----------------- |
| `==`        | Igual          | `5 == 5` → `True` |
| `!=`        | Diferente      | `5 != 3` → `True` |
| `>`         | Maior que      | `4 > 2` → `True`  |
| `<`         | Menor que      | `2 < 1` → `False` |
| `>=`        | Maior ou igual | `4 >= 4` → `True` |
| `<=`        | Menor ou igual | `3 <= 5` → `True` |

### Exemplo dos Relacionais

```python
idade = 20
print(idade >= 18)  # True
print(idade < 18)   # False
print(idade <= 18)  # False
print(idade > 18)   # True
print(idade != 18)  # True
print(idade == 18)  # False 

```

## 🔹 Lógicos

> Permitem combinar múltiplas expressões booleanas.

| 🔣 Operador | 💬 Exemplo       | 🎯 Resultado |
| ----------- | ---------------- | ------------ |
| `and`       | `True and False` | `False`      |
| `or`        | `True or False`  | `True`       |
| `not`       | `not True`       | `False`      |

### Tabela Verdade 🪟

> **Uma tabela verdade mostra todas as combinações possíveis de valores lógicos (True ou False) para uma determinada operação.** > Ela é fundamental para entender o comportamento de operadores como and, or e not.

| A | B | A and B | A or B | not A |
| - | - | ------- | ------ | ----- |
| ✅ | ✅ | ✅       | ✅      | ❌     |
| ✅ | ❌ | ❌       | ✅      | ❌     |
| ❌ | ✅ | ❌       | ✅      | ✅     |
| ❌ | ❌ | ❌       | ❌      | ✅     |

> ✅: ``True`` | ❌: ``False``

## 🔹 Conclusão ✅

Operadores relacionais permitem comparar valores. Operadores lógicos permitem combinar condições.

**Juntos, eles são a base de toda estrutura de decisão em Python (if, while, etc.).**

**Próximo Capítulo: [Operadores de Verificação](../aula_04/04_operadores_verificacao.md)**

---

## 📝 Exercícios Aula 03

### Peça a idade do usuário e informe se ele pode tirar carteira de motorista (idade >= 18)

### Crie um programa que pergunte duas notas e diga se o aluno foi aprovado (média >= 7)

### Leia um número inteiro

1. Mostre se ele é positivo, negativo ou zero.
2. Indique também se é par ou ímpar.

**[Gabarito](exercicios/README.md)**
