from tkinter import *
 
from tkinter import messagebox

root = Tk()

root.title("WELCOMMMMEEE")

root.geometry("500x600")

def msg ():
    messagebox.showwarning("ERROR", "VIRUS ATTACK!")

def topwin():
    top = Toplevel()
    top.title("STOP!")
    top.geometry("400x300")
    label = Label(top, text = "This is my top level window")
    label.pack()
    top.mainloop()

btn= Button(root,text = "MESSAGE BOX", command = msg)

btn1 = Button(root , text="Toplevel", command=topwin)

btn.pack()
btn1.pack()

root.mainloop()

