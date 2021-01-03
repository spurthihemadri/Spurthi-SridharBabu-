# -*- coding: utf-8 -*-


from tkinter import *
import math 
exp = " "  
def click(number): 
   global exp 
   exp = exp + str(number) 
   s.set(exp) 
 
def clickequal(): 
    try: 
        global exp 
        total = str(eval(exp)) 
        s.set(total) 
        expression = "" 
    except: 
        s.set(" error ") 
        expression = "" 
def clear(): 
    global exp 
    exp = "" 
    s.set("") 
  
if __name__ == "__main__": 
    r= Tk() 
    r.configure(background="light grey") 
    r.title("Simple Calculator") 
    r.geometry("300x300") 
    s = StringVar() 
    entry_field= Entry(r, textvariable=s,font=('Arial',12,'bold')) 
    entry_field.grid(columnspan=7, ipadx=70) 
    s.set('|') 
    b1 = Button(r, text=' 1 ', fg='blue', command=lambda:click(1), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b1.grid(row=2, column=0) 
  
    b2 = Button(r, text=' 2 ', fg='blue', command=lambda: click(2), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b2.grid(row=2, column=1) 
  
    b3 = Button(r, text=' 3 ', fg='blue', command=lambda: click(3), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b3.grid(row=2, column=2) 
  
    b4 = Button(r, text=' 4 ', fg='blue', command=lambda: click(4), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b4.grid(row=2, column=3) 
  
    b5 = Button(r, text=' 5 ', fg='blue', command=lambda: click(5), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b5.grid(row=3, column=0) 
  
    b6 = Button(r, text=' 6 ', fg='blue',  command=lambda: click(6), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b6.grid(row=3, column=1) 
  
    b7 = Button(r, text=' 7 ', fg='blue', command=lambda: click(7), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b7.grid(row=3, column=2) 
  
    b8 = Button(r, text=' 8 ', fg='blue',  command=lambda: click(8), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b8.grid(row=3, column=3) 
  
    b9 = Button(r, text=' 9 ', fg='blue',  command=lambda: click(9), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b9.grid(row=4, column=0) 
  
    b0 = Button(r, text=' 0 ', fg='blue', command=lambda: click(0), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    b0.grid(row=4, column=1) 
  
    plus = Button(r, text=' + ', fg='blue', command=lambda: click("+"), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    plus.grid(row=4, column=2) 
  
    minus = Button(r, text=' - ', fg='blue', command=lambda: click("-"), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    minus.grid(row=4, column=3) 
  
    mul= Button(r, text=' * ', fg='blue',  command=lambda: click("*"), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    mul.grid(row=5, column=0) 
  
    div = Button(r, text=' / ', fg='blue', command=lambda: click("/"), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    div.grid(row=5, column=1) 
  
    equal = Button(r, text=' = ', fg='blue',  command=clickequal, height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    equal.grid(row=5, column=2) 
  
    clear = Button(r, text='CLR', fg='blue', command=clear, height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    clear.grid(row=5, column=3) 
  
    Decimal= Button(r, text='.', fg='blue', command=lambda: click('.'), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    Decimal.grid(row=6, column=0) 
    
    Remainder= Button(r, text='REM', fg='blue', command=lambda: click('%'), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    Remainder.grid(row=6, column=1) 

    openparam= Button(r, text='(', fg='blue', command=lambda: click('('), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    openparam.grid(row=6, column=2) 

    closeparam= Button(r, text=')', fg='blue', command=lambda: click(')'), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    closeparam.grid(row=6, column=3) 

    sqroot= Button(r, text='SQRT', fg='blue', command=lambda: click('math.sqrt'), height=2, width=8,relief=RIDGE,borderwidth=3,font=('Arial',8,"bold")) 
    sqroot.grid(row=7, column=0) 


    r.mainloop() 