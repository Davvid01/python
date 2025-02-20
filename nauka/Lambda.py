"""
#zad1 https://www.w3resource.com/python-exercises/lambda/index.php
t1= lambda x: x+15
t2 = lambda x,y: x*y
print(t1(3))
print(t2(4,5))
#zad2
def test(n):
    return lambda x: x*n
podwojne=test(2)
print(type(podwojne))
print(podwojne(3))
potrojne=test(3)
print(potrojne(7))

#zad3
lista=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
x =sorted(lista, key=lambda t: t[0])
print(x)
sorting=lista.sort(key=lambda x: x[1])
#mimo, że lista jest w zmiennej sorting to metoda .sort() sortuje 'in place'/modyfikuje w miejscui zwraca None. Lista zostanie posotrowana, ale zwrocone zostanie None
print(lista)

#zad4
data=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
def sortowanie(x):
    return sorted(x, key=lambda t: t['make'])
print(sortowanie(data))

#zad5
lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sortowanie(n):
    return list(filter(lambda x:x%n==0,lista))
parzysta=sortowanie(2)
print(parzysta)
test=list(filter(lambda x: x%2==0,lista))
print(test)

nieparzyste=list(filter(lambda x: x%2!=0,lista))
print(nieparzyste)

#zad6
data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista=[]
lista1=[]
def square(data):
    for x in data:
        test= lambda x: x**2
        print(test(x))
        lista.append(test(x))
    return lista

def cube(data):
    for x in data:
        test= lambda x: x**3
        print(test(x))
        lista1.append(test(x))
    return lista1
print(square(data))
print(cube(data))

data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_basic= map(lambda x:x**3, data) #funkcja map słuzy do iterowania po np liscie używajac np. funkcji lambda
print(list(square_basic)) #nalezy stworzyc funkcje aby obiekty mogly być przechpwywane
 #The map() function is used to execute a specified function for each item in a inerrable.
#zad7
slowo='pies'
litera='r'
test=(lambda x,y: x[0]==y)(slowo,litera)

test2=lambda x: True if x.startswith('p') else False
print(test)
print(test2('pies'))

#zad8
from datetime import date, datetime as dt
curr_date=dt.now()
print(curr_date)
#lista=curr_date.split()
#print(lista)
month=lambda x:x.month
tim=lambda x: x.time()
print(month(curr_date))
print(tim(curr_date))

#zad9

obiekt='56'
print(type(obiekt))
#examine=lambda x: True if isinstance(x, int) else False  niepotrzebne True False - isinstance automatycznie to zrobi
examine=lambda x: isinstance(x, int)
print(examine(obiekt))
"""
#zad21
data=[2, 4, 6, 9, 11]
n=3
multiplying=list(map(lambda x: x*n, data))
#print(multiplying(3)) The map function applies a function to each item in the input list, but it doesn't take an additional argument like n directly within the lambda function.
print(multiplying)
to_string='-'.join(map(str, multiplying))
print(to_string)

#zad11
d1=[1, 2, 3, 5, 7, 8, 9, 10]
d2=[1, 2, 4, 8, 9]

intersection=list(filter(lambda x: x in d2, d1)) #in not ==
print(intersection)

#zad12
d3=[-1, 2, -3, 5, 7, 8, 9, -10]
rearange=