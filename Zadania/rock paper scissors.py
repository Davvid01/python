import random


def graj():
    wygrana_gracza = 0
    wygrana_komputera = 0
    while wygrana_gracza<3 and wygrana_komputera<3:
        wpisywanie=input("POdaj P, K lub N. Dla przerwania q: ")
        baza = (['p', 'k', 'n'])
        komputer = random.choice(baza)
        wpisywanie = wpisywanie.lower()
        if wpisywanie == 'q': #q z małej bo wyżej. lower wpisywanie
            break
        elif wpisywanie not in baza:
            print("zła dana. Wpisz ponownie")
            continue

        print(wpisywanie)
        print(komputer)

        if komputer == wpisywanie:
            print(  f"Remis! oboje wybraliście {komputer}. to was dyskwalifikuje")
        elif (komputer=='p' and wpisywanie=="k") or (komputer=='k' and wpisywanie=="n") or (komputer=='n' and wpisywanie=="p"):
            print( " przegrałes")
            wygrana_komputera +=1
        else:
            print("wygrałeś")
            wygrana_gracza+=1
        print(f"Punkty komputera: {wygrana_komputera} Punkty twoje: {wygrana_gracza}")
graj()







