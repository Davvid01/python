
def szukaj_max():
   # wpisanie=input("Podaj trzy liczby: ")
    baza=[4,98,6.5]
    print(baza)
    najwieksza=max(baza)
    print(najwieksza)
szukaj_max()




def maksymalna(x,y,z):
    dane = print("Podane liczby to:", x,y,z)
    if x>y:
        if x>z:
            return (f"Najwieksza liczba to: {x}")
        else:
            return(f"Njawieksza liczba to: {z}")
    elif y<z:
        return(f"Njawieksza liczba to: {z}") #return powoduje że argumenty zostaną udostępnione poza funkcje, np gdy tworzymy nową zmienną i przypsiujemy jej metode
    else:   #wszystko po return nie zostanie wywołane
        return(f"Njawieksza liczba to: {y}")
#print(maksymalna())
sprawdz=maksymalna
print(sprawdz(6,56,4.5))

def silnia(x):
    i=1
    wynik = 1
    while i<=x:
        wynik*=i
        i += 1
    return wynik
c=silnia(2)
print(c)

def silnia_rekurencja(x):
    if x<=1:
        return 1
    else:
        return x*silnia_rekurencja(x-1)       #działa jak pętla, wywoluje samą sirbie, wraca do początku
print(silnia_rekurencja(3))



