def add (a, b):
    return a + b
def subtract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    return a / b

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

is_deal_final_value = True

while is_deal_final_value:
    value_1 = int(input("Enter first number: "))
    value_2 = int(input("Enter second number: "))
    operation = input("Enter operation: + - * / ")
    final_value = operations_dict[operation](value_1,value_2)
    print(final_value)

    is_deal_final_value = bool(input("Enter a boolean value (True or False): "))

    if is_deal_final_value:
        value_2 = int(input("Enter second number: "))
        operation = input("Enter operation: + - * / ")
        final_value = operations_dict[operation](final_value, value_2)
        print(final_value)
        is_deal_final_value = bool(input("Enter a boolean value (True or False): "))
    else:
        is_deal_final_value = False

