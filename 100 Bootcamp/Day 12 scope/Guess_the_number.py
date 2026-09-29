import random 

def difficulty():
    chosen_difficulty = input("Choose a difficulty. Type 'easy or 'hard'")
    if chosen_difficulty == 'easy':
        return int(10)
    elif chosen_difficulty == 'hard':
        return int(5)



def random_number():
    number = random.randrange(1,100)
    return number


def check_guess(random_number, chosen_number):
    if chosen_number > random_number:
        print("Too high")
        return False
    elif chosen_number < random_number:
        print("Too low")
        return False
    elif chosen_number == random_number:
        print("Its correct!")
        return True

def game_guess_number():
    chosen_diffi = difficulty()
    correct_answer = False
    losowa_liczba=random_number()
    print(losowa_liczba)
    while chosen_diffi > 0 and correct_answer is False:
        pick_number = int(input("Make a guess: "))
        correct_answer = check_guess(losowa_liczba,pick_number)
        chosen_diffi -=1


print(game_guess_number())