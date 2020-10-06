import sys
import os
import tkinter
#import tkMessageBox
top=tkinter.Tk()

def helloCallBack():
    os.system('python3 mainCode.py gesture.sample.key')

B=tkinter.Button(top,text="hello",command= helloCallBack)
B.pack()
top.mainloop()