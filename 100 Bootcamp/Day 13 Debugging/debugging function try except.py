# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got this")

# my_function()

# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5)
# print(dice_images[dice_num])


# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You typed invalid number. Please try again with a numerical")
    age = int(input("How old are you"))


if age > 18:
        print(f"You can drive at age {age}.")