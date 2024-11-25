# class Użytkownik:
#      liczbaużytkowników=0
#      def __init__(self,nazwa,imie,nazwisko):
#          self.name=nazwa
#          self.first_name=imie
#          self.last_name=nazwisko
#          Użytkownik.liczbaużytkowników+=1
#
#
# class UżytkownikDrukarki(Użytkownik):
#     def __init__(self,nazwa,imie,nazwisko,liczbastron):
#         super(). __init__(nazwa,imie,nazwisko)
#         self.liczbaStron=liczbastron
#
#     def wydrukuj(self):
#         print(f'Użytkownik drukarki {self.name} ma na imie {self.first_name} i nazwisko {self.last_name}')
#
# użytkownik_id_2=UżytkownikDrukarki('pnow','Piotr','nowak',456)
# print(Użytkownik.liczbaużytkowników)
#
# użytkownik_id_drukarki=UżytkownikDrukarki('jkow','Jan','Kowalski',123)
# użytkownik_id_drukarki.wydrukuj()

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
# class Bus(Vehicle):
#     seating_capacity = 50
#     def __init__(self,name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)
#         # self.seating_capacity=seating_capacity
#         # self.
#     def drukowanie(self):
#         return (f"pojemnosc to {self.seating_capacity}")
# Volvo=Bus('Adam',50,34243)
# print(Volvo.drukowanie())

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
# class Bus(Vehicle):
#     def fare(self):
#         amount=super().fare()
#         total_amount=amount*1.1
#         return total_amount
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())
#
#

#zad2

# def mocne_haslo():
#     haslo=input("Podaj haslo: ")
#     znaki_spec=['%','#','@','!','*','&']
#     if len(haslo)<10:
#         print("Slabe haslo")
#         return False
#     if not any( x.isupper() for x in haslo):
#         print("good duze litery")
#         return False
#     if not any (x.islower() for x in haslo):
#         print("good male litery")
#         return False
#     if not any(x.isdigit() for x in haslo):
#         print("brakuje cyfry")
#         return False
#     if not any(x in znaki_spec for x in haslo):
#         print("Brakuje znaku specjalnego")
#         return False
#     else:
#         print("git haslo")
#         return True
#
# mocne_haslo()

#zad4

k=[[2,7,6],
    [9,5,1],
    [4,3,8]]

def suma_elementów(k):
    n=len(k) #liczba wierszy
    sum_row=sum(k[0])
    for i in range(1,n): #od 1 bo pierwszy wiersz już zsuowalismy
        if sum(k[i]) != sum_row:
            return False
    for x in range(n):
        print(x)
        #sum_col=0
        for j in range(n):
            print(j)
suma_elementów(k)

#zad3
class Bladpustyzbior():
    pass

def zbior_wspolny(a,b,c):
    if len(a)==0 or len(b)==0 or len(c)==0:
        raise Bladpustyzbior('A lub b lub c jest puste')
    wspólne_cyfry=[]
    for i in a:
        if i in b and i in c:
            wspólne_cyfry.append(i)
    return (wspólne_cyfry)
zbior_A=[]
zbior_B= (6,7,8.8,9.3)
zbior_C= {9.3,8.8}
print(zbior_wspolny(zbior_A,zbior_B,zbior_C))



