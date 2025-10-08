class Retangulo:
    def __init__(self,largura:float,altura:float):
        self.largura = largura
        self.altura = altura
    
    def __str__(self) -> str:
        return f"A área do retângulo = {self.largura * self.altura}"
    
    def __eq__(self, outro) -> bool:
        if isinstance(self,Retangulo):
            return (self.largura * self.altura) == (outro.largura * outro.altura)
        return False

    def __add__(self, outro):
        # Mantemos a largura do primeiro retângulo e calculamos a altura necessária
        if isinstance(outro, Retangulo):
            nova_area = (self.largura * self.altura) + (outro.largura * outro.altura)
            nova_altura = nova_area / self.largura
            return Retangulo(self.largura, nova_altura)
        return NotImplemented

# Testando a classe
r1 = Retangulo(4, 5)
r2 = Retangulo(2, 10)
r3 = Retangulo(4, 5)

print(r1)          # Retângulo(4 x 5)
print(r2)          # Retângulo(2 x 10)

# Verificando igualdade
print(r1 == r2)    # True → mesma área (20)
print(r1 == r3)    # True → mesma área (20)

# Somando retângulos
r4 = r1 + r2
print(r4)          # Retângulo(4 x 10.0) → área = 40
print(r4.largura * r4.altura)  # 40