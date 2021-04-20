import pyttsx3 as st
import os
import subprocess
import speech_recognition as sp
import time
st.speak("Namaste, Welcome to Virtual Human Program")
print("\t\t\t\t       Welcome \n\t\t\t\tto Virtual Human Program")
st.speak("Namaste, Which Program you want to process")
print("\t\t\tNamaste Which Program you want to process?")


while True:
    print("a)Want to work on AWS\nb)Want to work on hadoop")
    time.sleep(3)
    st.speak("Tell your need. i m listening")
    time.sleep(1)
    print("Tell your need .... we r listening...: " , end="")
    r = sp.Recognizer()
    with sp.Microphone() as source:
	    print("start saying")
	    audio = r.listen(source)
	    print("we are sending to google from their we recieve the text for you")
    p = r.recognize_google(audio)

    if ("start" in p) and ("with" in p) or ("work" in p) or ("working" in p) and ("with" in p) or ("AWS" in p):
        print("working on aws")
        import aws_voice.py
    #elif x == "b":
    elif ("start" in p) and ("with" in p) or ("work" in p) or ("working" in p) and ("with" in p) or ("hadoop" in p):
        import hadoop_voice.py
    else:
        exit()
