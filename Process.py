from tkinter import *
from tkinter import filedialog
import sys
import os

root = Tk()
root.geometry("500x500")
root.title("UnPass v1.0")

heading = Label(text="Main Process",fg="white",bg="Blue",width="500",height="3",font="10")
heading.pack()

#function
def open_txt():
    f = open("logs.txt", 'r')
    temp = f.read(300)
    Information.insert(END, temp)
    f.close()

#Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create scrollbar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#Text Box 
Information = Text(my_frame, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
Information.pack()

# Configure our scrollbar
text_scroll.config(command=Information.yview)

def crack():
    os.system('python3 mainCode.py gesture.sample.key')

B  = Button(root,text="Execute",bg='green', fg='white', command= lambda: [crack(), open_txt()])
B.pack(pady=10)
C = Button(root, text='Quit', width=20, bg='red', fg='white', command=root.quit)
C.pack()

root.mainloop()
