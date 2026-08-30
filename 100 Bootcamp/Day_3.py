
height = int(input("Jaki jest twój wzrost w cm?: "))
rachunek=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?: "))
    if age >=18:
        print("You pay 12$")
        rachunek+=12
    elif age >=12 or age <18:
        print("you pay 7$")
        rachunek+=7
    else:
        print("You pay 5$")
        rachunek+=5

    photos= input("Photos?: Yes/No: ")
    if photos == "Yes":
        print("3$")
        rachunek+=3
    print(f"Rachunek wynosi: {rachunek}$")
else:
    print("You cant ride")