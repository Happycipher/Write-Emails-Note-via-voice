import pyttsx3
import speech_recognition as sr
import os
import smtplib
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def clear():
  os.system('cls')

def takeCommand():
    #It takes michrophone input from the user and returns output

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Reconizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
       #print(e)
       print("Can you please repeat")
       speak("Can you please repeat")
       return ""
    return query

def voiceboard():
    #It takes michrophone input from the user and returns output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 5.0
        audio = r.listen(source)

    try:
        print("Reconizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
       #print(e)
       print("Can you please repeat")
    #    speak("Can you please repeat")
       return ""
    return query


def write_notepad():
    pyautogui.hotkey('winleft')
    pyautogui.click(123, 1052, duration=0.8)
    #print(pg.position())
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    print("sir do you want to type in note pad ")
    speak("sir do you want to type in note pad ")
    exit_msg = "sir do you want to save or exit"
    while True:
        clear()
        query = voiceboard().lower()
        if 'yes' in query:
            pass
            
        elif "no" in query or "say" in query or "speak" in query:
            query = voiceboard()
            pyautogui.typewrite(query)

        while True:
            clear()
            speak(exit_msg)
            print(exit_msg)
            query = takeCommand().lower()

            if "exit" in query or "save" in query:
                pyautogui.hotkey('alt', 'F4')
                pyautogui.press('enter')
                exit()

            else:
                break

def send_email():
        speak("Enter your email address")
        email_address = input('Enter your email address- ')
        speak("Enter your password")
        password = input('Enter your password -')
        speak("Enter the reciever's email address ")
        receiver_address = input("Enter the reciever's email address- ")
        # print(email_address)
        # print(password)
        f="do you want to send your mail"
        j = "Would you like to type your mail "
        while True:
            clear()
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(email_address, password)
                print(j)
                speak(j)
                query = takeCommand().lower()

                if "yes" in query:
                    print("What is the subject of the mail")
                    subject = input()
                    print("What is the body of the mail")
                    body = input()

                elif "no" in query or "say" in query or "speak" in query:
                    k = "What is the subject of the mail"
                    print(k)
                    speak(k)
                    query = takeCommand().lower()
                    subject = query
                    p = "What is the body of the mail"
                    print(p)
                    speak(p)
                    query = voiceboard().lower()
                    body = query

                while True:
                    clear()
                    print(f)
                    speak(f)
                    query = takeCommand().lower()
                    if "send mail" in query or 'yes' in query:
                        msg = f'Subject: {subject}\n\n{body}'
                        smtp.sendmail(email_address, receiver_address, msg)
                        t = "Your mail has been sent"
                        print(t)
                        speak(t)
                        exit()
                    elif "rewrite" in  query or "changes" in query or "correct" in query:
                        break
while True:
    clear()
    query = takeCommand().lower()
    if query =="notepad":
        write_notepad()
    if query =="email":
        send_email()
    elif query =="exit":
        exit()
