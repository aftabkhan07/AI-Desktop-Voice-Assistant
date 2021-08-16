#imp go on terminal (python -m venv venv)
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 475
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
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def dice():
    min_val = 1
    max_val = 6
    result=random.randint(min_val, max_val)
    speak (result)

def flipcoin():
    min_val = 1
    max_val = 2
    result=random.randint(min_val, max_val)
    if result==1:
        speak("Its heads")
    else:
        speak("Its tails")

def rockpaperscissor():
    choices = ["Rock", "Paper", "Scissor"]
    computer = random.choice(choices)
    player = False
    cpu_score = 0
    player_score = 0

    while True:
        speak("choose...")
        player =takeCommand().capitalize()
        ## Conditions of Rock,Paper and Scissor

        if player == computer:
            speak("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                speak("You lose!"+computer+ "covers"+ player)
                cpu_score+=1
            else:
                speak("You win!"+player+"smashes"+computer)
                player_score+=1
        elif player == "Paper":
            if computer == "Scissor":
                speak("You lose!"+computer+"cut"+player)
                cpu_score+=1
            else:
                speak("You win!"+player+ "covers"+ computer)
                player_score+=1
        elif player == "Scissor":
            if computer == "Rock":
                speak("You lose..."+computer+"smashes"+player)
                cpu_score+=1
            else:
                speak("You win!"+player+"cut"+computer)
                player_score+=1
        elif player=='Stop':
            speak("Final Scores:")
            speak(f"CPU:{cpu_score}")
            speak(f"Plaer:{player_score}")
            break

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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Javed' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "youremailEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my Mr Khan. I am not able to send this email")
        
        elif 'roll a dice' in query:
            speak("Rolling the dice....")
            dice()

        elif 'flip a coin' in query:
            speak("flipping the coin....")
            flipcoin()

        elif 'let\'s play' in query:
            speak("Ok Lets play rock paper scissor")
            rockpaperscissor()

        elif 'stop' in query:
            speak("Thankyou Sir, always happy to help")
            break    
