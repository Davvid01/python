def multiply(mnożenie):
    wynik=1
    for x in mnożenie:
        wynik=x*wynik

    return wynik
print(multiply((2,3,4,5,6)))
#zad4
def reverse_string(haslo):
    index =len(haslo)
    odwrocony_str= ''
    while index>0:
        odwrocony_str+=haslo[index-1] #-1 bo python nie zaczyna od 1 tylko od zera
        index= index-1
    return odwrocony_str
print(reverse_string("ghfd123"))

#zad5
def silnia(n):
    if n<=1:
        return 1
    else:
        return n*silnia(n-1)
print(silnia(4))

def silnia(n):
    wynik=1
    for x in range(2, n+1):
        wynik *=x
    return wynik
print(silnia(4))

#zad6
def duże_litery(n):
    if n in range (1945, 2022):
        print("jest g")
    else:
        print("nie jestem")
duże_litery(1959)

#zad7
def count(zdanie):
    u=0
    l=0
    for i in zdanie:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
        else:
            pass #zignoruj
    print(f"liczba dużych:  {u}")
    print(f"liczba dużych:  {l}")
count("Zawisza Pany")

#8
def unikalne(kody):
    x=[]
    for i in kody:
        if i not in x:
            x.append(i)     #dodaje numer z listy do pustej tablicy x
    return x

print(unikalne([1,2,3,3,3,4,5,6,6,7]))

#10
def parzyste(list):
    even=[]
    for x in list:
        if x%2==0:
            even.append(x)
    return even
print(parzyste([1,2,3,4,5,6,7,8]))









