# 🔹 Parâmetros e Escopo em Funções Python

Este capítulo aprofunda como funções lidam com valores e variáveis, mostrando como passar informações, definir valores padrão e entender onde as variáveis podem ser acessadas dentro do programa.

---

## 🔹 Parâmetros Opcionais com Valores Padrão

Parâmetros opcionais permitem que você defina valores padrões para os argumentos da função. Assim, se o usuário não passar um valor, a função usa o padrão.

> ✅ Sintaxe:

```python

def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")
```

> 📌 Exemplo de uso:

```python

saudacao()        # Saída: Olá, Usuário!
saudacao("Ana")   # Saída: Olá, Ana!
```

> 💡 Observação: Parâmetros com valores padrão devem sempre vir após os obrigatórios.

---

## 🔹 Argumentos Nomeados e a Ordem Correta

Argumentos nomeados permitem especificar explicitamente qual parâmetro está recebendo o valor. Isso torna o código mais legível e permite trocar a ordem dos argumentos.

> 📌 Exemplo:

```python
def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")

apresentar(idade=25, nome="Carlos")  # Saída: Meu nome é Carlos e tenho 25 anos.
```

> 💡 Dica: Sempre que misturar argumentos posicionais e nomeados, os posicionais devem vir primeiro.

### 🔹 Return e Múltiplos Retornos

A instrução return devolve um valor de uma função. Ao encontrar um return, a função termina a execução naquele ponto.

> ✅ Sintaxe:

```python
def soma(a, b):
    return a + b
```

> 📌 Exemplo:

```python
resultado = soma(3, 5)
print(resultado)  # Saída: 8
```

**Funções também podem retornar múltiplos valores como uma tupla, que pode ser desempacotada em variáveis separadas.**

> 📌 Exemplo:

```python
def operacoes(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

resultado_soma, resultado_produto = operacoes(3, 5)
print(resultado_soma, resultado_produto)  # Saída: 8 15
```

---

## 🔹 Escopo de Variáveis

O escopo define onde uma variável pode ser acessada:

- *Local*: Variáveis criadas dentro de funções só existem lá.
- *Global*: Variáveis criadas fora de funções podem ser acessadas em qualquer parte do código.

> 📌 Exemplo:

```python
variavel_global = "Sou global"

def exemplo():
    variavel_local = "Sou local"
    print(variavel_global)  # Funciona
    print(variavel_local)   # Funciona

exemplo()
# print(variavel_local)    # Erro! Não existe fora da função
```

> 💡 Dica: Use variáveis globais com cautela, pois podem dificultar a manutenção do código.

### 🔹 Exemplos Práticos

- *Função que retorna soma e produto*

```python
def calculos(a, b):
    return a + b, a * b

soma, produto = calculos(4, 5)
print(soma, produto)  # Saída: 9 20
```

#### Escopo local vs global

```python
x = 10  # global

def alterar_valor():
    x = 5  # local
    print("Dentro da função:", x)

alterar_valor()       # Dentro da função: 5
print("Fora da função:", x)  # Fora da função: 10
```

---

## ✅ Conclusão

Compreender parâmetros, argumentos, retorno de valores e o escopo de variáveis é essencial para escrever funções claras, reutilizáveis e seguras em Python.

- Parâmetros opcionais permitem funções mais flexíveis.
- Argumentos nomeados aumentam a legibilidade e evitam erros na ordem dos parâmetros.
- Return possibilita que funções devolvam valores, inclusive múltiplos valores simultaneamente.
- Escopo local e global ajuda a controlar onde suas variáveis podem ser acessadas, evitando efeitos colaterais indesejados.
- Dominar esses conceitos permite criar funções robustas, modulares e eficientes, que são a base de programas bem estruturados.

**Próximo capítulo: [Funções lambda e Boas Práticas](../aula_16/16_funcoes_lambda.md)**

---

## 📝 Exercícios da aula 15

### Função com múltiplos retornos

1. ``Crie uma função chamada estatisticas(lista) que receba uma lista de números``
2. ``Retorne o maior, o menor e a média.``
3. Depois, desempacote o ``retorno em três variáveis e exiba os resultados.``

### Escopo local e global

1. Crie uma ``variável global chamada saldo`` = 1000.
2. Depois, crie uma função chamada ``comprar(valor)`` que:

   1. ``Crie uma variável local saldo = 500;``  
   2. ``Subtraia o valor da compra do saldo local e exiba dentro da função.``

3. Por fim, mostre o valor de saldo fora da função para destacar a diferença de escopo

### Retorno condicional com ``return``

1. Crie uma função chamada ``verificar_idade(idade)`` que:
2. ``Retorne "Menor de idade" se a idade for menor que 18.``
3. ``Retorne "Maior de idade" caso contrário.``
4. Teste a função chamando-a com diferentes idades.

**[Gabarito](exercicios/README.md)**
