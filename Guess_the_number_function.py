import random


def user_number() -> int:
    """Get numbers from player between 1 and 100

    :rtype: int
    :return chosen number by player as int :
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")
    return result


def guess_the_number():
    """Main function of game"""
    random_number = random.randint(1, 100)
    player_number = user_number()
    while player_number != random_number:
        if player_number < random_number:
            print("To small!")
        else:
            print("To big!")
        player_number = user_number()
    print("You Win!")


if __name__ == '__main__':
    guess_the_number()
