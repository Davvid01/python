NIU=[8,2, 7,4]
#NIU.sort()
print(NIU)
def rosnące():
    #lista_licz
    for j in  NIU:
        for i in range(0, len(NIU)-j-1):
            if NIU[i]>NIU[i+1]:
                NIU[i]=NIU[i+1]
                NIU[i + 1]=NIU[i]
        print(NIU)
rosnące()
   # if wieksdze mniejsze lista,
    #zmienic
def rosnące1():
    n = len(NIU)
    for i in range(n):
        for j in range(0, n-i-1):
            if NIU[j] > NIU[j+1]:
                NIU[j], NIU[j+1] = NIU[j+1], NIU[j]
    print(NIU)

rosnące1()