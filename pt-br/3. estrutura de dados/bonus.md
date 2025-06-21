# 🌀 Bônus — Compreensões de Listas em Python

## 📌 O que é uma compreensão?

Uma **compreensão** é uma maneira concisa de criar novas sequências (como listas, conjuntos ou dicionários) aplicando uma expressão a cada item de um iterável.

Elas ajudam a tornar seu código **mais limpo, mais curto e, muitas vezes, mais legível**.

```python
# Maneira tradicional
squares = []
for i in range(5):
squares.append(i * i)

# Com compreensão de lista
squares = [i * i for i in range(5)]
```

---

## 🧩 Compreensão de Lista — Sintaxe

```python
[expressão para item em iterável se condição]
```

* `expressão`: o que você deseja fazer com cada item
* `item`: cada elemento do iterável
* `condição` (opcional): filtrar quais itens incluir

### ✅ Exemplos

```python
# Todos os números pares entre 0 até 10
evens = [x for x in range(11) if x % 2 == 0]

# Os números ao quadrado até o número 6
squares = [x**2 for x in range(1, 6)]

# Converte a lista de palavras e as transforma elas em palavras maiúsculas
palavras = ["python", "rocks"]
palavras_maisculas = [palavras.upper() for palavra in palavras]
```

---

## 🔄 Compreensões de Conjuntos e Dicionários

### Conjunto

```python
tamanho = {len(palavra) for palavra in ["hello", "world", "hi"]}
```

### Dicionário

```python
numeros_ao_quadrado = {x: x**2 for x in range(1, 6)}
print(numeros_ao_quadrado)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🧪 Hora do Desafio!

Tente resolver estes problemas usando compreensões:

1. Crie uma lista dos 10 primeiros múltiplos de 3.
2. Construa um conjunto de caracteres únicos (excluindo espaços) a partir de uma frase.
3. Crie um dicionário que mapeie números de 1 a 5 para seu fatorial.

---

## 🎯 Por que usar compreensões?

* Escreva um código mais limpo e expressivo
* Evita clichês desnecessários
* Transformações mais fáceis de identificar rapidamente

Mas lembre-se: **não sacrifique a legibilidade pela concisão**. Se ficar muito complexo, um laço regular pode ser melhor.

---

> 🚀 Dominar as compreensões tornará seu código Python mais rápido de escrever e mais fácil de ler. Um pequeno investimento para uma grande clareza!

**Próximo Módulo [orientação a objetos](../4.%20orientacao_objetos/readme.md)**