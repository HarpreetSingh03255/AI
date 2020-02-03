import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voice=engine.getProperty('voice')

engine.setProperty('voice',voice[0])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning! ")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon ")
    elif hour >=18:
        speak("Good Evening ")
    speak("I am HS Chatbot What can I do for you?")   
def sendemail(to,content1):
   f=open('pass.txt','r')
   str2=f.read()
   with smtplib.SMTP('smtp.gmail.com',587) as server:
       server.ehlo()
       server.starttls()
       server.login('honeyharpreet5669@gmail.com',str2)
       server.sendmail('honeyharpreet5669@gmail.com',to,content1)
       server.quit()
        
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening")
        r.pause_threshold = 0.5
        r.energy_threshold+=280
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
        
        try:
            query=r.recognize_google(audio,language='en-GB')
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language='en-GB'))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            speak("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            speak("Could not request results from Google Speech Recognition service")
        except Exception as e:
            print("try again")    
        
    return query   
    

if __name__ == "__main__":

    speak("hello sir")
    wishme()
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open linkedin' in query:
            webbrowser.open("linked.com")    
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir,The Time is"+strTime)
        elif 'visual studio' in query:
            vpath="C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Preview\\Common7\\IDE\\devenv.exe"
            os.startfile(vpath)
        elif 'u m s lpu' in query:
            webbrowser.open("ums.lpu.in")
        elif 'premiere pro' in query:
            prpath="C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2017\\Adobe Premiere Pro.exe"
            os.startfile(prpath)
        elif 'email':
            try:
                speak("What should I say")
                content=takecommand().lower()
                to='harpreetsingh03255@gmail.com'
                sendemail(to,content)
                speak("Sent")
                print("sent")
            except Exception as e:
                speak("Sorry the email was not being sent")    
                print("the email was not being sent")
        

            



        

       


