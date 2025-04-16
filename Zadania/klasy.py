# class Student:
#     # constructor
#     def __init__(self, name, age):
#         # Instance variable
#         self.name = name
#         self.age = age
#
# # create first object
# s1 = Student("Jessa", 20)
#
# # access instance variable
# print('Object 1')
# print('Name:', s1.name)
# print('Age:', s1.age)
#
# # create second object
# s2= Student("Kelly", 10)
#
# # access instance variable
# print('Object 2')
# print('Name:', s2.name)
# print('Age:', s2.age)
#
#
# class Vehicle:
#     def __init__(self):
#         self.engine = '1500cc'
#
# class Car(Vehicle):
#     def __init__(self, max_speed):
#         # call parent class constructor
#         super().__init__()
#         self.max_speed = max_speed
#
#     def display(self):
#         # access parent class instance variables 'engine'
#         print("Engine:", self.engine)
#         print("Max Speed:", self.max_speed)
#
# # Object of car
# car = Car(240)
# car.display()

class Vehicle:
    color = 'white'

    def __init__(self,imie,fotel,dupa,pojemnosc):
        self.name=imie
        self.max_speed=dupa
        self.mileage=fotel
        self.capacity=pojemnosc
    def seating_capacity(self, capacity):
        #capacity=capacity
        return f"The seating capacity of a {self.name} is {capacity} passengers and is {self.color}"
    def exc(self):
        print(self.max_speed)
    def fare(self):
        return self.capacity*100


class Bus(Vehicle):
    pass
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50) #zaciąga metode i jej atrybutty bezpośrednio z głównej
    def fare(self):
        return super().fare()*1.1
    # def __init__(self,predkosc,przebieg):
    #     #super().__init__(predkosc,przebieg)
    #     self.max_speed=predkosc
    #     self.mileage=przebieg
class Car(Vehicle):
    pass
auto=Vehicle('jakies', 70000,50,40)
print(auto.seating_capacity(40), auto.fare())
chinski=Bus('Jong',80000,70,50)
# ford=Car('focus',75000,140)
# print(ford.max_speed, ford.color, ford.seating_capacity(5))
print(chinski.fare())

print(type(auto))
#print(isinstance(auto))

print(type(chinski))
print(isinstance(chinski,Vehicle))
