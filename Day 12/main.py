from art import logo
import random

EASY_LEVEL_GUESSES = 10
HARD_LEVEL_GUESSES = 5



def game():
    print(logo)
    random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()


    if difficulty == "easy":
        print(random_number)
        print(f"You have {EASY_LEVEL_GUESSES} attempts remaining to guess the number.")






game()
