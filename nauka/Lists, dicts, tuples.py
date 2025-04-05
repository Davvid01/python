#zad2 https://www.w3resource.com/python-exercises/list-advanced/index.php
"""
def longest_increasing_subsequence(nums):
    dlg=len(nums)
    subq=1
    storage=[]
    for x in range(0,dlg-1):
        if nums[x]<nums[x+1]:
            subq+=1
        elif subq>=1:
            storage.append(subq)
            subq=0
    storage.append(subq)
    print(storage)
    return max(storage)
lista=[10, 20, 30, 40, 50, 60, 50, 80]
nums = [10, 20, 30, 40, 50, 30, 30, 20]
minus = [-1, -2, -3, -4, -5, -11, -12, -13]

print(longest_increasing_subsequence(lista))
print(longest_increasing_subsequence(nums))
print(longest_increasing_subsequence(minus))

#zad3
from itertools import permutations

def find_permutations(input_list):
    return list(permutations(input_list))

# Przykład użycia:
example_list = [1, 2, 3]
result = find_permutations(example_list)
print(result)

#zad 3https://www.w3resource.com/python-exercises/dictionary/
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

d.update({7:80})
print(d)

#zad3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
z=dic1.copy()
z.update(dic2)
z.update(dic3)

print(z)

#zad4
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def check_if(k):
    if k in d:
        return True
    else:
        False
print(check_if(6))

#zad5
def itereting():
    for k,v in d.items():
        print (k,v)
        print (d.items())
print(itereting())

#zad6
n=int(input("Podaj liczbe: "))
nd=dict()
for x in range(1, n+1):
    nd[x]=x*x
    print(d)
"""
#it integro
data = (20, 80, 15, 66, 23, 78, 44, 32)
data=list(data)
storage=[]
def sprawdzenie():
    for x in data:
        for y in data:
            if (x,y) not in storage and (y,x) not in storage and x+y==110:
                storage.append((x,y))
    return  storage
print(sprawdzenie())

lista = [1, 2, 3, 4, 5, 6, 7, 8]

def suma_liczb_parzystych():
    wynik = 0
    for x in lista:
        if x%2==0:
            wynik+=x
    return wynik
print(suma_liczb_parzystych())

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

def wspolne():
    result=[]
    for element in lista1:
            if element in lista2:
                result.append(element)
    return result
print(wspolne())
