
import random
from hangman_words import word_list

random.shuffle(word_list)
word = word_list[0].lower()
print(word)
placeholder = ""
isGameOver = False
display = ["_"] * len(word)
lives = 6

print("".join(display))

while not isGameOver:
    print(f"You have {lives} lives left.")
    guessed_letter = input("Guess a letter: ").lower()
    for index, letter in enumerate(word):
        if letter == guessed_letter:
            display[index] = letter

    print("".join(display))

    if "_" not in display:
        print("You win!")
        isGameOver = True

    lives -= 1

    if lives == 0 and "_" in display:
        print("You lose!")
        isGameOver = True


