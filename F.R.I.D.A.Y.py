
from calendar import calendar
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
def speak(audio):
    print("F.R.I.D.A.Y: " + audio)
    friday.say(audio)
    friday.runAndWait()
speak("Welcome back boss")
def date():
    Date = datetime.datetime.now().strftime("%A %d %B %Y")
    speak("Today is "+ Date )
date()
def time():
    Time = datetime.datetime.now().strftime("%I:%M %p")
    speak("Is " + Time + " now")
time()
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning sir")
    if hour>=12 and hour<18:
        speak("Good afternoon sir")
    if hour>18 and hour<24:
        speak("Good evening sir")
speak("Have a nice day, boss")
if __name__ ==" __main__ ":
    welcome()
