from tkinter import *
import tkinter as tk
import cv2
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import winshell
import requests
import wolframalpha
import pywhatkit as pwt
import json
import pyowm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = tk.Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 >= hour <= 12:
        var.set("Hello ! Good Morning ")
        window.update()
        speak("Hello ! Good Morning !")
    elif 12 > hour <= 18:
        var.set("Hello ! Good Afternoon !")
        window.update()
        speak("Hello ! Good Afternoon !")
    else:
        var.set("Hello ! Good Evening ")
        window.update()
        speak("Hello ! Good Evening !")
    speak("Myself RAMBO! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source, timeout=1, phrase_time_limit=15)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        speak("Pardon me, please say that again")
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='green')
    wishme()
    while True:
        btn1.configure(bg='dark blue')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            speak("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            break


        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")



        elif ('old are you' in query) or ('version' in query):
            var.set("Version 1")
            window.update()
            speak(" Version 1 Sir.")



        elif 'your name' in query:
            var.set("Myself RAMBO")
            window.update()
            speak("Myself RAMBO")



        elif 'who made you' in query:
            var.set("My Creator is Ayush, Arun ,Aditya and Hritik")
            window.update()
            speak("My Creator is Ayush, Arun ,Aditya and Hritik")



        elif 'sleep' in query:
            var.set('Sleeping...............')
            window.update()
            speak("OK !! time to sleep have a good day")
            quit()



        # System date and time
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%I %M %S %p")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)



        elif 'date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)




        elif 'open setups' in query:
            try:
                var.set("Opening Software")
                window.update()
                speak("Opening Software")
                os.startfile("G:\\Setups")
            except EXCEPTION as e:
                speak(e)
                print(e)
                window.update()



        elif 'series' in query:
            try:
                var.set("Opening OTD Series")
                window.update()
                speak("Opening OTD Series")
                os.startfile("F:\\series")
            except Exception as e:
                speak(e)
                print(e)
                window.update()




        elif 'open pycharm' in query:
            try:
                var.set("Opening Pycharm")
                window.update()
                speak("Opening Pycharm")
                os.startfile("E:\\Pycharm\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe")
            except Exception as e:
                speak(e)
                print(e)
                window.update()




        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")



        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")




        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')






        elif 'open python' in query:
            try:
                var.set("Opening Python")
                window.update()
                speak("Opening Python")
                os.startfile("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\python.exe")
            except Exception as e:
                speak(e)
                print(e)
                window.update()




        elif 'open anaconda' in query:
            try:
                var.set('Opening Anaconda')
                window.update()
                speak('opening anaconda')
                os.startfile("C:\\Users\\Dell\\Anaconda3\\pythonw.exe")
            except Exception as e:
                speak(e)
                print(e)
                window.update()



        elif 'news' in query:
            var.set('Opening news')
            window.update()
            api = "dbf4d2c568c045b2b59dbfc7eccc7045"
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api
            news = requests.get(url).json()
            article = news['articles']
            news = []
            for i in article:
                news.append(i['title'])

            for j in range(len(news)):
                speak(news[j])
                print(news[j])



        elif ('play music' in query) or ('music' in query):
            var.set('Here are your favorites')
            window.update()
            speak('Here are your favorites')
            music_dir = 'G:\\Best Of Bollywood Top 50 Songs'
            songs = os.listdir(music_dir)
            n = random.randint(0, 49)
            os.startfile(os.path.join(music_dir, songs[n]))



        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia :")
            speak(result)


        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")



        elif "where is" in query:                   # Google Map access
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")




        elif 'weather' in query:  # Open weather API
            api_key = "154644d7d2634138b6ebfd5a62ad36e4"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))



        elif 'on youtube' in query:  # Open anything on youtube
            song = query.replace('play', '')
            var.set('Playing on Youtube')
            speak('playing' + song)
            pwt.playonyt(song)

        elif 'calculate' in query:
            t = takeCommand()
            api = "5RTGTX-T469EH5QP9"
            client = wolframalpha.Client(api)
            res = client.query(t)

            answer = next(res.results).text
            var.set(answer)
            window.update()
            speak(answer)
            print(answer)



        elif 'open camera' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
                stream.release()

#GUI

def update(ind):
    frame = frames[ind % 10]
    ind += 1
    label.configure(image=frame)
    window.after(10, update, ind)


label2 = Label(window, textvariable=var1, bg='#730cfa')
label2.config(font=("Fixedsys", 30))
var1.set('YOU SAID:')
label2.pack(pady=10)

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Fixedsys", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='', format='gif -index %i' % i) for i in range(100)]
window.title('RAMBO ')

label = Label(window, width=500, height=150)
label.pack(pady=135)
window.after(0, update, 0)


def mode1():
    window.configure(bg='black')


def mode2():
    window.configure(bg='#f0f0f0')


btn0 = Button(text='SAY HI', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='START', width=20, command=play, bg='DARK BLUE')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='QUIT', width=20, command=window.destroy, bg='RED')
btn2.config(font=("Courier", 12))
btn2.pack()
btn3 = Button(window, text='DARK MODE', width=20, command=mode1, bg='Black', fg='White')
btn3.config(font=("Courier", 12))
btn3.pack()
btn4 = Button(window, text='LIGHT MODE', width=20, command=mode2, fg='Black', bg='WHITE')
btn4.config(font=("Courier", 12))
btn4.pack()

window.mainloop()
