# #
# # lista = [4, 6, 2]
# # n="0"
# # try :
# #     print(lista[n])
# # except IndexError :
# #     print("Nie da sie pobrac. Sprawdz czy lista ma tyle elementow.")
# # finally :
# #     print("Sprzątanie...")
# #     print("Koniec programu.")
# #
# # lista = [4, 6, 2]
# # n="0"
# # try :
# #     print(lista[n])
# #     print("Nie było błędu.")
# # except TypeError as blad:
# #     lan=""
# #     for arg in blad.args :
# #     lan += (arg + " ")
# #     raise Exception("Zły typ", lan)
# # print("Koniec programu.")
#
# # class BladTrojkata (Exception):
# #     opis = "Dla dowolnego trójkąta miara każdego boku \
# # musi być mniejsza lub równa sumie miar dwóch pozostałych"
# # a=1
# # b=5
# # c=10
# # try :
# #     if (a+b<c or a+c<b or b+c<a) :
# #         raise BladTrojkata
# # except BladTrojkata as e :
# #     print(e.opis)
#
# class Animal :
#     def move(self) :
#         print("Zwierz się porusza")
# class Dog(Animal) :
#     def move(self) :
#         print("Pies chodzi i biega")
#     def activate(self) :
#         #self.move()
#         super().move()
# d=Dog()
# d.activate()
#
# class Animal :
#     pass
# class Mammal (Animal):
#     pass
# class Dog (Mammal):
#     pass
# a = Animal()
# m = Mammal()
# d = Dog()
# print(isinstance(a, Animal))
# print(isinstance(m, Mammal))
# print(isinstance(m, Animal))
# print(isinstance(d, Dog))
# print(isinstance(d, Mammal))
# print(isinstance(d, Animal))

# class Language:
#     def say_hello(self):
#         raise NotImplementedError('Please use any')
# class French(Language):
#     pass
# class Chinese(Language):
#     def say_hello(self):
#         print('ni hao')
# def intro(lang):
#     lang.say_hello()
# sarthak=French()
# john=Chinese()
#
# intro(sarthak)
# intro(john)

# #LAMBDA
# def funkcja(f, liczba):
#     return f(liczba)
#
# print(funkcja(lambda x:x*x,3)) #możemy posługiwać sie tylko arguementem który stoi  przy lambda -zastosowanie dla krtokich dzialan
#
# def kwadrat(x):
#     return x*x
# print(kwadrat(5))
# wyn= (lambda y:y*y)(5)
# print(wyn)
#
# lam=lambda x:x*x
# print(lam(5))
# print(lam(4))
#
# lam2=lambda x,y: x*y
#
# print(lam2(4,5))
# print((lambda x, y: x+y)(6,7))

# lista = list(range(10))
#
#
# nowa =[i * 2 for i in lista]
# print(lista)
# print("Nowa:", nowa)
# nowa2=[i for i in lista if i %2 ==0]
# print(nowa2)
#
# argumenty= ["Sebastian",24]
# tekst= "czesc mam na imie {imie} i mam {wiek} lat.".format(imie=argumenty[0],wiek=argumenty[1])
# print(tekst)

# def semi_magic_square():
#     # Definiowanie pustej listy oraz liczby kolumn
#     square = []
#     length = int(input("Podaj liczbę kolumn: "))
#
#     # Tworzenie możliwości wpisywania wartości przez użytkownika
#     for i in range(length):
#         row = []
#         for j in range(length):
#             k = int(input(f"Podaj wartość ({i+1}, {j+1}): "))  # Poprawiono indeksację i komunikat
#             if k > 9:
#                 print("Podana wartość jest większa niż 9")  # Poprawiono komunikat
#                 return False
#
#             row.append(k)
#         square.append(row)
#     print(square)
#     # Warunek sprawdzający sumę wierszy
#     sum_row1 = sum(square[0])
#     for n in range(1, length):
#         sum_row = sum(square[n])
#         if sum_row != sum_row1:
#             print("To nie jest magiczny kwadrat")
#             return False
#
#     # Warunek sprawdzający sumę kolumn
#     for m in range(length):
#         col_sum = 0
#         for n in range(length):
#             s = square[n][m]
#             col_sum += s
#         if col_sum != sum_row1:
#             print("To nie jest magiczny kwadrat")
#             return False
#
#         # Warunek sprawdzający sumę przekątnych
#         diag_sum1 = 0
#         for t in range(length):
#             d = square[t][t]
#             diag_sum1 += d
#
#         diag_sum2 = 0
#         for y in range(length - 1, -1, -1):  # Poprawiono zakres i krok
#             d1 = square[y][y]
#             diag_sum2 += d1
#
#         if diag_sum1 != diag_sum2:
#             print("To nie jest magiczny kwadrat")
#             return False
#
#         # Komunikat końcowy po spełnieniu wszystkich warunków
#         print("To jest magiczny kwadrat")
#         return True
#
#
# semi_magic_square()

def moje_kolumny(square):
    dl=len(square)
    wiersz=square[0]
    for n in square:
        if sum(n)==sum(wiersz):
            print(sum(n))
            pass
        else:
            print(sum(n))
            return 'to nie magiczny'
    #tera kolumny
    s=0
    for x in range(dl):
        for i in range(dl):
            s+=square[x][i]
        if s==sum(wiersz):
            pass
        else:
            return 'kolumny nie zh=gdzaja sie'
    return 'TO magiczny!'



print(moje_kolumny([[2,7,6],[9,5,1],[4,3,8]]))