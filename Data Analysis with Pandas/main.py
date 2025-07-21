import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_counts = data['Primary Fur Color'].value_counts()

# 3. Convert the Series to a DataFrame for saving
# reset_index() converts the Series index (the colors) into a column
color_counts_df = color_counts.reset_index()

# 4. Rename the columns for clarity
color_counts_df.columns = ['Fur Color', 'Count']

# 5. Save the new DataFrame to a CSV file
# We use index=False to avoid writing the new index (0, 1, 2...) to the file
color_counts_df.to_csv("squirrel_fur_color_counts.csv")

print("File 'squirrel_fur_color_counts.csv' has been created successfully!")





