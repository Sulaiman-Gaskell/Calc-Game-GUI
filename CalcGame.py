import random
import sys
import time
import tkinter as tk
from subprocess import call
from tkinter import *
from tkinter import ttk
from turtle import width

# Welcome menu
welcome = Tk()
welcome.title('Calc_Game 2 launcher')
welcome.configure(bg='black')
width, height = welcome.winfo_screenwidth(), welcome.winfo_screenheight()
welcome.geometry('600x400')

def on_closing():
    sys.exit()

welcome.protocol("WM_DELETE_WINDOW", on_closing)

label = ttk.Label(welcome,text='V1.1.0', foreground='white',background='black').pack()
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
root.title('Calc_game 2')
root.resizable(False, False)
root.configure(bg = 'black')
root.attributes('-fullscreen', True)
var = tk.IntVar()
root.protocol("WM_DELETE_WINDOW", on_closing)

#line design
width = root.winfo_screenwidth() / 1000
line =Frame(root, bg='white', height=root.winfo_screenheight() / 172.8,width=width)
line.place(y=root.winfo_screenheight() /5.959 )
root.update()
time.sleep(0.1)

while width < root.winfo_screenwidth():
    width += 15
    line =Frame(root, bg='white', height=root.winfo_screenheight() / 172.8,width=width)
    line.place(y=root.winfo_screenheight() /5.959 )
    root.update()
    time.sleep(0.000001)

pB = Frame(root,  bg='white', height=root.winfo_screenheight() / 172.8,width=root.winfo_screenwidth() / 5)
pBCount = 0

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
while pBCount < 5:
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
        text = 'Question ' + str(gameNum),
        bg='black',
        fg='white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    )
    gameNumO.place(x=root.winfo_screenwidth() / 1.375,y=0)
    



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
        global pBCount
        if pOperation == operation:
            pBCount += 1
            isCorrect = 'Correct!'
            oCorrect.configure(fg = 'green')
            pB.configure(bg='green')
            pB.configure(width=root.winfo_screenwidth() / 5 * pBCount)
            pB.place(y=root.winfo_screenheight() /5.959)
        else:
            isCorrect = 'Incorrect'
            oCorrect.configure(fg = 'red')
            #ouput

        a.configure(state=DISABLED)
        s.configure(state=DISABLED)
        m.configure(state=DISABLED)
        d.configure(state=DISABLED)
        oCorrect.configure(text=isCorrect)
        root.update()
        time.sleep(1.5)
        oCorrect.configure(text=' ')

    #addition button
    a = tk.Button(
        root,
        text = 'Addition',
        bg = 'black',
        fg = 'green',
        width=10,
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(1),
        cursor= 'hand2',
        state=DISABLED
    )
    root.update()
    time.sleep(0.2)
    a.grid(column=0, row=0, sticky=tk.E, padx=0,pady=(0.395*root.winfo_screenheight(),0))
    root.update()
    time.sleep(0.1)


    #subtraction button
    s = tk.Button(
        root,
        text = 'Subtraction',
        bg = 'black',
        fg = 'blue',
        width=10,
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(2),
        cursor= 'hand2',
        state=DISABLED
    )
    s.grid(column=1, row=0,sticky=W, padx=0,pady=(0.395*root.winfo_screenheight(),0))
    root.update()
    time.sleep(0.1)

    #Multiply button
    m = tk.Button(
        root,
        text = 'Multiply',
        bg = 'black',
        fg = 'yellow',
        width=10,
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(3),
        cursor= 'hand2',
        state=DISABLED  
    )
    m.grid(column=0, row=1, sticky=tk.E, padx=0,pady=0)
    root.update()
    time.sleep(0.1)

    #division button
    d = tk.Button(
        root,
        text = 'Division',
        bg = 'black',
        fg = 'purple',
        width=10,
        activebackground = 'black',
        activeforeground = 'white',
        font=('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command=lambda: choice(4),
        cursor= 'hand2',
        state=DISABLED
    )
    d.grid(column=1, row=1,sticky=W, padx=0,pady=0)
    a.configure(state=NORMAL)
    s.configure(state=NORMAL)
    m.configure(state=NORMAL)
    d.configure(state=NORMAL)
    root.update()
    time.sleep(0.2)

    gameNum +=1




    root.update()
    d.wait_variable(var)
    question.configure(text='')


root.destroy()    
call(['python', 'CalcGame.py'])
sys.exit()


    





