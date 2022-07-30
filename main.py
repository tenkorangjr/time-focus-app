from tkinter import *
import time
from math import floor
import sys


sys.setrecursionlimit(100000)  # avoid recursion error

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
counter = True


def reset():
    """Resetting edited global variable and the Tk screen"""
    global counter, rep
    counter = False

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    rep = 0


def start():
    """Starting the timer from WORK"""
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 2 == 0:
        timer_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    elif rep % 8 == 0:
        timer_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


def count_down(count):
    """Does the countdown for the Pomodoro App"""
    global counter  # Since we'll be editing the global mark and counter
    count_min = floor(count/60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    # Show the minutes and seconds on the screen
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 and counter:  # to check whether counter is True
        window.update()  # Update the screen
        time.sleep(1)
        window.after(func=count_down(count - 1), ms=1)
    elif counter:  # Only counter is True and count is equal to 0
        mark = ""
        work_sessions = floor(rep/2)
        for _ in range(work_sessions):
            mark += '✔'
        check_mark.config(text=mark)
        start()
    else:
        #  To set the timer to 00.00 right after exiting the .after() method
        reset()
        counter = True


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Focus App")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bg=YELLOW, bd=-1, command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, bg=YELLOW, bd=-1, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
