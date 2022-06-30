from tkinter import *
from tkinter import ttk
import time
me = Tk()
me.geometry("500x470")
me.title("CALCULATOR")
me.iconbitmap('calc.ico')
me.config(background='#999', cursor='plus')
melabel = Label(me, text="CALCULATOR", bg='#999', font=("Times", 30, 'bold'))
melabel.pack(side=TOP)
global readme
global today
today = time.strftime("%H:%M:%S   %d/%m/%Y")
readme = open("history.txt", "a")

global operator
textin = StringVar()
operator = ""

def clickbut(number):  # lambda:clickbut(1)
    global operator
    operator = operator + str(number)
    textin.set(operator)


def equlbut():
    global operator
    readme.write(operator)
    readme.write('\n')
    readme.write(today)
    readme.write('\n')
    add = str(eval(operator))
    textin.set(add)
    operator = ''


def equlbut():
    global operator
    readme.write(operator)
    readme.write('\n')
    readme.write(today)
    readme.write('\n')
    sub = str(eval(operator))
    textin.set(sub)
    operator = ''


def equlbut():
    global operator
    readme.write(operator)
    readme.write('\n')
    readme.write(today)
    readme.write('\n')
    mul = str(eval(operator))
    textin.set(mul)
    operator = ''


def equlbut():
    global operator
    readme.write(operator)
    readme.write('\n')
    readme.write(today)
    readme.write('\n')
    div = str(eval(operator))
    textin.set(div)
    operator = ''


def clrbut():
    global operator
    div = ''
    textin.set(div)
    operator = ''

def memoryplus():
    global operator
    global memory
    memory = operator




metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

but1 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
              font=("Courier New", 16, 'bold'))
but1.place(x=10, y=110)

but2 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
              font=("Courier New", 16, 'bold'))
but2.place(x=75, y=110)

but3 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
              font=("Courier New", 16, 'bold'))
but3.place(x=140, y=110)

but4 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
              font=("Courier New", 16, 'bold'))
but4.place(x=10, y=180)

but5 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
              font=("Courier New", 16, 'bold'))
but5.place(x=75, y=180)

but6 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
              font=("Courier New", 16, 'bold'))
but6.place(x=140, y=180)

but7 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=10, y=250)

but8 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
              font=("Courier New", 16, 'bold'))
but8.place(x=75, y=250)

but9 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
              font=("Courier New", 16, 'bold'))
but9.place(x=140, y=250)

but0 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
              font=("Courier New", 16, 'bold'))
but0.place(x=10, y=320)

butdot = Button(me, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                font=("Courier New", 16, 'bold'))
butdot.place(x=75, y=320)

butpl = Button(me, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
               font=("Courier New", 16, 'bold'))
butpl.place(x=205, y=110)

butsub = Button(me, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                font=("Courier New", 16, 'bold'))
butsub.place(x=205, y=180)

butml = Button(me, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
               font=("Courier New", 16, 'bold'))
butml.place(x=205, y=250)

butdiv = Button(me, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                font=("Courier New", 16, 'bold'))
butdiv.place(x=205, y=320)

butclear = Button(me, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=110)

butequal = Button(me, padx=151, pady=14, bd=4, bg='white', command=equlbut, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=390)

butpot = Button(me, padx=12, pady=13, bd=4, bg='white', text="aⁿ", command=lambda: clickbut("**"),
                font=("Times", 16, 'bold'))
butpot.place(x=346, y=390)

butsqrt = Button(me, padx=14, pady=14, bd=4, bg='white', text="√", command=lambda: clickbut("**0.5"),
                font=("Courier New", 16, 'bold'))
butsqrt.place(x=346, y=320)

butpi = Button(me, padx=14, pady=14, bd=4, bg='white', text="π", command=lambda: clickbut(3.141592),
                font=("Courier New", 16, 'bold'))
butpi.place(x=346, y=250)

butmemoryplus = Button(me, padx=8, pady=14, bd=4, bg='white', text="M+", command=memoryplus, font=("Courier New", 16, 'bold'))
butmemoryplus.place(x=346, y=110)

butmemoryuse = Button(me, padx=14, pady=14, bd=4, bg='white', text="M", command=lambda: clickbut(memory),
                font=("Courier New", 16, 'bold'))
butmemoryuse.place(x=346, y=180)


me.mainloop()