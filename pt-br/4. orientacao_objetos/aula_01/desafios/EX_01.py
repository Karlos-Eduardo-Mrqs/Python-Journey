class Carro:
    def __init__(self,marca:str,modelo:str,ano:int,cor:str,quilometragem:float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def apresentar(self):
        print("--------------------------------------------")
        print(f"Marca : {self.marca} | Modelo : {self.modelo} | Ano : {self.ano} | Cor : {self.cor} | Quilometragem : {self.quilometragem} |")
        print("--------------------------------------------")
        
carro = Carro("Pegeout","Pegeout 2008",2023,"vermelho",12_000.0)
carro2 = Carro("Honda", "Civic", 2022,"azul",15_000.0)
carro.apresentar()
carro2.apresentar()