import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def pobierz_dane_waluty(kod_waluty, data_poczatkowa, data_koncowa):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{kod_waluty}/{data_poczatkowa}/{data_koncowa}/?format=json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dane = response.json().get('rates', [])

        if not dane:
            print('Brak danych dla podanych parametrów.')
            return pd.DataFrame()

        return pd.DataFrame(dane)

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych: {e}')
        return pd.DataFrame()


def pobierz_dane_zlota(data_poczatkowa, data_koncowa):
    url = f'http://api.nbp.pl/api/cenyzlota/{data_poczatkowa}/{data_koncowa}/?format=json'

    try:
        response = requests.get(url)
        response.raise_for_status()
        dane = response.json()

        if not dane:
            print('Brak danych dla podanych parametrów.')
            return pd.DataFrame()

        return pd.DataFrame(dane)

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych: {e}')
        return pd.DataFrame()


def pobierz_kurs_waluty(kod_waluty):
    url_waluty = f'http://api.nbp.pl/api/exchangerates/rates/a/{kod_waluty}/'

    try:
        response_waluty = requests.get(url_waluty)
        response_waluty.raise_for_status()
        kurs_waluty = response_waluty.json()['rates'][0]['mid']

        return kurs_waluty

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania kursu {kod_waluty}: {e}')
        return None


def pobierz_cene_zlota_dzisiaj():
    url_zloto_dzisiaj = 'http://api.nbp.pl/api/cenyzlota/today'

    try:
        response_zloto = requests.get(url_zloto_dzisiaj)
        response_zloto.raise_for_status()
        dane_zloto = response_zloto.json()

        if not dane_zloto or not isinstance(dane_zloto, list):
            print('Brak danych dla ceny złota dzisiaj.')
            return 'Brak danych'

        # Access the first element of the list and then the 'cena' key within the dictionary
        cena_zlota = dane_zloto[0].get('cena', 'Brak danych')
        return cena_zlota

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych ceny złota dzisiaj: {e}')
        return 'Błąd'




def rysuj_wykres(dane, kod, tytul, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dane['effectiveDate'], dane['mid'], marker='o')
    ax.set_title(f'{tytul} od {dane["effectiveDate"].min()} do {dane["effectiveDate"].max()}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Kurs')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


def rysuj_wykres_zlota(dane_zlota, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dane_zlota['data'], dane_zlota['cena'])
    ax.set_title(f'Kurs złota od {dane_zlota["data"].min()} do {dane_zlota["data"].max()}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Kurs złota')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)


def porownaj():
    waluta = combo_waluta.get()
    rok = combo_rok.get()

    data_poczatkowa = f'{rok}-01-01'
    data_koncowa = f'{rok}-12-31'

    dane_waluty = pobierz_dane_waluty(waluta, data_poczatkowa, data_koncowa)
    dane_zlota = pobierz_dane_zlota(data_poczatkowa, data_koncowa)

    if not dane_waluty.empty:
        rysuj_wykres(dane_waluty, waluta, f'Kurs {waluta}', ramka_wykresow)
    else:
        print(f'Brak danych kursu {waluta} do wyświetlenia.')

    if not dane_zlota.empty:
        rysuj_wykres_zlota(dane_zlota, ramka_wykresow)
    else:
        print('Brak danych kursu złota do wyświetlenia.')

    # Wyświetl kurs wybranej waluty
    kurs_waluty = pobierz_kurs_waluty(waluta)
    if kurs_waluty is not None:
        label_kurs.config(text=f'Aktualny kurs {waluta}: {kurs_waluty}')
    else:
        print(f'Brak danych kursu {waluta}.')

    # Wyświetl cenę złota z dzisiaj
    cena_zlota_dzisiaj = pobierz_cene_zlota_dzisiaj()
    if cena_zlota_dzisiaj is not None:
        label_cena_zlota.config(text=f'Aktualna cena złota: {cena_zlota_dzisiaj}')
    else:
        print('Brak danych ceny złota z dzisiaj.')


okno = tk.Tk()
okno.title('Porównanie Kursów Walut, Złota i Wybranej Waluty')

label_waluta = ttk.Label(okno, text='Wybierz walutę:')
label_waluta.pack()

combo_waluta = ttk.Combobox(okno, values=['USD', 'GBP', 'CHF', 'CNY', 'EUR', 'CAD', 'CNY'])
combo_waluta.pack()

label_rok = ttk.Label(okno, text='Wybierz rok:').pack()

combo_rok = ttk.Combobox(okno, values=['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'])
combo_rok.pack()

przycisk_porownaj = ttk.Button(okno, text='Porównaj', command=porownaj)
przycisk_porownaj.pack()

ramka_wykresow = tk.Frame(okno)
ramka_wykresow.pack()

label_kurs = ttk.Label(okno, text='Aktualny kurs:')
label_kurs.pack()

label_cena_zlota = ttk.Label(okno, text='Aktualna cena złota:')
label_cena_zlota.pack()

okno.mainloop()
body = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = body.json()
step = input('Enter your currency [USD/EUR/CHF]:')
currency_client =step.upper()
quantity = int(input('specify how much money you want to exchange:'))

for rate in response[0]['rates']:
    if currency_client==rate['code']:
        result=quantity*rate['mid']
        print(rate['currency'])
        print(rate['code'])
        print(rate['mid'])
        print(f'W rezultacie otrzymasz: {result}PLN')
        print('-'*20)
