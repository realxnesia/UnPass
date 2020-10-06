from tkinter import *
from tkinter import filedialog
import sys
import os
import tkinter
#import tkMessageBox

root = Tk()
root.geometry("500x500")
root.title("UnPass v1.0")

heading = Label(text="Main Process",fg="white",bg="Green",width="500",height="3",font="10")
heading.pack()

#open file dari txt
#f = open("log.txt", "r")
#print(f.read())
#DeviceTemp = f.readline()
#f.close()


#Label(root, text=)
#ambil variable penampung



def crack():
    os.system('python3 mainCode.py gesture.sample.key')

B=tkinter.Button(root,text="Execute",command= lambda: crack())
B.pack()

root.mainloop()


# print("proses...")