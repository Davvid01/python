#name = input("What is your name?")

#print(len("Hello " + f"{name}" "!"))

#print(len(input("What is your name?")))
##
##username=input("What is your name?")
##length = len(username)
##print(length)

#KOmentowanie wielu linii kodu w VS CODE: zaznaczam kod i Shift+Alt+A  

""" print("Welcome to the Band Name Generator\nWhat is your name of city?\n")
miasto=input()
imie=input("What is your name?: \n")
print("Your band is "+miasto+ " " + imie)

print("Hello"[-1])

#Large integerse
print(123_456_789 + 1) #python interpretuje tak samo jak:123456789 albo 123,456,789


#len(1234)
print(type(123))

print(int("123")+int("123"))


print("Liczba liter: " + str(len(input("Podaj swoje imie: "))))
 """

print(5/3)
print(5//3) #obcina liczbę po przecinku
print(2**3) # potęgowanie

#KOlejność
#PEMDAS parentheses (), exponents **, multiplication * or division /, addition + or suntraction -

print(3* ((3 + 3)/3) -3)
print(3* (3 + 3)/3 -3)

wzrost=1.88
waga=87

BMI=waga/wzrost**2

print(round(BMI, 2)) #zaokrągla matematycznie
print(int(BMI)) # obcina liczby dziesiętne

score = 0
score +=1
print("Your score is " + str(score))
wygrywanie= True
#f-string  nie trzeba konwertować danych
print(f"Twoj wynik to {score}, your wzrost to {wzrost}, Wygrywasz {wygrywanie} ")