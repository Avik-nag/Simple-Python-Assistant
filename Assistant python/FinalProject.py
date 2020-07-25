import speech_recognition as sr
import sounddevice as sd
import scipy.io.wavfile
import wavio
import simpleaudio
from gtts import gTTS 
import os
import webbrowser
from playsound import playsound
from googlesearch import search

playsound("askname.mp3")
fs = 44100  # Sample rate
seconds = 2  # Duration of recording
print("Started recording name")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait() 
print("Stopped recording name")
output=wavio.write("output.wav", myrecording, fs ,sampwidth=2)
print("output file written to disk")
r = sr.Recognizer()
output = sr.AudioFile("D:\VS_Code workspace\p1\output.wav")
with output as source:
    try:
        audio = r.record(source)
        command=(r.recognize_google(audio))
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        playsound("negative1.mp3") 
        print("Google Speech Recognition could not understand audio")
         
    except sr.RequestError: 
        playsound("negative2.mp3")
        print("Could not request results from Google")

with open('c.txt' , 'w') as mycommand:  #writing the command to c.txt file
    mycommand.write(command)
mycommand.close
        
with open('c.txt' , 'r') as mycommand:     #reading the file and storing to string = line
    line=mycommand.readline()       
mycommand.close
playsound('D:\VS_Code workspace\p1\welcome.mp3')
mytext = 'Hey'+line+'how can i help you today?'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("name.mp3") 
playsound("name.mp3") 

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

print("Started recording")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait() 
print("Stop recording")
wavio.write("output1.wav", myrecording, fs ,sampwidth=2)
print("output file written to disk")
r = sr.Recognizer()
output = sr.AudioFile("D:\VS_Code workspace\p1\output1.wav")
with output as source:
    try:
        audio = r.record(source)
        command=(r.recognize_google(audio))
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        playsound("negative1.mp3") 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError: 
        playsound("negative2.mp3")
        print("Could not request results from Google")
        
with open('d.txt' , 'w') as mycommand:  #writing the command to c.txt file
    mycommand.write(command)
mycommand.close
        
with open('d.txt' , 'r') as mycommand:     #reading the file and storing to string = line
    line=mycommand.readline()       
mycommand.close
def main():
    if (line.lower().find('open google') != -1):
        url='http://www.google.com'
        webbrowser.open(url)
        print('Opened google successfully')
        
    elif (line.lower().find('whatsapp') != -1): #or ((line in howareyou) !=-1): 
        playsound('D:\VS_Code workspace\p1\whatsup.mp3')
        print('Doing my thing')
        
    elif(line.lower().find('songs') != -1):
        url='https://www.youtube.com/watch?v=DQ4r7HegRQw&list=PL__KJp8p02kUGoqVCQq3PdD5Tsc-YYRol'
        webbrowser.open(url)
        print('opened youtube playlist')
        
    elif (line.lower().find('open youtube') != -1):
        url='http://www.youtube.com'
        webbrowser.open(url)
        print('Opened youtube successfully')
    
    elif(line.lower().find('restart') !=-1):
        os.system("shutdown /r /t 1")
        print('Restarting device in 3..2..1')
        
    elif (line.lower().find('weather') != -1):
        url='https://openweathermap.org/'
        webbrowser.open(url)
        print('Opened weather successfully')
    else:
        for j in search(line, tld="co.in", num=10, stop=1, pause=2): 
            print(j)
            playsound("notfound.mp3")
            webbrowser.open(j)
print('searching command')
main()
print('All command\'s executed')