import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    deck=[]
    computer_deck=[]
    round=0
    stand = 'y'
    while stand == 'y':
        stand=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
        if stand == 'y':
            if round == 0:
                deck = random.choices(cards,k=2)
                computer_deck = random.choices(cards,k=2)
                round+=1
                print(f"Your card {deck}")
                print(f"Computer's card {computer_deck[0]}")
            else:
                deck.append(random.choice(cards))
                computer_deck.append(random.choice(cards))
                print(f"Your card {deck}")
        elif stand=='n':
            final_score=sum(deck)
            final_score_computer=sum(computer_deck)

            print(f"YOur final hand: {deck} " + f"final score: {final_score}" )
            print(f"YOur final hand: {computer_deck} " + f"final score: {final_score_computer}" )
blackjack()