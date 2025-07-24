numbers = [1,2,3,5]
name = "Pandula"

new_numbers = [number+1 for number in numbers]
new_name_letter_list = [l for l in name]

new_range = [n*2 for n in range(1,5)]

names = ["Pandu", "Shaki", "Monohara", "Mandawala", "test", "ArR"]

short_name = [name.capitalize() for name in names if len(name) > 5]

print(short_name)