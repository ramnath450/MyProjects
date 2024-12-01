import requests
import pyttsx3
import json

city = input("Enter City name : ")
url = f"https://api.weatherapi.com/v1/current.json?key=a326f48af9c04f17add154014241311&q={city}"

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w =wdic["current"]["temp_c"]
print(w)
w1 = wdic["current"]["humidity"]
print(w1)
w2 = wdic["location"]["localtime"]
print(w2)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.getProperty("rate")
engine.setProperty("rate", 150)
engine.say(f"The temperature in {city} is {w} degree celsius and The humidity in {city} is {w1} percent and the time is {w2}")
engine.runAndWait()