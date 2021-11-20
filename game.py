from tkinter import *
import tkinter.font as font
import random
import sys,os
shuffle_num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,""]
click=0
def layout():
    os.system('3x3.py')
def level1():
    global click
    global click1
    click=0
    click=click+50
    click1=click
def level2():
    global click
    global click1
    click=0
    click=click+100
    click1=click
def level3():
    global click
    global click1
    click=0
    click=click+200
    click1=click
def status():
    label2.config(text="Kindly Select Your Level",font=font2,width=19,height=2)
    b.config(state=NORMAL)
    c.config(state=NORMAL)
    d.config(state=NORMAL)
    e.config(state=NORMAL)
    f.config(state=NORMAL)
    g.config(state=NORMAL)
    h.config(state=NORMAL)
    i.config(state=NORMAL)
    j.config(state=NORMAL)
    k.config(state=NORMAL)
    l.config(state=NORMAL)
    m.config(state=NORMAL)
    n.config(state=NORMAL)
    o.config(state=NORMAL)
    p.config(state=NORMAL)
    q.config(state=NORMAL)
    buttonofshuffle.config(state=NORMAL)
    clear.config(state=NORMAL)
    entry.config(state=NORMAL)
    shuffle()
def window_exit():
    global click
    global click1
    click=click1
    entry.delete(0,END)
    entry.insert(0,click)
    entry.config(state=NORMAL)
    label2.config(text="Best Of Luck!",font=font_style,bg="burlywood2",bd=8,fg="black",height=1,width=12)    
def shuffle():
    random.shuffle(shuffle_num)
    q.config(text=shuffle_num[0])
    b.config(text=shuffle_num[1])
    c.config(text=shuffle_num[2])
    d.config(text=shuffle_num[3])
    e.config(text=shuffle_num[4])
    f.config(text=shuffle_num[5])
    g.config(text=shuffle_num[6])
    h.config(text=shuffle_num[7])
    i.config(text=shuffle_num[8])
    j.config(text=shuffle_num[9])
    k.config(text=shuffle_num[10])
    l.config(text=shuffle_num[11])
    m.config(text=shuffle_num[12])
    n.config(text=shuffle_num[13])
    o.config(text=shuffle_num[14])
    p.config(text=shuffle_num[15])   
def one():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
        
    entry.delete(0,END)
    entry.insert(0,click)
    if e["text"]=="":
        x=b["text"]
        b["text"]=""
        e["text"]=x
    elif c["text"]=="":
        x=b["text"]
        b["text"]=""
        c["text"]=x
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def two():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=c["text"]
    
    if b["text"]=="":
        b["text"]=x
        c.config(text="")
    elif f["text"]=="":
        f["text"]=x
        c.config(text="")
    elif d["text"]=="":
        d["text"]=x
        c.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def three():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=d["text"]
    if c["text"]=="":
        c["text"]=x
        d.config(text="")
    if g["text"]=="":
        g["text"]=x
        d.config(text="")
    if p["text"]=="":
        q["text"]=x
        d.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def sixteen():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=q["text"]
    if d["text"]=="":
        d["text"]=x
        q.config(text="")
    if h["text"]=="":
        h["text"]=x
        q.config(text="")
def four():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=e["text"]
    if b["text"]=="":
        b["text"]=x
        e.config(text="")
    if i["text"]=="":
        i["text"]=x
        e.config(text="")
    if f["text"]=="":
        f["text"]=x
        e.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def six():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=g["text"]
    if f["text"]=="":
        f["text"]=x
        g.config(text="")
    if d["text"]=="":
        d["text"]=x
        g.config(text="")
    if h["text"]=="":
        h["text"]=x
        g.config(text="")
    if k["text"]=="":
        k["text"]=x
        g.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def seven():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=h["text"]
    if g["text"]=="":
        g["text"]=x
        h.config(text="")
    if p["text"]=="":
        q["text"]=x
        h.config(text="")
    if l["text"]=="":
        l["text"]=x
        h.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def eight():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=i["text"]
    if e["text"]=="":
        e["text"]=x
        i.config(text="")
    if m["text"]=="":
        m["text"]=x
        i.config(text="")
    if j["text"]=="":
        j["text"]=x
        i.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def nine():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=j["text"]
    if i["text"]=="":
        i["text"]=x
        j.config(text="")
    if f["text"]=="":
        f["text"]=x
        j.config(text="")
    if k["text"]=="":
        k["text"]=x
        j.config(text="")
    if n["text"]=="":
        n["text"]=x
        j.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def ten():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=k["text"]
    if j["text"]=="":
        j["text"]=x
        k.config(text="")
    if g["text"]=="":
        g["text"]=x
        k.config(text="")
    if l["text"]=="":
        l["text"]=x
        k.config(text="")
    if o["text"]=="":
        o["text"]=x
        k.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def eleven():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=l["text"]
    if k["text"]=="":
        k["text"]=x
        l.config(text="")
    if h["text"]=="":
        h["text"]=x
        l.config(text="")
    if p["text"]=="":
        p["text"]=x
        l.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def twelve():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=m["text"]
    if i["text"]=="":
        i["text"]=x
        m.config(text="")
    if n["text"]=="":
        n["text"]=x
        m.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def thirteen():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=n["text"]
    if m["text"]=="":
        m["text"]=x
        n.config(text="")
    if j["text"]=="":
        j["text"]=x
        n.config(text="")
    if o["text"]=="":
        o["text"]=x
        n.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def fourteen():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=o["text"]
    if n["text"]=="":
        n["text"]=x
        o.config(text="")
    if k["text"]=="":
        k["text"]=x
        o.config(text="")
    if p["text"]=="":
        p["text"]=x
        o.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def fifteen():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=p["text"]
    if o["text"]=="":
        o["text"]=x
        p.config(text="")
    if l["text"]=="":
        l["text"]=x
        p.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
def five():
    global click
    click=click-1
    if click==((click1)/2):
        label2.config(text="Half Of the way covered",font=less_size,width=25,height=1)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==((click1)-1):
        label2.config(text="Best OF Luck!",font=less_size,width=25,height=2)
    elif click==5:
        label2.config(text="Be Carefull limited moves left",font=less_size,width=28)
    elif click==0:
        label2.config(text="Sorry!You are out of the moves",font=less_size,width=25,height=1)
        window.quit()
        b.config(state=DISABLED)
        c.config(state=DISABLED)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=DISABLED)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=DISABLED)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        l.config(state=DISABLED)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=DISABLED)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
    entry.delete(0,END)
    entry.insert(0,click)
    x=f["text"]
    if e["text"]=="":
        e["text"]=x
        f.config(text="")
    if c["text"]=="":
        c["text"]=x
        f.config(text="")
    if j["text"]=="":
        j["text"]=x
        f.config(text="")
    if g["text"]=="":
        g["text"]=x
        f.config(text="")
    elif b["text"]=="1" and c["text"]=="2" and d["text"]=="3" and q["text"]=="4" and e["text"]=="5" and f["text"]=="6" and g["text"]=="7" and h["text"]=="8" and i["text"]=="9" and j["text"]=="10" and k["text"]=="11" and l["text"]=="12" and m["text"]=="13" and n["text"]=="14" and o["text"]=="15" and p["text"]=="":
        label2.config(text="YOU WON!")
window=Tk()
window.title("Shuffle Game")
window.geometry('525x750')
window.config(bg="burlywood")
font_style=font.Font(size=38,weight="bold")
font2=font.Font(size=25,weight="bold")
font1=font.Font(size=28,weight="bold")
font3=font.Font(size=39,weight="bold")
less_size=font.Font(size=20,weight="bold")
a=Button(window,text="PLAY",bd=8,fg="black",bg="burlywood2",height=1,width=13,font=font_style,command=status)
a.place(x=54,y=0)
myfont=font.Font(size=25,weight='bold')
b=Button(window,text=shuffle_num[0],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=one)
b.place(x=62,y=120)
c=Button(window,text=shuffle_num[1],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=two)
c.place(x=62,y=200)
d=Button(window,text=shuffle_num[2],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=three)
d.place(x=62,y=280)
q=Button(window,text=shuffle_num[3],bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=sixteen)
q.place(x=62,y=360)
e=Button(window,text=shuffle_num[4],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=four)
e.place(x=165,y=120)
f=Button(window,text=shuffle_num[5],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=five)
f.place(x=165,y=200)
g=Button(window,text=shuffle_num[6],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=six)
g.place(x=165,y=280)
h=Button(window,text=shuffle_num[7],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=seven)
h.place(x=165,y=360)
i=Button(window,text=shuffle_num[8],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=eight)
i.place(x=268,y=120)
j=Button(window,text=shuffle_num[9],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=nine)
j.place(x=268,y=200)
k=Button(window,text=shuffle_num[10],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=ten)
k.place(x=268,y=280)
l=Button(window,text=shuffle_num[11],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=eleven)
l.place(x=268,y=360)
m=Button(window,text=shuffle_num[12],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=twelve)
m.place(x=371,y=120)
n=Button(window,text=shuffle_num[13],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=thirteen)
n.place(x=371,y=200)
o=Button(window,text=shuffle_num[14],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=fourteen)
o.place(x=371,y=280)
p=Button(window,text=shuffle_num[15],fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=4,font=myfont,command=fifteen)
p.place(x=371,y=360)
buttonofshuffle=Button(window,text="Shuffle",fg="black",bg="burlywood2",bd=8,state=DISABLED,height=1,width=6,font=font_style,command=shuffle)
buttonofshuffle.place(x=50,y=440)
clear=Button(window,text="RESTART",fg="black",bg="burlywood2",bd=8,state=DISABLED,height=2,width=10,font=font2,command=window_exit)
clear.place(x=260,y=440)
moves=Label(window,text="Total Moves",bg="burlywood2",bd=8,fg="black",font=myfont,height=1,width=10)
moves.place(x=80,y=560)
entry=Entry(window,bg="burlywood2",bd=8,state=DISABLED,fg="black",font=myfont,width=3)
entry.place(x=290,y=560)
label2=Label(window,text="Click On Play Button To Start!",font=less_size,bg="burlywood2",bd=8,fg="black",height=1,width=24)
label2.place(x=46,y=630)
menu=Menu(window)
window.config(menu=menu)
levelmenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Level",menu=levelmenu)
levelmenu.add_command(label="Advance",command=level1)
levelmenu.add_command(label="Intermediate",command=level2)
levelmenu.add_command(label="Begginer",command=level3)

layoutmenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Layout",menu=layoutmenu)
layoutmenu.add_command(label="3x3",command=layout)
mainloop()





