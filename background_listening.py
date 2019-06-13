#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time

import speech_recognition as sr

import pyttsx3 

import serial 

import itertools
#from nanpy import(ArduinoApi,SerialManager)  

#try:
 #  mcucontrol = serial.Serial('/dev/ttyUSB0',115200) 
#except: 
 #  print("Serial error") 
engine = pyttsx3.init() 
# this is called from the background thread

engine.setProperty('rate',180)
engine.setProperty('volume',0.9)
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',en_voice_id)
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + recognizer.recognize_google(audio))
        dict = {"turn on radar","turn on power","turn on light"}
        
        if str(recognizer.recognize_google(audio) in dict) == 'True':
             print(recognizer.recognize_google(audio) in dict)
             if recognizer.recognize_google(audio) == 'turn on radar':
                #try: 
                 # mcucontrol.write("A")
                  engine.say("Now" + recognizer.recognize_google(audio))    
                  engine.runAndWait()
                #except:
                 # print("Error")
             if recognizer.recognize_google(audio) == 'turn on power':
                #try:
                 # mcucontrol.write("B") 
                  engine.say("Now" + recognizer.recognize_google(audio))    
                  engine.runAndWait()
                #except: 
                 # print("Error")
             if recognizer.recognize_google(audio) == 'turn on light':
                # try:
                 # mcucontrol.write("C") 
                  engine.say("Now" + recognizer.recognize_google(audio))    
                  engine.runAndWait()
                 #except: 
                 # print("Error")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
for _ in itertools.count():time.sleep(0.9)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
#stop_listening(wait_for_stop=False)

# do some more unrelated things
#while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
