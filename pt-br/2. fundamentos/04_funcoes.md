# 🧰 Funções em Python

Funções são blocos de código reutilizáveis que podem ser chamados para realizar uma tarefa específica. Elas ajudam a tornar o código mais organizado, modular e fácil de entender.

## 📌 Por que usar funções?

- **Reutilização de código:** evita repetir o mesmo código várias vezes.
- **Modularização:** organiza o código em blocos lógicos e independentes.
- **Melhor legibilidade e manutenção:** facilita o entendimento e a alteração do código.

## 🔹 Declaração de funções com def

Para criar uma função, utilizamos a palavra-chave def, seguida do nome da função, parênteses e dois pontos. O corpo da função é indentado.

> ✅ Sintaxe:

```python
def nome_da_funcao(parâmetros):
    # código da função
    return valor
```

> 📌 Exemplo de uso: Função simples que imprime uma saudação.

```python
def saudacao():
    print("Olá, bem-vindo!")

saudacao()  # Saída: Olá, bem-vindo!
```

## 🔷 Parâmetros e Argumentos

Parâmetros são as variáveis listadas na declaração da função. Argumentos são os valores passados para a função quando ela é chamada.

> 📌 Exemplo de uso:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Carlos")  # Saída: Olá, Carlos!
```

## 🔷 Argumentos Padrão e Nomeados

Em Python, podemos tornar parâmetros opcionais atribuindo a eles valores padrão. Também podemos especificar valores por nome, o que permite mudar a ordem dos argumentos e aumenta a legibilidade do código.

### Parâmetros com valores padrão

Parâmetros com valores padrão permitem que você defina um valor "automático" para um parâmetro, caso ele não seja informado na chamada da função. Isso torna o parâmetro opcional e evita erros ao chamar a função com menos argumentos.

> ✅ Sintaxe:

```python
def nome_da_funcao(parâmetro1=valor1, parâmetro2=valor2):
    # código
```

> 📌 Exemplo de uso:

```python
def saudacao(nome="Usuário"):
    print(f"Olá, {nome}!")

saudacao()       # Saída: Olá, Usuário!
saudacao("Ana")  # Saída: Olá, Ana!
```

#### 📘 Explicação

No exemplo acima, a função saudacao foi definida com um valor padrão "Usuário" para o parâmetro nome. Assim, se o usuário não passar nenhum argumento, "Usuário" será usado automaticamente.

### Argumentos Nomeados

Argumentos nomeados permitem passar os valores especificando o nome do parâmetro. Isso torna a chamada da função mais clara e permite mudar a ordem dos argumentos, sem afetar a lógica.

> 📌 Exemplo de uso:

```python
def saudacao(nome, idade):
    print(f"Olá, {nome}. Você tem {idade} anos.")

saudacao(idade=25, nome="Carlos")  # Saída: Olá, Carlos. Você tem 25 anos.
```

#### 📘 Explicação

Mesmo que idade venha antes de nome na chamada da função, ela funciona corretamente porque os argumentos foram nomeados. Isso é útil para funções com muitos parâmetros, ou quando queremos deixar o código mais legível.

## 🔷 return

A instrução return é usada para devolver um valor de uma função. Quando uma função encontra um return, ela encerra a execução e retorna o valor especificado.

> ✅ Sintaxe:

```python
def soma(a, b):
    return a + b
```

> 📌 Exemplo de uso:

```python
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # Saída: 8
```

## 🔷 Funções com Múltiplos Retornos

Em Python, uma função pode retornar mais de um valor de uma vez. Esses valores são retornados como uma tupla (mesmo que você não veja os parênteses) e podem ser desempacotados em variáveis separadas.

> ✅ Sintaxe

```python
def nome_funcao():
    return valor1, valor2, ..., valorN
```

> 📌 Exemplo explicado

```python
def operacoes(a, b):
    soma = a + b
    produto = a * b
    return soma, produto  # retorna dois valores
```

### 💡 Dica útil

Você pode misturar argumentos posicionais e nomeados, mas os posicionais devem vir antes dos nomeados.Isso garante clareza na leitura e evita erros na chamada da função. Exemplo:

```python
def dados_pessoais(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

dados_pessoais("Ana", 30, cidade="São Paulo")
```

## 🔹 Escopo de Variáveis

O escopo de uma variável determina onde ela pode ser acessada. Existem dois tipos de escopo em Python:

- **Escopo Local:🚩** Variáveis definidas dentro de uma função, acessíveis apenas dentro dessa função.
- **Escopo Global:🌐** Variáveis definidas fora de qualquer função, acessíveis em qualquer parte do código.

> 📌 Exemplo de uso de escopo:

```python
variavel_global = "Eu sou global!"

def exemplo():
    variavel_local = "Eu sou local!"
    print(variavel_global)  # Acessa a variável global
    print(variavel_local)   # Acessa a variável local

exemplo()
# print(variavel_local)  # Erro! Não pode acessar variáveis locais fora da função.
```

## 🔷 Funções Anônimas com lambda

As funções anônimas, ou funções lambda, são funções pequenas e sem nome, geralmente usadas para operações simples que podem ser feitas em uma única linha. Elas são muito úteis em funções como map(), filter() e sorted(). 

> ✅ Sintaxe:

```python
variavel = lambda argumentos: expressão
```

> 📌 Exemplo de uso:

```python
soma = lambda x, y: x + y
print(soma(3, 5))  # Saída: 8
```

--

# Conclusão 🚀

As funções em Python são blocos de código reutilizáveis que permitem organizar e modularizar seu programa, tornando-o mais legível, eficiente e fácil de manter. Elas são fundamentais para reduzir a repetição de código e facilitar a criação de programas escaláveis.

Ao entender como definir e chamar funções, como passar parâmetros e retornar valores, você será capaz de criar soluções mais sofisticadas e elegantes. Além disso, as funções podem ter parâmetros padrão, variáveis e retornar múltiplos valores, o que aumenta ainda mais sua flexibilidade.

## 📝 Exercícios de Funções

1. **Função de soma**
Crie uma função que receba dois números como parâmetros e retorne a soma deles.

2. **Função de média**
Crie uma função que receba uma lista de números e retorne a média desses números.

3. **Função de fatorial**
Implemente uma função que calcule o fatorial de um número.

4. **Função de verificação de número primo**
Crie uma função que determine se um número fornecido é primo.

5. **Função de contagem de caracteres**
Faça uma função que conte a quantidade de ocorrências de um caractere em uma string.

## 🔧 Dicas para a prática:

- **Modularização de código:**
Divida seu código em funções pequenas, cada uma responsável por uma tarefa específica, para facilitar a manutenção e reutilização.

- **Funções recursivas:**
Experimente criar funções recursivas para problemas que podem ser divididos em subproblemas menores, como o cálculo de fatorial ou a resolução de problemas de busca e ordenação.

> Agora é hora de colocar o aprendizado em prática! ✨🐍 Continue explorando e criando suas próprias funções para resolver problemas do cotidiano e aprimorar suas habilidades em Python!

**Próximo Modulo : [Estrutura de Dados](../3.%20estrutura%20de%20dados/README.md)**