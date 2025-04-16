import random
import random
from random import randint
from math import pi
from math import sqrt as pierwiastek
import math

# #print(random.randint(1,10))
# print(randint(1,10))
# print(pi)
# random.randint
# print(int(pierwiastek(5)))
# class Person:
#     def __init__(ktos, imie):
#         ktos.gig = imie
#
#     def print_name(bob):
#         print (f"My name is {bob.gig}.")
#
# osoba = Person(2)
# osoba.print_name()
# print(osoba)
#
# class Organizm:
#     def __init__(self, gatunek, domena):    #specjalna metoda KONSTRUKTOR,która pozwala zmienić dane wejściowe
#         self.wybieram=domena    #domena to druga zmienna która szuka argumentu z metody innit tylko, wąsko
#             #^zmienna to zmienna globalna dla całej klasy, szerszy kotekst
#         self.tubedziegat=gatunek
#     def scharakteryzuj(self, powitanie="hej" ):  #self powoduje, że możemy szukac innych zmiennych spoza metody, jest odwołanie i pozwlala programowi szukać szerzej
#         #self.gatunek=
#         return powitanie + " , jestem " + self.wybieram + " a dokładniej"+ str(self.tubedziegat)
# leia=Organizm('kot', 'zwierze')
# #print(leia.wybieram)
# print(leia.scharakteryzuj())
# bazyl=Organizm('grzyb','muchomor')
# #bazyl.gatunek="jaszczurka"
# print(bazyl.scharakteryzuj('sjema'))
#
# class Pracownik:
#     def __init__(self, ID, dział):
#         self.podaID=ID
#         self.podaDep=dział
# class Pracownik_biurowy(Pracownik):
#     def specjalizacja(self):
#         print("IT")
#
# class Menadżer(Pracownik_biurowy):
#     def specjalizacja(self):
#         print("bazy danych")
# class pracownikSprzedaży(Pracownik_biurowy):
#     def __init__(self,IDklienta):
#         self.klient=IDklienta
#     def dodrukowania(self):
#         print(f'Sergio wspołpracuje z klientem o ID {self.klient}')
# class Pracownik_magazyn(Pracownik):
#     def responsibility(self):
#         return("taśma")
#
# Sergio=pracownikSprzedaży('10000')
# Sergio.dodrukowania()
#
#
#
# Dawid=Pracownik_biurowy(90,"controlling")
# print(Dawid.podaID)
# print(Dawid.podaDep)
# Dawid.specjalizacja()
#
# Tomasz = Pracownik_magazyn(456, "hala1")
# print(Tomasz.responsibility())
#
# Blazej = Menadżer(123,"controlling")
# Blazej.specjalizacja()
#
#
# HERMETYZACJA
# class Test:
#     __lista=[] #teraz widzą to tylko metody wewnatrz klasy
#     def dodaj(self,arg):
#         self.__lista.append(arg)
#     def zdejmiij(self):
#         if len(self.__lista)>0:
#             return self.__lista.pop(len(self.__lista)-1) #pop zdejmuje po indeksie
#         else:
#             return
# obiekt=Test()
# obiekt.dodaj('Es')
# obiekt.dodaj('fds')
# #obiekt._Test__lista.append('X')
# print(obiekt.zdejmiij())
# #print(obiekt._Test__lista)

#__metody__
# class Punkt2d:
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
#         self.odleglosc=math.sqrt(x**2+y**2)
#     def __add__(self, drugi):
#         return Punkt2d(self.x+drugi.x, self.y + drugi.y)
#     def __lt__(self, other):
#         return self.odleglosc< other.odleglosc
#     def __eq__(self, other):
#         return self.x==other.x and self.y==other.y
#     def __len__(self):
#         return int(round(self.odleglosc,0))
#
# p1=Punkt2d(3,5)
# p2=Punkt2d(2,8)
# kolo=Punkt2d(9,4)
# print(kolo.odleglosc)
# p3=p1+p2+kolo
# print(p3.y)
# print(p1.x,p2.x,p3.x,p3.y)
# print(p1<kolo)
# print(p2==p2) #każdy print odwoluje sie do konkretnej metody ktora rozwiazuje zapytanie
#
# print(p3.x,p3.y,p3.odleglosc)
# print(len(p3))

#DESTRUKTOR

# class Test:
#     # def __new__(cls):
#     #     print("Hello Class")
#     def __del__(self):
#         print("Bye Class")
# #instacjonowanie klasy to moment kiedy klasa przeradza się w obiekt
# obj = Test() #obiekt nie jest niszcozny bo posiada referencje do obj2
# obj2=obj #obiekt nie jest niszcozny
# lista =[obj2,obj] #znowu metoda del wywolywana jest na koncu bo stworzylsimy refrencje lista ktora to wstrzymuje do zakonczenia programu
# del obj #usuwa daną zmienną
# del obj2
# del lista[1]
# print("koniec")

#METODY KLAS ORAZ METODY STATYCZNE

class Czlowiek:
    def __init__(self, imie):
        self.imie=imie
    def przedstaw(self):
        print(f"Ten człowiek zwie się {self.imie}")

    @classmethod
    def nowy_czlowiek(cls, imie): #sprawia że mozna odwołac sie do metody, od teraz to nie obekt wywoluje metode a klasa, jest do tej klasy statycznie przypisana
        return cls(imie) #cls (class) bo te atrybuty nie wystepują wyżej, cls wysyla imie do metody __init

    @staticmethod
    def przywitaj(arg): #nie przyjmuje argumentu cls
        print('Cześć '+ arg)

człowiek1= Czlowiek.nowy_czlowiek('Ewa') #dlatego tutaj używam metodą do klasy,a nie jak zawsze do obiektu i zadziała
człowiek1.przedstaw()
człowiek2= człowiek1.nowy_czlowiek('Adi')
człowiek2.przedstaw()
Czlowiek.przywitaj('Adi')
Czlowiek.przywitaj('Tom')
# luj=Czlowiek('Tomek')
# luj.przedstaw()