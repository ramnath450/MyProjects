import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import time

def sptext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            print("Recognizing.....")
            data=r.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 100)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":

    if "hello alexa" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "My name is aditaya"
                speechtx(name)
            elif "old are you" in data1:
                age = "I am 2 years old"
                speechtx(age)

            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            
            elif "youtube" in data1:
                webbrowser.open("www.youtube.com")

            elif "codecademy" in data1:
                webbrowser.open("www.codecademy.com")

            elif "play song" in data1:
                add = "C://Users/aditaya/Downloads/song"
                listsong = os.listdir(add)
                os.startfile(os.path.join(add, listsong[1]))

            elif "exit" in data1:
                speechtx("thankyou")
                break
            time.sleep(10)

    else:
        print("thanks")