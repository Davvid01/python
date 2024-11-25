def piramida():
    wysokosc=int(input("podaj wysokosc: "))

    for i in range(0, wysokosc*2):
        if i==0:
            continue
        if i<=wysokosc:
            for j in range (0,i):
                print("#", end="")
        else:
            for j in range (i-1, wysokosc*2-1):
                print("#", end="")
        print("")
piramida()