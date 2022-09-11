import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

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
            if 'veronica' in command:
                command = command.replace('veronica', '')
                print(command)
    except:
        pass
    return command


def run_veronica():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'what can you do' in command:
        talk("I can play music, tell jokes and search the internet")
    elif 'name' in command:
        talk("Your name is Aryan Shetty")
    elif 'who are you' in command:
        talk("I am an AI designed by Aryan Shetty")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'cricket' in command:
        talk("You are a bowling all-rounder")
    elif 'bye veronica' in command:
        talk("Bye Bye")
        exit()
    else:
        talk('Please say something')


while True:
    run_veronica()
