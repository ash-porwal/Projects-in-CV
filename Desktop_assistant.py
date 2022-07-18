import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour == 12:
        speak("Good Noon!")
    elif hour > 12 and hour <= 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("How may I help you?")
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == '__main__':
    wishMe() 

    while True  :
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5 )
            speak("Acoording to wikipedia")
            print(results)
            speak(results)
        
        if 'time' in query:
            current_time = (datetime.datetime.now().strftime("%H:%M:%S"))
            speak(f"Sir, The time is {current_time}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        # elif 'play random song' or 'play random song' in query:
        #     osho = 'D:\\ashish\\Osho\\Osho MahaGeeta'
        #     songs = os.listdir(osho)
        #     print(songs)
        #     num  = random.randint(1,101)
        #     os.startfile(os.path.join(osho, songs[num]))
