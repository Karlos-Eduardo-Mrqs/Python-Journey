# Exercício de Polimorfismo — Aula 08 (Módulo 3)

Este desafio explora o polimorfismo, mostrando como diferentes classes podem compartilhar o mesmo método com comportamentos distintos.

---

## [🔹 Classe base e subclasses com comportamento próprio](EX_01.py)

```py
class Veiculo:
    def mover(self):
        print("O veículo está se movendo.")

class Carro(Veiculo):
    def mover(self):
        print("O carro está dirigindo pela estrada.")

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está sendo pedalada pela ciclovia.")

def fazer_mover(objeto):
    objeto.mover()

carro = Carro()
bicicleta = Bicicleta()

fazer_mover(carro)
fazer_mover(bicicleta)

class Barco(Veiculo):
    def mover(self):
        print("O barco está navegando pelo mar.")

barco = Barco()
fazer_mover(barco)
```

> 🧠 Explicação

- Classe base Veiculo

1. Define o método genérico ``mover()``, representando o comportamento comum de um veículo se mover.
2. Serve como ``“molde”`` para outras classes que herdarão esse comportamento.

- Subclasses Carro, Bicicleta e Barco

1. Cada uma reescreve o método ``mover()`` para definir seu próprio comportamento.
2. Isso é chamado de sobrescrita de método (``method overriding``).
3. Carro: ``“O carro está dirigindo pela estrada.”``
4. Bicicleta: ``“A bicicleta está sendo pedalada pela ciclovia.”``
5. Barco: ``“O barco está navegando pelo mar.”``

- Função ``fazer_mover(objeto)``

1. Recebe qualquer objeto e chama ``objeto.mover().``
2. Como cada classe tem sua própria implementação de ``mover()``, o Python executa o método correspondente ao tipo do objeto recebido.
3. Isso é polimorfismo em ação: a mesma chamada (``objeto.mover()``) gera comportamentos diferentes conforme o tipo do objeto.

- Criação dos objetos e execução

1. Quando ``fazer_mover(carro)`` é chamado, o método de Carro é usado.
2. O mesmo acontece para ``Bicicleta`` e ``Barco``, cada um com seu comportamento distinto.

### ✅ Conceitos aplicados

1. *Herança:* todas as subclasses herdam de Veiculo.
2. *Polimorfismo:* o mesmo método (``mover()``) tem comportamentos diferentes em cada classe.
3. *Sobrescrita de métodos:* redefinição de um método herdado.
4. *Abstração de comportamento:* a função ``fazer_mover()`` trabalha com qualquer tipo de veículo, sem precisar saber qual é.

---

## 💡 Conclusão

Esse exercício mostra como o polimorfismo torna o código flexível e reutilizável, permitindo tratar diferentes objetos de forma uniforme, mas com resultados específicos de cada tipo.

**Próximo Capítulo : [Abstração](../../aula_05/05_abstracao.md)**
