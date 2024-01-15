import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(width=500, height=300)


#Label
label = tkinter.Label(text="LABEL", font=("arial", 24, "bold"))
label.pack(side="top")

label.pack()

label.config(text="New Text")
label["text"] = "New Text2"

def button_clicked():
    label["text"] = txt_box.get()
    
button = tkinter.Button(text="Click", command=button_clicked)
button.pack()


txt_box = tkinter.Entry()
txt_box.pack()

user_input = txt_box.get()










window.mainloop()