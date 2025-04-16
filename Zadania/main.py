from locale import currency

import requests

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
