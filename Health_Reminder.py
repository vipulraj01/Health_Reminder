from pygame import mixer
from datetime import datetime
def getdate():
    return datetime.datetime.now()
while True:
    t =datetime.now()
    currenttime = t.strftime("%H:%M:%S")
    watertime = {"09:00:00","10:00:00","11:00:00","12:00:00","13:00:00","14:00:00","15:00:00","16:00:00","17:00:00"}
    eyetime = {"09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00","12:00:00","12:30:00","13:00:00","13:30:00","14:00:00","14:30:00","15:00:00","15:30:00","16:00:00","16:30:00","17:00:00"}
    physicaltime= {"09:45:00","10:30:00","11:15:00","12:00:00","12:45:00","13:30:00","14:15:00","15:00:00","15:45:00","16:30:00"}
    if currenttime == watertime:
        mixer.init()
        mixer.music.load("Water.mp3")
        mixer.music.play()
        while True:
            print("Its Your Water Drinking Time. Please Drink Water")
            print("Please type drank if you had drank the water")
            f = open("drinkwater.txt","a")
            user = input(" ")
            time = str(getdate())
            f.write(user + "[" + time +user+ "]")
            f.close
            if user == "drank":
                mixer.music.pause()
            elif watertime == eyetime:
                mixer.init()
                mixer.music.load("Eye.mp3")
                mixer.music.play()
                while True:
                    print("Its Your Eye Exercise Time. Please Do Eye Exercise")
                    print("Please type Eydone if you had done the Eye Exercise")
                    f = open("eyeexercise.txt","a")
                    user = input(" ")
                    time = str(getdate())
                    f.write(user + "[" + time +user+ "]")
                    f.close
                    if user == "Eydone":
                        mixer.music.pause()
            elif watertime == physicaltime:
                mixer.init()
                mixer.music.load("Physical.mp3")
                mixer.music.play()
                while True:
                    print("Its Your Physical Exercise Time. Please Do Physical Exercise")
                    print("Please type Exdone if you had done the Physical Exercise")
                    f = open("physical.txt","a")
                    user = input(" ")
                    time = str(getdate())
                    f.write(user + "[" + time +user+ "]")
                    f.close
                    if user == "Exdone":
                        mixer.music.pause()
    if currenttime == eyetime:
        mixer.init()
        mixer.music.load("Eye.mp3")
        mixer.music.play()
        while True:
            print("Its Your Eye Exercise Time. Please Do Eye Exercise")
            print("Please type Eydone if you had done the Eye Exercise")
            f = open("eyeexercise.txt","a")
            user = input(" ")
            time = str(getdate())
            f.write(user + "[" + time +user+ "]")
            f.close
            if user == "Eydone":
                mixer.music.pause()
            elif watertime == physicaltime:
                mixer.init()
                mixer.music.load("Physical.mp3")
                mixer.music.play()
                while True:
                    print("Its Your Physical Exercise Time. Please Do Physical Exercise")
                    print("Please type Exdone if you had done the Physical Exercise")
                    f = open("physical.txt","a")
                    user = input(" ")
                    time = str(getdate())
                    f.write(user + "[" + time +user+ "]")
                    f.close
                    if user == "Exdone":
                        mixer.music.pause()
    if currenttime == physicaltime:
        mixer.init()
        mixer.music.load("Physical.mp3")
        mixer.music.play()
        while True:
            print("Its Your Physical Exercise Time. Please Do Physical Exercise")
            print("Please type Exdone if you had done the Physical Exercise")
            f = open("physical.txt","a")
            user = input(" ")
            time = str(getdate())
            f.write(user + "[" + time +user+ "]")
            f.close
            if user == "Exdone":
                mixer.music.pause()
        
        
                
                
                

    
       
        