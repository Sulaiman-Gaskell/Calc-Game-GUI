import random
import sys
import time
import tkinter as tk
from subprocess import call
from tkinter import *
from tkinter import ttk



def on_closing():
    sys.exit()

root = tk.Tk()
root.title('Calc_game 2')
root.resizable(False, False)
root.configure(bg = 'black')
root.attributes('-fullscreen', True)
var = tk.IntVar()
root.protocol("WM_DELETE_WINDOW", on_closing)

while True:
    #Difficulty selector

    def dS(d):
        var.set(1)
        global difficulty
        if d == 1:
            difficulty = 1
        elif d == 2:
            difficulty = 2
        elif d == 3:
            difficulty = 3
        

    dBanner = Label(
        root,
        text='Choose a difficulty:',
        bg='black',
        fg='white',
        font = ('Helvetica bold',int(root.winfo_screenwidth() / 32)),
        width = int(root.winfo_screenwidth() / 74),
    )
    dBanner.grid(column=0,row=0)

    easy = tk.Button(
        root,
        text = 'Easy',
        bg = 'black',
        fg = 'green',
        activebackground = 'black',
        activeforeground = 'green',
        font = ('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        width = int(root.winfo_screenwidth() / 74),
        command = lambda: dS(1),
        cursor= 'hand2',  
    )
    easy.grid(column=0, row=1 ,pady=(root.winfo_screenheight() / 30, 0))


    medium = tk.Button(
        root,
        text = 'Medium',
        bg = 'black',
        fg = 'yellow',
        activebackground = 'black',
        activeforeground = 'yellow',
        font = ('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command = lambda: dS(2),
        width = int(root.winfo_screenwidth() / 74),
        cursor= 'hand2',
    )
    medium.grid(column=0, row=2,pady=(root.winfo_screenheight() / 70, 0))

    hard = tk.Button(
        root,
        text = 'Hard',
        bg = 'black',
        fg = 'red',
        activebackground = 'black',
        activeforeground = 'red',
        font = ('Helvetica bold',int(root.winfo_screenwidth() / 16)),
        command = lambda: dS(3),
        width = int(root.winfo_screenwidth() / 74),
        cursor= 'hand2',
    )
    hard.grid(column=0, row=3,pady=(root.winfo_screenheight() / 70, 0))


    easy.wait_variable(var)
    easy.destroy()
    medium.destroy()
    hard.destroy()
    dBanner.destroy()


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
    while pBCount < 5: ##################
        if difficulty == 1:
            num1 = random.randint(25,100)
            num2 = random.randint(2,25)
        elif difficulty == 2:
            num1 = random.randint(25, 150)
            num2 = random.randint(-25, 25)
        elif difficulty == 3:
            num1 = random.randint(-50, 150)
            num2 = random.randint(-100, -50)
            

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

        question.place(x=root.winfo_screenwidth() / 3.072, y=root.winfo_screenheight() / 5.76)
        gameNum +=1




        root.update()
        d.wait_variable(var)
        question.configure(text='')

    break
    

root.destroy()
root = tk.Tk()
root.title('Calc_game 2')
root.resizable(False, False)
root.configure(bg = 'black')
root.attributes('-fullscreen', True)
var = tk.IntVar()
root.protocol("WM_DELETE_WINDOW", on_closing)

finishTxt = tk.Label(
    root,
    text = 'Well done you completed this difficulty!',
    bg = 'black',
    fg = 'green',
    font = ('Helvetica bold',int(root.winfo_screenwidth() / 32)),

).pack()


def com(wC):
    root.destroy()
    if wC == 1:
        call(['python', 'CalcGame.py'])
        sys.exit()
    elif wC == 2:
        call(['python', 'launcher.py'])
        sys.exit()

pA = tk.Button(
    root,
    text = 'Play again',
    bg = 'black',
    fg = 'white',
    font = ('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    activebackground = 'black',
    activeforeground = 'white',
    cursor= 'hand2',
    command = lambda: com(1),

).pack(pady = (200,0))

RtL = tk.Button(
    root,
    text = 'Exit',
    bg = 'black',
    fg = 'white',
    font = ('Helvetica bold',int(root.winfo_screenwidth() / 32)),
    activebackground = 'black',
    activeforeground = 'white',
    cursor= 'hand2',
    width = 9,
    command = lambda: com(2),
).pack()


root.mainloop()





    





