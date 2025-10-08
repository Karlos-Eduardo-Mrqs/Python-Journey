# ✍️ Declaração e Chamadas de Funções

Para criar uma função em Python, utilizamos a palavra-chave def, seguida do nome da função, parênteses (que podem conter parâmetros) e dois pontos. O corpo da função deve ser indentado.

> Essa estrutura permite que você defina blocos de código reutilizáveis que podem receber valores de entrada (argumentos) e executar uma ação sempre que forem chamados.

---

## 📌 Sintaxe básica com def

```python
def saudacao():
    print("Olá! Seja bem-vindo(a).")
```

- ``def`` → palavra-chave que indica a criação de uma função
- ``saudacao`` → nome da função (escolhido pelo programador)
- ``()`` → espaço para receber parâmetros (aqui vazio)
- ``:`` → marca o início do bloco da função
- ``Corpo da função`` → sempre indentado (geralmente 4 espaços)

### 📌 Chamando funções

Depois de declarar, basta chamar a função pelo nome:

```python
saudacao()
```

> Saída:

```cmd
Olá! Seja bem-vindo(a).
```

---

## 📌 Parâmetros e Argumentos

Uma função pode receber informações externas para personalizar sua execução. Esses valores são chamados de argumentos quando enviados e de parâmetros quando definidos na função.

```python
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")

saudacao("Carlos")
saudacao("Ana")
```

---

## 📌 Argumentos Posicionais e Nomeados

Em Python, os argumentos podem ser passados de duas formas:

- *Posicionais* → respeitam a ordem definida na função;
- *Nomeados* → indicam explicitamente a qual parâmetro pertencem

```python

def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")

# Argumentos posicionais
apresentar("Carlos", 20)

# Argumentos nomeados (ordem não importa)
apresentar(idade=25, nome="Ana")
```

---

## 📌 Conclusão

Nesta etapa, aprendemos a declarar funções com def, a chamá-las e a usar parâmetros e argumentos para tornar nossas funções mais dinâmicas.
Também vimos que podemos usar argumentos posicionais ou nomeados, garantindo maior flexibilidade no código.

No próximo capítulo, exploraremos com mais profundidade os parâmetros opcionais, retornos de valores e o conceito de escopo, ampliando as possibilidades no uso de funções.

**Próximo Capítulo: [Parâmetros e Escopo](../aula_15/15_parametros_escopo.md)**

---

## 📝 Exercícios Aula 14 - Módulo 2

### Função com parâmetro único

Crie uma função chamada dobro que receba um número e exiba o dobro dele.

### Função com múltiplos parâmetros

Crie uma função chamada ``dados_pessoa`` que receba nome, idade e cidade, e exiba:

### Função com valor calculado

Crie uma função chamada ``calcular_media`` que receba duas notas e calcule a média.

### Função demonstrando argumentos nomeados

Crie uma função chamada produto que receba ``nome, preço e quantidade``.

**[Gabarito](exercicios/README.md)**
