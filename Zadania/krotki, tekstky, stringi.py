krotka=(2,3,4,6,7,8)
#nie mozna przypisać jej zmiennych
lista=[1,2,3,4,5,6,7]
lista2=[]
print(krotka)
print(krotka.count(8))
print(krotka.index(4))
print(krotka[-100:-1])
print(krotka[2::3]) #srodkowy dwourkopek pusty oznacza ze wycinamy do końca, a trzecia cyfra to co który lelement wybieramy
print(krotka[:3:2]) #od początku wybueramy do trzeciego nr 3
print(krotka[:3:-1]) #oznacza że wybieramy od końca (od końca pierwszy indeks ma numer 1!!! -a nie zero)
print(lista[::-1])
lista2=[]
lista=[1,2,3,4,5,6,7]
for x in range(lista[6],lista[2],-1):
    lista2.append(x)
print(lista2)
for i in enumerate(lista):
    print(i[0]+1,i[1])





