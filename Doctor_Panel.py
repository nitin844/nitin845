import pyttsx3
#import speech_recognition as sr
import datetime
import os
from tkinter import *
import pymysql
import threading
from tkinter import ttk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()
window.geometry("800x600+150+50")
window.title('Doctor Panel')
window.configure(bg="white")
title=Label(window,text='Doctor Panel',bd=10,relief=GROOVE,font=('times new roman',40,'bold'))
title.pack(side=TOP,fill=X)

manage_Frame=Frame(window,bd=4,relief=RIDGE)
manage_Frame.place(x=10,y=100,width=350,height=460)
m_title=Label(manage_Frame,text='Doctor Details',font=('times new roman',20,'bold'))
m_title.grid(row=0,columnspan=2,pady=2)

myLabel_form = Label(text="DOCTOR FORM",font="Monospace 10 bold",bg="white",fg="grey")
myLabel_form.pack()
myLabel_form.place(x=76,y=60)


myLabel_line = Label(bg="lavender")
myLabel_line.pack()
myLabel_line.place(x=76,y=90,width="640",height="2")

myLabel_line1 = Label(bg="seashell4")
myLabel_line1.pack()
myLabel_line1.place(x=0,y=530,width="940",height="2")











global var_Doctor_Name
global var_Hospital_Name
global var_email
global var_mobile_number
global var_address
var1 = StringVar()
var_Doctor_Name = StringVar()
var_Hospital_Name = StringVar()
var_email = StringVar()
var_mobile_number = StringVar()
var_address = StringVar()


myLabel_Doctor_name = Label(text="Doctor Name",font=("Sansserif 10 ",10,'bold'), bg="white",fg="black")
myLabel_Doctor_name.pack()
myLabel_Doctor_name.place(x=56,y=150)

Entry_Doctor_name = Entry(textvar=var_Doctor_Name,font="Sansserif 10",bg="white",fg="black")
Entry_Doctor_name.pack()
Entry_Doctor_name.place(x=160,y=150,height="25")


myLabel_var_Hospital_Name = Label(text="Hospital Name",font=("Sansserif 10",10,'bold'),bg="white",fg="black")
myLabel_var_Hospital_Name.pack()
myLabel_var_Hospital_Name.place(x=56,y=200)

Entry_var_Hospital_Name = Entry(textvar=var_Hospital_Name,font="Sansserif 10",bg="white",fg="black")
Entry_var_Hospital_Name.pack()
Entry_var_Hospital_Name.place(x=160,y=200,height="25",width="120")



myLabel_email = Label(text="Doctor-Email",font=("Sansserif 10",10,'bold'),bg="white",fg="black")
myLabel_email.pack()
myLabel_email.place(x=56,y=260)

Entry_email = Entry(textvar=var_email,font="Sansserif 10",bg="white",fg="black")
Entry_email.pack()
Entry_email.place(x=160,y=260)






myLabel_address = Label(text="Address",font=("Sansserif 10",10,'bold'),bg="white",fg="black")
myLabel_address.pack()
myLabel_address.place(x=56,y=320)

Entry_address = Entry(textvar=var_address,font="Sansserif 10",bg="white",fg="black")
Entry_address.pack()
Entry_address.place(x=160,y=320,height=30)





myLabel_var_mobile_number = Label(text="mobile number",font=("Sansserif 10",10,'bold'),bg="white",fg="black")
myLabel_var_mobile_number.pack()
myLabel_var_mobile_number.place(x=56,y=390)

Entry_var_mobile_number = Entry(textvar=var_mobile_number,font="Sansserif 10",bg="white",fg="black")
Entry_var_mobile_number.pack()
Entry_var_mobile_number.place(x=160,y=390,height=20)









btn = Button(text="Create",bg="blue3",fg="white")
btn.pack()
btn.place(x=670,y=550,width="100",height="25")

btn0 = Button(text="Cancel",bg="slateblue",fg="white")
btn0.pack()
btn0.place(x=560,y=550,width="100",height="25")





detail_Frame=Frame(window,bd=4,relief=RIDGE)
detail_Frame.place(x=400,y=100,width=390,height=440)


lbl_search=Label(detail_Frame,text='Search By',fg='black',font=('times new roman',13,'bold'))
lbl_search.grid(row=0,column=0,pady=10,padx=2,sticky='w')

combo_Search=ttk.Combobox(detail_Frame,width=10,font=("Sansserif 10",8,'bold'),state='readonly')
combo_Search['values']=('Doctor_Name','Hospital_Name')
combo_Search.grid(row=0,column=1,padx=2,pady=10)

txt_Search=Entry(detail_Frame,font=('times new roman',6,'bold'),bd=5,relief=GROOVE)
txt_Search.grid(row=0,column=2,pady=10,padx=5,sticky='w')

searchbtn=Button(detail_Frame,text='Search',width=6

).grid(row=0,column=3,pady=10)
showallbtn=Button(detail_Frame,text="Show All",width=6).grid(row=0,column=4,pady=10)

Table_Frame=Frame(detail_Frame,bd=4,relief=RIDGE)
Table_Frame.place(x=2,y=70,width=380,height=360)

scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

Patient_table=ttk.Treeview(Table_Frame,columns=( 'name','age','gender','health','Doctor','Past','email','Phone','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=Patient_table.xview)
scroll_y.config(command=Patient_table.yview)
Patient_table.heading('name',text='Name')
Patient_table.heading('age',text='Age')
Patient_table.heading('gender',text='Gender')
Patient_table['show']='headings'
Patient_table.column('name',width=100)
Patient_table.column('age',width=100)
Patient_table.column('gender',width=100)
Patient_table.pack(fill=BOTH,expand=1)



Patient_table.pack()























def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var1.set("Good Morning ")
        window.update()
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        var1.set("Good Afternoon  ")
        window.update()
        speak("Good Afternoon")
    else:
        var1.set("Good Evening ")
        window.update()
        speak("Good Evening")
        speak("I'm  Dr. Oxo ")
    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var1.set("Listening.....")
        window.update()
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        var1.set("Recoginizers...")
        window.update()
        print("Recoginizers.....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it again please sir")
        return "None"
    var1.set(query)
    window.update()
    return query





if __name__ == "__main__":
    wishMe()

    if True:
        query = takeCommand().lower()

        if 'Not Agree' in query:
            takeCommand()


        elif 'make' in query:    
          
           try:
            
              speak("Doctor Name")
              query_Doctor_Name = takeCommand()
              var_Doctor_Name.set(query_Doctor_Name)
              window.update
            
              speak('var Hospital Name')
              query_Hospital_Name = takeCommand()
              var_Hospital_Name.set(query_Hospital_Name)
              window.update()

              

              speak(" Your Email id   ")
              query_email = takeCommand()
              var_email.set(query_email)
              window.update()

              speak("Your Number ")
              query_number = takeCommand()
              var_mobile_number.set(query_number)
              window.update()

              speak("Your Address")
              query_add = takeCommand()
              var_address.set(query_add)
              window.update()

              speak("Thank Your")
              speak("Any Correction")


        
           except Exception as e:

               print(e)

    




          
window.mainloop()
