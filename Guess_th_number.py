import random

random_number = random.randint(1, 100)
user_number = 0
while user_number != random_number:
    try:
        user_number = int(input("Guess the number: "))
    except ValueError:
        print("It's not a number!")
        continue
    if user_number < random_number:
        result = "To small!"
    elif user_number > random_number:
        result = "To big!"
    else:
        result = "You win!"
    print(result)
