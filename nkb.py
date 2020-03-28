from tkinter import *




window = Tk()
window.geometry("1350x700+0+0")
window.title('Doctor Panel')

title=Label(window,text='Doctor Panel',bd=10,relief=GROOVE,font=('times new roman',40,'bold'))
title.pack(side=TOP,fill=X)

manage_Frame=Frame(window,bd=4,relief=RIDGE,bg='crimson')
manage_Frame.place(x=20,y=100,width=450,height=560)
m_title=Label(manage_Frame,text='bsnb',font=('times new roman',40,'bold'))
m_title.grid(row=0,columnspan=2,pady=2)

window.mainloop()