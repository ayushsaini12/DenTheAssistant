import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import calendar
import time
import math
import wikipedia
import webbrowser
import os
import smtplib
# import winsound
import pyautogui
from tkinter import *
from playsound import playsound
import subprocess
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Catching your words....")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Got it...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("sorry can you repeat...")
        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello den this side, how can i help you")


def brightness():
    try:
        query = takeCommand().lower()
        if '25' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1610, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '50' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1684, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '75' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1758, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        elif '100' in query or 'full' in query:
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(1835, 960)
            pyautogui.click()
            pyautogui.moveTo(1880, 1050)
            pyautogui.click()
            speak('If you again want to change brihtness, say, change brightness')
        else:
            speak('Please select 25, 50, 75 or 100....... Say again.')
            brightness()
    except:
        speak('Something went wrong')
        with open ('bright.txt','w') as f:
                f.write(query+ "\n")


def assisrun():

    wishMe()
    while True:
        query = takeCommand().lower()

        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("ok opening youtube")
            break
        elif 'open Amazon Prime' in query or 'open prime' in query:
            webbrowser.open("https://primevideo.com")
            speak('ok opening prime video')
            break
        elif 'open hotstar' in query:
            webbrowser.open("https://hotstar.com")
            speak('ok opening hotstar')
            break
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            break
        elif 'open netflix' in query:
            webbrowser.open('https://www.netflix.com/in/')
            speak('ok opening netflix')
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "den" in query or "hi there" in query:

            wishMe()
            speak("den in your service")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Universe.")
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            break
        elif 'stop' in query:
            speak("thank you for using den")
            break
        elif 'ok stop' in query:
            speak("thank you for using den")
            break
        elif 'terminate' in query:
            speak("thank you for using den")
            break
        elif 'bye' in query:
            speak("Bye sir")
            break
        elif 'calculat' in query:
            os.system('calc.exe')
            break
        elif 'add' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'ad' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif '+' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'plus' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'subtract' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'minus' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif 'multipl' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open my calculator.')
        elif ' x ' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open calculator.')
        elif 'slash' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open calculator.')
        elif '/' in query:
            speak(
                'If you want to do any mathematical calculation then give me a command to open calculator.')
        elif ('increase' in query or 'decrease' in query or 'change' in query or 'minimize' in query or 'maximize' in query) and 'brightness' in query:
            speak('At what percent should I kept the brightness, 25, 50, 75 or 100?')
            brightness()
        elif 'open map' in query or ('let' in query and 'map' in query and 'open' in query):
            speak('ok opening maps.')
            webbrowser.open('https://www.google.com/maps')
            break
        elif 'google maps' in query or ('let' in query and 'map' in query and 'open' in query):
            speak('ok opening maps.')
            webbrowser.open('https://www.google.com/maps')
            break
        elif 'news' in query:
            webbrowser.open('https://www.bbc.com/news/world/asia/india')
            break
        elif 'online shop' in query or (('can' in query or 'want' in query or 'do' in query or 'could' in query) and 'shop' in query) or ('let' in query and 'shop' in query):
            speak(
                'From which online shopping website, you want to shop? Amazon or flipkart?')
            query = takeCommand().lower()
            if 'amazon' in query:
                speak('ok opening amazon')
                webbrowser.open('https://www.amazon.in')
                break
            elif 'flip' in query:
                webbrowser.open('https://www.flipkart.com')
                break
            else:
                speak(
                    'Sorry sir, the website are you talking about is new to me.')
            break
        elif 'dictionary' in query:
            webbrowser.open('https://www.dictionary.com')
            time.sleep(3)
            speak('Enter the word, in the search bar of the dictionary, whose defination or synonyms you want to know')
            break
        elif 'cabs' in query or (('can' in query or 'want' in query or 'do' in query or 'could' in query) and 'taxi' in query):
            speak(
                'From which service do you like to get a cab.')
            query = takeCommand().lower()
            if 'ola' in query:
                speak('ok opening ola')
                webbrowser.open('https://www.olacabs.com')
                break
            elif 'uber' in query:
                speak('ok opening uber')
                webbrowser.open('https://www.uber.com')
                break
            elif 'rapido' in query:
                speak('ok opening rapido')
                webbrowser.open('https://www.rapido.bike/')
                break
            else:
                speak(
                    'Sorry sir, the website are you talking about is new to me.')
            break

        elif 'food' in query or (('can' in query or 'want' in query or 'do' in query or 'could' in query) and 'food' in query) or ('hungry' in query):
            speak(
                'from which platform do you like to get some food.')
            query = takeCommand().lower()
            if 'swiggy' in query:
                speak('ok opening swiggy')
                webbrowser.open('https://www.swiggy.com')
                break
            elif 'zomato' in query:
                speak('ok opening zomato')
                webbrowser.open('https://www.zomato.com')
                break
            else:
                speak(
                    'Sorry sir, the website are you talking about is new to me.')
            break
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak('ok opening facebook')
            break
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak('ok opening instagram')
            break
        elif 'open twitter' in query:
            webbrowser.open("https://www.twitter.com")
            speak('ok opening twitter')
            break
        else:
            with open ('extra.txt','w') as f:
                f.write(query+ "\n")
        
