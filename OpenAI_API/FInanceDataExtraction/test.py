from openai import OpenAI
import json
import pandas as pd
import openai

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

def extract_financial_data(text):
    prompt = get_prompt_financial() + text
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user","content": prompt}]
    )
    content = response.choices[0]['message']['content']

    try:
        data = json.loads(content)
        return pd.DataFrame(data.items(), columns=["Measure", "Value"])

    except (json.JSONDecodeError, IndexError):
        pass

    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })



def get_prompt_financial():
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text = '''
    Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $
    '''
    df = extract_financial_data(text)

    print(df.to_string())