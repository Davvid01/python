lista = [4, 6, 2]
n=3
try :
    print(lista[n])
    print("Nie było błędu.")
except IndexError :
    print("Nie da sie pobrac. Sprawdz czy lista ma tyle elementow.")
print("Koniec programu.")


lista = [4, 6, 2]
n="0"
try :
    print(lista[n])
except IndexError :
    print("Nie da sie pobrac. Sprawdz czy lista ma tyle elementow.")
finally :
    print("Sprzątanie...")
print("Koniec programu.")


lista = [4, 6, 2]
n="0"
try :
    print(lista[n])
    print("Nie było błędu.")
except TypeError as blad:
    lan=""
    for arg in blad.args :
        lan += (arg + " ")
    raise Exception("Zły typ", lan)
print("Koniec programu.")

class BladTrojkata (Exception):
    opis = "Dla dowolnego trójkąta miara każdego boku \
musi być mniejsza lub równa sumie miar dwóch pozostałych"
a=1
b=5
c=10
try :
    if (a+b<c or a+c<b or b+c<a) :
        raise BladTrojkata
except BladTrojkata as e :
    print(e.opis)