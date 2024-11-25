# NIU=[8,2,7,4]
# x=sorted(NIU)
# print(x)
class Babelki:
    def __init__(self):
        self.NIU=[8,2,7,4]
    def malejąco(self):
        self.razy=len(self.NIU)
        for i in range (self.razy):
            for j in range(0,self.razy-i-1):
                if self.NIU[j]<self.NIU[j+1]:
                    self.NIU[j],self.NIU[j+1]=self.NIU[j+1],self.NIU[j]
        return self.NIU
    def rosnąco(self):
        #return self.razy
        for i in range (self.razy):
            for x in range (0, self.razy-i-1):
                if self.NIU[x]>self.NIU[x+1]:
                    self.NIU[x],self.NIU[x+1]=self.NIU[x+1],self.NIU[x]
        return self.NIU
test=Babelki()
wynik=test.malejąco()
print(wynik)

d=test.rosnąco()
print(d)