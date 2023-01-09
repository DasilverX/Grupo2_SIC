# Samsung innovation campus
# by: Profe Jose
# python version : 3.9.12
# libraries:
    #keras                         2.10.0
    #Keras-Preprocessing           1.1.2
    #nltk                          3.7
    #numpy                         1.21.5
    #tensorflow                    2.10.1
    #tensorflow-estimator          2.10.0
    #tensorflow-io-gcs-filesystem  0.27.0
    
def start():
    import pip
    
    pip.main(["install","numpy==1.21.5"])
    pip.main(["install","nltk==3.7"])
    pip.main(["install","tensorboard==2.10.1"])
    pip.main(["install","tensorflow-estimator==2.10.0"])
    pip.main(["install","keras==2.10.0"])
    pip.main(["install","Keras-Preprocessing==1.1.2"])
    pip.main(["install","tensorflow==2.10.1"])
    pip.main(["install","selenium"])    
        
    
# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start()
