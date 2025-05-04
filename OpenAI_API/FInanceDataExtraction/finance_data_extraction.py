from openai import OpenAI
import json
import pandas as pd
# Wczytaj klucz API z pliku tekstowego
def load_api_key(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        exit(1)
api_key_path = "../api_key.txt" #Starting with ../ moves one directory backward and starts there
api_key = load_api_key(api_key_path)

# Konfiguracja klienta OpenAI
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=api_key,
)

def extract_financial_data(text): #takes the news article as a text and retrieve our request
    prompt = get_prompt_financial() + text
    response= client.chat.completions.create(
        model="gpt-4.1",
        messages= [{"role":"user", "content": prompt}]
    )
    tresc=response.choices[0].message.content

    try:
        data = json.loads(tresc)
        return pd.DataFrame(data.items(),columns=["Measure", "Value"])
    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

def get_prompt_financial() -> object:
    return '''From the news article below, extract ONLY the following data: 
1. Company Name
2. Stock Symbol
3. Revenue (total revenue for the company; ignore product-specific revenue)
4. Net Income
5. EPS
If any of these fields are missing, return "can't find". Do NOT include product-specific data or extra details. Always return a valid JSON object.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============

    '''
""" https://www.cnbc.com/2023/05/04/apple-aapl-earnings-report-q2-2023.html """
artykul="Apple reported second-fiscal quarter earnings on Thursday that beat Wall Street’s soft expectations, driven by stronger-than-anticipated iPhones sales. Apple CEO Tim Cook told CNBC that the quarter was “better than we expected.” However, Apple’s overall sales fell for the second quarter in a row. The tech giant’s shares rose nearly 2% in extended trading, and continued climbing when Apple gave forecast data points about the current quarter. Here’s how the company did versus Wall Street expectations per Refinitiv consensus expectations: EPS: $1.52 per share vs. $1.43 expected Revenue: $94.84 billion vs. $92.96 billion expected Gross margin: 44.3% vs. 44.1% expected Apple reported $24.16 billion in net income during the quarter compared to $25.01 billion in the year-earlier period. Total revenue was off 3% from $97.28 billion in the prior quarter. Here’s how Apple’s individual product lines did versus StreetAccount consensus expectations: iPhone revenue: $51.33 billion vs. $48.84 billion expected Mac revenue: $7.17 billion vs. $7.80 billion expected iPad revenue: $6.67 billion vs. $6.69 billion expected Other Products revenue: $8.76 billion vs. $8.43 billion expected Services revenue: $20.91 billion vs. $20.97 billion expected"

df=extract_financial_data(artykul)
print(df.to_string())
print(artykul)








"""
# Zapytanie do API
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "jaka różnica między uczeniem maszynowym, a AI. Odpowiedz w 3 zdaniach",
        },
    ],
    model="gpt-4o-mini",
    temperature=1,
    max_tokens=4096,
    top_p=1,
)

# Wyświetlenie odpowiedzi
print(response.choices[0].message.content)
"""