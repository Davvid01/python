#zad 1 https://www.w3resource.com/python-exercises/python-basic-exercises.php
""" https://www.w3resource.com/python-exercises/python-functions-exercises.php
string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
print(f"Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, Like a diamond in the sky. \nTwinkle, twinkle, little star, How I wonder what you are")
#zad2
import sys
print(sys.version)
import datetime

x=datetime.datetime.now()
print(x)
#zad4
import math
x=float(input('Podaj promien: '))

pole=x**2*math.pi
print(f'pole wynosi: {pole}')
#zad5
imie=input("Podaj swoje imie: ")
nazwisko=input("Podaj swoje nazwisko: ")

#zad6
liczby=input("Podaj swoje liczby po ,: ")

lista=liczby.split(",")
print(lista)
tupla=tuple(lista)
print(tupla)
lista[0] = "zmieniony element"
print("Lista po zmianie elementu:", lista)
try:
    tupla[0] = "zmieniony element"
except TypeError:
    print('nie można')

#zad9
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1])
#zad10
exam_st_date = (11, 12, 2014)
print(f"The examination will start from :  %d / %d / %i" % exam_st_date)
#10
a = int(input("Input an integer: "))
n1=int('%s' % a)
n2=int('%s%s' % (a,a))

print(n1+n2)

#zad14
import datetime
f_date=datetime.date(2024,7,2)
l_date=datetime.date(2024,7,11)
x=l_date-f_date
print(x.days)

#zad1 JSON
import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"])

print(python_obj["Name"])
#zad 1 https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-1.php

def test(data):
    if len(data)==set(data): #oczyszcza liste
        return True
    else:
        return False



print(test([1,2,33,4,5,55]))

# zad1
zbior=[23.43,43,65.23]

def maximum(x, y):
    if x>y:
        return x
    else:
        return y
def max_3(x, y, z):
    if maximum(x,y)>z:
        return maximum(x,y)
    return z
print(max_3(3,6,-5))

#zad2

def suma(liczby):
    c=0
    for y in liczby:
        c+=y
    return c
print(suma([8, 2, 3, 0, 7]))

#zad3
def multiply(liczby):
    total=liczby[0]
    for x in liczby[1:]:
        total=total*x
        #print(total)
    return total
print(multiply((8, 2, 3, -1, 7)))

#zad 4
def reversed(string):
    #rever=string.split[]
    answer=""
    for x in string[::-1]:
        answer+=x
    reversedstr=''
    liczba_element=len(string)
    print(liczba_element)
    while liczba_element>0:
        reversedstr+=string[liczba_element-1]
        liczba_element=liczba_element-1
    return reversedstr
print(reversed("1234abcd"))

#zad 5
def factorial(n):
    numbers=[]
    nope=[]
    for x in range(1,n+1):
        if n%x==0:
            numbers.append(x) #this manner I fill the list
        else:
            nope.append(x)
    return f"These are factorials: {numbers}\nthese not: {nope}"
print(factorial(24))

def facts(n):
    numbers=1
    for x in range(1,n+1):
        numbers=numbers*x
    return numbers
print(facts(55))

#zad 7
def falls_within(x):
    if x in range(0,24):
        return f"{x} is in the range"
    return False
print(falls_within(24))

#zad 8
def distinctive(lista):
    nowa=[]
    for x in lista[::-1]:
        if x not in nowa:
            nowa.append(x)
#        else:
 #           pass
    return nowa
print(distinctive([1,2,3,3,3,3,4,5]))

#zad 9
def prime(x):
    if x>=10:
        if x%2!=0 and x%3!=0 and x%7!=0 and x%4!=0 and x%5!=0 and x%6!=0:
            return True
        else:
            return False
    elif x==1:
        return False
    elif x in [2,3,5,7]:
        #if x%2==0 or x%3!=0 or x%4!=0:
        return True
    else:
        return False
print(prime(7))

#zad 10
def even(lista):
    para=[]
    for x in lista:
        if x%2==0:
            para.append(x)
    return para
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))

class Employee(object):
   def my_method(self):
      print("I am Vikram")
name = Employee()
name.my_method()

#zad11
def perfect(example):
    divisors=[]
    summary=0
    for x in range(1,example):
        if example%x==0:
            divisors.append(x)
            print(divisors)
    for x in divisors:
        summary+=x
        if summary==example:
            return f"{example} is perfect"
    return False
print(perfect(8128))

#zad12
def palindrome(example):
    store=""
    nospace=example.replace(" ","")
    print(example.replace(" ",""))
    for x in example.replace(" ","")[::-1]: #od końca
        store+=x
        print(store)
    return store==nospace
print(palindrome("kaj  ak"))

def spljo(example):
    print(example.split()) #whitespace is default separator of elements in the list
    print(",".join(example.split())) #double quotes defines how elements from the list will be seperated
print(spljo(" kaj ak "))

#zad 13
test=[]
def pascal(liczba_wierszy):

    trow =[1]
    y=[0]
    for x in range(max(liczba_wierszy,0)):
        print(trow)
        trow=[l+r for l, r in zip(trow +y, y+trow)]
    return liczba_wierszy >= 1
print(pascal(5))

for x in range(max(10, 0)):
    print(x)
#zad14
import string
print(string.ascii_lowercase)
def pangram(sentence):
    letters=''
    alphabet=list(string.ascii_lowercase)
    sentence=sentence.lower()
    for x in sentence:
        if x not in letters:
            letters+=x
            #print(letters)
    test=''.join(letters.split())
    print(test)
    print(sorted(test))
    if sorted(test)==alphabet:
        return True
    return False
print(pangram("The quick brown fox jumps over the lazy dog"))

#zad15
def hyphen(example):
    sepa='-'.join(sorted(example.split('-'))) #the default seperator is backspace
    print(sepa)
print(hyphen("green-red-yellow-black-white"))

#zad16
lista=[]
for x in range(1,21):
    lista.append(x**2)
print(lista)

#zad17
def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
def italic(fn):
    def nowy():
        return "<i>" + fn() + "</i>"
    return nowy

# Define the underline decorator
def underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@bold
@italic
@underline
def tekst():
    return "To jest przkładowy tekst"
print(tekst())

#zad18
kod='print("hello world")' #pay attention to quotes
exec(kod) #wykonuje funckje w stringu

#zad19
def outer(a):
    def inner(b):
        nonlocal a
        return a+b
    return inner
f = outer(5)
print(f(4)) #The code creates a closure where the inner function has access to the a variable from the outer function. When you call f(5), it returns 10 because a is 5 from the outer function and b is 5 from the call to f.

#zad20
def fun():
    a, b, c = 1, 2.25, 333
    str = 'GeeksForGeeks'
print(fun.__code__.co_nlocals)

#zad21
import time

startlog=time.time()
print(startlog)

def tess():
    global startlog #bez zmiennej global nie moglem edytować zmiennej startlog niżej
    if time.time() - 3 > startlog:
        print("minely 3 sekundy")
        startlog=time.time()
while True:
    tess()
    #time.sleep()
"""