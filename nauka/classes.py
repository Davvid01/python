#zad1/2/3 https://pynative.com/python-object-oriented-programming-oop-exercise/
class Cars:
    def __init__(self, name, max_speed, mileage):
        self.imie = name
        self.predkosc = max_speed
        self.przebieg= mileage
    def wyswietlanie(self):
        print(f"{self.imie} osiąga {self.predkosc}km/h oraz przebieg to {self.przebieg}")

    def miejsca (self, capacity=4):
        return f"The seating capacity of a {self.imie} is {capacity} passengers" #return należy wydrukować
"""zad3
class Bus(Cars):
    pass

class Bus(Cars):
    def cocik (self):
        return super().miejsca(50) #The super function returns a temporary object of the parent class that allows us to call a parent class method inside a child class method.
#modelX.wyswietlanie()
#print(modelX.miejsca())

#school_bus.wyswietlanie()
#print(school_bus.cocik())
"""
#zad5/6
class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed, mileage, capacity):
        self.imie = name
        self.predkosc = max_speed
        self.przebieg = mileage
        self.pojemnosc = capacity
    def podsumowanie(self):
        return f"Color: {self.color}, Vehicle name: {self.imie}"
    def fare(self):
        return self.pojemnosc * 100
        #return f"Total fare is {final_amount}PLN"

class Bus(Vehicle):
    def adjustment(self):
        kwota =  super().fare()
        return kwota*1.1

class Car(Vehicle):
    pass
individual_car = Car('modelX',220, 30000,2)
school_bus=Bus('solaris3',90,150000,50)
print(individual_car.podsumowanie())
print(school_bus.podsumowanie())
print(individual_car.imie, individual_car.color, individual_car.przebieg)
print(individual_car.fare())
print(school_bus.adjustment())



#zad7
print(school_bus.__class__)
print(school_bus.__class__.__name__)
print(school_bus.__class__.__qualname__)
print(type(school_bus)) #school bus belongs to Bus class
#zad8
print(isinstance(school_bus, Vehicle)) #checks whether schoolbus instance belongs to Vehicle class also

