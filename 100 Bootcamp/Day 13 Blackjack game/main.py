import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"



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
                if sum(computer_deck) < 17:
                    computer_deck.append(random.choice(cards))
                print(f"Your card {deck}")
        elif stand=='n':
            final_score = calculate_score(deck)
            final_score_computer = calculate_score(computer_deck)

            print(f"YOur final hand: {deck} " + f"final score: {final_score}" )
            print(f"Computer's final hand: {computer_deck} " + f"computer's final score: {final_score_computer}" )

    print(compare(final_score,final_score_computer))
    #return {"player" : deck, "computer" : computer_deck}
print(blackjack())


while input("Do you want to play a new game? 'y' or 'no'") == "y":
    print("\n" * 20)
    blackjack()

#print(compare())