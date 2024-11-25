def iletoma():
    słowo=input("podaj słowa: ")
    i = 0               #jeżeli i=0 zadeklarowałbym w pętli to za kązdym razem odswiezaloby sie do wartosci 0
    for x in słowo:
        if x==' ' :
            i+=1
    print(f"liczba spacji to: {i} liczba wyrazów to: {i+1}liczba znaków: ",len(słowo), end=" ")  #jeżeli print byłby w pętli to po każdym wykonaniu petli drukowałby wynik i, a my chcemy tylk o koncowy wynik
    print("dąb")


def iletomazzajec():
    slowo = input("Podaj słowo:")
    liczba_wyrazów=len(slowo.split()) # ze stringa tworzy liste elementów, każda spacja to oddzielenie
    print(slowo)
    zamiana_spacji_na_nic=slowo.replace(" ","")
    iloscliter= len(zamiana_spacji_na_nic)
    liczba_spacji=slowo.count(' ') #zlicza powtórzenia danego znkau
    print(f"Nasz teskt składa się z {iloscliter} liter oraz {liczba_spacji} spacji oraz {liczba_wyrazów}")
iletomazzajec()