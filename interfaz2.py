#librerias
from tkinter import *
import tkinter as tk
import os
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
listener = sr.Recognizer()
asis = pyttsx3.init()

voices = asis.getProperty('voices')
asis.setProperty('voice', voices[0].id)

# ventana
app = tk.Tk()
app.geometry('800x200')
app.resizable(width=False,height=False)
bg = PhotoImage(file='fondo.png')
#app.configure(background=bg)
tk.Wm.wm_title(app, 'J.A.R.V.I.S')


#manejo de imagen
main_file = os.path.dirname(__file__)
#directorio
folder_img = os.path.join(main_file,"imagen")


#icono de ventana
app.iconbitmap(os.path.join(folder_img,"icono.ico"))



#alexa
def talk(text):
    asis.say(text)
    asis.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Hola, te estoy escuchando')
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language="es")
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:   
        pass
    return command


def run_alexa():
    command = take_command()
    print (command)         
           
    if ('hora' in command) or ('tiempo' in command):
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('la hora es ' + time)
        talk('la hora es ' + time) 
        
    elif 'dime' in command:
        wiki = command.replace('dime', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info) 
        
    elif 'reproduce' in command:
        song = command.replace('reproduce', '')
        talk('reproduciendo ' + song)
        pywhatkit.playonyt(song)
        
    else:
        talk('Buscando en google para ti')
        pywhatkit.search(command)


#funcion para salir del programa
def salir():
    app.quit()


tk.Label(
    app,
    image=bg,
).place(
    x=0,
    y=0
)

tk.Label(
    app,
    text='Bienvenido al asistente virtual J.A.R.V.I.S',
    font=('Courier',22),
    fg='white',
    bg='#00a8e8',
    justify='center',
    relief='flat'
    ).pack()

tk.Button(
    app,
    text='Iniciar',
     font=('Courier',14),
     bg='black',
     fg='white',
     command=run_alexa,
     activebackground='#F50743',
     borderwidth=15,
     relief='groove',
     overrelief='raised',
     cursor='heart'
 ).pack(
     side=RIGHT,
     expand=1,
     pady=20
 )

tk.Button(
    app,
    text='Salir',
     font=('Courier',14),
     bg='black',
     fg='white',
     command=salir,
     activebackground='#F50743',
     borderwidth=15,
     relief='groove',
     overrelief='raised',
     cursor='pirate'
    ).pack(
     side=LEFT,
     expand=1,
     pady=20
 )




app.mainloop()