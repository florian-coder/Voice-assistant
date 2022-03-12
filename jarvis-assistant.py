import datetime
import os
import sys
import webbrowser
from time import sleep
import pywhatkit as kit
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import python_weather
import asyncio

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
ab = 0

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

async def getweather(w):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Washington DC")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()
def run_jarvis():
    nr=0
    command = take_command()
    print(command)
  #  if 'what is the weather in' in command:
      #  place = command.replace('in', '')
        #talk('the weather in' + place + 'is' )
      #  getweather(place)
        #loop = asyncio.get_event_loop()
       # loop.run_until_complete(getweather())
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open notepad' in command:
            talk("opening notepad")
            os.system('notepad.exe')  # porneste notepad
    elif 'open wordpad' in command:
        talk("opening wordpad")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\WordPad')
    elif 'open paint' in command:
        talk("opening paint")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint')
    elif'go away' in command:
        talk('I am happy that I was helpful master' + name + '. Have a nice day!')
        sys.exit(':)')
    elif 'thank you' in command:
        talk("My pleasure master" + name)
    elif 'search' in command:
        search_term = command.replace('search', '')
        url = "https://www.google.com.tr/search?q={}".format(search_term)
        webbrowser.open(url)
    elif 'what is' in command:
        word = command.replace('what is', '')
        talk(kit.info(word))
    elif 'open' in command:
        word = command.replace('open', '')
        talk('opening' + word)
        #chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        #os.startfile(chrome_path)

        if word == 'youtube':
            url = "https://www.youtube.com"
            os.system("start \"\" https://www.youtube.com/")

        if word == 'instagram':
            webbrowser.open_new_tab('https://www.instagram.com/')
        if word == 'chess':
            webbrowser.open('https://www.chess.com/home', new=1)
    elif 'close' in command:
       word = command.replace('close', '')
       if word == ' google':
            os.system("TASKKILL /F /IM chrome.exe")

    elif 'change your voice' in command:
        nr=nr+1
        nr=nr%2
        engine.setProperty('voice', voices[nr].id)
    else:
        talk('Please say the command again master Florian.')

talk("Hello. Tell me your name to continue:")
print("Hello. Tell me your name to continue:")
command = take_command()
name = command
talk("Hello master" + name + " Tell me the password to continue:")
print("Hello master" + name + " Tell me the password to continue:")
password = "1"

while ab ==0:
    command = take_command()
    if command == password:
        ab=1
        break
    print(command)
    talk('Please repeat the password')
    print('Please repeat the password')
if ab == 1:
    talk('I am here at your service master '+ name)
    print('I am here at your service master' + name)
while ab == 1:
    run_jarvis()

