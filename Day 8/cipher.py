from collections import deque
import string

def get_rotated_alphabet(shift_amount):

    d = deque(alphabet)
    d.rotate(shift_amount)
    rotated_alphabet = list(d)
    return rotated_alphabet