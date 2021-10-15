import pyaudio # for installing pyaudio try this -pip install pipwin  then pipwin install pyaudio
import pyttsx3 #pip install pyttsx3 - for initialing voice commands
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# I have used sapi5 for voice and used voices[1].id which is a female voice. whereas voices[0].id which is a male voice
# Sapi5 is a Microsoft developed speech API , Helps in systhesis and recoding of voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # getting details of current voice
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''
    This function wil take the audio input and speak it loudly

    '''
    engine.say(audio)
    engine.runAndWait() # Without this command , speech will not be audible to us.


def wishMe():
    '''
     This function will greet you on the basis of hour !
    :return: Time
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am CHERRY Sir, your personal assistant . Please tell me how may I help you")

def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    :return: query - the function you asked cherry about!
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    '''
   This will take email id of the person you want to send email to and its content
   This will call the smtp server to login in the users mail id and send the mail

    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('codewithmavrick@gmail.com', 'cherru@123')
    server.sendmail('codewithmavrick@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            songs_dir = "C:\\Users\\Omkar Magare\\PycharmProjects\\firstProg\\CherryPA\\favsongs" # "C:\\Users\\ormag\\PycharmProjects\\firstProg\\CherryPA\\favsongs"
            song = os.listdir(songs_dir)
            print(song)
            os.startfile(os.path.join(songs_dir,song[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'stop' in query:
            exit()
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "codewithmavrick@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry omkar . I am not able to send this email")
