
import random
word_list = ["aardvark", "baboon", "camel"]
random.shuffle(word_list)
word = word_list[0].lower()
print(word)
placeholder = ""
isGameOver = False
display = ["_"] * len(word)

print("".join(display))

while not isGameOver:
    guessed_letter = input("Guess a letter: ").lower()
    for index, letter in enumerate(word):
        if letter == guessed_letter:
            display[index] = letter
    print("".join(display))

    if "_" not in display:
        print("You win!")
        isGameOver = True


