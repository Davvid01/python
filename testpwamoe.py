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

        cena_zlota = dane_zloto[0].get('cena', 'Brak danych')
        return cena_zlota

    except requests.exceptions.RequestException as e:
        print(f'Błąd podczas pobierania danych ceny złota dzisiaj: {e}')
        return 'Błąd'

def rysuj_wykres(dane, kod, tytul, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(len(dane)), dane['mid'], marker='o')
    ax.set_title(f'{tytul} od {dane["effectiveDate"].min()} do {dane["effectiveDate"].max()}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Kurs')
    ax.set_xticks(range(len(dane)))
    ax.set_xticklabels([d.strftime('%Y-%m-%d') for d in pd.to_datetime(dane['effectiveDate'])], rotation=45, ha='right')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

def rysuj_wykres_zlota(dane_zlota, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range(len(dane_zlota)), dane_zlota['cena'])
    ax.set_title(f'Kurs złota od {dane_zlota["data"].min()} do {dane_zlota["data"].max()}')
    ax.set_xlabel('Data')
    ax.set_ylabel('Kurs złota')
    ax.set_xticks(range(len(dane_zlota)))
    ax.set_xticklabels([d.strftime('%Y-%m-%d') for d in pd.to_datetime(dane_zlota['data'])], rotation=45, ha='right')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

def exchange_currency(event=None):
    currency_client = combo_waluta.get().upper()
    quantity_text = entry_quantity.get()  # Get the quantity from the entry field
    if quantity_text.strip():  # Check if the entry is not empty
        try:
            quantity = float(quantity_text)

            # Get the current exchange rate for the selected currency
            url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_client}/'
            response = requests.get(url)
            data = response.json()
            if 'rates' in data and len(data['rates']) > 0:
                exchange_rate = float(data['rates'][0]['mid'])
                result = quantity * exchange_rate
                label_currency_converter.config(text=f"W rezultacie otrzymasz: {result:.2f} PLN")
            else:
                label_currency_converter.config(text="Brak danych dla przelicznika walut")
        except ValueError:
            label_currency_converter.config(text="Nieprawidłowa wartość ilości pieniędzy")
    else:
        label_currency_converter.config(text="Proszę wprowadzić ilość pieniędzy")

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

root = tk.Tk()
root.title('Kalkulator walutowy')

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Currency Converter
label_waluta = ttk.Label(main_frame, text="Wybierz walutę:")
label_waluta.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

combo_waluta = ttk.Combobox(main_frame, values=["USD", "EUR", "GBP"])
combo_waluta.grid(row=0, column=1, padx=5, pady=5)

label_quantity = ttk.Label(main_frame, text="Ilość pieniędzy:")
label_quantity.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_quantity = ttk.Entry(main_frame)
entry_quantity.grid(row=1, column=1, padx=5, pady=5)

button_convert = ttk.Button(main_frame, text="Przelicz", command=exchange_currency)
button_convert.grid(row=2, column=1, padx=5, pady=5)

label_currency_converter = ttk.Label(main_frame, text="")
label_currency_converter.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Currency Comparison
label_rok = ttk.Label(main_frame, text="Wybierz rok:")
label_rok.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

combo_rok = ttk.Combobox(main_frame, values=["2021", "2022", "2023"])
combo_rok.grid(row=4, column=1, padx=5, pady=5)

button_porownaj = ttk.Button(main_frame, text="Porównaj", command=porownaj)
button_porownaj.grid(row=5, column=1, padx=5, pady=5)

# Frames for plots
ramka_wykresow = ttk.Frame(root)
ramka_wykresow.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

root.mainloop()
