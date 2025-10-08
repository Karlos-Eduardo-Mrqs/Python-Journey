# 🧰 Funções em Python

Funções são blocos de código reutilizáveis que podem ser chamados para realizar uma tarefa específica. Elas ajudam a tornar o código mais organizado, modular e fácil de entender. Com funções, você consegue:

- **✅ Reutilizar código sem repetir blocos**
- **✅ Modularizar programas em partes lógicas**
- **✅ Melhorar legibilidade e manutenção**
- **✅ Facilitar a criação de programas escaláveis**

> Em Python, funções são criadas com ``def`` ou de forma anônima com ``lambda``.

---

## 📚 Estrutura de estudo das funções

Para facilitar o aprendizado, vamos dividir as funções em blocos de afinidade:

### [🔹 1. Introdução às Funções](13_O_que_sao_funcoes.md)

Apresenta o conceito de funções, suas vantagens e um exemplo simples para começar a praticar. 👉 Inclui:

1. O que são funções ?
2. Por que usar funções ?
3. Função simples de saudação
4. Exemplos de uso: Criar uma função que imprime uma mensagem de boas-vindas
5. Demonstrar a reutilização de um bloco de código

## [🔹 2. Declaração e Chamadas de Funções](14_declaracao_de_funcoes.md)

Explora como escrever e chamar funções, e como passar informações para elas usando parâmetros e argumentos. 👉 Inclui:

1. Sintaxe com ``def``
2. Chamando funções
3. Parâmetros e argumentos
4. Argumentos posicionais e nomeados
5. Exemplos de uso: Função que recebe o nome do usuário e imprime uma saudação personalizada
6. Uso de argumentos nomeados para alterar a ordem sem afetar a execução

## [🔹 3. Parâmetros e Escopo](15_parametros_escopo.md)

Aborda a profundidade de como funções lidam com valores e variáveis, incluindo retornos e escopo de variáveis. 👉 Inclui:

1. Parâmetros opcionais com valores padrão
2. Argumentos nomeados e a ordem correta
3. return e múltiplos retornos (tuplas)
4. Escopo local vs global
5. Exemplos práticos
6. Exemplos de uso:
7. Função que retorna a soma e o produto de dois números
8. Demonstrar escopo local e global de variáveis

## [🔹 4. Funções Anônimas (lambda) e Boas Práticas](16_funcoes_lambda.md)

Apresenta funções pequenas e sem nome, ideais para operações rápidas ou como argumentos de outras funções. 👉 Inclui:

1. O que são funções lambda ?
2. Sintaxe e exemplos simples
3. Quando usar: ``map``, ``filter``, ``sorted``
4. Modularização do código com funções pequenas
5. Mistura de argumentos posicionais e nomeados
6. Funções recursivas
7. Exemplos de uso: Soma de dois números com lambda
8. Aplicar ``map()`` ou ``filter()`` em listas
9. Função recursiva para cálculo de fatorial

---

### 💡 Dica útil

Você pode misturar argumentos posicionais e nomeados, mas os posicionais devem vir antes dos nomeados.Isso garante clareza na leitura e evita erros na chamada da função. Exemplo:

```python
def dados_pessoais(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

dados_pessoais("Ana", 30, cidade="São Paulo")
```

---

## Conclusão 🚀

As funções em Python são blocos de código reutilizáveis que permitem organizar e modularizar seu programa, tornando-o mais legível, eficiente e fácil de manter. Elas são fundamentais para reduzir a repetição de código e facilitar a criação de programas escaláveis.

Ao entender como definir e chamar funções, como passar parâmetros e retornar valores, você será capaz de criar soluções mais sofisticadas e elegantes. Além disso, as funções podem ter parâmetros padrão, variáveis e retornar múltiplos valores, o que aumenta ainda mais sua flexibilidade.

## 🔧 Dicas para a prática

- **Modularização de código:**
Divida seu código em funções pequenas, cada uma responsável por uma tarefa específica, para facilitar a manutenção e reutilização.

- **Funções recursivas:**
Experimente criar funções recursivas para problemas que podem ser divididos em subproblemas menores, como o cálculo de fatorial ou a resolução de problemas de busca e ordenação.

> Agora é hora de colocar o aprendizado em prática! ✨🐍 Continue explorando e criando suas próprias funções para resolver problemas do cotidiano e aprimorar suas habilidades em Python!

**Próximo Modulo : [Estrutura de Dados](../../3.%20estrutura%20de%20dados/)**

---

## 📝 Exercícios Aula 12

### Função de soma

Crie uma função que receba dois números como parâmetros e retorne a soma deles.

### Função de média

Crie uma função que receba uma lista de números e retorne a média desses números.

### Função de fatorial

Implemente uma função que calcule o fatorial de um número.

### Função de verificação de número primo

Crie uma função que determine se um número fornecido é primo.

### Função de contagem de caracteres

Faça uma função que conte a quantidade de ocorrências de um caractere em uma string.

**[Gabarito](exercicios/README.md)**
