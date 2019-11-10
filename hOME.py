
import tkinter as tk
from tkinter import*
import random
import time
import sqlite3
from tkinter import messagebox
from tkinter import messagebox
import pickle
import perceptron
from perceptron import Perceptron  
r= Tk()
#======================================
r.title('Home Page')
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
l=Label(r,font=('Times New Roman',30,'bold italic'),text='ELECTRIC GRID STABILITY',fg='black',bd=10,anchor='w')
l.place(x=400,y=10)

embed=Frame(r,width=600,height=400)
embed.place(x=8,y=200)
l1=Label(embed,font=('Times New Roman',18,'bold italic'),text='An electrical grid, electric grid or power grid,is',fg='black',bd=10,anchor='w')
l1.place(x=50,y=10)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='an interconnected network for delivering electricity',fg='black',bd=10,anchor='w')
l2.place(x=2,y=50)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='Electricity from distributed generation constitutes',fg='black',bd=10,anchor='w')
l2.place(x=2,y=90)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='only small amounts.',fg='black',bd=10,anchor='w')
l2.place(x=2,y=130)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='..... Here we have developed some neural network ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=170)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='training models on electric grid stability data  ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=210)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='Collected from UCI....... ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=250)
l2=Label(embed,font=('Times New Roman',18,'bold italic'),text='For more information of Electric Grid Stability Click below...  ',fg='black',bd=10,anchor='w')
l2.place(x=2,y=290)

import webbrowser
new = 1
url = "https://www.tandfonline.com/doi/abs/10.1080/14786450512331325910"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(embed, text = "Click here",width=15,font=('Times New Roman',15,'bold'),bg='brown',command=openweb)
Btn.place(x=190,y=330)
embed1=Frame(r,width=500,height=400)
embed1.place(x=800,y=210)

background_imag1 = PhotoImage(file="i4.png")
backgrounda1 = Label(embed1, image=background_imag1, bd=0)
backgrounda1.pack()

####################

def user_form():
    fw= Toplevel()
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





#################
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
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text="Size of Stable data values  : 3620",fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=70)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text="Size of Unstable data values: 6830 ",fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=110)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[5],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=150)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[6],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=190)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[7],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=230)
        l=Label(f2,font=('Times New Roman',20,'bold italic'),text=a[8],fg='black',bd=10,anchor='w',bg='DeepSkyblue')
        l.place(x=5,y=290)
        l=Label(tw,font=('Times New Roman',20,'bold italic'),text=" Check the Results With your own inputs........ ",fg='black',bd=10,anchor='w',bg='DeepSkyBlue')
        l.place(x=250,y=450)
##########################
        
######################   
        btnl=Button(tw,text='Check', width=10,font=('Times New Roman',20,'bold italic'),bg='black',fg='white',relief='groove',command=user_form)
        btnl.place(x=180,y=530)
        def Code():
           import webbrowser
           new = 1
           url = "https://github.com/Lovely-Professional-University-CSE/major-project-ca-1-electrical_grid_stability-25-26-27-28/blob/master/%20training%20with%20perceptron.ipynb"
           webbrowser.open(url,new=new)

        btnl=Button(tw,text='Github Code', width=10,font=('Times New Roman',20,'bold italic'),bg='black',fg='white',relief='groove',command=Code)
        btnl.place(x=750,y=530)
        btnl=Button(tw,text='Training Models', width=15,font=('Times New Roman',20,'bold italic'),bg='black',fg='white',relief='groove',command=model_window)
        btnl.place(x=420,y=530)
    btnl=Button(f2,text='Start Training', width=15,font=('Times New Roman',20,'bold italic'),bg='black',fg='white',relief='raised',command=trained)
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
l2=Label(embed2,font=('Times New Roman',18,'bold italic'),text='Click to Go to the data training Models',fg='black',bd=10,anchor='w')
l2.place(x=4,y=5)
Btn = Button(embed2, text = "GO",width=15,font=('Times New Roman',15,'bold italic'),bg='orange',relief='ridge',command=model_window)
Btn.place(x=160,y=50)


