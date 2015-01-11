import sys
from Tkinter import *

def mhello():
    mtext =ment.get()
    print 'hello'
    mlabel2 = Label(mGui,text=mtext, fg='green',bg='grey').pack()
    return

mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+100+100')
mGui.title('VCC')

mlabel = Label(mGui,text='My label', fg='red',bg='blue').pack()
mbutton = Button(mGui,text='OK', command=mhello, fg='yellow',bg='black').pack()
mentry = Entry(mGui,textvariable=ment).pack()
print 'hello'

#ylabel = Label(text='My label', fg='red',bg='blue').pack()

mGui.mainloop()
