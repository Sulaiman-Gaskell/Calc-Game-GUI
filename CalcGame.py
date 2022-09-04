import random
import sys
import time
import tkinter as tk
from subprocess import call
from tkinter import *
from tkinter import ttk

# Welcome menu
welcome = tk.Tk()
welcome.title('Calc_Game launcher')
welcome.geometry('600x400+50+50')
welcome.resizable(False, False)
welcome.configure(bg='black')


label = ttk.Label(welcome,text='V1.0.2', foreground='white',background='black').pack()
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

# Count down
root = tk.Tk()
root.title('Calc_game')
root.geometry('600x400+50+50')
root.resizable(False, False)
root.configure(bg = 'black')
root.attributes('-fullscreen', True)
var = tk.IntVar()

counter = Label(
    root,
    bg = 'black',
    fg = 'white',
    font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
)


counter.place(relx=.5, rely=.5,anchor= CENTER)


count = 3
while True:
    counter.configure(text=count)
    count -= 1
    if count > 0:
        root.update()
        time.sleep(1)
    else:
        break

root.update()
time.sleep(1)
counter.configure(text='Go!')
root.update()
time.sleep(1)
counter.destroy()

#Main game
gameNum = 1
while gameNum < 6:
    num1 = random.randint(2,100)
    num2 = random.randint(2,10)

    operation = random.randint(1,4)
    if operation == 1:
        answer = num1 + num2
    elif operation == 2:
        answer = num1 - num2
    elif operation == 3:
        answer = num1 * num2
    elif operation == 4:
        answer = round(num1 / num2)


    oCorrect = tk.Label(
        root,
        text = '',
        fg = 'white',
        bg = 'black',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    )
    oCorrect.place(x=0,y=0)

    #Info labels
    gameNumO = tk.Label(
        root,
        text = str(gameNum)+'/5',
        bg='black',
        fg='white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    )
    gameNumO.place(x=root.winfo_screenwidth() / 1.097,y=0)

    #quick design line
    colour ="#"+("%06x"%random.randint(0,16777215))
    line =Frame(root, bg=colour, height=root.winfo_screenheight() / 172.8,width=root.winfo_screenwidth() / 0.9)
    line.place(y=root.winfo_screenheight() /5.959 )


    #question label
    question = tk.Label( 
        root,
        text = str(num1) + '    _______    ' + str(num2) + ' = ' + str(answer),
        bg = 'black',
        fg = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    )
    question.place(x=root.winfo_screenwidth() / 3.072, y=root.winfo_screenheight() / 5.76)

#######################################################
    def choice(pOperation):
        var.set(1)
        global isCorrect
        
        if pOperation == operation:
            isCorrect = 'Correct!'
            oCorrect.configure(fg = 'green')
        else:
            isCorrect = 'Incorrect'
            oCorrect.configure(fg = 'red')
            #ouput

        oCorrect.configure(text=isCorrect)
        root.update()
        time.sleep(2)
        oCorrect.configure(text=' ')

    #addition button
    a = tk.Button(
        root,
        text = '  Addition   ',
        bg = 'black',
        fg = 'green',
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(1),
        cursor= 'hand2',
    )
    a.grid(column=0, row=0, sticky=tk.E, padx=0,pady=(0.395*root.winfo_screenheight(),0))


    #subtraction button
    s = tk.Button(
        root,
        text = 'Subtraction',
        bg = 'black',
        fg = 'blue',
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(2),
        cursor= 'hand2',
    )
    s.grid(column=1, row=0,sticky=W, padx=0,pady=(0.395*root.winfo_screenheight(),0))

    #Multiply button
    m = tk.Button(
        root,
        text = '   Multiply   ',
        bg = 'black',
        fg = 'yellow',
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(3),
        cursor= 'hand2',  
    )
    m.grid(column=0, row=1, sticky=tk.E, padx=0,pady=0)

    #division button
    d = tk.Button(
        root,
        text = '   Division  ',
        bg = 'black',
        fg = 'purple',
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(4),
        cursor= 'hand2',
    )
    d.grid(column=1, row=1,sticky=W, padx=0,pady=0)
    gameNum +=1
    root.update()
    d.wait_variable(var)
    
    question.configure(text='')


root.destroy()    
call(['python', 'CalcGame.py'])
sys.exit()


    





