import requests
import pandas as pd

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


print(df)
df.head()
df.info()


##print(lista_aktualne)

##for x in dane_json:
##    for y in x.iteritems:
##        print(y)
## 

