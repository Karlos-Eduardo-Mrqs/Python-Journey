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
