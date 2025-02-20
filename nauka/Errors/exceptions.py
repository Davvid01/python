#zad1 https://www.w3resource.com/python/python-exceptions-with-examples.php
"""
try:
    result=100/0
except ZeroDivisionError:
    print("cannot divide")

try:
    my_list = [1, 2, 3, 4]
    print(my_list[4])
except IndexError:
    print('Wrong index')
except ZeroDivisionError: #Python checks each 'except' block in the order they are written.
    print("cannot divide")

try:
    my_list = [1, 2, 3, 4]
    print(my_list[4])
except Exception as e:
    print(f'does not work. Occured {e}') #'as e' allows you to capture the exception object and retrieve the error message
#zad4
try:
    file=open('test.txt', 'r')
except FileNotFoundError:
    print(f'nie ma pliku {FileNotFoundError}')
finally:
    print('this will be always excecuted') #runs whether or not an exception occurred, making it ideal for cleanup actions like closing files or releasing resources.
#zad5
def check_age(x):
    if x<18:
        raise ValueError('You must be older than 18') #fuction ends with Valueerro
    else:
        print('Age valid')
try:
    print(check_age(17))
except ValueError as e: #it is given an outcome of function - ValueError - so it returns an print
    print(f'Error: {e}')

#zad6

class Mojwlasnyblad(Exception):
   pass
def myfunc():
    raise Mojwlasnyblad('sth went wrong')
#print(myfunc())

try:
    myfunc()
except Mojwlasnyblad as e:
    print(f' the text is: {e}')

try:
    result=100/2
except ZeroDivisionError:
    print("cannot divide")
else:
    print('Division succesful', result)
"""
#zad10 https://www.w3resource.com/python-exercises/python-exception-handling-exercises.php
x=2
try:
    x.append('k')
except AttributeError:
    print('Zly atrybut')
#zad2
try:
    x=int(input("Podaj integer: "))
except ValueError:
    print(f'{x} to nie liczba calkowita')
finally:
    print(x)
