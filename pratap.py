# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 07:12:17 2019

@author: Pratap ksp
"""

import tkinter as tk
from tkinter import*
pw=Tk()
pw.title("LVQ")
pw.geometry('1350x750+0+0')
background_imag2 = PhotoImage(file="back.png")
backgrounda = Label(pw, image=background_imag2, bd=0)
backgrounda.pack()
l=Label(pw,font=('Times New Roman',25,'bold italic'),text='LVQ Model',fg='green',bd=10,anchor='w',bg='white')
l.place(x=550,y=30)
f1=Frame(pw,width=800,height=500,relief='sunken',bg='black')
f1.place(x=300,y=120)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='      The Learning vector Quantization algorithm is a lot like ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=10)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='     k-nearest neighbours,predictions are made by finding match ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=50)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='    among library of patterns, these are learned from training data. ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=90)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='  It is prototype based supervised classification algorithm and counterpart  ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=130)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='                of vector quantization systems.  ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=170)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='     LVQ is special case of an ANN (precisely it applies hebbian learning    ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=210)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='     It is precursor  to self organising maps and neutral gas related   ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=250)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='     Key issue in LVQ is the measure of euclidean distance or similarity ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=290)
l=Label(f1,font=('Times New Roman',20,'bold italic'),text='     for training and classification. ',fg='white',bd=10,anchor='w',bg='black')
l.place(x=5,y=330)
f2=Frame(f1,width=400,height=80,relief='sunken',bg='white')
f2.place(x=200,y=390)
def trained():
    with open("LVQ.txt","r") as fp:
        data=fp.readlines()
    a=[]
    j=0
    for i in data:
       a.append(i.strip())

    f2 =Frame(pw,width=600,height=500,relief='sunken',bg='DeepSkyBlue')
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
btnl=Button(f2,text='Start Training', width=15,font=('arial',20,'bold'),bg='black',fg='white',relief='raised',command=trained)
btnl.place(x=60,y=15)
pw.mainloop()
