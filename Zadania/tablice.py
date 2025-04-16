lista = [1, 2.4, "abc"]

print(lista)
print(lista[2]) #index o 1 mniej niż zakres naszej listy
lista [2]='essa'

print(lista)

tekst= 'siema eniu'
print(tekst[3])

print(lista +["f""g"])
print(lista*3)
print("podaj długosc listy: ",len(lista))

i=0
while i < len(lista):
    print(lista[i])
    i+=1

lista.clear()       #metoda gdy wywoluje funkcje spod obiektu
print(lista)
lista.append("dupa")      #append - dołącza na końcu
lista.append(3)
print(lista)
lista.append(['f','l'])
print(lista)
print(lista[2][0])      #pierwszy nawias wskazuje który indeks wybieramy(dodatkowa lista to cały jeden indeks), drugi nawias który element listy(tej dodatkowej)
#print(lista.insert(2,"ello"))      #dołącza element we wsakzanym miesjcu

print("ilość: ", lista.count('dupa')) #metoda, która sprawdza ile elementów znajduje się na liście
print("index: ", lista.index(3))    #sprawdza na któym indeksie jest dany element
lista.remove(3)
print(lista)

lista2=[4,7,4,2,5,7]
print("min:",min(lista2))
#lista2.sort()
print(lista2)
lista2.reverse() #odwraca elementy
print(lista2)
lista2.clear()
print(lista2)


