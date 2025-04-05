zmienna=("Jestem botem ok"'\n'
          "jej")
lista=['a','b','c','a']
liczby=[1,2,3,4,6]
# print(zmienna)
# print('T'.join(zmienna))
# print('T'.join(lista))
#
# print(zmienna.replace('Jestem','Bywam'))
# lista[lista.index('a',1,4)]='d'  #index szuka danej zmiennej 1,3 rto zakres w jakim szukamy
# print(lista)
# print(zmienna.startswith("Jestem"))
#
# print("ba" in "trebaczek")
# print(zmienna.upper())
# print(zmienna.lower())
"""
if all([i%2==0 for i in liczby]):
    print("wszystkie parzyste")

if any([i%2==0 for i in liczby]):
    print("joo")

for i in enumerate(lista):
    print(i[0]+1,"->"'\t',i[1])

def wyszukaj_liczbe():
    komunikat=input("Podaj komunikat: ")
    komunikat=list(komunikat)
    komunikat=map(int, komunikat)
    print(komunikat)
    print(type(komunikat))
    slowo = "ba1na2ny3"
    suma_lista=[]
    for x in komunikat:

print(wyszukaj_liczbe())
"""

def wyszukaj_liczbe():
    komunikat=input("Podaj komunikat: ")
    litery_lista = list(komunikat)
    suma_lista = []
    for x in litery_lista:
        if x.isdigit():
            suma_lista.append(x)

    odpowiedz=int(suma_lista[0])+ int(suma_lista[-1])

    return odpowiedz
print(wyszukaj_liczbe())