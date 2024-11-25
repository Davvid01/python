def piramida_poziom():
    wysokość= int(input("daj wysokosc: "))
    if wysokość <1:
        print("wart. niepoprwanwa")
        return
    for i in range(1,wysokość*2):   #wysokkosc razy 2 bo pierwsze schodzi do szcyztui i musi zjechac jeszcze nizej wiec drugi zasięg
        #pokazała w notatniku róznice piramid, w poziomej
        #liczba_hashy=(i,wysokosc*2-i)    #do 10 rzędu liczba #=liczbie wierszy, ale od szcyztu jadac w dół
        #mamy zakres do wyskoości, czyli "#" skaczą po kolei do szczytu czyli uzyjemy for
        #(14->i, 2*10(wysokość)-i(14)=6)
        liczba_hashy = min(i, wysokość*2 - i) #min powoduje że bierze sb znak # i wybiera mniejszą liczbe, zeby wiedziec ile razy wyprintować hasha
        lista = "#"*liczba_hashy
        print(lista)
piramida_poziom()