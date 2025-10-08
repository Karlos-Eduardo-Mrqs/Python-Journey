class Animal:
    def comer(self):
        print("O animal está comendo.")
    
    def dormir(self):
        print("O animal está dormindo.")

class Cachorro(Animal):
    def latir(self):
        print("O cachorro está latindo: Au Au!")

class Gato(Animal):
    def miar(self):
        print("O gato está miando: Miau!")

animal = Animal()
animal.comer()
animal.dormir()

cachorro = Cachorro()
cachorro.latir()
cachorro.comer()
cachorro.dormir()

gato = Gato()
gato.miar()
gato.comer()
gato.dormir()
