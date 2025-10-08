# Exercícios de Orientação a Objetos em Python — Aula 01 (Módulo 4)

Este projeto contém a resolução de exercícios de programação orientada a objetos (POO) em Python, incluindo criação de classes, atributos, métodos e herança.

---

## [🔹 1. Classe Carro](EX_01.py)

```py
class Carro:
    def __init__(self,marca:str,modelo:str,ano:int,cor:str,quilometragem:float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def apresentar(self):
        print("--------------------------------------------")
        print(f"Marca : {self.marca} | Modelo : {self.modelo} | Ano : {self.ano} | Cor : {self.cor} | Quilometragem : {self.quilometragem} |")
        print("--------------------------------------------")
        
carro = Carro("Pegeout","Pegeout 2008",2023,"vermelho",12_000.0)
carro2 = Carro("Honda", "Civic", 2022,"azul",15_000.0)
carro.apresentar()
carro2.apresentar()
```

> Explicação:

1. ``class Carro:`` define a classe Carro com atributos e métodos.
2. ``O método __init__`` é o construtor, responsável por inicializar os atributos do objeto (marca, modelo, ano, cor, quilometragem).
3. ``self`` representa a própria instância do objeto.
4. ``apresentar()`` é um método que imprime os detalhes do carro.
5. ``carro e carro2`` são objetos criados a partir da classe Carro.
6. Chamadas ``carro.apresentar()`` e ``carro2.apresentar()`` exibem as informações de cada carro.

---

## [🔹 2. Herança com animais](EX_02.py)

```py
class Animal:
    def comer(self):
        print("O animal está comendo.")
    
    def dormir(self):
        print("O animal está dormindo.")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo: Au Au!")

class Gato(Animal):
    def miar(self):
        print("O gato está miando: Miau!")

animal = Animal()
animal.comer()
animal.dormir()

cachorro = Cachorro()
cachorro.latir()
cachorro.comer()
cachorro.dormir()

gato = Gato()
gato.miar()
gato.comer()
gato.dormir()
```

> Explicação:

1. ``class Animal`` define uma classe base com métodos comuns a todos os animais: ``comer()`` e ``dormir()``.

2. ``class Cachorro(Animal)`` cria uma subclasse de Animal. Cachorro herda os métodos ``comer()`` e ``dormir()`` e adiciona o método específico ``latir()``.

3. ``class Gato(Animal)`` é outra subclasse que herda os métodos da classe Animal e adiciona ``miar()``.

4. ``Objetos animal, cachorro e gato`` demonstram ``herança e polimorfismo:`` cada subclasse pode usar métodos da classe base e seus próprios métodos específicos.

5. Chamar ``cachorro.comer()`` ou ``gato.dormir()`` mostra que métodos da classe base funcionam para todas as subclasses.

---

## ✅ Conceitos abordados

1. *Classes e objetos:* definição de estruturas que representam entidades do mundo real.
2. *Construtor (__init__):* inicializa os atributos do objeto.
3. *Métodos:* funções dentro da classe que definem comportamentos.
4. *Herança:* permite criar subclasses que herdam atributos e métodos da classe base.
5. *Polimorfismo:* objetos de subclasses podem usar métodos da classe base e métodos próprios.

**Próximo Capítulo : [Encapsulamento](../../aula_02/02_encapsulamento.md)**
