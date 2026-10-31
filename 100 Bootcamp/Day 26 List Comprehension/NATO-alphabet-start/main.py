student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

slowa = pd.read_csv("Day 26 List Comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")
#
# print(slowa.head(5))

alphabet_dict = {wiersz.letter:wiersz.code for (nr_wiersza,wiersz) in slowa.iterrows()}
print(alphabet_dict)

#ta sama wersja klasyczna
alphabet_dict={}
for nr_wiersza, wiersz in slowa.iterrows():
    alphabet_dict[wiersz.letter] = wiersz.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

lista_slow=[]
for letter in word:
    lista_slow.append(alphabet_dict[letter])


#list comprehension
lista_slow = [alphabet_dict[item] for item in word]

print(lista_slow)