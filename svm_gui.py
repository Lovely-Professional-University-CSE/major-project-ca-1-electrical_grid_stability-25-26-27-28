import numpy as np
import PIL
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import seaborn as sn
from sklearn.externals import joblib
import glob
import seaborn as sns
import pickle
import os
from random import *


def description():

    root = tk.Tk()
    root.title(10 * "\t" + "DESCRIPTION")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width=width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width=width, height=height, bg="lightblue")
    canvas.pack()
    f = open("PerceptronData.txt", "r").readlines()
    count = 0
    for line in f:

        canvas.create_text(700, 200+(count*40), text=line, font=('Helvetica', 30, 'bold'), fill='red')
        count+=1

def graphs():
    root = tk.Toplevel()
    root.title(10 * "\t" + "SVM HOME")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width=width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width=width, height=height, bg="grey")
    canvas.pack()

    # for file in os.listdir('proimages'):
    #     img = Image.open('proimages/'+file)
    #     img = img.resize((600, 400), Image.ANTIALIAS)
    #     img.save(file)

    img = tk.PhotoImage(file='box.png')
    canvas.create_image(50, 10, image=img, anchor="nw")
    img1 = tk.PhotoImage(file='scatter.png')
    canvas.create_image(750, 10, image=img1, anchor="nw")
    img2 = tk.PhotoImage(file='count.png')
    canvas.create_image(50, 400, image=img2, anchor="nw")
    img3 = tk.PhotoImage(file='density.png')
    canvas.create_image(750, 400, image=img3, anchor="nw")
    root.mainloop()


def trained_model():
    try:
        with open('svm.pkl', 'rb') as file:
            saved_model = pickle.load(file)
        with open('lists.pkl', 'rb') as f:
            lists = pickle.load(f)
            x_test, y_test = lists[0], lists[1]
        pred = saved_model.predict(x_test)
        accuracy = accuracy_score(pred, y_test)
    except:
        print('there is no pretrained model')

    root = tk.Tk()
    root.title(10 * "\t" + "TRAINED MODEL")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width=width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width=width, height=height, bg="lightblue")
    canvas.pack()
    canvas.create_text(700, 300, text='ACCURACY : '+str(accuracy), font = ('Helvetica', 30, 'bold'), fill='red')
    tk.Button(canvas, text = 'Description',command= description, bg="lightblue", height=3, width=50).place(x=525, y=350)
    tk.Button(canvas, text = 'Maps', command=graphs, bg="lightblue", height=3, width=50).place(x=525, y=410)
    root.mainloop()

def custom_train():
    def back():
        root.destroy()
        svm_home()
    root = tk.Toplevel()
    root.title(10 * "\t" + "SVM HOME")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width=width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width=width, height=height, bg="lightblue")
    canvas.pack()
    img = tk.PhotoImage(file='form1.png')
    canvas.create_image(30, 250, image=img, anchor="nw")
    rand = StringVar()
    rand1 = StringVar()
    rand2 = StringVar()
    rand3 = StringVar()
    l = Label(root, font=('Times New Roman', 35, 'bold italic'), text='User Data Form', fg='black', bd=10, anchor='w',
              bg="white")
    l.place(x=500, y=20)
    l = Label(root, font=('Times New Roman', 15, 'bold italic'), text='Reaction time of participant(Tau): ', fg='black',
              bd=10, anchor='w', bg="white")
    l.place(x=700, y=250)
    t = Entry(root, font=('Times New Roman', 16), textvariable=rand, bd=10, insertwidth=4, bg='powder blue',
              justify='right', relief='flat')
    t.place(x=1010, y=250)
    l = Label(root, font=('Times New Roman', 15, 'bold italic'), text='Nominal Power Consumed(p):         ', fg='black',
              bd=10, anchor='w', bg="white")
    l.place(x=700, y=330)
    t1 = Entry(root, font=('Times New Roman', 16), textvariable=rand1, bd=10, insertwidth=4, bg='powder blue',
               justify='right', relief='flat')
    t1.place(x=1010, y=330)
    l = Label(root, font=('Times New Roman', 15, 'bold italic'), text='coefficient(-->) to price elasticity   ',
              fg='black', bd=10, anchor='w', bg="white")
    l.place(x=700, y=410)
    t2 = Entry(root, font=('Times New Roman', 16), textvariable=rand2, bd=10, insertwidth=4, bg='powder blue',
               justify='right', relief='flat')
    t2.place(x=1010, y=410)
    l = Label(root, font=('Times New Roman', 15, 'bold italic'), text='Stability(Real,positive or negative):', fg='black',
              bd=10, anchor='w', bg="white")
    l.place(x=700, y=490)
    t3 = Entry(root, font=('Times New Roman', 16), textvariable=rand3, bd=10, insertwidth=4, bg='powder blue',
               justify='right', relief='flat')
    t3.place(x=1010, y=490)

    def Function():

        if __name__ == '__main__':
            with open('svm.pkl', 'rb') as f:
                mp = pickle.load(f)
        x1 = t.get()
        x2 = t1.get()
        x3 = t2.get()
        x4 = t3.get()
        test = []
        for i in range(4):
            test.append(float(x1.strip()))
        for i in range(4):
            test.append(float(x2.strip()))
        for i in range(4):
            test.append(float(x3.strip()))
        test.append(float(x4.strip()))
        print(test)
        y_test = mp.predict([np.array(test)])
        if y_test == 0:
            state = 'Unstable'
        else:
            state = 'Stable'
        messagebox.showinfo('Result', 'The electric grid with your given data is %s electric Grid' % (state))
        finw = tk.Toplevel()
        finw.title('User Data Form')
        finw.geometry('1350x750+0+0')
        finw.config(bg='lightblue')
        l = Label(finw, font=('Times New Roman', 20, 'bold italic'),
                  text='The Electric Grid with your given inputs is ', fg='black', bd=10, anchor='w', bg='aqua')
        l.place(x=200, y=200)
        l = Label(finw, font=('Times New Roman', 20, 'bold italic'), text=state, fg='red', bd=10, anchor='w',
                  bg='aqua')
        l.place(x=250, y=250)
        l = Label(finw, font=('Times New Roman', 20, 'bold italic'), text="Grid Power Station", fg='black', bd=10,
                  anchor='w', bg='aqua')
        l.place(x=370, y=250)
        l = Label(finw, font=('Times New Roman', 20, 'bold italic'), text="Thank You..........", fg='black', bd=10,
                  anchor='w', bg='aqua')
        l.place(x=360, y=330)

        def fun1():
            finw.destroy()

        Btn = Button(finw, text="Close", width=15, font=('arial', 15, 'bold'), bg='blue', relief='sunken', command=fun1)
        Btn.place(x=340, y=400)

    Btn = Button(root, text="Submit", bg = 'lightblue', width=15, font=('arial', 15, 'bold'),command=Function)
    Btn.place(x=900, y=580)
    Btn = Button(root, text="back", bg='lightblue', width=15, font=('arial', 15, 'bold'), command=back)
    Btn.place(x=900, y=640)
    root.mainloop()

def svm_home():

    def trained():
        root.destroy()
        trained_model()

    def custom():
        root.destroy()
        custom_train()


    root = tk.Toplevel()
    root.title(10*"\t"+"SVM HOME")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width = width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width = width, height = height, bg="grey")
    canvas.pack()
    img = tk.PhotoImage(file='back1.png')
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.create_text(300, 300, text='Support Vector Machine(SVM):', font = ('Helvetica', 30, 'bold'), fill='red')
    canvas.create_text(320, 500, text='A support vector machine (SVM) is machine learning algorithm \n'
                                    'that analyzes data for classification and regression analysis.\n '
                                    'SVM is a supervised learning method that looks at data and sorts \n'
                                    'it into one of two categories.An SVM outputs a map of the sorted\n'
                                    ' data with the margins between the two as far apart as possible.',
                       font = ('Helvetica',15, 'bold'), fill='red')
    tk.Button(canvas, text = "trained_model", bg = "lightblue", command = trained, height=3, width=50).place(x = 1100, y=310)
    tk.Button(canvas, text="custom_train", bg="lightblue", command=custom, height=3, width=50).place(x=1100, y=380)
    tk.Button(canvas, text = 'back', bg="lightblue", height=3, width=50).place(x=1100, y=480)
    root.mainloop()

