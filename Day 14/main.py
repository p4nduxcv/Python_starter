from art import logo, vs
from gamedata import data
import random

print (logo)
current_score = 0
game_should_continue = True


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f" {account_name}, a {account_desc}, from {account_country}"

def compare(guess, a_followers, b_followers):
    # Here return true or false
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A-: {format_data(account_a)}")
    print(vs)
    print(f"Against B-: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    account_a_fc = account_a["follower_count"]
    account_b_fc= account_b["follower_count"]

    is_correct = compare(guess, account_a_fc, account_b_fc)

    if is_correct:
        current_score += 1
        print(f"You're right! Current score: {current_score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {current_score}")





