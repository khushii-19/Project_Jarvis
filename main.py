# pip install speechrecognition pyaudio
# pip install setuptools
# pip install pyttsx3
import speech_recognition as sr  # we can use speech_recognition as sr in code from now used for speech regognition online and offline
import webbrowser  # opens web browser for giving any command to jarvis and its inbuilt module no need to install it
import pyttsx3  # converts text to speech
import musicLibrary
import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai
from gtts import gTTS
import pygame
import os

# will create recognizer object
recognizer = sr.Recognizer()  # it is a class and helps in speech recognition

# initializing pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

newsapi = os.getenv("NEWS_API_KEY")


# function to create speech
def speak_old(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        try:
            song = c.split(" ")[1] #yaha pe play qatal aaya to it will convert it into list by spliting [play , qatal]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Song not found.")
        except:
            speak("Please say the song name after 'play'")
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 

load_dotenv()
def aiProcess(command):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-2.5-pro')
    prompt = f"You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please.\nUser: {command}"
    response = model.generate_content(prompt)
    print(response.text)
    return response.text


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes I am listening")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))



