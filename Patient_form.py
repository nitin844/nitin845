import pyttsx3
#import speech_recognition as sr
import datetime
import os
from tkinter import *
import pymysql
import threading

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()
window.geometry("800x600+150+50")
window.configure(bg="white")


global var_name
global var_age
global var_gender
global var_health
global var_Doctor
global var_Past
global var_email 
global var_Phone
global var_address
var1 = StringVar()
var_name = StringVar()
var_age = StringVar()
var_gender = StringVar()
var_health = StringVar()
var_Doctor = StringVar()
var_Past = StringVar()
var_email = StringVar()
var_Phone = StringVar()
var_address = StringVar()





myLabel_form = Label(text="CREATE A FORM",font="Monospace 10 bold",bg="white",fg="grey")
myLabel_form.pack()
myLabel_form.place(x=76,y=60)


myLabel_line = Label(bg="lavender")
myLabel_line.pack()
myLabel_line.place(x=76,y=90,width="640",height="2")

myLabel_line1 = Label(bg="seashell4")
myLabel_line1.pack()
myLabel_line1.place(x=0,y=530,width="940",height="2")

btn = Button(text="Create",bg="blue3",fg="white")
btn.pack()
btn.place(x=670,y=550,width="100",height="25")

btn0 = Button(text="Cancel",bg="slateblue",fg="white")
btn0.pack()
btn0.place(x=560,y=550,width="100",height="25")

myLabel_name = Label(text="Name",font="Sansserif 10 ", bg="white",fg="black")
myLabel_name.pack()
myLabel_name.place(x=76,y=120)

Entry_name = Entry(textvar=var_name,font="Sansserif 10",bg="white",fg="black")
Entry_name.pack()
Entry_name.place(x=76,y=150,height="25")

myLabel_age = Label(text="Age",font="Sansserif 10",bg="white",fg="black")
myLabel_age.pack()
myLabel_age.place(x=360,y=120)

Entry_age = Entry(textvar=var_age,font="Sansserif 10",bg="white",fg="black")
Entry_age.pack()
Entry_age.place(x=360,y=150,height="25",width="60")

myLabel_gender = Label(text="Gender",font="Sansserif 10",bg="white",fg="black")
myLabel_gender.pack()
myLabel_gender.place(x=540,y=120)

Entry_gender = Entry(textvar=var_gender,font="Sansserif 10 ",bg="white",fg="black")
Entry_gender.pack()
Entry_gender.place(x=540,y=150,height="25",width="100")


myLabel_health = Label(text="Health-Issue ",font="Sansserif 10",bg="white",fg="black")
myLabel_health.pack()
myLabel_health.place(x=76,y=200)

Entry_health = Entry(textvar=var_health,font="Sansserif 10",bg="white",fg="black")
Entry_health.pack()
Entry_health.place(x=76,y=230,height=50,width="200")

myLabel_doctor= Label(text="Doctor",font="Sansserif 10",bg="white",fg="black")
myLabel_doctor.pack()
myLabel_doctor.place(x=360,y=200)

Entry_doctor = Entry(textvar=var_Doctor,font="Sansserif 10",bg="white",fg="black")
Entry_doctor.pack()
Entry_doctor.place(x=360,y=230,height="25",width="130")

myLabel_Past = Label(text="Past-Checkup",font="Sansserif 10",bg="white",fg="black")
myLabel_Past.pack()
myLabel_Past.place(x=540,y=200)

Entry_Past = Entry(textvar=var_Past,font="Sansserif 10",bg="white",fg="black")
Entry_Past.pack()
Entry_Past.place(x=540,y=230,height="25")


myLabel_email = Label(text="Patient-Email",font="Sansserif 10",bg="white",fg="black")
myLabel_email.pack()
myLabel_email.place(x=76,y=320)

Entry_email = Entry(textvar=var_email,font="Sansserif 10",bg="white",fg="black")
Entry_email.pack()
Entry_email.place(x=76,y=350)

myLabel_Phone = Label(text="Phone.Number",font="Sansserif 10",bg="white",fg="black")
myLabel_Phone.pack()
myLabel_Phone.place(x=360,y=320)

Entry_Phone = Entry(textvar=var_Phone,font="Sansserif 10",bg="white",fg="black")
Entry_Phone.pack()
Entry_Phone.place(x=360,y=350)


myLabel_address = Label(text="Address",font="Sansserif 10",bg="white",fg="black")
myLabel_address.pack()
myLabel_address.place(x=76,y=420)

Entry_address = Entry(textvar=var_address,font="Sansserif 10",bg="white",fg="black")
Entry_address.pack()
Entry_address.place(x=76,y=450,height=60)









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
        speak("I'm      ALexa  ")
    


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
            
              speak("Name Sir")
              query_name = takeCommand()
              var_name.set(query_name)
              window.update
            
              speak("Age")
              query_age = takeCommand()
              var_age.set(query_age)
              window.update()

              speak("Gender")
              query_gender = takeCommand()
              var_gender.set(query_gender)
              window.update()

              speak("Health Problems")
              query_health = takeCommand()
              var_health.set(query_health)
              window.update()

              speak("Doctor Oppointment")
              query_doctor = takeCommand()
              var_Doctor.set(query_health)
              window.update()

              speak("Past History ")
              query_past = takeCommand()
              var_Past.set(query_past)
              window.update()

              speak(" Your Email id   ")
              query_email = takeCommand()
              var_email.set(query_email)
              window.update()

              speak("Your Number ")
              query_number = takeCommand()
              var_Phone.set(query_number)
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
