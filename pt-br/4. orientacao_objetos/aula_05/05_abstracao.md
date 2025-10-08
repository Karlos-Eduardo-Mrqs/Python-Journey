# 🟦 Abstração em Python

A abstração é um princípio da programação orientada a objetos (POO) que consiste em ocultar detalhes internos de implementação e expor apenas o necessário para o uso de um objeto ou sistema. Ela ajuda a simplificar a complexidade do código e define interfaces claras para interação com objetos.

## 📌 Conceitos-chave

- *Separação de responsabilidades:* O usuário da classe não precisa conhecer detalhes internos para utilizar seus métodos.

- *Interfaces claras:* Define quais métodos ou funcionalidades estão disponíveis externamente.

- *Ocultamento de complexidade:* Permite que classes internas ou métodos privados não sejam acessados diretamente.

- *Classes abstratas:* Classes que não podem ser instanciadas diretamente, servindo como base para outras classes.

---

## 🔹 Criando Classes Abstratas em Python

**Uma classe abstrata é uma classe que não pode ser instanciada diretamente.** Ela serve como modelo para outras classes (subclasses) que devem implementar determinados métodos obrigatoriamente.

Em outras palavras: ela define o “contrato” do que as subclasses precisam fazer, mas não diz exatamente como fazer.

```python
from abc import ABC, abstractmethod

# Classe abstrata
class Veiculo(ABC):

    @classmethod
    @abstractmethod
    def mover(self):
        pass  # método abstrato, sem implementação
```

> Python fornece o módulo abc (Abstract Base Classes) para criar classes e métodos abstratos.

**Explicação linha por linha:**

1. *from abc import ABC, abstractmethod →* importa os recursos necessários para criar classes e métodos abstratos.

2. *class Veiculo(ABC): →* define a classe abstrata Veiculo, que herda de ABC.

3. *@abstractmethod →* indica que o método mover() precisa ser implementado por qualquer subclasse.

4. *def mover(self): pass →* método sem implementação. Subclasses serão obrigadas a fornecer o código real.

---

## 🔹 Criando Classes Concretas em Python

Para usar a classe abstrata, criamos subclasses concretas que implementam todos os métodos abstratos:

```python

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo sobre rodas.")

class Barco(Veiculo):
    def mover(self):
        print("O barco está navegando na água.")
```

### 🔹 Testando Abstração

```python
# carro = Veiculo()  # Erro! Não pode instanciar classe abstrata

meu_carro = Carro()
meu_barco = Barco()

meu_carro.mover()  # O carro está se movendo sobre rodas.
meu_barco.mover()  # O barco está navegando na água.

```

> ✅ A abstração força as subclasses a implementar métodos essenciais, garantindo consistência e segurança no design do sistema.

---

## 🔹 Diferenças entre Abstração e Encapsulamento ?

**Embora ambos pareçam “esconder detalhes”, eles têm objetivos distintos:**

- **Abstração** é sobre o que um objeto faz. Ela define uma interface clara, mostrando apenas os métodos essenciais e ocultando como eles funcionam internamente.

- **Encapsulamento** é sobre como os dados são protegidos. Ele garante que os atributos e métodos internos de um objeto sejam acessados de forma segura, controlando quem pode ler ou alterar os valores.

---

## ✅ Vantagens da Abstração

- **Simplifica o código:** usuários interagem apenas com métodos essenciais.

- **Promove consistência:** subclasses implementam os mesmos métodos obrigatórios.

- **Facilita manutenção:** alterações internas não afetam o uso externo da classe.

- **Aumenta a segurança:** oculta detalhes críticos e protege a lógica interna.

---

## 📝 Conclusão

A abstração é essencial para criar sistemas claros, seguros e de fácil manutenção. Ela define o que um objeto faz, sem expor como ele faz, permitindo que você desenvolva sistemas complexos de forma organizada.

> 💡 Dica: Sempre que uma classe tiver responsabilidades que precisam ser definidas, mas não implementadas, considere usar abstração. Isso fortalece o design e prepara seu código para expansão futura.

**Próximo capítulo: [Métodos Mágicos](../aula_06/06_metodos_magicos.py)**

---

### 📝 Desafio

1. Crie uma classe abstrata Forma com método ``area()``.

2. Crie subclasses ``Quadrado`` e ``Circulo`` que implementem o método ``area()``.

3. Teste criando instâncias das subclasses e chamando ``area()``.

4. Adicione outro método abstrato ``perimetro()`` e implemente nas subclasses.

**[Comentando Desafio](desafios/)**
