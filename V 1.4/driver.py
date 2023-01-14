from time import sleep
from os.path import isfile
# _________________________________MAIN________________________
# Driver program
if __name__ == '__main__':

    
    from requirement import requirement_start
    print("Checking requirements...")
    requirement_start()
    sleep(1)

    if not isfile("intents.json"):
        from intents_reference import start_intents
        print("Creating intents...")
        start_intents()
        sleep(1)
        
    if not isfile("chatbot_model.h5"):
        from model_builder import start_model
        print("Creating model...")
        start_model()
        sleep(1)
    
    from keep_session import start_keep_session
    print("Startign session...")
    start_keep_session()
    sleep(1)
        
    from whatsapp_bot import whatsapp_bot_init
    print("Startign chatbot...")
    whatsapp_bot_init()
