import random
word_list = ["aardvark", "baboon", "camel"]
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
random_word = random.choice(word_list)
print(random_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#litera =  input("Podaj literę: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

sprawdzenie=0   
game_over = False
lista_pomocnicza=[]
lives=6
while not lives<=0:
    litera =  input("Podaj literę: ").lower()
    placeholder=""
    for x in random_word:
        if x==litera:
            sprawdzenie+=1
            placeholder+=litera  
            lista_pomocnicza.append(x)
        elif x in lista_pomocnicza:
            placeholder+=x
        else:
            placeholder+="_"
    print(placeholder) 


    if litera not in random_word:
        lives-=1
        if lives ==0:
            print("Game over")



    if  "_" not in placeholder:
        game_over = True

    print(stages[lives])

