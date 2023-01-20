#librerias
import webbrowser as wb
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
wikipedia.set_lang('es')

# ventana
app = tk.Tk()
app.geometry('800x500')
app.resizable(width=False,height=False)
bg = PhotoImage(file = "fondo.png")
tk.Wm.wm_title(app, 'Grappes Asisstant')

#manejo de imagen
main_file = os.path.dirname(__file__)
#directorio
folder_img = os.path.join(main_file)


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
        talk('No se detecto ninguna camara')
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
    try:
        wb.open("https://wa.link/7dc5lp") # Link de char directo a Grappes BOT (Posiblemente inactivo)
    except:
        print('Algo ha salido mal...')

#alexa
def talk(text):
    asis.say(text)
    asis.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Hola, te estoy escuchando')
            voice = listener.listen(source)
            sleep(1)
            print("reconociendo...")
            sleep(1)
            print("reconociendo...")
            sleep(1)
            talk("Esto es lo que te he entendido...")
            print("Esto es lo que te he entendido...")
            sleep(0.5)
            command = listener.recognize_google(voice,language="es")
            command = command.lower().strip()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                
            return command
    except:
        return ''
        
def run_alexa():
    command = take_command()
    
    if command == "":
        talk('Lo siento, no te he podido escuchar')
        print('Lo siento, no te he podido escuchar')
        
    else:
        talk(command)
        print(command)         
        if ('ayuda' in command) or ('qué puedes hacer' in command):
            talk('Puedo darte la hora actual, prueba con, dime la hora')
            print('Puedo darte la hora actual, prueba con, dime la hora')
            talk('Puedo darte el clima actual de tu zona, prueba con, dame el clima')
            print('Puedo darte el clima actual de tu zona, prueba con, dame el clima')
            talk('Puedo investigar en la wikipedia, prueba con, dime python o investiga samsung')
            print('Puedo investigar en la wikipedia, prueba con, dime python o investiga samsung')
            talk('Puedo buscarte un video en youtube, prueba con, reproduce musica a alegre')
            print('Puedo buscarte un video en youtube, prueba con, reproduce musica a alegre')
            talk('Puedo abrir la camara de tu dispositivo, prueba con, abre la camara')
            print('Puedo abrir la camara de tu dispositivo, prueba con, abre la camara')
            talk('si no entiendo lo que me pides, lo buscaré en google directamente')
            print('si no entiendo lo que me pides, lo buscaré en google directamente')
            
        elif ('hora' in command) :
            time = datetime.datetime.now().strftime('%I:%M %p')    
            talk('la hora es ' + time) 
            print('La hora es ' + time)
            
        elif ('dime' in command) or ('investiga' in command):
            wiki = command.replace('dime', '')
            wiki = command.replace('investiga', '')
            info = wikipedia.summary(wiki, 2, auto_suggest=True)
            talk(info)
            print(info)
            
        elif 'reproduce' in command:
            song = command.replace('reproduce', '')
            talk('reproduciendo ' + song)
            pywhatkit.playonyt(song)
        
        elif ('clima' in command) or ('tiempo' in command):
            talk(f"Usted se encuentra en: {city}")
            print(f"Usted se encuentra en: {city}")
            clima, temperatura, feels_like = get_weather_report(city)
            talk(f"La temperatura actual es {temperatura}, pero se siente más como {feels_like}")
            print(f"La temperatura actual es {temperatura}, pero se siente más como {feels_like}")
            talk(f"EL clima está {clima}")
            print(f"EL clima está {clima}") 
        
        elif ('camara' in command) or ('cámara' in command):
            talk('abriendo camara')
            print('abriendo camara')
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
