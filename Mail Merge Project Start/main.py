import re
import os

with open("Input/Letters/starting_letter.txt") as starting_letter:
    contents = starting_letter.read()
    match = re.search(r'\[(.*?)\]', contents)

with open("Input/Names/invited_names.txt") as invited_names:
    # contents = invited_names.readline()
    names = []
    for line in invited_names:
        cleaned_line = line.strip()
        names.append(cleaned_line)

output_dir = "Output/ReadyToSend"
os.makedirs(output_dir, exist_ok=True)

for name in names:
    # For each name, replace the placeholder in the original letter content
    personalized_letter = contents.replace("[name]", name)

    # Create a new file path for the personalized letter
    file_path = os.path.join(output_dir, f"letter_for_{name}.txt")

    # Write the new letter content to the new file
    with open(file_path, "w") as new_letter:
        new_letter.write(personalized_letter)

print("Successfully generated all letters!")