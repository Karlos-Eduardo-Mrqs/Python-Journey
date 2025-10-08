# 🔹 Funções Anônimas (lambda) e Boas Práticas

Além das funções criadas com def, o Python também permite declarar funções anônimas, *chamadas de lambda*. Elas são úteis quando precisamos de funções rápidas, pequenas e temporárias, sem necessidade de declarar um nome.

---

## 1. O que são funções lambda?

Uma função lambda é uma função pequena e anônima que:

> **Não possui nome;**
> **É definida em uma única linha;**
> **Retorna sempre o resultado de uma única expressão.**

- 📌 Exemplo simples:

```python
soma = lambda x, y: x + y
print(soma(3, 5))  # 8
```

## 2. Sintaxe

A estrutura é sempre:

```python
lambda argumentos: expressão
```

- ``argumentos`` → parâmetros da função.
- ``expressão`` → operação a ser retornada.

## 3. Quando usar?

1. Quando precisamos de funções curtas e rápidas;

2. Em funções que recebem outras funções como argumento (``map``, ``filter``, ``sorted``);

3. Quando não compensa criar uma função completa com ``def``.

## 4. Exemplos práticos

### 🔹 ``map()`` com lambda

Aplica uma função em todos os elementos de uma coleção:

```python
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25]
```

### 🔹 ``filter()`` com lambda

Filtra valores de acordo com uma condição:

```python
numeros = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [10, 20, 30]
```

### 🔹 ``sorted()`` com lambda

Permite definir regras de ordenação personalizadas:

```python
nomes = ["Ana", "Carlos", "Beatriz", "João"]
ordenados = sorted(nomes, key=lambda nome: len(nome))
print(ordenados)  # ['Ana', 'João', 'Carlos', 'Beatriz']
```

## 5. Modularização com funções pequenas

Usar lambda ajuda a modularizar o código em tarefas curtas, tornando-o mais conciso:

```python
# Funções pequenas para cálculos rápidos
dobro = lambda x: x * 2
quadrado = lambda x: x ** 2

print(dobro(5))     # 10
print(quadrado(4))  # 16
```

## 6. Mistura de argumentos

As funções lambda também aceitam valores padrão e argumentos nomeados:

```python
calculo = lambda a, b=2, c=1: a * b + c
print(calculo(5))        # 11 (5*2 + 1)
print(calculo(5, 3))     # 16 (5*3 + 1)
print(calculo(5, c=10))  # 20 (5*2 + 10)
```

## 7. Funções Recursivas

Embora não seja comum, é possível criar funções recursivas com lambda. *📌 Exemplo: fatorial:*

```python
fatorial = (lambda f: (lambda x: 1 if x == 0 else x * f(f)(x-1)))(
    lambda f: (lambda x: 1 if x == 0 else x * f(f)(x-1))
)

print(fatorial(5))  # 120
```

> ⚠️ Esse estilo funciona, mas perde legibilidade. 👉 Para recursão, prefira sempre def.

## 8. Boas Práticas

> ✅ Use lambda quando:

1. A função for simples (uma única linha);
2. Você não precisará reutilizá-la várias vezes;
3. Ela for usada como argumento em funções como ``map``, ``filter`` ou ``sorted``.

> ❌ Evite lambda quando:

1. O código ficar difícil de ler;
2. Você precisar de múltiplas instruções ou documentação.
3. A função tiver lógica complexa.

> 📌 Regra de ouro: Se a função precisa de mais de uma linha → use def.

---

## 💡 Conclusão

lambda é uma forma prática de criar funções rápidas e simples. Muito útil com funções como ``map``, ``filter`` e ``sorted``. Ajuda na modularização, mas deve ser usada com cautela para não comprometer a legibilidade. Para funções complexas ou reutilizáveis, prefira ``def``.

### 🧾 Exercícios práticos

1. Crie uma função lambda que receba um número e retorne o dobro.
2. Use ``map()`` com lambda para converter temperaturas de Celsius para Fahrenheit.
3. Use ``filter()`` com lambda para selecionar apenas os nomes que começam com "A".
4. Ordene uma lista de dicionários com ``sorted()`` e lambda pela idade:

```python
pessoas = [
    {"nome": "Carlos", "idade": 25},
    {"nome": "Ana", "idade": 30},
    {"nome": "Beatriz", "idade": 22}
]
```

**[Gabarito](exercicios/README.md)**
