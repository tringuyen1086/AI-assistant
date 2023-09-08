import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# initialize voice recognizer (listener)
listener = sr.Recognizer()

# initialize speech and set up voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

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
            if 'Triz' in command:
                command = command.replace('Triz', '')
                print(command)
    except:
        pass
    return command

def run_AI():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'how you doing' in command:
        talk('I am doing great. Thank you for asking. How about yourself?')
        if 'fine' or 'thank you' in command:
            talk('sounds great')
    elif 'what is your name' in command:
        talk('My dad named me Triz. I am a virtual assistant who are willing to help you with your questions')
    elif 'how old are you' in command:
        talk('I was born on August 18, 2023.')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p') #time with am or pm %p = am or pm
        print(time)
        talk('The current time is ' + time)
    elif 'who' in command:
        person = command.replace('who ', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what' in command:
        subject = command.replace('what', '')
        info2 = wikipedia.summary(subject, 2)
        print(info2)
        talk(info2)
    elif 'do you love me' in command:
        talk('Yes, I do love you so much')
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'do you have a boyfriend' in command:
        talk('No, I am too young to be in a relationship')
    else:
        talk('Would you please say the command again')

run_AI()

while True:
    run_AI()


# resources:
# https://pypi.org/project/SpeechRecognition/
# https://pypi.org/project/pyttsx3/.
# https://pypi.org/project/PyAudio/
# https://pypi.org/project/pywhatkit/
# https://pypi.org/project/pyjokes/