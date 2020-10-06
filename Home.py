from tkinter import *
import sys
import os
import tkinter

def save_info():
    DeviceName_info = Device.get()
    Description_info = Description.get()
    Version_info = c.get()
    #print(DeviceName_info, Description_info)

    file = open("log.txt", "w")
    space = str("\n")
    file.write("DeviceName  :" + DeviceName_info )
    file.write(space)
    file.write("Description :" + Description_info)
    file.write(space)
    file.write("Version     :" + Version_info)
    file.close()

    Device_entry.delete(0, END)
    Description_entry.delete(0, END)

def call_back():
    os.system('python3 Process.py')


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    root.title("UnPass v1.0")

    Header = Label(root, text="Gathering Information",width=20,font=("bold", 20))
    Header.place(x=90,y=53)
   

    #Device
    Device = Label(root, text="Device Name",width=20,font=("bold", 10))
    Device.place(x=80,y=130)
    Device = StringVar()
    Device_entry = Entry(textvariable=Device)#### textvariable merupakan variable untuk input
    Device_entry.place(x=240,y=130)

    #Description
    Description = Label(root, text="Description",width=20,font=("bold", 10))
    Description.place(x=68,y=180)
    Description = StringVar()
    Description_entry = Entry(textvariable=Description) ###
    Description_entry.place(x=240,y=180)

    #Version
    Version = Label(root, text="Version",width=20,font=("bold", 10))
    Version.place(x=70,y=230)

    list1 = ['Kitkat','Lolipop','Marshmellow'];
    c=StringVar()
    droplist=OptionMenu(root,c, *list1)
    droplist.config(width=15)
    c.set('select your version') 
    droplist.place(x=240,y=230)

    #Button
    Button(root, text='PrintInfo',width=20,bg='blue',fg='white',command=save_info).place(x=180,y=300)
    Button(root, text='Quit', width=20, bg='red', fg='white', command=root.quit).place(x=180,y=330)

    #Button Hack
    Button(root, text='Hack', width=20, bg='green', fg='white', command=call_back).place(x=180,y=360)


    root.mainloop()
    #https://www.youtube.com/watch?v=CKeFRDXYwcA