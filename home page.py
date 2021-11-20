from tkinter import *
import tkinter.font as font
import sys,os
def create_window():
    os.system('design.py')
window=Tk()
window.config(bg="burlywood")
window.geometry("330x250")
font1=font.Font(size=38,weight="bold")
font2=font.Font(size=20,weight="bold")
b=Label(window,text="Hello!",font=font1,bg="burlywood2",fg="black",height=1,width=6)
b.place(x=70,y=20)
b1=Button(window,text="Click Here To Start",bg="burlywood2",fg="black",height=2,width=17,font=font2,command=create_window)
b1.place(x=20,y=100)
window.mainloop()
