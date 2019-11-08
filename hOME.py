
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
    l=Label(pw,font=('Times New Roman',25,'bold italic'),text='Perceptron Model',fg='black',bd=10,anchor='w',bg='violet')
    l.place(x=550,y=30)
    f1=Frame(pw,width=800,height=500,relief='sunken',bg='black')
    f1.place(x=300,y=120)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='      A perceptron is a neural network unit (an artificial neuron) that ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=10)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='does certain computations to detect features or business intelligence  ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=50)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='in the input data. It is a Single Layer. It is also used in Supervised ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=90)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='learning.It also helps to classify the given input data.            ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=130)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='Since we have the electric grid dataset which is to be classified as     ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=170)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='Stable and Unstable on the given features.                               ',fg='blue',bd=10,anchor='w',bg='black')
    l.place(x=5,y=210)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='Our dataset contains 14 FEATURES in which our target output is in last   ',fg='green',bd=10,anchor='w',bg='black')
    l.place(x=5,y=250)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='column which is the "stabf" features which represents Stable or Unstable',fg='green',bd=10,anchor='w',bg='black')
    l.place(x=5,y=290)
    l=Label(f1,font=('Times New Roman',20,'bold italic'),text='Start the Training Using Perceptron Network',fg='green',bd=10,anchor='w',bg='black')
    l.place(x=5,y=330)
    f2=Frame(f1,width=400,height=80,relief='sunken',bg='white')
    f2.place(x=200,y=390)
    def trained():
        tw=Tk()
        tw.title("Perceptron")
        tw.geometry('1350x750+0+0')
        tw.config(bg="DeepSkyBlue")
        l=Label(tw,font=('Times New Roman',30,'bold italic'),text="Results after Training the network",fg='black',bd=10,anchor='w',bg='DeepSkyBlue')
        l.place(x=300,y=30)
        l=Label(tw,font=('Times New Roman',30,'bold italic'),text="     with Perceptron Network      ",fg='black',bd=10,anchor='w',bg='DeepSkyBlue')
        l.place(x=300,y=90)
        with open("PerceptronData.txt","r") as fp:
            data=fp.readlines()
        a=[]
        j=0
        for i in data:
            a.append(i.strip())

        f2=Frame(tw,width=600,height=500,relief='sunken',bg='DeepSkyBlue')
        f2.place(x=300,y=160)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[0],fg='black',bd=10,anchor='w',bg='DeepSkyBlue')
        l.place(x=5,y=30)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[1],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=70)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[5],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=110)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[6],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=150)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[7],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=190)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[8],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=230)
        btnl=Button(tw,text='Back', width=10,font=('arial',20,'bold'),bg='black',fg='white',relief='groove',command=trained)
        btnl.place(x=150,y=510)
        def Code():
           import webbrowser
           new = 1
           url = "https://github.com/Lovely-Professional-University-CSE/major-project-ca-1-electrical_grid_stability-25-26-27-28/blob/master/%20training%20with%20perceptron.ipynb"
           webbrowser.open(url,new=new)

 
        btnl=Button(tw,text='Github Code', width=10,font=('arial',20,'bold'),bg='black',fg='white',relief='groove',command=Code)
        btnl.place(x=750,y=510)
        btnl=Button(tw,text='Training Models', width=15,font=('arial',20,'bold'),bg='black',fg='white',relief='groove',command=model_window)
        btnl.place(x=400,y=510)
    btnl=Button(f2,text='Start Training', width=15,font=('arial',20,'bold'),bg='black',fg='white',relief='raised',command=trained)
    btnl.place(x=60,y=15)
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


