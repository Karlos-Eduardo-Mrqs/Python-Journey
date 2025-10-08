# 📘 Classes e Objetos

Bem-vindo ao primeiro capítulo do Módulo 4! 🚀  
Antes de mergulharmos em código, vamos entender **o que é Programação Orientada a Objetos (POO)**.  

---

## 🔹 Introdução à POO

A **Programação Orientada a Objetos** é um paradigma que permite modelar o mundo real dentro do seu código.  

Em vez de apenas criar funções e variáveis soltas (programação procedural), na POO você organiza **dados e comportamentos** em entidades chamadas **objetos**.  

- **Classe**: é o “molde” ou “projeto” que define como um objeto deve ser.  

- **Objeto**: é uma instância concreta de uma classe, ou seja, algo criado a partir do molde.  

Pense em **uma classe como a planta de uma casa**, e **os objetos como as casas construídas a partir dessa planta**.  

---

## 📖 Por que usamos POO?

Na programação procedural (com funções e variáveis soltas), o código tende a crescer e ficar **difícil de organizar** conforme o projeto aumenta.  
Por exemplo, se você tem várias funções que manipulam dados de pessoas, é fácil perder controle de quais dados pertencem a quem, ou acabar duplicando código.

A **Programação Orientada a Objetos** resolve isso ao permitir que dados e comportamentos relacionados fiquem **juntos dentro de objetos**.  
Assim, você consegue:

- Organizar o código de forma mais **clara e modular**;  
- Reutilizar estruturas já criadas, evitando **duplicação**;  
- Modelar problemas do mundo real de forma mais **natural e intuitiva**;  
- Facilitar manutenção e expansão do software no futuro.

---

## 📖 Criando sua primeira classe

Vamos criar uma classe simples chamada `Pessoa`:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # atributo
        self.idade = idade    # atributo

    def apresentar(self):     # método
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

1. ``class Pessoa:`` → Define a classe Pessoa; é como um molde que descreve como os objetos dessa classe devem ser.

2. ``__init__(self, nome, idade):`` → Construtor da classe, chamado automaticamente quando um objeto é criado; serve para inicializar os atributos do objeto.

3. ``self.nome`` e ``self.idade`` → Atributos do objeto; armazenam os dados específicos de cada instância da classe.

4. ``self`` → Referência ao próprio objeto; permite que cada objeto mantenha seus próprios valores de atributos na memória.

5. ``apresentar(self)`` → Método da classe; é uma função que define um comportamento do objeto, podendo acessar seus atributos através de self.

---

## 📖 Criando objetos (instâncias)

Agora, vamos criar objetos da classe Pessoa:

```python

# Entrada dos Objetos

p1 = Pessoa("João", 25)
p2 = Pessoa("Carlos", 30)

p1.apresentar()
p2.apresentar()

# Saída dos Objetos

Olá, meu nome é João e tenho 25 anos.
Olá, meu nome é Carlos e tenho 25 anos.

```

## 📝 Conclusão

Agora que você aprendeu sobre classes e objetos em Python, é hora de colocar a mão na massa!  

✅ **Desafios sugeridos:**

1. Crie uma classe `Carro` com atributos como `marca`, `modelo` e `ano`, e um método `apresentar()` que mostre essas informações.  

2. Crie duas ou mais instâncias da classe `Carro` e teste chamando o método `apresentar()` de cada objeto.  

3. Experimente adicionar novos atributos aos objetos depois da criação, como `cor` ou `quilometragem`, e veja como cada objeto mantém seus próprios dados.  

4. Tente criar uma classe `Animal` com métodos `comer()` e `dormir()`, e depois crie instâncias diferentes (`Cachorro`, `Gato`) para testar os comportamentos.  

> Praticar criando objetos e manipulando seus atributos e métodos ajuda a internalizar o conceito de POO e a entender como modelar o mundo real dentro do código.  

**[Comentando Desafios](desafios/README.md)**

---

**Próximo capítulo [Encapsulamento](../aula_02/02_encapsulamento.md)**
