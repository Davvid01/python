import art

print(art.logo)

""" def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"Welcome to {location}.")

greet_with(name="Alice", location="Wonderland")


def calculate_love_score(name1,name2):
    merged=name1+name2
    slowo="True"
    placeholder=0
    placeholder_love=0
    for x in merged.lower():
        if x in slowo.lower():
            placeholder+=1
        if x in "love":
            placeholder_love+=1
    print(f"Love score for {name1} and {name2}: {placeholder}{placeholder_love}")

calculate_love_score("Kanye West", "Kim Kardashian") """

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(text, shift):
    shifted_text = ""
    for letter in text:
        pozycja = alphabet.index(letter)       
        print(f"Current position: {pozycja}")

        shifted_position = pozycja + shift
        shifted_position %= len(alphabet) # 0-25 modulo powoduje liczenie indeksu od początku
        shifted_text += alphabet[shifted_position]
    print(f"Encrypted message: {shifted_text}")
#encrypt(text, shift)



def decrypt(text, shift,encode_or_decode):
    shifted_text = ""

    for letter in text:
        pozycja = alphabet.index(letter)       
        print(f"Current position: {pozycja}")

        shifted_position = pozycja - shift
        shifted_position %= len(alphabet) # 0-25 modulo powoduje liczenie indeksu od początku
        shifted_text += alphabet[shifted_position]
    print(f"Dencrypted message: {shifted_text}")
#decrypt(text, shift,direction)


#uprościć kod tylko do jednej funckji (matematycznie z ifem)
def caesar(slowo,przesuniecie,kierunek):
    if kierunek == "encode":
        encrypt(slowo,przesuniecie)
    elif kierunek == "decode":
        decrypt(slowo,przesuniecie)

#caesar(przesuniecie=shift, kierunek=direction,slowo=text)



def caesar_2(slowo, przesuniecie,encode_or_decode):
    shifted_text = ""

    if encode_or_decode =="decode":
        przesuniecie *= -1

    for letter in slowo:
        pozycja = alphabet.index(letter)   

        if letter not in alphabet:
            shifted_text+= letter #litera nie z alfabetu jest pominieta i dodana do outputu
        else:
            
            print(f"Current position: {pozycja}")

            shifted_position = pozycja + przesuniecie
            shifted_position %= len(alphabet) # 0-25 modulo powoduje liczenie indeksu od początku
            shifted_text += alphabet[shifted_position]
    print(f"Dencrypted message: {shifted_text}")



should_continue = 'Yes'

while should_continue.lower() == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_2(encode_or_decode=direction, przesuniecie=shift,slowo=text)

    should_continue= input("Type 'yes' if you want to go again. Otherwise, type 'no'")