# 🟦 Polimorfismo em Python

O polimorfismo é um princípio da programação orientada a objetos (POO) que permite que objetos de diferentes classes sejam tratados de forma uniforme, desde que compartilhem métodos com o mesmo nome.

Ele promove flexibilidade e reutilização de código, permitindo que diferentes objetos respondam de maneiras distintas à mesma operação.

## 📌 Conceitos-chave

- *Polimorfismo de métodos:* Diferentes classes implementam métodos com o mesmo nome, mas comportamentos distintos.

- *Reutilização de código:* Funções ou estruturas podem operar em objetos diferentes sem precisar conhecer sua classe exata.

- *Flexibilidade:* Permite escrever código mais genérico e adaptável a novos tipos de objetos.

---

## 🔹 Sintaxe Básica

```python
class Animal:
    def falar(self):
        print("O animal faz um som")

class Cachorro(Animal):
    def falar(self):
        print("Au Au!")

class Gato(Animal):
    def falar(self):
        print("Miau!")
```

### 🔹 Testando Polimorfismo

```python
def fazer_animal_falar(animal):
    animal.falar()

# Criando instâncias
dog = Cachorro()
cat = Gato()

# Chamando a mesma função para diferentes objetos
fazer_animal_falar(dog)  # Au Au!
fazer_animal_falar(cat)  # Miau!
```

> 💡 Mesmo usando a mesma função fazer_animal_falar, cada objeto responde de forma diferente. Isso é polimorfismo em ação.

---

## 🔹 Polimorfismo com Classes Diferentes

O polimorfismo não exige que as classes estejam relacionadas por herança. O importante é que os objetos implementem o método esperado.

```python
class Pato:
    def falar(self):
        print("Quack!")

pato = Pato()
fazer_animal_falar(pato)  # Quack!
```

> ✅ A função funciona para qualquer objeto que tenha o método falar(), independentemente da classe.

---

## 🔹 Vantagens do Polimorfismo

- **Flexibilidade:** funções e métodos podem operar com diferentes tipos de objetos.

- **Reutilização de código:** evita duplicação de funções específicas para cada classe.

- **Manutenção simplificada:** novas classes podem ser integradas sem alterar o código existente.

- **Extensibilidade:** facilita a adição de novos comportamentos sem modificar código antigo.

---

## 📝 Conclusão

O polimorfismo é essencial para escrever código genérico, flexível e reutilizável. Ele permite que diferentes objetos respondam de formas específicas à mesma operação, tornando o código mais limpo e preparado para mudanças ou expansões futuras.

> **💡 Dica:** Sempre que precisar que funções ou métodos lidem com diferentes tipos de objetos de forma uniforme, considere aplicar polimorfismo. Ele é um dos pilares que torna a POO poderosa e escalável.

**Próximo capítulo: [Abstração](../aula_05/05_abstracao.md)**

---

### 📝 Desafio

1. Crie uma classe Veiculo com método ``mover()``.

2. Crie subclasses ``Carro`` e ``Bicicleta``, sobrescrevendo o método ``mover()`` com comportamentos diferentes.

3. Crie uma função ``fazer_mover(objeto)`` que chama ``objeto.mover()``.

4. Teste a função com instâncias de ``Carro`` e ``Bicicleta``.

5. Adicione outra classe ``Barco`` e teste sem alterar a função ``fazer_mover()``.

**[Comentando Desafio](desafios/README.md)**

---
