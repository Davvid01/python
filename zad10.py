# #11
# # def perfekt(liczba):
# #     lista=[]
# #     for i in range(1,liczba):
# #         if liczba%i==0:
# #             lista.append(i)
# #     return  lista
# # def sprawdzanie(lista, liczba):
# #     if sum(lista)==liczba:
# #         return "Liczba jest perfekt"
# #     else:
# #         return "liczba nie jest perfetk"
# #
# # podana_liczba=int(input("Podaj liczbe całkowitą: "))
# # wynik=perfekt(podana_liczba)
# # print(perfekt(podana_liczba))
# # print(sprawdzanie(wynik,podana_liczba))
#
# #12
# # def palindrom(slowo):
# #     return slowo.replace(" ","")
# # def odrwacanie(slowo):
# #     odwrocone_slwo=''
# #     index = len(slowo)
# #     while index>0:
# #         odwrocone_slwo+=slowo[index-1] #dlaczego na samym koncu wypluwa 3?
# #         index=index-1
# #     return odwrocone_slwo
# # def sprawdzanie(slowo):
# #     #print(palindrom(slowo))
# #     #(odrwacanie(palindrom(slowo)))
# #     if palindrom(slowo)==odrwacanie(palindrom(slowo)): #dlaczego przy zmiennej słowo nie działał
# #         return "Prawda"                                # bo brało poćżatkowe słowe ze spacjami dlatego odrwocenie było ze spacjami
# #     else:
# #         return "Fałsz"
# # slowo=input("Podaj słowo: ")
# # print(palindrom(slowo))
# # print(odrwacanie(palindrom(slowo)))
# # print(sprawdzanie(slowo))
#
# # #13
# # from math import factorial
# #
# # # input n
# # n = 5
# # for i in range(n):
# #     for j in range(n - i + 1):
# #         # for left spacing
# #         print(end=" ")
# #
# #     for j in range(i + 1):
# #         # nCr = n!/((n-r)!*r!)
# #         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
# #
# #     # for new line
# #     print()
# #
# #
# #
# # def piram_pion():
# #     wysokość = 3
# #     y = wysokość - 1
# #
# #     while y >= 0:
# #         x = 0  # Initialize x to 0
# #         while x < (wysokość * 2 - 1):  # Adjust the condition for the inner loop
# #             if x >= y and x < (wysokość * 2 - 1 - y):
# #                 print(int(1), end=" ")
# #             else:
# #                 print(" ", end=" ")
# #             x = x + 1
# #         print("")
# #         y = y - 1
#
# #piram_pion()
#
# #14\
# def alfabet(slowo):
#     zbiór=set("abcdefghijklmnopqrstuvwxyz")
#     slowo=''.join(slowo.lower().split())
#     sprawdzająca=[]
#     for x in slowo:
#          for j in zbiór:
#              if x==j:
#                 sprawdzająca.append(j)
#     sprawdzająca.sort()
#     if zbiór==set(sprawdzająca):
#         return "To jest to"
#     else:
#         return "to nie to"
#
# #slowo=input("Podaj słowo: ")
# print(alfabet(slowo=input("Podaj słowo: ")))
#
# #15
# # def myslniki():
# #     slowa=input("Podaj slowa oddzielona myslnikami: ")
# #     slowa_bez_myslnikow=slowa.replace('-',' ')
# #     lista_slow=slowa_bez_myslnikow.split()
# #     b=sorted(lista_slow)
# #     razem = '-'.join(b)
# #     return razem
# # print(myslniki())
#
# #16
def kwadraty():
    duże=[]
    for x in range (1,31):
        duże.append(x**2)
    return duże
print(kwadraty())
#
# #17
# #def make_bold(fn):
#    #fdc def wrapped():
#     #     return "<b>" + fn() + "</b>"
#     # return wrapped
#
# # def make_italic(fn):
# #     def wrapped():
# #         return "<i>" + fn() + "</i>"
# #     return wrapped
# #
# # def make_underline(fn):
# #     def wrapped():
# #         return "<u>" + fn() + "</u>"
# #     return wrapped
# # @make_bold
# # @make_italic
# # @make_underline
# # def hello():
# #     return "hello world"
# # print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
# # fs
# from time import sleep
# import math
# def delay(fn, ms, *args):
#   sleep(ms / 1000)
#   return fn(*args)
# print("Square root after specific miliseconds:")
# print(delay(lambda x: math.sqrt(x), 100, 16))
# print(delay(lambda x: math.sqrt(x), 1000, 100))
# print(delay(lambda x: math.sqrt(x), 2000, 25100))
#18

print(""
      "fdfdfd"
      "dfdf"
      "fd")
#21
