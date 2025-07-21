# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()

average_temp = sum(temp_list) / len(temp_list)

# print(average_temp)

# print(data["temp"].max())

# print(data[data.day == "Monday"])

highest_temp = data.temp.max()
highest_temp_day = data[data.temp == highest_temp].day.values[0]



print(f"Highest Temp is on {highest_temp_day}")

