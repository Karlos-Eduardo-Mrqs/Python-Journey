# Exercício de Classes Abstratas — Aula 05 (Módulo 4)

Este exercício trabalha com classes abstratas e métodos obrigatórios, mostrando como diferentes formas geométricas (como quadrado e círculo) podem compartilhar a mesma estrutura, mas com cálculos distintos.

---

## [🔹 Classe abstrata e subclasses geométricas](EX_01.py)

```py
from abc import ABC, abstractmethod
import math

class Forma(ABC):

    @classmethod
    @abstractmethod
    def area(cls):
        print("Denominando a área da forma !")
    
    @classmethod
    @abstractmethod
    def perimetro(cls):
        print("Denominando o perimetro da forma !")
    

class Quadrado(Forma):
    def __init__(self,lado:float):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4

class Circulo(Forma):
    
    def __init__(self,raio:float):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio

# Testes
qd = Quadrado(4)
cr = Circulo(3)

print("Quadrado:")
print("Área:", qd.area())
print("Perímetro:", qd.perimetro())

print("\nCírculo:")
print("Área:", cr.area())
print("Perímetro:", cr.perimetro())
```

> 🧠 Explicação

- Importação da biblioteca *abc* (*Abstract Base Class*)

1. Permite criar classes abstratas, que servem como ``“modelo”`` para outras classes.
2. A classe abstrata não pode ser instanciada diretamente.

- Classe abstrata Forma

1. Usa ``@abstractmethod`` para definir métodos obrigatórios que todas as subclasses devem implementar.
2. Define dois comportamentos esperados: ``area()`` e ``perimetro()``
3. Dessa forma, qualquer classe que herde de Forma precisa ter sua própria versão desses métodos.

- Classe Quadrado (``subclasse concreta``)

1. Herda de Forma.
2. Implementa os métodos exigidos:
3. ``area() retorna lado².``
4. ``perimetro() retorna 4 × lado.``

- Classe Circulo (``subclasse concreta``)

1. Também herda de Forma. Calcula:
2. ``area() = π × raio².``
3. ``perimetro() = 2 × π × raio.``
4. Usa a biblioteca math para acessar o valor de ``π (math.pi).``

- Testes e execução

1. São criadas instâncias de Quadrado e Circulo.
2. Para cada forma, são exibidos os resultados dos métodos ``area()`` e ``perimetro()``.

### ✅ Conceitos aplicados

1. Abstração: a classe Forma define uma interface comum sem implementar cálculos.
2. Herança: Quadrado e Circulo herdam de Forma.
3. Polimorfismo: cada forma tem sua própria implementação de ``area()`` e ``perimetro().``
4. Encapsulamento de comportamento: cada classe cuida de seus próprios detalhes matemáticos.
5. Uso de biblioteca externa (math): para cálculos precisos de π.

## 💡 Conclusão

Este exercício mostra como classes abstratas são usadas para padronizar comportamentos em subclasses diferentes, mantendo o código organizado, extensível e coerente. Se amanhã você quiser criar uma nova forma, como Triangulo, basta herdar de Forma e implementar ``area()`` e ``perimetro()`` — sem alterar o código existente.

**Próximo Capítulo : [Métodos Mágicos](../../aula_06/06_metodos_magicos.md)**
