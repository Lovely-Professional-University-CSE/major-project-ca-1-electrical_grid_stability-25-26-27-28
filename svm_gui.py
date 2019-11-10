import numpy as np
import PIL
from PIL import Image
import tkinter as tk
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

def description():

    root = tk.Tk()
    root.title(10 * "\t" + "SVM")
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

def maps():
    pass

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
    root.title(10 * "\t" + "SVM")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    frame = tk.Frame(root, width=width, height=height)
    frame.pack()
    canvas = tk.Canvas(frame, width=width, height=height, bg="lightblue")
    canvas.pack()
    canvas.create_text(700, 300, text='ACCURACY : '+str(accuracy), font = ('Helvetica', 30, 'bold'), fill='red')
    tk.Button(canvas, text = 'Description',command= description, bg="lightblue", height=3, width=50).place(x=525, y=350)
    tk.Button(canvas, text = 'Maps', command=maps, bg="lightblue", height=3, width=50).place(x=525, y=410)


def custom_train():
    pass

def svm_home():

    def trained():
        root.destroy()
        trained_model()

    def custom():
        root.destroy()
        custom_train()

    def back():
        root.destroy()
        print('put your home file hear')

    root = tk.Tk()
    root.title(10*"\t"+"SVM")
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
    tk.Button(canvas, text = 'back', bg="lightblue", command=back, height=3, width=50).place(x=1100, y=480)
    root.mainloop()

svm_home()
