#__________________LIBS_____________________
import nltk, json, pickle, random
import numpy as np
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model

#__________________GLOBAL_VARS_____________________
stemmer = SnowballStemmer('spanish')
model=load_model("chatbot_model.h5")
intents= json.loads(open("intents.json").read())
words=pickle.load(open("words.pkl","rb"))
classes=pickle.load(open("classes.pkl","rb"))


def clean_up_sentence(sentence):
    sentence_words=nltk.word_tokenize(sentence) # tokenizamos
    sentence_words=[stemmer.stem(word.lower()) for word in sentence_words] #lematizamos
    return sentence_words

def bow (sentence,words,show_details=True):
    sentence_words=clean_up_sentence(sentence)
    bag=[0]*len(words)
    for i in sentence_words:
        for j, w in enumerate(words):
            if w==i:
                bag[j]=1
    return (np.array(bag))

def predict_class(sentence,model):
    p = bow(sentence,words,show_details=False)    
    res = model.predict(np.array([p]))[0]   
    ERROR_THRESHOLD = 0.55   
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD] 
    results.sort(key = lambda x: x[1], reverse = True)  
    return_list = []    
    for r in results:   
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})   
    return return_list 

def get_response(ints,intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]    
    for i  in list_of_intents: 
        if (i["tag"] == tag):
            result = random.choice(i["responses"])
            break
    return result
    
def chatbot_response(text): 
    ints = predict_class(text,model)
    res = get_response(ints,intents)
    return res
    
def bot(texto_us):
        res = chatbot_response(texto_us)
        return res
