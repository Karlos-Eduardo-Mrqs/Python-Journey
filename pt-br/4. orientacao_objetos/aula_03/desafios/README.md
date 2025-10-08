# Exercício de Herança com Veículos — Aula 03 (Módulo 4)

Este exercício demonstra como subclasses podem herdar atributos e métodos de uma classe base, e adicionar comportamentos específicos.

---

## [🔹 1. Classe Veículo e subclasses](EX_01.py)

```py
class Veiculo:
    def __init__(self,nome:str,modelo:str):
        self.nome = nome
        self.modelo = modelo
    
    def informacoes(self):
        print("Informações do veículo")
        print(f" Nome : {self.nome} | Moddelo : {self.modelo} |")
    
class Carro(Veiculo):
    def acelerar(self):
        print("Acelerando ...")

class Moto(Veiculo):
    def empinar(self):
        print("Empinando ...")

carro = Carro("Toyota", "Corolla")
moto = Moto("Honda", "CG 160")

carro.informacoes()
carro.acelerar()

moto.informacoes()
moto.empinar()
```

> Explicação

- Classe base Veiculo

1. Define atributos comuns a todos os veículos: nome e modelo.
2. O método ``informacoes()`` imprime detalhes do veículo.
3. Essa classe funciona como template para outros tipos de veículos.

- Subclasse Carro

1. Herda os atributos e métodos de Veiculo.
2. Adiciona um método específico: ``acelerar().``
3. Permite que objetos do tipo Carro usem ``informacoes()`` da classe base e também ``acelerar()`` da própria subclasse.

- Subclasse Moto

1. Também herda de Veiculo.
2. Adiciona um método específico: ``empinar()``.
3. Objetos do tipo Moto podem acessar métodos da classe base (``informacoes()``) e seu próprio método (``empinar()``).

- Objetos carro e moto

1. Cada objeto instancia a sua respectiva classe.
2. Chamadas como ``carro.informacoes()`` mostram que a herança funciona, enquanto ``carro.acelerar()`` e ``moto.empinar()`` mostram os comportamentos específicos de cada subclasse.

### ✅ Conceitos abordados

1. *Herança simples:* subclasse reutiliza atributos e métodos da classe base.
2. *Métodos específicos da subclasse:* cada tipo de veículo pode ter funcionalidades próprias.
3. *Reuso de código:* evita duplicação, mantendo atributos comuns na classe base.
4. *Polimorfismo básico:* objetos diferentes (Carro e Moto) podem usar o mesmo método informacoes() de formas consistentes.

**Próximo Capítulo : [Polimorfismo](../../aula_04/04_polimorfismo.md)**
