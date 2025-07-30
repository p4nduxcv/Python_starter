from tkinter import *

window = Tk()
window.title("Starter")
window.minsize(500,300)

#Label
my_label = Label(text="Im the Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

# Entry (Label or Input)
input = Entry()
input.pack()

#Button
def button_clicked():
    # print("Clicked")
    # my_label.config(text="Clicked")
    my_label.config(text=input.get())

button = Button(text="Tab", command=button_clicked)
button.pack()









mainloop()

