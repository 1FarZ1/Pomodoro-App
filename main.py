from customtkinter import *
from tkinter import *
from time import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
checks=""
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pressed():
    global reps
    if reps % 8==0:
        count_down(1)
        Timer.config(text="Break",fg=RED)
    elif reps % 2==1:
        count_down(2)
        Timer.config(text="Work",fg=PINK)
    else :
        count_down(3)
        Timer.config(text="Break",fg=RED)
def reset_pressed():
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text="00:00")
    Timer.config(text="Timer",fg=GREEN)
    check.config(text="")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(n):
    global reps
    global checks
    mins=int(n/60)
    sec= n %60
    if sec < 10:
        sec= "0"+str(sec)
    canvas.itemconfig(time_text,text=f"{mins}:{sec}")
    if n >0:
        window.after(1000,count_down,n-1)
    else:
        reps=reps+1
        if reps % 2==0:
            checks+="x"
            check.config(text=checks)
        start_pressed()
# ---------------------------- UI SETUP ------------------------------- #
# set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue" 
window=Tk()
window.config(bg=YELLOW,padx=100,pady=50)
window.title("Pomodoro_app")


Timer=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
Timer.grid(column=1,row=0)
canvas= Canvas(width=200, height=224,highlightthickness=0,bg=YELLOW)
img=PhotoImage(file="Day28/tomato.png")
canvas.create_image(100,112,image=img)
time_text=canvas.create_text(100,130,text="25:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)
start=CTkButton(text="Start",command=start_pressed,text_color="black",fg_color=GREEN,hover_color=RED)
start.grid(column=0,row=2)
reset=CTkButton(text="reset",command=reset_pressed,fg_color=GREEN,text_color="black",hover_color=RED)
reset.grid(column=2,row=2)
check=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check.grid(column=1,row=3)
window.mainloop()