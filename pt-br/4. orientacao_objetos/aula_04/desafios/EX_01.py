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
