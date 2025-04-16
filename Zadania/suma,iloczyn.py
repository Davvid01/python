NIU=[8,2,7,4]

def ilosuma():
    x=int(input(f"Podaj wartość: "))       # bez int zostaje sam string
    print ("x= ", x)
    for i in NIU:           #pętla w pętli, pojedynczo dla kazdego elementu programy przerobi jeszcze calą liste
       for y in NIU:
            razem = i + y
            mnożenie=i*y
            if razem == x and y!=i:
                print(f"suma cyfry {i} oraz {y} daje razem podaną {x}")
            if mnożenie==x and y!=i:
                print(f"iloczyn cyfry {i} oraz {y} daje razem podaną {x}")
    if x!=razem and x!=mnożenie:
            print("żadna liczba nie spelnia")





ilosuma()