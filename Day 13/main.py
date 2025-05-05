enamies = 1

def increase_enamies(enamies):
    print(f"Enamies Inside Function: {enamies}")
    return enamies + 1

enamies = increase_enamies(enamies)
print(f"Enamies Outside Function: {enamies}")

