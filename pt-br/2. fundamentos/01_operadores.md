# 🔢 Operadores em Python

Operadores são símbolos usados para realizar operações em variáveis e valores. Eles são essenciais para manipular dados e executar cálculos dentro de um programa. Dependendo do tipo de operação que você deseja realizar, você usará diferentes tipos de operadores. Em Python, os operadores podem ser classificados nas seguintes categorias:

## 🔹 Aritméticos ➕➖✖️➗

> **Os operadores aritméticos são usados para realizar operações matemáticas, como somar, subtrair, multiplicar e dividir valores.**
> Eles são úteis em qualquer situação onde cálculos precisam ser feitos — seja para somar a idade de usuários, calcular descontos ou multiplicar valores em um carrinho de compras.

| 🧮 Operador | 📝 Descrição | 💡 Exemplo |
|------------|--------------|------------|
| `+` | Adição | `2 + 3` → `5` |
| `-` | Subtração | `5 - 2` → `3` |
| `*` | Multiplicação | `4 * 2` → `8` |
| `/` | Divisão | `10 / 2` → `5.0` |
| `//` | Divisão inteira | `10 // 3` → `3` |
| `%` | Módulo (resto) | `10 % 3` → `1` |
| `**` | Potência | `2 ** 3` → `8` |

## 🔹 Relacionais 🔎

> **Esses operadores comparam dois valores e retornam um resultado booleano (``True`` ou ``False``).**
> São essenciais em estruturas de decisão, como ``if``, pois nos ajudam a saber se algo é maior, menor, igual ou diferente de outro valor.

| 🔁 Operador | 🤔 Significado | 💡 Exemplo |
|------------|----------------|------------|
| `==` | Igual | `5 == 5` → `True` |
| `!=` | Diferente | `5 != 3` → `True` |
| `>` | Maior que | `4 > 2` → `True` |
| `<` | Menor que | `2 < 1` → `False` |
| `>=` | Maior ou igual | `4 >= 4` → `True` |
| `<=` | Menor ou igual | `3 <= 5` → `True` |

## 🔹 Lógicos 🔗

> **Os operadores lógicos são utilizados para combinar expressões booleanas.**
> São muito úteis quando queremos verificar múltiplas condições ao mesmo tempo. Por exemplo: verificar se um usuário está logado e tem permissões de administrador.

### 📘 Tabela Verdade

> **Uma tabela verdade mostra todas as combinações possíveis de valores lógicos (True ou False) para uma determinada operação.**
> Ela é fundamental para entender o comportamento de operadores como and, or e not.

| A | B | A and B | A or B | not A |
|---|---|----------|---------|--------|
| ✅ | ✅ | ✅ | ✅ | ❌ |
| ✅ | ❌ | ❌ | ✅ | ❌ |
| ❌ | ✅ | ❌ | ✅ | ✅ |
| ❌ | ❌ | ❌ | ❌ | ✅ |

> **✅: ``True`` | ❌: ``False``**

### 🔹 Exemplos 🔗

| 🔣 Operador | 💬 Exemplo | 🎯 Resultado |
|-------------|------------|--------------|
| `and` | `True and False` | `False` |
| `or` | `True or False` | `True` |
| `not` | `not True` | `False` |

**Dica🔎:**

- ``and`` -> só retorna True se ambos forem ``True``.
- ``or`` -> retorna ``True`` se pelo menos um for ``True``.
- ``not`` -> 🔁 inverte o valor

> 📌 O operador `not` só depende de um valor (unário), diferente de `and` e `or`, que comparam dois valores.

## 🔹 Operadores de Identidade 🆔

> Usados para verificar se duas variáveis apontam para o mesmo objeto na memória, e não apenas se têm o mesmo valor.

| Operador | Descrição | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `is`     | Retorna `True` se as variáveis referenciam o mesmo objeto na memória | `a is b` | `True` ou `False` |
| `is not` | Retorna `True` se os objetos forem **diferentes** | `a is not b` | `True` ou `False` |

**💡 Dica: a == b compara os valores, enquanto a is b compara se são o mesmo objeto na memória.**

### Exemplo 🆔

```python
a = [1, 2]
b = a
c = [1, 2]
print(a is b)     # True → a e b são o mesmo objeto
print(a is c)     # False → a e c têm o mesmo conteúdo, mas são objetos diferentes
```

## 🔹 Operadores de Membros  🔎📦

> Usados para testar se um valor existe dentro de uma sequência, como listas, strings ou dicionários.

| Operador | Descrição | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `in`     | Retorna `True` se o valor estiver presente | `'a' in 'Carlos'` | `True` |
| `not in` | Retorna `True` se o valor **não** estiver presente | `5 not in [1,2,3]` | `True` |

### Exemplo 🔎📦

```python
frutas = ['maçã', 'banana']
print('banana' in frutas)       # True
print('laranja' not in frutas)  # True
print("uva" in frutas) # False
```

## 🔹 Operadores Bit a Bit (Bitwise) 🧠⚙️

> Operam diretamente em bits, sendo úteis em programação de baixo nível, redes, criptografia ou manipulação de permissões binárias.

| 🔢 Operador | 📛 Nome | 💬 Descrição |
|-------------|---------|---------------|
| `&` | AND | Retorna 1 se **ambos** os bits forem 1 |
| Uma barra  | OR | Retorna 1 se **algum** bit for 1 |
| `^` | XOR | Retorna 1 se os bits forem **diferentes** |
| `~` | NOT | Inverte todos os bits |
| `<<` | Shift à esquerda | Desloca bits para a esquerda |
| `>>` | Shift à direita | Desloca bits para a direita |

**💡 Lembre-se: números são representados em binário internamente. Por exemplo, 5 em binário é 0101.**

### Exemplo 🧠⚙️

```python
a = 5      # binário: 0101
b = 3      # binário: 0011
print(a & b)  # 1 → 0001 (0101 & 0011)
print(a | b)  # 7 → 0111 (0101 | 0011)
```

## 🔹 Atribuição 📝

> **Servem para armazenar valores em variáveis.** Além do clássico ``=``, existem operadores que realizam uma operação e já atualizam o valor da variável, como ``+=``, ``-=``, etc. Isso deixa o código mais limpo e direto.

| 🔢 Operador | 🟰 Equivalente            | 💡 Exemplo               |
| ----------- | ------------------------- | ------------------------ |
| `=`         | Atribuição simples        | `x = 10` → `x` vale `10` |
| `+=`        | Soma e atribui            | `x += 5` → `x = x + 5`   |
| `-=`        | Subtrai e atribui         | `x -= 3` → `x = x - 3`   |
| `*=`        | Multiplica e atribui      | `x *= 2` → `x = x * 2`   |
| `/=`        | Divide e atribui          | `x /= 4` → `x = x / 4`   |
| `//=`       | Divisão inteira e atribui | `x //= 3` → `x = x // 3` |
| `%=`        | Módulo e atribui          | `x %= 2` → `x = x % 2`   |
| `**=`       | Exponenciação e atribui   | `x **= 3` → `x = x ** 3` |

---

## ⚖️ Precedência dos Operadores

A ordem que o Python usa para resolver expressões:

1. `()` Parênteses
2. `**` Exponenciação
3. `+`, `-` (unário)
4. `*`, `/`, `//`, `%`
5. `+`, `-` (binário)
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in`
11. `not`
12. `and`
13. `or`
14. `=`, `+=`, `-=`, etc.

---

## 🚀 Conclusão

Os operadores em Python são ferramentas essenciais para realizar operações e comparar dados de forma eficiente. A partir dessa visão geral, você pode realizar desde simples cálculos aritméticos até manipulação avançada de dados com operadores lógicos, bit a bit e de atribuição.

**Para continuar avançando no seu aprendizado, aqui estão algumas sugestões de exercícios:**

- *Operadores Aritméticos:* Crie um programa que faça as quatro operações matemáticas com números fornecidos pelo usuário

- *Operadores Relacionais:* Desenvolva um sistema que compare a idade de duas pessoas e diga quem é mais velho.

- *Operadores Lógicos:* Implemente uma função que verifique se um número está entre dois valores (usando and e or).

- *Operadores de Membros:* Crie um programa que pergunte ao usuário por um item e verifique se esse item está em uma
lista de compras.

- *Operadores Bit a Bit:* Experimente manipular os bits de um número e veja como ele altera o valor.

**🔍 Dica:** A prática constante é a chave para solidificar o entendimento dos operadores. Com o tempo, eles se tornarão naturais no seu código!

**💡 Próximos Passos:** Depois de dominar os operadores, explore como utilizá-los em estruturas condicionais e estruturas de repetição. Isso vai permitir que você escreva programas mais dinâmicos e interessantes!

> Dominar os operadores te dá controle total sobre como seu programa toma decisões e transforma dados. Essa é a base para criar sistemas inteligentes e eficientes!

**Próximo arquivo : [condicionais](02_condicionais.md)**
