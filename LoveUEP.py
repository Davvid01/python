NIU=[8,2,7,4]
def kocham_UEP():
    for x in range (1,101):
        if x%3==0 and x%5==0:
            print("LoveUEP")
        elif x==50:
            print(NIU, end=" 1 ")
        elif x%3==0:
            print("Love", end=",")
        elif x%5==0:
            print("UEP")
        else:
            print(x)
kocham_UEP()

