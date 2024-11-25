def piram_pion():
    wysokość=3
    y=wysokość-1

    while y>=0: #gdy warunek
        # for gdy zakres
        x=1
        while x< (wysokość*2):
            if x>y and x< (wysokość*2-y):
                print(int('1', end =" "))#end odpowiada za zejscie w dół??
            else:
                print(" ",end=" ")
            x=x+1
        print("")  #pusty print drukuje i wtedy przejdz do kolejnej linii
        y=y-1
    else:
        exit()
    x+=1 #x zwiększa się o 1 w pętli while!!
#idzie spac spac hash spac spac dół itd

piram_pion()    #od razu printuje bo jest wewnątrz kodu print