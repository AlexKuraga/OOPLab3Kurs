from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def get_summary(self):
        pass

class Sportcar(Vehicle):
    def get_summary(self):
        print(f'Sportcar: {self.brand} {self.model}')

class SUV(Vehicle):
    def get_summary(self):
        print(f'SUV: {self.brand} {self.model}')

class Motorbike(Vehicle):
    def get_summary(self):
        print(f'Motorbike: {self.brand} {self.model}')
    pass

sportcar = Sportcar("Lamborghini ", "Veneno")
suv = SUV("Genesis", "GV80")
motorbike = Motorbike("Harley-Davidson", "Fat Bob")
sportcar.get_summary()
suv.get_summary()
motorbike.get_summary()