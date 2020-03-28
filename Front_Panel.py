from tkinter import *
import speech_recognition as sr
import pyttsx3
import os
import threading


def window():

    window = Tk()
    window.geometry("390x590+500+50")
    window.title('Main panel')
    window.configure(background="floralwhite")
    photo = PhotoImage(file="C:/Users/Nkb/Downloads/Assistant.gif")

    myLabel1 = Label(image=photo,width = 400,height=400,bg='floralwhite',fg="floralwhite")
    myLabel1.pack()
    myLabel1.place(x=0,y=0)

    mylabel_name = Label(text="Dr.Shree",font="Sans-Serif 10 bold",bg="Pink",fg="Purple")
    mylabel_name.pack()
    mylabel_name.place(x=0,y=5,width=100)

    global var1
    var1 = StringVar()

    bar = Label(textvar=var1,font="Monospace 10 ",bg="Pink",fg="red")
    bar.pack()
    bar.place(x=0,y=550,width=390,height=40)
    window.mainloop()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

       
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
       
        print("Recoginizers.....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say it again please sir")
        return "None"
       
    return query




if __name__ == "__main__":
    window()
    takeCommand()
    

