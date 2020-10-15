import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from googlesearch import search

#Setting up pyttsx3 and voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Defininf take command function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #To increase pause
        audio = r.listen(source)

        try:
            print("Understanding...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except Exception:
            print("I was unable to understand that. Please say that again...")
            return "None"
    return query

#Defining the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Defining the wish me function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    
    speak("I am your virtual friend. Please tell me how may I help you")



if __name__ == "__main__":
    wishme()
    while(True):
        q = takeCommand()
        if 'friend' in q:
            query = takeCommand().lower()

            #Executing Tasks

            if 'wikipedia' in query:
                speak("Searching in wikipedia...")
                query = query.replace("wikipedia", "") 
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)
        
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")
            
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            
            elif 'play music' in query:
                music_dir = 'music'
                songs = os.listdir(music_dir)
                indx = random.randint(0, len(songs))
                speak("Playing " + songs[indx])
                os.startfile(os.path.join(music_dir, songs[indx]))
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir ,The time is {strTime}")
            
            elif 'open brave' in query:
                bravePath = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                os.startfile(bravePath)