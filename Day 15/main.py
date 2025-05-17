from data import MENU, resources
is_machine_on = True

profit = 0

def price_calculator():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return round(total,2)

def is_enough_resources(coffe_type):
    ingredients = MENU[coffe_type]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item):
            print(f"Sorry, not enough {item}")
            return False
    return True


def is_enough_price(coffe_type):
    inserted_coin_v = price_calculator()
    if inserted_coin_v < MENU[coffe_type]["cost"]:
        print(f"Sorry, You have only $ {inserted_coin_v} || {coffe_type} is {MENU[coffe_type]["cost"]}")
        return False
    print(f"Your Change - {inserted_coin_v - MENU[coffe_type]["cost"]}")
    return True

def report():
    for item, amount in resources.items():
        print(f"{item.capitalize()} - {amount}")
    print(f"Profit - {profit}")

def make_coffee(coffee_type):
    ingredients = MENU[coffee_type]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    global profit
    profit += MENU[coffee_type]["cost"]


while is_machine_on:
    choice = input("What type of coffee do you want? (espresso/latte/cappuccino):")
    if choice == "off":
        is_machine_on = False
        break
    elif choice == "report":
        report()
    elif choice in MENU:
        if is_enough_resources(choice) and is_enough_price(choice):
            make_coffee(choice)
            print(f"Here is your {choice} ☕. Enjoy!")
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
