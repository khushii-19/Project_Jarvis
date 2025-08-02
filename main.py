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
import pygame #to change voice
import os

# will create recognizer object
recognizer = sr.Recognizer()  # it is a class and helps in speech recognition

# initializing pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

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
            song = " ".join(c.split(" ")[1:]).strip()
            if song:
                link = musicLibrary.music.get(song.lower())  # assuming keys are lowercase
                if link:
                    webbrowser.open(link)
                    speak(f"Playing {song}")
                else:
                    speak("Song not found.")
            else:
                speak("Please say the song name after 'play'")
        except:
           speak("Please say the song name after 'play'")
        
    elif "news" in c.lower():
            print("Fetching news...")
            api_key = "15b9845f96014cf985ffefc8752e2912"  # replace this with your actual API key

            url = f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&pageSize=5&apiKey={api_key}"

            response = requests.get(url)
            data = response.json()
            if data["status"] == "ok" and data["articles"]:
                for article in data["articles"]:
                    title = article["title"]
                    print("Title:", title)
                    speak(title)
            else:
                speak("Sorry, I couldn't find any recent news.")

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
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
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






