import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return f"Computer played {computer}, it's a tie"
    elif (is_win(user, computer)):
        return f"Computer played {computer}, You won"

    return f"Computer played {computer}, Computer won"


def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')):
        return True


print(play())
