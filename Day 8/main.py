def calculate_love_score(name1, name2):
    true_total = 0
    love_total = 0

    combined_name = (name1 + name2).upper()

    true_total =  sum(combined_name.count(letter) for letter in "TRUE")
    love_total = sum(combined_name.count(letter) for letter in "LOVE")


calculate_love_score("Asife", "Biriyani")