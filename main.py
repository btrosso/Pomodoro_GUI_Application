from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#00B4D8"
RED = "#FF1700"
GREEN = "#06FF00"
ORANGE = "#FF8E00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", bg="black", fg=BLUE)
    check_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=ORANGE)
        count_down(short_break_sec)
    else:
        timer_label.config(text="WORK!", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg="black")

canvas = Canvas(width=500, height=340, bg="black", highlightthickness=0)
img = PhotoImage(file="kick_ass.png")
canvas.create_image(250, 170, image=img)
timer_text = canvas.create_text(100, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# label
timer_label = Label()
timer_label.config(text="TIMER", bg="black", fg=BLUE, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

check_label = Label()
check_label.config(bg="black", fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=2)

# buttons
start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()
