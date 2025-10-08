# 📝 Exercícios Resolvidos — Aula 16 (Módulo 2)

Nesta aula, aprendemos funções anônimas (lambda), e como utilizá-las com map(), filter() e sorted() para simplificar operações comuns em listas e coleções.

---

## 🔹 1. Função Lambda — Dobro de um número

```py
dobro = lambda num: num * 2

print(dobro(4))  # Saída: 8
print(dobro(6))  # Saída: 12
```

> 📌 Explicação:

1. ``lambda num: num*2`` cria uma função anônima que recebe um número e retorna o dobro.
2. Não precisa declarar com def e pode ser usada imediatamente.
3. Ideal para funções simples de linha única.

## 🔹 2. Conversão de Temperatura — Celsius para Fahrenheit com map()

```py
valor_celsius = [38.5, 15.6, 36.8, 37.0]

valor_farenheit = list(map(lambda celsius: (celsius * 9/5) + 32, valor_celsius))

print(valor_farenheit)
```

> 📌 Explicação:

1. ``map()`` aplica a função lambda em cada elemento da lista.
2. Cada valor de Celsius é convertido para Fahrenheit.
3. Resultado é convertido em lista com list().

## 🔹 3. Filtrar nomes que começam com "A" usando filter()

```py
nomes = ["Ana", "Carlos", "Amanda", "Beatriz", "Arthur", "João"]

nomes_com_A = list(filter(lambda nome: nome.startswith("A"), nomes))

print(nomes_com_A)
```

> 📌 Explicação:

1. ``filter()`` seleciona apenas os elementos que retornam True na função lambda.
2. Aqui, usamos ``startswith("A")`` para pegar nomes que começam com a letra ``"A"``.

## 🔹 4. Ordenar lista de dicionários por idade usando sorted()

```py
pessoas = [
    {"nome": "Carlos", "idade": 25},
    {"nome": "Victor", "idade": 30},
    {"nome": "Beatriz", "idade": 22}
]

ordenacao_idade = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(ordenacao_idade)
```

> 📌 Explicação:

1. ``sorted()`` ordena a lista com base no valor retornado pela função lambda.
2. ``key=lambda pessoa: pessoa["idade"]`` indica que a ordenação deve ser feita pelo campo idade de cada dicionário.
3. Resultado: lista ordenada do mais novo para o mais velho.

**Próximo Módulo : [Programação Orientada a Objetos](../../../4.%20orientacao_objetos/README.md)**
