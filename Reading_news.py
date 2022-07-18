from unittest import result
import requests
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=fa984c183c7342bf9982e17c61c8e341")

result = data.json()
print()

print("Articles:")
news = result['articles']

print()

if __name__ == "__main__":
    speak("Top Today's News trending in India:")
    for i  in range(0,10):
        print(i+1, end="- ")
        print(news[i]['description'])
        print()
        speak(news[i]['description'])
        if i == 8:
            speak("So our last news for today is ")
        elif i>=9:
            break
        else:
            speak("Moving To Our next news")
        
    speak("That is all for today, have a good day!")