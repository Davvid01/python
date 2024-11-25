def zad1():
    df = pd.read_csv('movies.csv', sep=';', encoding = "ISO-8859-1",skiprows=[1])
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    filtered_df = df[df['Year'] == 1990]

# Display the resulting DataFrame
    print(filtered_df.head().to_string())
zad1()

def zad2():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1", skiprows=[1])
    #print(df.head(10000).to_string())
    print(df.groupby('Director')['Length'].mean())
zad2()

def zad3():
    filtered_df = df[['Title', 'Director', 'Popularity']]
    filtered_df.to_csv('output.csv', index=False, sep=';', encoding='ISO-8859-1')

zad3()

def zad4():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    filmy_nagrodzone = df[df['Awards'] == 'Yes']

    procent_nagrodzone = (len(filmy_nagrodzone) / len(df)) * 100
    print(f"Procent filmów z nagrodami: {procent_nagrodzone:.2f}%")
zad4()

def zad5():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    kubrick = df[df['Director'] == 'Kubrick, Stanley']
    print(kubrick)
zad5()

def zad6():
    df = pd.read_csv('movies3.csv', sep=';', encoding="ISO-8859-1")
    df['Popularity'] = df['Popularity'].str.strip()
    df['Popularity'] = pd.to_numeric(df['Popularity'], errors='coerce')
    popularnosc = df[df['Subject'] == 'Comedy']['Popularity'].sum()
    print(popularnosc)
zad6()