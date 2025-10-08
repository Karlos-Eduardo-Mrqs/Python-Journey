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

print("nCírculo:")
print("Área:", cr.area())
print("Perímetro:", cr.perimetro())
