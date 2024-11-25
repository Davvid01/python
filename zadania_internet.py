#zad1 github
# x=2114
# print(x%1000)
# def szukanie_parzystej():
#     lista=[]
#     for x in range (2000,3201):
#         if x%7==0 and not x%5==0:
#             lista.append(x)
#     return str(lista)
#
# print(szukanie_parzystej())
#zad1 w3resource
# def method():
#     while True:
#         try:
#             x=input("podaj 3 liczby oddzielone spacja: ")
#             x=x.split()
#             x=[float(znak) for znak in x] #konwertowanie stringa na float!!!
#             print(x)
#             return (max(x))
#         except ValueError:
#             pass #print("Nie podałes liczby")
#method()

#zad2,3
# def sumowanie(liczby):
#     wynik=1
#     for x in liczby:
#         wynik*=x
#     return wynik
# print(sumowanie((8,2,3,-1,7)))

#zad4
# def reverse():
#     slowo="123abcd"
#     reversed=''
#     for i in range (len(slowo)-1,-1,-1):
#         reversed+=slowo[i]
#     return reversed
# print(reverse())
# def ds():
#     lista = []
#     for x in reversed("1234abcd"):
#         lista.append(x)
#     '#'.join(lista)
#     return lista
# print(ds())

#zad5
# def czynnik(x):
#     while True:
#         try:
#             if x==1:
#                 return 1
#             lista=[]
#             i=x
#             while i>0:
#                 if x%i==0:
#                     lista.append(i)
#                 i-=1
#             wynik=len(lista)
#             return wynik
#         except (ValueError,TypeError):
#             return ("podaj liczbe")
# print(czynnik('slon'))

# def mnozenie(x):
#     if x==1:
#         return 1
#     lt=1
#     for n in range (1, x+1):
#         lt*=n
#     return lt
# print(mnozenie(4))

#zad6
# def falls():
#     x=int(input("POdaj liczbę: "))
#     y=input('Podaj zakres: ')
#     y = y.split()
#     y=[int(i) for i in y]
#     y=sorted(y)
#     if x in range (y[0], y[len(y)-1]+1):
#         return "miescie sie"
#     else:
#         return "nie miescie"
# print(falls())

#zad7
# def low_high():
#     slowo='The quick Brow Fox'
#     cal=0
#     callow=0
#     for x in slowo:
#         if x.isupper():
#             cal+=1
#         if x.islower():
#             callow+=1
#     return f'{cal} and {callow}'
# print(low_high())

#zad8
# def unique(x):
#     lista=[]
#     for y in x:
#         if y not in lista:
#             lista.append(y)
#     return lista
# print(unique(([1,2,3,3,3,3,4,5])))

#zad9
# def prime():
#     x=int(input('Podaj liczbe : '))
#     i=x
#
#     while i>0:
#         if x%i==0 and x!=i and i!=1:
#             return f'Liczba {x} nie jest pierwszą '
#         i -= 1
#     return 'jest pierwszą'

#print(prime())

#zad10
# def parzyste(x):
#     lista_parzsyte=[]
#     for y in x:
#         if y%2==0 and y>0:
#             lista_parzsyte.append(y)
#     return lista_parzsyte
# A=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(parzyste(A))

#zad11
# def perfect():
#     liczba = int(input('Podaj liczbe : '))
#     i=liczba
#     lista=[]
#     y=0
#     while i>0:
#         if liczba%i==0 and liczba!=i:
#             y+=i
#         i-=1
#     if y==liczba:
#         return 'To liczba perfekt'
#     return 'NIe jest perfekt'
# print(perfect())

#zad12
# def palindrom(zdanie):
#     zdanie=zdanie.replace(' ','')
#     zdanie=[znak for znak in zdanie]
#     print(zdanie)
#     y=len(zdanie)
#     lista=[]
#     for x in reversed(zdanie):
#         lista.append(x)
#     print(lista)
#     if zdanie==lista:
#         return 'To palindrom!'
# print(palindrom('nurses run'))

#zad13
#zad 14
# import string
# import sys
# def pangram(x):
#     x=x.lower().replace(" ","")
#     lista=[]
#     for index in x:
#         if index not in lista:
#             lista.append(index)
#     lista.sort()
#     print(lista)
#     if lista==list(string.ascii_lowercase):
#         return 'palindrom'
# X="The quick brown fox jumps over the lazy dog"
# print(pangram(X))
# print(list(string.ascii_lowercase))

#15
# def hyphen(x):
#     #x=x.replace("-"," ")
#     x=x.split('-')
#     x.sort()
#     x="-".join(x)
#     return x
# zdanie=input("Podaj zdanie oddzielone -:")
# print(hyphen(zdanie))
#16
# def kwadraty():
#     lista=[]
#     for x in range(1,31):
#         lista.append(x**2)
#     return lista
# print(kwadraty())
#2 baza
# def silne_haslo():
#     haslo=input("Podaj haslo: ")
#     lista=['!',"@",'#','$','%','^','&','*']
#     if len(haslo)<10:
#         return 'slabe'
#     if not any(x.isupper() for x in haslo):
#         return 'slabe'
#     if not any(x.islower() for x in haslo):
#         return 'slabe'
#     if not any(x.isdigit() for x in haslo):
#         return 'slabe'
#     if any(x in lista for x in haslo):
#         return 'silne'
#     # for x in haslo:
#     #     if x in lista:
#     #         pass
#     #         if haslo.islower() #and haslo.isupper(): # and haslo.isdigit():
#     #             print('silne!')
# print(silne_haslo())
# #4 baza
# def magiczny():
#     k=[[2,7,6],[9,5,1],[4,3,8]]
#     lt=len(k)
#     for x in range(0,lt):
#         for j in range(0,lt):
#             if sum(k[x])==sum(k[j]):
#                 print(f'wiersze {x} i {j} sa sobie równe')
#             else:
#                 return 'To nie jest magiczny kwadrat'
#     g=0
#     z=0
#     y=0
#     for x in k:
#         g+=x[0]
#         z+=x[1]
#         y+=x[2]
#     if g==z==y:
#         return 'to kwadrat magiczny'
#
#             # if k[x,j]==k[x+1,j]==k[x+1,j]:
#                 #(print("kolumny zgadzaja sie")
#
# print(magiczny())

#1
# class Użytkownik:
#     liczbaUżytkownikow=0
#     def __init__(self,nazwa,imie,nazwisko):
#         self.nazwa=nazwa
#         self.imie=imie
#         self.nazwisko=nazwisko
#     liczbaUżytkownikow+=1
# class UżytkownikDrukarki(Użytkownik):
#     def __init__(self,nazwa,imie,nazwisko,liczbastron):
#         super().__init__(nazwa,imie,nazwisko)
#         self.liczbastron=liczbastron
#     def pompa(self):
#         return f'{self.nazwa},{self.imie},{self.liczbastron}'
# pioter=Użytkownik('pnow','Piotr', 'Nowak')
# print(pioter.nazwa,pioter.imie,pioter.nazwisko)
# tomi=UżytkownikDrukarki('jakow','jan','kowalski',45,)
# print(tomi.liczbastron,tomi.pompa())

#3
class Bładzbioru(Exception):
    pass
def trzyzbiory(x,y,z):
    if x==[] or y==[] or z==[]:
        raise Bładzbioru
    krotka=[]
    for index in x:
        if not index in krotka and index in z and index in y:
            krotka.append(index)
    return tuple(krotka)
X=[1,2,2]
Y=['str',1,2]
Z=[1,2,3]
print(trzyzbiory(X,Y,Z))

