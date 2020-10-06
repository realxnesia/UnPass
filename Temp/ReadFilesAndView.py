#https://stackoverflow.com/questions/30993991/read-contents-of-txt-file-and-display-in-tkinter-gui-python

from tkinter import *


def save(e,e1,e2):
    open("log.txt","w").close()
    text = e.get() + "\t" + e1.get() + "\t" +  e2.get() + "\t"
    with open("text.txt", "a") as f:
        f.write(text)

def loadme(l,l2):
    f = open('log.txt','r')
    line = f.readline()
    la1,la2,la3 = line.split()
    l.config(text=la1)
    l2.config(text=la2)
    f.close()

def main():
    root = Tk()
    
    c = Canvas(root,width=600)
    c.pack(side = 'left',expand=1,fill=BOTH)

    c2 = Canvas(c,width=600)
    c2.pack(side = 'left',expand=1,fill=BOTH)
    
    c3 = Canvas(c,width=600)
    c3.pack(side = 'left',expand=1,fill=BOTH)

    w1 = Label(c2, text="Controller value")
    w1.pack()
    e = Entry(c2)
    e.pack()
    
    w2 = Label(c2, text="Velocity")
    w2.pack()
    e1 = Entry(c2)
    e1.pack()
    
    #w3 = Label(c2, text="Desired Heading")
    #w3.pack()
    #e2 = Entry(c2)
    #e2.pack()
    
    toolbar = Frame(c2)
    b = Button(toolbar, text="save", width=9, command=lambda:save(e,e1,e2))
    b.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

    l = Label(c3,text='',bg='red')
    l.pack(side='left',expand=1,fill='x')
    l2 = Label(c3,text='',bg='yellow')
    l2.pack(side='left',expand=1,fill='x')
    #l3 = Label(c3,text='',bg='blue')
    #l3.pack(side='left',expand=1,fill='x')

    b2 = Button(c3,text='load',command=lambda:loadme(l,l2))
    b2.pack(fill='x')
    root.mainloop()

if __name__ == '__main__':
    main()

