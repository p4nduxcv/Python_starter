from tkinter import *
import pandas

def save_password():
    """Gets data from input fields and saves it to a CSV file."""
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # Don't save if any field is empty
    if not website or not email or not password:
        print("Please fill in all fields.")
        return

    # Create a dictionary for the new entry.
    # The keys will be the column headers.
    new_data = {
        'Website': [website],
        'Email': [email],
        'Password': [password]
    }

    # Create a DataFrame from the new data.
    df = pandas.DataFrame(new_data)

    # Define the output file name
    csv_file_name = 'passwords.csv'

    # Check if the file already exists to decide whether to write the header
    # file_exists = isfile(csv_file_name)

    # Append the DataFrame to the CSV file.
    # mode='a' means append.
    # header=not file_exists writes the header only if the file is new.
    # index=False prevents writing the DataFrame index.
    df.to_csv(csv_file_name, mode='a', index=False)

    print(f"Password for '{website}' saved to {csv_file_name}.")

    # Clear the input fields after saving
    website_input.delete(0, END)
    password_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate")
generate_button.grid(row=3, column=2 )
add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)






window.mainloop()