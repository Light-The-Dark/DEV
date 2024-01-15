from tkinter import *

def convert_miles():
    convert = input.get()
    converted_label.config(text=float(convert) * 1.60934)


window = Tk()
window.title("Miles/KM")
window.minsize(height=100, width=190)

miles = Label(text="Miles")
miles.grid(row=0, column=1)

input = Entry(width=10)
input.grid(row=1, column=1)

kilometers = Label(text="Kilometers")
kilometers.grid(row=2, column=1)

button = Button(text="Convert",command=convert_miles)

button.grid(row=1, column=0)
button.config()

converted_label = Label()
converted_label.grid(row=1,column=2)





window.mainloop()

