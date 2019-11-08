import tkinter as tk
from tkinter import*
import random
import sqlite3
from tkinter import messagebox
import pickle
import perceptron
from perceptron import Perceptron  # Import Foo into main_module's namespace explicitly
fw= Tk()
fw.title('User Data Form')
fw.geometry('1350x750+0+0')
fw.config(bg='brown')
background_imag = PhotoImage(file="form.png")
backgrounda = Label(fw, image=background_imag, bd=0)
backgrounda.pack()
embed=Frame(fw,width=600,height=400)
embed.place(x=8,y=200)
background_imag1 = PhotoImage(file="form1.png")
backgrounda1 = Label(embed, image=background_imag1, bd=0)
backgrounda1.pack()
rand=StringVar()
rand1=StringVar()
rand2=StringVar()
rand3=StringVar()
l=Label(fw,font=('Times New Roman',35,'bold italic'),text='User Data Form',fg='black',bd=10,anchor='w',bg="white")
l.place(x=500,y=20)
l=Label(fw,font=('Times New Roman',15,'bold italic'),text='Reaction time of participant(Tau): ',fg='black',bd=10,anchor='w',bg="white")
l.place(x=700,y=250)
t=Entry(fw,font=('Times New Roman',16),textvariable=rand,bd=10,insertwidth=4,bg='powder blue',justify='right',relief='flat')
t.place(x=1010,y=250)
l=Label(fw,font=('Times New Roman',15,'bold italic'),text='Nominal Power Consumed(p):         ',fg='black',bd=10,anchor='w',bg="white")
l.place(x=700,y=330)
t1=Entry(fw,font=('Times New Roman',16),textvariable=rand1,bd=10,insertwidth=4,bg='powder blue',justify='right',relief='flat')
t1.place(x=1010,y=330)
l=Label(fw,font=('Times New Roman',15,'bold italic'),text='coefficient(-->) to price elasticity   ',fg='black',bd=10,anchor='w',bg="white")
l.place(x=700,y=410)
t2=Entry(fw,font=('Times New Roman',16),textvariable=rand2,bd=10,insertwidth=4,bg='powder blue',justify='right',relief='flat')
t2.place(x=1010,y=410)
l=Label(fw,font=('Times New Roman',15,'bold italic'),text='Stability(Real,positive or negative):',fg='black',bd=10,anchor='w',bg="white")
l.place(x=700,y=490)
t3=Entry(fw,font=('Times New Roman',16),textvariable=rand3,bd=10,insertwidth=4,bg='powder blue',justify='right',relief='flat')
t3.place(x=1010,y=490)
def Function():

    if __name__=='__main__':
        with open('final.pkl', 'rb') as f:
            mp= pickle.load(f)
    x1=t.get()
    x2=t1.get()
    x3=t2.get()
    x4=t3.get()
    test=[]
    for i in range(4):
        test.append(float(x1.strip()))
    for i in range(4):
        test.append(float(x2.strip()))
    for i in range(4):
        test.append(float(x3.strip()))
    test.append(float(x4.strip()))
    print(test)
    import numpy as np
    y_test=mp.predict(np.array(test))
    if y_test>0:
        state='Unstable'
    else:
        state='Stable'
    messagebox.showinfo('Result','The electric grid with your given data is %s electric Grid'%(state))
    finw=Tk()
    finw.title('User Data Form')
    finw.geometry('1350x750+0+0')
    finw.config(bg='aqua')
    l=Label(finw,font=('Times New Roman',20,'bold italic'),text='The Electric Grid with your given inputs is ',fg='black',bd=10,anchor='w',bg='aqua')
    l.place(x=200,y=200)
    l=Label(finw,font=('Times New Roman',20,'bold italic'),text="Unstable",fg='black',bd=10,anchor='w',bg='aqua')
    l.place(x=250,y=250)
    l=Label(finw,font=('Times New Roman',20,'bold italic'),text="Grid Power Station",fg='black',bd=10,anchor='w',bg='aqua')
    l.place(x=370,y=250)
    l=Label(finw,font=('Times New Roman',20,'bold italic'),text="Thank You..........",fg='black',bd=10,anchor='w',bg='aqua')
    l.place(x=360,y=330)
    def fun1():
        finw.destroy()
    Btn = Button(finw, text = "Close",width=15,font=('arial',15,'bold'),bg='blue',relief='sunken',command=fun1)
    Btn.place(x=340,y=400)
Btn = Button(fw, text = "Submit",width=15,font=('arial',15,'bold'),bg='powder blue',relief='sunken',command=Function)
Btn.place(x=900,y=580)
fw.mainloop()
