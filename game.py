from tkinter import *
#from tkinter.ttk import Radiobutton
from threading import Thread
from random import *
from time import sleep
window = Tk()
window.geometry("450x400")

up = PhotoImage(file="up.png")
die = PhotoImage(file="die.png")
down = PhotoImage(file="down.png")
check = PhotoImage(file="check.png")

#States
started = False
tries = 0
curnum = 0

curhex = '#00FF00'
window.title("GTN")
title = Label(window, text="GTN - Guess The Number", font='Arial 20')
instructions = Label(window, text="Choose the game's difficulty and click Randomize to start the game.\n You can click Randomize again to restart the game.", font='Arial 9')
status = Label(window, image=up)
randbnt = Button(window, text="Randomize", command=lambda : game())
exitbtn = Button(window, text="Exit", command=exit)
textbox1 = Entry(window, width=20)
textbox1["state"] = DISABLED
trieslbl = Label(window, text="Tries: 0")
rb1 = StringVar()
thinklbl = Label(window, text='')
rb1.set('100')
dif1 = Radiobutton(window, text="Ez (0-50)", var=rb1, value='50', selectcolor='red' )
dif2 = Radiobutton(window, text="Normal (0-100)", var=rb1, value='100',selectcolor='red' )
dif3 = Radiobutton(window, text="Hard (0-150)", var=rb1, value='150',selectcolor='red' )
choose = Label(window, text="Choose difficulty: ")
#status = Label(window, text="   Idle", font='Arial 20')
status = Label(window, image=die)
trieslbl.configure(foreground=curhex)  
thinklbl.grid(column=0, row=8)
def game():
    global started, curnum, rb1, trieslbl, tries, status, die, thinkan
    status.config(image=die)
    if started:
        thinkan()
        curnum = randint(0, int(rb1.get()))
        tries = 0
        trieslbl.config(text="Tries: " + str(tries))
    else:
        thinkan()
        started = True
        textbox1.config(state='normal')
def clear():
    global textbox1
    textbox1.delete(0, END)
def thinkan():
    global thinklbl, sleep
    thinklbl.configure(text=".")
    thinklbl.update()
    sleep(0.50)
    thinklbl.configure(text="..")
    thinklbl.update()
    sleep(0.50)
    thinklbl.configure(text="...")
    thinklbl.update()
    sleep(0.50)
    thinklbl.configure(text="")
    thinklbl.update()
def answer(ans : str):
    global started, curnum, tries, status, up, check, down, trieslbl, textbox1, randbnt, dif1, dif2, dif3, curhex
    if (not int(textbox1.get()) > 150) and (not int(textbox1.get()) < 0):
        if int(textbox1.get()) != curnum:
            tries += 1
            trieslbl.config(text="Tries: " + str(tries))
            if int(textbox1.get()) > curnum:
                status.config(image=down)
            else:
                status.config(image=up)
            clear()
            if tries < 3:
                trieslbl.configure(foreground=curhex)     
            elif (tries > 2) and (tries < 7):
                trieslbl.configure(foreground='yellow')
            else:
                trieslbl.configure(foreground='red')
        else:
            clear()
            status.config(image=check)
            textbox1.config(state='disabled')
            started = False
title.grid(column=0, row=0, columnspan=4)
instructions.grid(column=0, row=1, columnspan=4)
choose.grid(column=0, row=2)
dif1.grid(column=1, row=2)
dif2.grid(column=2, row=2)
dif3.grid(column=3, row=2)
textbox1.grid(column=0, row=3, columnspan=4)
status.place(x=250, y=120)
randbnt.grid(column=0, row=4)
exitbtn.grid(column=0, row=5)
trieslbl.grid(column=1, row=5)
window.bind("<Return>", lambda a: answer(""))
window.mainloop()