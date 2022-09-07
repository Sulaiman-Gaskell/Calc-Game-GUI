import random
import sys
import time
import tkinter as tk
from subprocess import call
from tkinter import *
from tkinter import ttk

# Welcome menu
welcome = Tk()
welcome.title('Calc_Game 2 launcher')
welcome.configure(bg='black')
width, height = welcome.winfo_screenwidth(), welcome.winfo_screenheight()
welcome.geometry('600x400')

def on_closing():
    sys.exit()

welcome.protocol("WM_DELETE_WINDOW", on_closing)

label = ttk.Label(welcome,text='V1.2.0', foreground='white',background='black').pack()
button = tk.Button(
    welcome,
    text='''Welcome to the Calculator game!
Click anywhere to play''',
    font = ('Helvetica bold',26),
    width=200,
    height=90,
    bg='black',
    fg='blue',
    activebackground='black',
    activeforeground='white',
    command= lambda: welcome.destroy(), 
).pack()

welcome.mainloop()
call(['python', 'CalcGame.py'])
sys.exit()