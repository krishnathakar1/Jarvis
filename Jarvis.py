import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    print("Initialising project jarvis...")
    speak("Initialising project jarvis...")

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir!")
        speak("Good Morning Sir!.")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!")
        speak("Good Afternoon Sir!.")

    else:
        print("Good Evening Sir!")
        speak("Good Evening Sir!.")

    print("How may I help you ?")
    speak("How may I help you ?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening your command...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry sir I didn\'t hear that properly...Can you please repeat ?",e)
        speak("Sorry sir I didn\'t hear that properly...Can you please repeat ?")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        #Search on wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #Wish birthday
        elif 'it\'s divyam birthday today' in query:
            print("Hey Divyam, Its Jarvis here. Wish you a very Happy Birthday")
            speak("Hey Divyam, Its Jarvis here. Wish you a very Happy Birthday")

        #open youtube
        elif 'jarvis open youtube' in query:
         webbrowser.open("youtube.com")

        #open google
        elif 'jarvis open google' in query:
            webbrowser.open("google.com")

        #open stackoverflow
        elif 'jarvis open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        #music
        elif 'jarvis play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        #time
        elif 'jarvis what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        #location
        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on, I will show you where " + location + " is.")
            os.system('cmd /k "start chrome https://www.google.nl/maps/place/"'+ location)
            # os.system("start chrome https://www.google.nl/maps/place/" + location)

        #email
        elif 'email to krishna' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kthakar@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend krishna bhai. I am not able to send this email")


         #calculator
        elif 'add two numbers' in query:
            print("Inside Calculator")
            try:
                speak("Please give me a value")
                a = takeCommand()
                a = int(a)
                speak("Please give me another value")
                b = takeCommand()
                b = int(b)
                s = a + b
                print(s)
                speak(str(s))

            except:
                print("Error")

        else:
            print("Sorry sir, I cant do that for this moment but my developer is constantly upgrading me")
            speak("Sorry sir, I cant do that for this moment but my developer is constantly upgrading me")