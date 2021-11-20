from tkinter import *
import tkinter.font as font
import sys,os
def window1():
    os.system('game.py')
def window2():
    os.system('3x3.py')
window=Tk()
window.config(bg="red")
window.geometry('400x300')
font1=font.Font(size=12,weight="bold")
font2=font.Font(size=12,weight="bold")
l1=Label(window,text="Select The Layout Of your Game",width=35,height=2,bd=8,bg="yellow",fg="black",font=font1)
l1.place(x=20,y=30)
b1=Button(window,text="4x4",width=10,height=3,bd=8,bg="yellow",fg="black",command=window1,font=font2)
b1.place(x=120,y=90)
b2=Button(window,text="3x3",width=10,height=3,bd=8,bg="yellow",fg="black",command=window2,font=font2)
b2.place(x=120,y=180)
mainloop()
