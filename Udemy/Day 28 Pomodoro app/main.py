from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MINUTE_SECONDS = 60
set = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global set
    global timer
    global checkmarks

    set = 0
    window.after_cancel(timer)
    checkmarks = ""
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text=checkmarks)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_count():
    global set
    global checkmarks
    set += 1

    if set % 8 == 0:
        countdown(LONG_BREAK_MIN * MINUTE_SECONDS)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
    elif set % 2 == 0:
        countdown(SHORT_BREAK_MIN * MINUTE_SECONDS)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
    else:
        countdown(WORK_MIN * MINUTE_SECONDS)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
        checkmarks += "✔"
        
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    min = count // 60
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if count >= 0:
        timer = window.after(1000, countdown, count-1)
        canvas.itemconfig(timer_text, text=f"{min}:{seconds}")

    else:
        checkmark_label.config(text=checkmarks)
        timer_count()
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\alazarix\Files\Day-27\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 125, text="00:00", font=(FONT_NAME, 20, "bold"), fill="black")
canvas.grid(row=2, column=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=timer_count)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row=3, column=2)

checkmarks = ""
checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)


window.mainloop()
