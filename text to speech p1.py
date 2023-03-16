import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
app = Tk()
app.geometry('350x350')
app.resizable(0,0)
app.config(bg = 'Yellow')
app.title('Nishant Shishodia- Text-to-speech-recognition')
Label(app, text = 'Text-to-speech-recognition' , font='arial 20 bold' , bg ='yellow').pack()
Label(app, text ='Nishant Shishodia' , font ='arial 15 bold', bg = 'yellow').pack(side = BOTTOM)
Label(app, text ='Please Enter Your Text', font ='arial 15 bold', bg ='yellow').place(x=20,y=60)
Msg = StringVar()
entry_field = Entry(app,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)
def Text_to_speech_recognition():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Nishant Shishodia.mp3')
    playsound('Nishant Shishodia.mp3')
    os.remove('Nishant Shishodia.mp3')
def Exit():
    app.destroy()
def Reset():
    Msg.set("")
Button(app, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech_recognition, width =4).place(x=25, y=140)
Button(app,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(app, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)
app.mainloop()