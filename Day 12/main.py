from art import logo
import random

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5


def set_difficulty(difficulty):
    if difficulty == "easy":
        return EASY_LEVEL_GUESSES
    else:
        return HARD_LEVEL_GUESSES


def game():
    print(logo)
    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    turns = set_difficulty(difficulty)

    print(turns)

    while turns > 0:
        guessed_number = int(input(f"Guess a number between 1 and 100. You have {turns} attempts left: "))
        if guessed_number == random_number:
            print("You win!")
            break
        elif guessed_number > random_number:
            print("Too high.")
            turns -= 1
        elif guessed_number < random_number:
            print("Too low.")
            turns -= 1

        if turns == 0:
            print("You have out of attempts. You lose.")
            return





game()
