import speech_recognition as sr # recognise speech
import playsound # to play an audio files
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import speedtest
import pyttsx3
import bs4 as bs
import urllib.request
import datetime
import keyboard
import calendar

class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(asis_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
       'June', 'July', 'August', 'September', 'October', 'November',   
       'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                      '7th', '8th', '9th', '10th', '11th', '12th',                      
                      '13th', '14th', '15th', '16th', '17th', 
                      '18th', '19th', '20th', '21st', '22nd', 
                      '23rd', '24th', '25th', '26th', '27th', 
                      '28th', '29th', '30th', '31st']
   
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'
    
def SpeedTest():
    engine_speak("Checking speed.....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)
    if there_exists(["uploading"]):
         engine_speak(f"The uploading speed is {correctUpload} mbp/s")
   
    elif there_exists(["downloading"]):
         engine_speak(f"The Downloading speed is {correctDown} mbp/s")    

    else:
        engine_speak(f"The downloading is {correctDown}mbps and The Uploading Speed is {correctUpload}mbps")

      
def CloseAPPS():
    engine_speak("ok Sir , Wait a Second!")

    if there_exists(["chrome"]):
        os.system("TASKKILL /F /im chrome.exe")
    elif there_exists(["steam"]):
        os.system("TASKKILL /F /im steam.exe")
    elif there_exists(["vlc"]):
        os.system("TASKKILL /F /im vlc.exe")
    elif there_exists(["config"]):
        os.system("TASKKILL /F /im dxdiag.exe")
        engine_speak("Your Command has been Successfully Completed !")    
    


def respond(voice_data):
    # 1: greeting and fun
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            engine_speak("my name is " + asis_obj.name)
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name) # remember name in asis object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking , what about u sir" + person_obj.name)
    
    if there_exists(["who i am","who am i"]):
        engine_speak("If you talk then definately your human" + person_obj.name)
    
    if there_exists(["who made you", "who created you and "]):
        engine_speak(" I have been created by Ajay and Ammar" + person_obj.name)

    if there_exists(["what is love"]):
        engine_speak("It is 7th sense that destroy all other senses" )
    
    if there_exists(["who are you","what are you"]):
        engine_speak("I am your Personal assistant created by Ajay and Ammar" + person_obj.name)
    
    if there_exists(["reason you created","reason"]):
        engine_speak("I was created as a Minor project by Master Ajay and Master Ammar")

    if there_exists(["why you came to world"]):
        engine_speak("Thanks to Ajay and Ammar. further It's a secret")

    if there_exists(["jokes","say a joke","tell me a joke"]):
        engine_speak("What’s the difference between England and a tea bag the answer is.....The tea bag stays in the cup longer..hahahahaha")

    if there_exists(["can you laugh again","laugh"]):
        engine_speak("am I joke to you")
    
    if there_exists(["people hate me"]):
        engine_speak("Love your haters,they are your biggest fan")
    
    if there_exists(["good morning"]):
        engine_speak("Good morning sir How can I assist u")
    
    if there_exists(["good afternoon"]):
        engine_speak("Good afternoon sir How can I assist u")
    
    if there_exists(["good evening"]):
        engine_speak("Good evening sir How can I assist u")

    if there_exists(["good night"]):
        engine_speak("Good night sir have a sweet Dream")
    
    if there_exists(["i love you"]):
        engine_speak("better Luck next time ")
    
    if there_exists(["feeling bored","bored","i am sad"]):
        engine_speak("Alright, I can tell u a joke.....u r the best person i have ever seen in these world . how was the joke hahaha")

    if there_exists(["thank you","thanks","thanks that was good"]):
        engine_speak(" Ok you are welcome") 

    if there_exists(["tell me another joke","next joke"]):
        engine_speak(" Why couldn't the leopard play hide and seek? Because he was always spotted.haahaahaa")

    if there_exists(["open chrome"]):
        engine_speak(" opening chrome") 
        codePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        os.startfile(codePath)
    
    if there_exists(["open code"]):
        engine_speak(" openning visual studio") 
        codePath ="C:/Users/Achu/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        os.startfile(codePath)
    if there_exists(["open steam"]):
        engine_speak(" openning Steam") 
        codePath ="C:/Program Files (x86)/Steam/Steam.exe"
        os.startfile(codePath)
    if there_exists(["open vlc"]):
        engine_speak(" openning vlc") 
        codePath ="C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
        os.startfile(codePath)
    if there_exists(["open system config"]):
        engine_speak(" openning config") 
        codePath ="C:/Windows/System32/dxdiag.exe"
        os.startfile(codePath)
        

    if there_exists(["fine","i am fine"]):
        engine_speak("It's good to know that your fine")

    if there_exists(["sing one song","sing a song"]):
        engine_speak("Tsamina mina, eh eh Waka waka, eh eh Tsamina mina zangalewa This time for Africa")
    
    if there_exists(["do you believe in ghost"]):
        engine_speak("yes I am one among them")
    
    if there_exists(["are you ghost"]):
        engine_speak("i don't want to talk about that again")
    
    if there_exists(["birthday","when is your birthday"]):
        engine_speak(" birthday let me check............My birthday is on 20/2/2021")
    
    if there_exists(["what can you do","what is special about you"]):
        engine_speak("open websites Example: open youtube.com time: Example: what time it is?,date: Example: what date it is?,launch applications: Example: launch chrome,tell me: Example: tell me about India, weather: Example: what weather/temperature in Mumbai?,news: Example: news for today ")
    
    if there_exists(["set alarm"]):
        engine_speak("enter the time sir !")
        time =input(":Enter the time:")
        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                engine_speak("Time too Wake Up Sir!Time too Wake Up Sir!Time too Wake Up Sir!Time too Wake Up Sir!Time too Wake Up Sir!")
                engine_speak(time)
                engine_speak("Closing Alarm")
            elif now>time:
                break
    if there_exists(["date"]):
            get_date = getDate()
            engine_speak(get_date)
    
    if there_exists(["downloading speed"]):
       SpeedTest() 
     
    if there_exists(["uploading speed"]):
       SpeedTest() 
    
      
    if there_exists(["internet speed"]):
       SpeedTest() 

    if there_exists(["close chrome"]):
        engine_speak(" Closing chrome") 
        CloseAPPS()
    if there_exists(["close steam"]):
        engine_speak(" Closing steam") 
        CloseAPPS()
    if there_exists(["close vlc"]):
        engine_speak(" Closing vlc") 
        CloseAPPS()
    if there_exists(["close config","close system config"]):
        engine_speak(" Closing system config") 
        CloseAPPS()

  # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for",]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube search","youtube"]):
        search_term = voice_data.split("search")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    #7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    
    # search for music
    if there_exists(["play music"]):
        search_term= voice_data.split("music")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to"+ search_term +"enjoy sir")
    #search for amazon.com
    if there_exists(["amazon search"]):
        search_term = voice_data.split("search")[-1]
        url="https://www.amazon.in/s?k="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on amazon.com")

    #search for amazon.com
    if there_exists(["flipkart search"]):
        search_term = voice_data.split("search")[-1]
        url="https://www.flipkart.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term + "on flipkart.com")
         
         
    #make a note
    if there_exists(["make a note"]):
        search_term=voice_data.split("for")[-1]
        url="https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")
        
    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")
    #facebook
    if there_exists(["open facebook","enjoy facebook"]):
        search_term=voice_data.split("for")[-1]
        url="https://www.facebook.com/login/"
        webbrowser.get().open(url)
        engine_speak("opening facebook")

    #open twitter
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")
     #open twitter
    
    if there_exists(["open whatsapp"]):
        search_term=voice_data.split("for")[-1]
        url="https://web.whatsapp.com/"
        webbrowser.get().open(url)
        engine_speak("opening whats app web in google")

    #wikipedia
    if there_exists(["wikipedia search","open wikipedia"]):
        search_term = voice_data.split("search")[-1]
        url = "https://en.wikipedia.org/wiki/" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on wikipedia")
   

    #8 time table
    if there_exists(["show my time table"]):
        im = Image.open("E:/images/WhatsApp Image 2021-03-18 at 2.13.56 PM.jpeg")
        im.show()
    
    #9 weather
    if there_exists(["weather","tell me the weather report","whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")
    
    #open gmail
    if there_exists(["open my mail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")
    #open google
    if there_exists(["open google","google.com"]):
        search_term = voice_data.split("for")[-1]
        url="https://www.google.co.in/"
        webbrowser.get().open(url)
        engine_speak("here you can Search anything You wish Sir")
    

    #10 stone paper scisorrs
    
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        #engine_speak("hi")
        if pmove==cmove:
            engine_speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            engine_speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            engine_speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            engine_speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            engine_speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            engine_speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            engine_speak("Computer wins")

    #11 toss a coin
    if there_exists(["toss","toss a coin","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)

    #12 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")
        
    #13 screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/Achu/Pictures/Screenshots/screenshot.png') 
    
    
    #14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition=record_audio("what do you need the definition of")
        url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found '+definitions[1])
            else:
                engine_speak ('Here is what i found '+definitions[2])
        else:
                engine_speak("im sorry i could not find the definition for "+definition)


    if there_exists(["exit", "quit", "goodbye","bye","end"]):
        engine_speak("we could continue more sir, but.,,...,,,,,..,,,,, byee")
        exit()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'tutu'
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond
# import speech_recognition as sr #recognise speech
# import playsound #to play the audio file
# from gtts import gTTS #goggle text so speech
# import random
# from time import ctime #get time detials
# import webbrowser
# import ssl #This module provides access to Transport Layer Security (often known as “Secure Sockets Layer”) encryption and peer authentication facilities for network sockets, both client-side  and server-side.  This module uses the OpenSSL library
# import certifi #Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.
# import time
# import os #to remove the creted audio the files
# from  PIL import Image #The Image module provides a class with the same name which is used to represent a PIL image. The module also provides a number of factory functions, including functions to load images from files, and to create new images.
# import subprocess #The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
# import pyautogui
# import pyttsx3
# import bs4 as bs #Beautiful Soup is a library that makes it easy to scrape information from web pages. 
# import urllib.request #The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
# import wikipedia
# class person:
#     name=''
#     def setName(self,name):
#         self.name = name

# class asis:
#     name=''
#     def setName(self,name):
#         self.name = name
        
# def there_exists(terms):
#     for term in terms:
#         if term in voice_data:
#             return True
        
# def engine_speak(text):
#     text = str(text)
#     engine.say(text)
#     engine.runAndWait()
    
# r = sr.Recognizer() #initialize a recogniser
# #listen for audio and convert to text
# def record_audio(ask=""):
#     with sr.Microphone as source: #microphne as source
#         if ask:
#             engine_speak(ask)
#         audio =r.listen(source, 5, 5)#listen to audio via source
#         print("Lokking the Database")
#         voice_data = ''
#         try :
#             voice_data= r.reocognize_google(audio)#convert audio to text
#         except sr.UnknownValueError: #error: reconizer doesn't understand
#             engine_speak('Sorry sir, did not get that')
#         except sr.RequestError:
#             engine_speak("Sorry sir, server down")#error : recognizer is not connected
#         print(">>", voice_data.lower())#print waht user said
#         return voice_data.lower()
            
# #get string and make audio file to be played
# def engine_speak(audio_string):
#     audio_string=str(audio_string) 
#     tts = gTTS(text=audio_string , lang='en')#text to speech(voice)
#     r = random.randint(1,20000000)
#     audio_file='audio' + str(r) + '.mp3'
#     tts.save(audio_file)#save as mp3
#     playsound.playsound(audio_file)#to play the sound
#     print(asis_obj.name +":",audio_string)#print what app said
#     os.remove(audio_file)#remove the audio file ##let us check at last by comenting it whether it says
    
# def respond(voice_data):
#     # 1) if got greeting
#     if there_exists(['hey','hi','hola','hello','wassup',]):
#         greetings=["Hi sir, What we gonna do today?" +person_obj.name, "Hi sir, what are we doing today?" +person_obj.name, "Hi sir, How can i help you?"+person_obj.name]
#         greet=greetings[random.randint(0,len(greetings)-1)]
#         engine_speak(greet)
        
#     #2))name
#     if there_exists(["whta is your name","what's your name","tell me your name"]):
#         if person_obj.name:
#             engine_speak("whats with my name")
#         else:
#             engine_speak("I dont know my sir,please assighn my name by saying command your name should be ,,,,and sir will be priviledged to know your name ")
            
#     if there_exists(["your name should be"]):
#         asis_name =voice_data.split("be")[-1].strip()
#         engine_speak("Okay sir,Ill remember my name"+asis_name)
#         asis_obj.setName(asis_name)#remember name in asis object
        
#     if there_exists(["my my name is"]):
#         person_name = voice_data.split("is")[-1].strip()
#         engine_speak("Okay sir ill remember your name is" + person_name)
#         person_name.setName(person_name)#remember name in person object
        
#     #3)) greeting
#     if there_exists(["how are you bro","hoe are you","how are you doing",]):
#         engine_speak("I m very well sir, how are you? thanks for asking"+person_name)
        
#     #4))time
#     if there_exists(["whats the time","tell me the time","what time is it"]):
#         time = ctime().split(" ")[3].split(":")[0:2]
#         if time[0]=="00":
#             hours='12'
#         else:
#             hours = time[0]
#         minutes = time[1]
#         time = hours + "hours and" + minutes + "minutes"
#         engine_speak(time)
        
#     #5))search google
#     if there_exists(["search for"]) and 'youtube' not in voice_data:
#         search_term=voice_data.split("for")[-1]
#         url = "https://google.com/search?q=" + search_term
#         webbrowser.get().openURL(url)
#         engine_speak("Her is what i found for"+search_term)
        
#     #6))) search youtube
#     if there_exists(["search for youtube for","youtube"]):
#         search_term=voice_data.split("for")[-1]
#         url="https://www.youtube.com/results?search_query="+ search_term
#         webbrowser.get().open(url)
#         engine_speak("Here is what i found for "+ search_term + "on youtube")
        
#     #7)) time table
#     if there_exists(["show me my time table"]):
#         im = Image.open(r"")
#         im.show()
        
#     #8))) get to know the weather
#     if there_exists(["weather","how the weather outside","Please get the report of waether"]):
#         search_term=voice_data.split("for")[-1]
#         url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
#         webbrowser.get().open(url)#opens the webrowser
#         engine_speak("Here is your report sir")
    
#     #9)) get to know stock price
#     if there_exists(["price of"]):
#         search_term=voice_data.split("for")[-1]
#         url="https://google.com/search?q="+ search_term
#         webbrowser.get().open(url)
#         engine_speak("Here is what i found for"+ search_term)
    
#     #10 get to listen music
#     if there_exists("listen","play music"):
#         search_term=voice_data.split("for")[-1]
#         url="https://open.spotify.com/search/"+search_term
#         webbrowser.get().open(url)
#         engine_speak("Enjoy sir")
#     #11 screenshot
#     if there_exists(["capture","my screen","screenshot"]):
#         myScreenshot=pyautogui.screenshot()
#         myScreenshot.save('')
        
#4)) search wikipedia for defination
    
#     if there_exists(["defination of"]):
#         definition=record_audio("what do you need denination of")
#         url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
#         soup=bs.BeautifulSoup(url,'lxml')
#         definitions=[]
#         for paragraph in soup.find_all('p'):
#             definitions.append(str(paragraph.txt))
#         if definitions:
#             if definitions[0]:#if condi is false
#                 engine_speak('i am sorry sir i could not find the definitios please try websearch')
#             elif definitions[1]:#if condition is true
#                 engine_speak('here is what is found for'+ definitions[1])
#             # else:
#             # engine_speak('Here is what i found '+ definitions[2])
#         else:
#             engine_speak('i could not find the definition of'+definitions +'server down:user warning: have a websearch')

#     #10 stone paper scisorrs
#     if there_exists(["game"]):
#         voice_data = record_audio("choose among rock paper or scissor")
#         moves=["rock", "paper", "scissor"]
    
#         cmove=random.choice(moves)
#         pmove=voice_data
        

#         engine_speak("The computer chose " + cmove)
#         engine_speak("You chose " + pmove)
#         #engine_speak("hi")
#         if pmove==cmove:
#             engine_speak("the match is draw")
#         elif pmove== "rock" and cmove== "scissor":
#             engine_speak("Player wins")
#         elif pmove== "rock" and cmove== "paper":
#             engine_speak("Computer wins")
#         elif pmove== "paper" and cmove== "rock":
#             engine_speak("Player wins")
#         elif pmove== "paper" and cmove== "scissor":
#             engine_speak("Computer wins")
#         elif pmove== "scissor" and cmove== "paper":
#             engine_speak("Player wins")
#         elif pmove== "scissor" and cmove== "rock":
#             engine_speak("Computer wins")

#     #11 toss a coin
#     if there_exists(["toss","flip","coin"]):
#         moves=["head", "tails"]   
#         cmove=random.choice(moves)
#         engine_speak("The computer chose " + cmove)

#     #12 calc
#     if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
#         opr = voice_data.split()[1]

#         if opr == '+':
#             engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
#         elif opr == '-':
#             engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
#         elif opr == 'multiply':
#             engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
#         elif opr == 'divide':
#             engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
#         elif opr == 'power':
#             engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
#         else:
#             engine_speak("Wrong Operator")
#     # for exit       
#     if there_exists(["exit","goodbye","quit","take some rest bro"]):
#         engine_speak("We could continue more sir, well goodbye")
#         exit()
        
        
# time.sleep(1)

# person_obj = person()
# asis_obj = asis()
# asis_obj.name = 'Nick'
# engine = pyttsx3.init()
            
# while(1):
#     voice_data = record_audio("Recording") # get the voice input
#     print("Done")
#     print("Q:", voice_data)
#     respond(voice_data) # respond
    
    

