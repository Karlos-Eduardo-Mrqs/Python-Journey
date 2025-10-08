# ⚙️ Estruturas de Repetição em Python

As estruturas de repetição permitem que um bloco de código seja executado várias vezes, com base em uma condição ou em um número específico de iterações.

Elas são essenciais para automatizar tarefas repetitivas e processar grandes volumes de dados de forma eficiente.

## 📌 Por que são importantes?

- Permitem automatizar tarefas repetitivas;
- Facilitam o processamento de coleções de dados;
- Tornam o código mais compacto e fácil de entender;

---

## 📚 Estrutura de estudo dos loopings

Para facilitar o aprendizado, vamos dividir os loopings em blocos de afinidade:

### [1. loopings_contaveis.md](10_loopings_contaveis.md)

> 👉 Focado em for e situações em que sabemos quantas vezes queremos repetir.

- Explicação sobre ``for``;
- Uso de ``range()`` (com início, fim e passo);
- Iteração em listas, tuplas, strings, dicionários;
- Funções auxiliares: ``enumerate()``, ``zip()``;
- Compreensões de listas ``(list comprehension)``;
- Exercícios práticos.

### [2. loopings_nao_contaveis.md](11_loopings_nao_contaveis.md)

> 👉 Focado em while e situações em que não sabemos quantas vezes vai repetir, só depende de uma condição.

- Explicação sobre ``while``;
- Diferença entre contável e não contável;
- Cuidados com loops infinitos;
- Controle de fluxo: ``break``, ``continue``, ``pass``;
- Exemplos práticos de repetição até o usuário digitar algo ou até uma condição ser atingida;
- Exercícios práticos.

---

## 🚀 Conclusão

As estruturas de repetição são fundamentais para automatizar tarefas e trabalhar com grandes volumes de dados em Python. Com elas, você pode repetir ações com base em condições (`while`) ou percorrer sequências de forma eficiente (`for`), além de controlar o fluxo de execução com `break`, `continue` e `pass`.

Ao dominar também ferramentas como `range()`, `enumerate()`, `zip()` e compreensões de listas, você torna seu código mais limpo, elegante e poderoso.

### 🔧 Dicas para a prática

- **Use `for` quando souber quantas vezes precisa repetir algo.**
- **Use `while` quando a repetição depender de uma condição.**
- **Explore funções como `range()`, `enumerate()` e `zip()` para tornar seus loops mais poderosos.**
- **Pratique a leitura e escrita de compreensões de lista — elas tornam seu código mais enxuto e expressivo.**

> Obs.: leia os outros capítulos sobre looppings antes de você continuar sua jornada !

**Próximo Capítulo : [Funções](../aula_12/12_funcoes.md)**

---

## 📝 Exercícios aula 09

### Contar de 1 a 10 usando `for`

Crie um programa que utilize um loop `for` para imprimir os números de 1 a 10.

### Contador com `while`

Faça um programa que conte de 0 até 20, pulando de 2 em 2, utilizando `while`.

### Soma de uma lista

Utilize um `for` para somar todos os elementos de uma lista de números inteiros. A lista é ``numeros = [8,7,9,8,5,5,6,10,4,5,8,2,3]``

### Busca com `break`

Crie um programa que faça o usuário digitar uma lista de numeros inteiros, pare até que o usuário digite 0, após isso, imprima a lista dos números.

### Filtrar pares com `continue`

Percorra uma lista de 1 a 10 e imprima apenas os números pares, utilizando `continue` para ignorar os ímpares.

### Compreensão de listas

Crie uma nova lista com os quadrados dos números de 1 a 10 usando list comprehension.

**[Gabarito](exercicios/README.md)**
