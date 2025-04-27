import string
from collections import deque

direction = input("Encode or Decode?").lower()
text7 = input("Enter Your Message:").lower()
shift_amount = int(input("Enter Shift Amount:"))



def encrypt(original_text, shift_amount):
    original_text_array = list(original_text)
    alphabet = list(string.ascii_lowercase)
    d = deque(alphabet)
    d.rotate(shift_amount)
    rotated_alphabet = list(d)
    encrypted_text = ""

    for letter in original_text_array:
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_text += rotated_alphabet[index]
        else:
            # If not a letter (maybe a space, number, etc.), keep it as is
            encrypted_text += letter
    print(encrypted_text)

def decript(original_text, shift_amount):
    original_text_array = list(original_text)
    alphabet = list(string.ascii_lowercase)
    d = deque(alphabet)
    d.rotate(-shift_amount)
    rotated_alphabet = list(d)
    decrypted_text = ""

    for letter in original_text_array:
        if letter in alphabet:
            index = alphabet.index(letter)
            print(index)
            decrypted_text += rotated_alphabet[index]
        else:

            decrypted_text += letter
            print(decrypted_text)

    print(decrypted_text)

decript(text7, shift_amount)




