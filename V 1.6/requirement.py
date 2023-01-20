import pip, nltk

def requirement_start():
    pip.main(["install","numpy==1.21.5"])
    pip.main(["install","nltk==3.7"])
    pip.main(["install","tensorboard==2.10.1"])
    pip.main(["install","tensorflow-estimator==2.10.0"])
    pip.main(["install","keras==2.10.0"])
    pip.main(["install","Keras-Preprocessing == 1.1.2"])
    pip.main(["install","tensorflow==2.10.1"])
    pip.main(["install","selenium==4.7.2"])
    pip.main(["install","wikipedia == 1.4.0"])
    pip.main(["install","SpeechRecognition == 3.9.0 "])
    pip.main(["install","pyaudio == 0.2.13"])
    pip.main(["install","pywhatkit == 5.4"])
    
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('universal_tagset')
    nltk.download('spanish_grammars')
    nltk.download('tagsets')
    nltk.download('stopwords')
    nltk.download('omw-1.4')
