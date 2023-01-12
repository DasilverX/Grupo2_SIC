#___________________LIBS______________________
import json, pickle, nltk
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense,Dropout
from tensorflow.keras.optimizers import SGD
from nltk.stem import SnowballStemmer

#__________________GLOBAL_VARS___________________
stemmer = SnowballStemmer('spanish')
ignore_words=["?","¿","!","¡"]
data_file= open("intents.json").read()
intents = json.loads(data_file)
    
#________________________TOKENIZADOR___________________
def tokenizer():
    words=[]
    classes=[]
    documents=[]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            w=nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w,intent["tag"]))
            if intent["tag"] not in classes:
                classes.append(intent["tag"])     
    return words,classes,documents

#___________________LEMATIZADOR__________________         
def lematizer(words,classes,documents):  
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words2=words    
    pickle.dump(words,open("words.pkl","wb"))
    pickle.dump(classes,open("classes.pkl","wb"))
    return words2

#______________________PREPROC____________________
def training(words,classes,documents):
    training=[]
    output_empty=[0]*len(classes)
    for doc in documents: 
        bag=[]
        pattern_words=doc[0]
        pattern_words= [stemmer.stem(word.lower()) for word in pattern_words  if word not in ignore_words ]
        for palabra in words:
            bag.append(1) if palabra in pattern_words else bag.append(0) 
        output_row =list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag,output_row])
    training=np.array(training) 
    x_train= list(training[:,0])
    y_train= list(training[:,1])  
    return x_train,y_train

#______________________MODEL_BUILDER__________________
def model_builder(x_train,y_train):
    model = Sequential()
    model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64,activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(y_train[0]),activation='softmax'))
    sgd=SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True) 
    model.compile(loss="categorical_crossentropy",optimizer=sgd,metrics=["accuracy"])
    hist=model.fit(np.array(x_train),np.array(y_train),epochs=300,batch_size=5,verbose=1)
    model.save("chatbot_model.h5",hist)

#_____________________MODEL_STARTER__________________
def start_model():   
    words,classes,documents = tokenizer()
    words2 = lematizer(words,classes,documents)
    x_train, y_train = training(words2, classes, documents)
    model_builder(x_train,y_train)   
