# 🟦 Herança em Python

A herança é um dos pilares da programação orientada a objetos (POO) que permite criar novas classes a partir de classes existentes, reutilizando código e promovendo hierarquias lógicas entre objetos.

## 📌 Conceitos-chave

- *Classe base (ou superclasse):* Classe original que fornece atributos e métodos.

- *Classe derivada (ou subclasse):* Classe que herda os atributos e métodos da classe base e pode adicionar ou sobrescrever funcionalidades.

- *Reutilização de código:* Evita duplicação, permitindo que subclasses usem o que já foi definido na classe base.

- *Sobrescrita (override):* Subclasses podem alterar o comportamento de métodos da superclasse.

---

## 🔹 Sintaxe Básica

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("O animal faz um som")

# Subclasse herda de Animal
class Cachorro(Animal):
    def falar(self):
        print("Au Au!")
```

## 🔹 Testando a Herança

```python
animal = Animal("Gato")
animal.falar()  # O animal faz um som

dog = Cachorro("Rex")
dog.falar()     # Au Au!
print(dog.nome) # Rex
```

> 💡 A subclasse Cachorro reutilizou o atributo nome da superclasse Animal e sobrescreveu o método falar.

---

## 🔹 Chamando o método da superclasse

Você pode chamar métodos da superclasse dentro da subclasse usando ``super():``

```python
class Gato(Animal):
    def falar(self):
        super().falar()  # chama o método da classe base
        print("Miau!")
        
gato = Gato("Mimi")
gato.falar()
# Saída:
# O animal faz um som
# Miau!
```

---

## 🔹 SuperClasse X Subclasse

| Aspecto      | Superclasse                 | Subclasse                                    |
| ------------ | --------------------------- | -------------------------------------------- |
| Definição    | Classe original             | Classe que herda a superclasse               |
| Atributos    | Definidos e compartilhados  | Pode adicionar novos ou usar os existentes   |
| Métodos      | Definidos para reutilização | Pode sobrescrever ou adicionar novos métodos |
| Reutilização | Fornece funcionalidades     | Reaproveita funcionalidades da superclasse   |
| Exemplos     | `Animal`                    | `Cachorro`, `Gato`                           |

---

## ✅ Vantagens da Herança

- **Reutilização de código:** evita duplicação.

- **Hierarquias claras:** organiza classes de forma lógica.

- **Facilidade de manutenção:** mudanças na superclasse podem refletir em todas as subclasses.

- **Flexibilidade:** subclasses podem modificar ou estender comportamentos.

---

## 📝 Conclusão

A herança é essencial para escrever código limpo e organizado em POO. Ela permite reaproveitar funcionalidades de classes existentes, criar hierarquias coerentes e sobrescrever métodos quando necessário.

> 💡 Dica: Use a herança para representar relações “é um” (por exemplo, “Cachorro é um Animal”). Para relações “tem um”, considere composição ao invés de herança.

**Próximo capítulo: [Polimorfismo](../aula_04/04_polimorfismo.md)**

---

### 📝 Desafio

1. Crie uma classe ``Veiculo`` com atributos ``marca`` e ``modelo`` e um método ``informacoes()``.

2. Crie subclasses ``Carro`` e ``Moto`` que herdam de ``Veiculo``.

3. Adicione métodos específicos nas subclasses, como ``acelerar()`` e ``empinar()``.

4. Teste criando instâncias e chamando os métodos, incluindo a sobrescrita de algum método da superclasse.

**[Comentando Desafio](desafios/README.md)**
