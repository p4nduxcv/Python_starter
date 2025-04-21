
import random
word_list = ["aardvark", "baboon", "camel"]

random.shuffle(word_list)
word = word_list[0].lower()
print(word)
placeholder = ""
display = ""

for letter in range(1, len(word) + 1):
    placeholder += "_"
print(placeholder)

guessed_letter = input("Enter Letter: ")

for letter in word:
    if letter == guessed_letter:
        display += guessed_letter
    else:
        display += "_"
print(display)
