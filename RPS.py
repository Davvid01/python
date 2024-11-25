import random


def graj():
    wygrana_gracza = 0
    wygrana_komputera = 0
    while wygrana_gracza < 3 and wygrana_komputera < 3:
        wpisywanie = input("Podaj P, K lub N. Dla przerwania Q: ")
        baza = ['p', 'k', 'n']
        komputer = random.choice(baza)
        wpisywanie = wpisywanie.lower()

        if wpisywanie == 'q':
            break
        elif wpisywanie not in baza:
            print("Zła dana. Wpisz ponownie")
            continue

        print(wpisywanie)
        print(komputer)

        if komputer == wpisywanie:
            print(f"Remis! Oboje wybraliście {komputer}. To was dyskwalifikuje")
        elif (komputer == 'p' and wpisywanie == "k") or (komputer == 'k' and wpisywanie == "n") or (
                komputer == 'n' and wpisywanie == "p"):
            print("Przegrałeś")
            wygrana_komputera += 1
        else:
            print("Wygrałeś")
            wygrana_gracza += 1

        print(f"Punkty komputera: {wygrana_komputera} Punkty twoje: {wygrana_gracza}")


graj()
