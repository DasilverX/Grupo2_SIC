from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import re # para limpiar los string
from unicodedata import normalize #normalizar caracteres del español
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

filepath = "./whatsapp_session.txt"
driver = webdriver

def crear_driver_session():
    
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if cnt == 0:
                executor_url = line
            if cnt == 1:
                session_id = line

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)
                
    org_command_execute = RemoteWebDriver.execute

    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    RemoteWebDriver.execute = org_command_execute

    return new_driver


def whatsapp_bot_init():
    global driver
    driver = crear_driver_session()
        
def buscar_chats():
    print("BUSCANDO CHATS")
    sleep(1)
    
    #  VERIFICAR QUE HAYA UN CHAT SELECCIONADO
    # CHAT SELECCIONADO
    if len(driver.find_elements(By.CLASS_NAME,"IVxyB")) == 0:
        print("CHAT ABIERTO")
        message = identificar_mensaje()                                
        if message != None:
            return True
        
    # CHAT NO SELECCIONADO
    else:
        chats = driver.find_elements(By.CLASS_NAME,"_1Oe6M")
        print(len(chats))
        print("BUSCANDO MENSAJES NO LEIDOS")
        for chat in chats:
            chats_mensajes = chat.find_elements(By.CLASS_NAME,"_1pJ9J") # el circulo de mensaje no leido
            if len(chats_mensajes) == 0:
                continue
            else:
                print("MENSAJE SIN LEER")
                chat.click()
                return True
    return False

def identificar_mensaje():
    print("MENSAJE...")
# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    whatsapp_bot_init()
    buscar_chats()
