#librerias
from time import sleep
from tkinter import *
import tkinter as tk
import os
import cv2 as cv
import requests
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
asis = pyttsx3.init()

voices = asis.getProperty('voices')
asis.setProperty('voice', voices[0].id)

# ventana
app = tk.Tk()
app.geometry('800x500')
app.resizable(width=False,height=False)
bg = PhotoImage(file=r'C:\Users\josea\Desktop\proyecto SIC\Grupo2_SIC\V 1.6\SIC-Foto-de-Grupo-1024x680.png')
#app.configure(background=bg)
tk.Wm.wm_title(app, 'Grappes Asisstant')


#manejo de imagen
main_file = os.path.dirname(__file__)
#directorio
folder_img = os.path.join(main_file,r"C:\Users\josea\Desktop\proyecto SIC\Grupo2_SIC\imagen")


#icono de ventana
app.iconbitmap(os.path.join(folder_img,"icono.ico"))

#clima



def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

#Función para conseguir el clima según dirección ip
def get_weather_report(city):
    api_key="e3453007916c7512aeb9747917270fe3"
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=sp&appid={api_key}&units=metric").json()
    weather = res["weather"][0]["description"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

ip_address = find_my_ip()
city = requests.get(f"https://ipapi.co/{ip_address}/city/").text


#abrir camara
def abrir_camara():
    capturarVideo = cv.VideoCapture(0)
    if not capturarVideo.isOpened():
        print('No se detecto ninguna camara')
        exit()
    while True:
        _,frame = capturarVideo.read()
        grises = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('Camara',frame)
        if cv.waitKey(1) == ord('q'):
            break
    capturarVideo.release()
    cv.destroyAllWindows()


#abrir bot
def abrir_chatbot():
    print('si funciona')
    os.system('cmd /c ')




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
            sleep(3)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:   
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)         
           
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
    
    elif 'clima' in command:
        print(f"Usted se encuentra en: {city}")
        clima, temperatura, feels_like = get_weather_report(city)
        print(f"La temperatura actual es {temperatura}, pero se siente más como {feels_like}")
        print(f"EL clima está {clima}") 
    
    elif 'canara' in command:
        abrir_camara()

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
    text='Bienvenido al asistente virtual Grappes',
    font=('Courier',22),
    fg='white',
    bg='#00a8e8',
    justify='center',
    relief='raised',
    ).pack(
        ipady=10
    )

tk.Button(
    app,
    text='Abrir Grappes_BOT',
     font=('Courier',14),
     bg='black',
     fg='white',
     command=abrir_chatbot,
     activebackground='#00a8e8',
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
    text='Abrir Grappes Asistente',
     font=('Courier',14),
     bg='black',
     fg='white',
     command=run_alexa,
     activebackground='#00a8e8',
     borderwidth=15,
     relief='groove',
     overrelief='raised',
     cursor='pirate'
    ).pack(
     side=LEFT,
     expand=1,
     pady=20
 )



#loop de la ventana
app.mainloop()