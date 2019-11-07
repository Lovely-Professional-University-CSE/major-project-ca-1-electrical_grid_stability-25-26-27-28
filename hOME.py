
import tkinter as tk
from tkinter import*
import random
import time
import sqlite3
from tkinter import messagebox
r= Tk()
#======================================
r.title('Non Regular Registration Form')
r.geometry('1350x750+0+0')
r.config(bg='brown')
background_imag = PhotoImage(file="i2.png")
backgrounda = Label(r, image=background_imag, bd=0)
backgrounda.pack()   
top=Frame(r,width=1300,height=50,bg='brown',relief=SUNKEN)
top.pack(side=TOP)
f1=Frame(r,width=800,height=700,bg='brown',relief=SUNKEN,padx=10)
f1.pack(side=LEFT)
f2=Frame(r,width=600,height=700,bg='brown',relief='ridge',padx=100)
f2.pack(side=RIGHT)
l=Label(r,font=('arial',30,'bold'),text='ELECTRIC GRID STABILITY',fg='black',bd=10,anchor='w')
l.place(x=400,y=10)

embed=Frame(r,width=600,height=400)
embed.place(x=8,y=200)
l1=Label(embed,font=('arial',18,'bold'),text='An electrical grid, electric grid or power grid,is',fg='black',bd=10,anchor='w')
l1.place(x=50,y=10)
l2=Label(embed,font=('arial',18,'bold'),text='an interconnected network for delivering electricity',fg='black',bd=10,anchor='w')
l2.place(x=2,y=50)
l2=Label(embed,font=('arial',18,'bold'),text='Electricity from distributed generation constitutes',fg='black',bd=10,anchor='w')
l2.place(x=2,y=90)
l2=Label(embed,font=('arial',18,'bold'),text='only small amounts.',fg='black',bd=10,anchor='w')
l2.place(x=2,y=130)
l2=Label(embed,font=('arial',18,'bold'),text='..... Here we have developed some neural network ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=170)
l2=Label(embed,font=('arial',18,'bold'),text='training models on electric grid stability data  ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=210)
l2=Label(embed,font=('arial',18,'bold'),text='Collected from UCI....... ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=250)
l2=Label(embed,font=('arial',18,'bold'),text='For more information of Electric Grid Stability Click below...  ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=290)

import webbrowser
new = 1
url = "https://www.tandfonline.com/doi/abs/10.1080/14786450512331325910"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(embed, text = "Click here",width=15,font=('arial',15,'bold'),bg='brown',command=openweb)
Btn.place(x=190,y=330)
embed1=Frame(r,width=500,height=400)
embed1.place(x=800,y=210)

background_imag1 = PhotoImage(file="i4.png")
backgrounda1 = Label(embed1, image=background_imag1, bd=0)
backgrounda1.pack()
def Perceptron_Window():
    pw=Toplevel()
    pw.title("Perceptron")
    pw.geometry('1350x750+0+0')
    background_imag2 = PhotoImage(file="Percep.png")
    backgrounda = Label(pw, image=background_imag2, bd=0)
    backgrounda.pack()
    l=Label(pw,font=('arial',25,'bold'),text='Perceptron Model',fg='black',bd=10,anchor='w',bg='medium purple')
    l.place(x=500,y=30)
    f1=Frame(pw,width=500,height=100)
    f1.place(x=200,y=500)
    pw.mainloop()
def model_window():
    mw=Toplevel()
    mw.title('DATA PREDICTION')
    mw.geometry('1350x750+0+0')
    background_imag2 = PhotoImage(file="i6.png")
    backgrounda = Label(mw, image=background_imag2, bd=0)
    backgrounda.pack()
    l=Label(mw,font=('arial',25,'bold'),text='Prediction Models of',fg='black',bd=10,anchor='w',bg='snow')
    l.place(x=500,y=10)
    l=Label(mw,font=('arial',25,'bold'),text='Electric Grid Stability Dataset',fg='black',bd=10,anchor='w',bg='snow')
    l.place(x=430,y=80)    
    btnl=Button(mw,text='Perceptron Model', width=30,font=('arial',20,'bold'),bg='white',command=Perceptron_Window)
    btnl.place(x=0,y=300)
    btnl=Button(mw,text='SOM Model', width=30,font=('arial',20,'bold'),bg='white')
    btnl.place(x=0,y=400)
    btnl=Button(mw,text='SVM Model', width=30,font=('arial',20,'bold'),bg='white')
    btnl.place(x=0,y=500)
    btnl=Button(mw,text='LVQ Model', width=30,font=('arial',20,'bold'),bg='white')
    btnl.place(x=0,y=600)
    mw.mainloop()
embed2=Frame(r,width=500,height=100)
embed2.place(x=800,y=500)
l2=Label(embed2,font=('arial',18,'bold'),text='Click to Go to the data training Models',fg='black',bd=10,anchor='w')
l2.place(x=4,y=5)
Btn = Button(embed2, text = "GO",width=15,font=('arial',15,'bold'),bg='orange',relief='ridge',command=model_window)
Btn.place(x=160,y=50)


