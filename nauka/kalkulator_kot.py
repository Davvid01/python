def cat_age(age):
    if age<2:
        return f"Marion ma {age*12+1} lat i jest kitten"
    elif age in range(2,10):
        wiek=20
        for x in range(2,age+1):
            wiek+=5
        return f"Kot ma {wiek} lat i jest adult"
    else:
        wiek=60
        for x in range(10,age+1):
            wiek+=5
        return f"Kot ma {wiek} lat i jest seniorką"
def age():
    test=input('Czy twój kot ma więcej niż jeden rok? TAK/NIE: ').lower().strip()=='tak' #Remove spaces at the beginning and at the end of the string:
    print(test)
    if test==True:
        return int(input(f"Ile lat ma twój kot?: "))
    else:
        miesiace=int(input(f"Ile miesięcy ma twój kot? "))
        return miesiace/12
#print(age())
print(cat_age(age()))