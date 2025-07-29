# numbers = [1,2,3,5]
# name = "Pandula"
#
# new_numbers = [number+1 for number in numbers]
# new_name_letter_list = [l for l in name]
#
# new_range = [n*2 for n in range(1,5)]
#
# names = ["Pandu", "Shaki", "Monohara", "Mandawala", "test", "ArR"]
#
# short_name = [name.capitalize() for name in names if len(name) > 5]
#
# print(short_name)



# Dictionary Comprehension
import random
names = ["Alex", "Morrison", "Carlos", "Kyle", "kopr"]

student_score = {name:random.randint(1,100) for name in names}
print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score > 60}

print(passed_students)

#Coding test 2

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temperature * (9/5)) + 32 for (day, temperature) in weather_c.items()}


print(weather_f)