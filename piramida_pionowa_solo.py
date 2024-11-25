def piramida():
        wysokosc=int(input(f"Podaj wysokość: "))
        y=int(wysokosc-1)
        while y>=0:
            x = 1
            while x< wysokosc*2:
                if x>y and x< wysokosc*2-y:
                    print ("#", end= '')
                    x+=1
                else:
                    print("p", end='')
                    x+=1
            else:
                print("")
            y-=1

piramida()

