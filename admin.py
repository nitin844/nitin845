from tkinter import *
import threading
from tkinter import ttk



window = Tk()
window.geometry("600x400+150+50")
window.title('Admin Panel')
window.configure(bg="white")
title=Label(window,text='Admin Panel',bd=10,relief=GROOVE,font=('times new roman',40,'bold'))
title.pack(side=TOP,fill=X)


manage_Frame=Frame(window,bd=4,relief=RIDGE)
manage_Frame.place(x=10,y=80,width=250,height=280)


myLabel_form = Label(text="Doctor Details",font="Monospace 10 bold",bg="white",fg="grey")
myLabel_form.pack()
myLabel_form.place(x=30,y=90)


myLabel_line = Label(bg="lavender")
myLabel_line.pack()
myLabel_line.place(x=76,y=90,width="640",height="2")

myLabel_line1 = Label(bg="seashell4")
myLabel_line1.pack()
myLabel_line1.place(x=70,y=12,width="940",height="2")


btn = Button(text="Update",bg="blue3",fg="white")
btn.pack()
btn.place(x=10,y=360,width="50",height="25")

btn0 = Button(text="Clear",bg="slateblue",fg="white")
btn0.pack()
btn0.place(x=100,y=360,width="50",height="25")

Table_Frame=Frame(manage_Frame,bd=4,relief=RIDGE)
Table_Frame.place(x=2,y=30,width=240,height=240)














detail_Frame=Frame(window,bd=4,relief=RIDGE)
detail_Frame.place(x=300,y=80,width=290,height=280)

myLabel_form = Label(text="Patient Details",font="Monospace 10 bold",bg="white",fg="grey")
myLabel_form.pack()
myLabel_form.place(x=320,y=90)



btn = Button(text="Update",bg="blue3",fg="white")
btn.pack()
btn.place(x=320,y=360,width="50",height="25")

btn0 = Button(text="Clear",bg="slateblue",fg="white")
btn0.pack()
btn0.place(x=420,y=360,width="50",height="25")

Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE)
Table_Frame.place(x=2,y=30,width=280,height=240)



window.mainloop()