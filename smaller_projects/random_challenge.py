import random


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x}: '))

        if guess_number < random_number:
            print("Sorry, guess again. Too low")
        elif guess_number > random_number:
            print("Sorry, guess again Too high")

    return f"Congrats you guessed the number {x} correctly."


# print(guess(10))


def computer_guess(x):
    low = 1
    high = x
    feedback = " "

    while feedback != 'c':

        if low != high:
            guess_number = random.randint(low, high)
        else:
            guess_number = low

        feedback = input(
            f"is {guess_number} too high (H) too low (L), or correct (C)???: ").lower()

        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number + 1

    return f"Computer guessed your number, {guess_number} correctly"


print(computer_guess(10))
