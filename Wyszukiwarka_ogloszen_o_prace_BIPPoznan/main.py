import requests
import pandas as pd
from google import genai


url_urzad_miasta = 'https://bip.poznan.pl/api-json/bip/oferty-pracy/urzad-miasta-poznania/'

r = requests.get(url_urzad_miasta)

print(r.status_code)
print(r.headers)


dane_json = r.json()
##print(f"Dane JSONr: {dane_json}")

lista_aktualne = dane_json['bip.poznan.pl']['data'][0]['oferty_pracy']['items'][0]['oferta']

for oferta in lista_aktualne:
    print(f"Stanowisko: {oferta['stanowisko']}")
    print(f"Wydział: {oferta['nazwa_organizacja']}")


df = pd.DataFrame(lista_aktualne)
df['data_publikacji']= pd.to_datetime(df['data_publikacji'])
df['termin_skladania_ofert']= pd.to_datetime(df['termin_skladania_ofert'])


df = df.drop(['numer_referencyjny','id','id_organizacja'], axis=1) #the axis number (0 for rows and 1 for columns.)
#df.drop(columns=['numer_referencyjny', 'id_organizacja'], inplace=True) Dzięki inplace=True nie musisz pisać df = ..., bo Pandas zmodyfikuje tę samą tabelę w pamięci. Obie metody są poprawne, ale ta z inplace jest bardzo czytelna

print(df)
df.head()
df.info()


##print(lista_aktualne)

##for x in dane_json:
##    for y in x.iteritems:
##        print(y)
## 

df_text = df.to_markdown(index=False)
print(df_text)


client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f'Analyze which job offers suits to my profile. All job offers are from Poznan city hall. Im interested in smart cities and junior data analyst. {df_text}. Wypisz tylko stanowiska bez komentarza'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
