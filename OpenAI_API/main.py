import os
from openai import OpenAI

# Wczytaj klucz API z pliku tekstowego
def load_api_key(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        exit(1)

# Ścieżka do pliku z kluczem API
api_key_path = "api_key.txt"
api_key = load_api_key(api_key_path)

# Konfiguracja klienta OpenAI
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=api_key,
)

# Zapytanie do API
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "List 3 distinct differences between deep thinking models and standard LLMs like GPT-4o",
        },
    ],
    model="gpt-4o-mini",
    temperature=1,
    max_tokens=4096,
    top_p=1,
)

# Wyświetlenie odpowiedzi
print(response.choices[0].message.content)
