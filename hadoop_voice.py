import pyttsx3 as st
import speech_recognition as sp
import time

import os
import subprocess
st.speak("Setup Hadoop Cluster")
while True:
    print("\t\t\t Hadoop Cluster Required")
    print("a)Start Namenode Service \nb)Start Datanode Service\nC)Login YOur client NOde")
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
    if ("start" in p) and ("Namenode" in p) and ("Service" in p):
   # Req = (input("\t\t\tEnter Your Requirement :"))
    #if Req == "a":
        st.speak("Provide your Namenode  IP for login  via ssh to start service")
        print("Provide YOur Namenode IP")
        ip = input("Enter your IP :")
        os.system("ssh root@{} systemctl stop firewalld".format(ip) ) 
        os.system("ssh root@{} hadoop-daemon.sh start namenode".format(ip) )        
       # This above command for starting namenode service
         

    if ("Start" in p) and ("Datanode" in p) and ("Service" in p) :
    #elif Req == "b":
        print("b")
        st.speak("Number of Datanode you need") 
        N = int(input("No. of datanode U need? :"))
        st.speak("Provide your Datanode  IP for login  via ssh to start service")
        for i in range(N):
            ip = input("Enter your IP :")
            os.system("ssh root@{} systemctl stop firewalld".format(ip) ) 
            os.system("ssh root@{} hadoop-daemon.sh start datanode".format(ip) )   

    if ("Enter" in p) or ("Login" in p) or ("Start" in p) and ("clinet" in p) and ("node" in p) :   
    #elif Req == "c":
        print("c")
        st.speak("Your client Node is available, Enter your client Node IP")
        os.system("ssh root@{} systemctl stop firewalld".format(ip) ) 
        os.system("ssh root@{} hadoop dfsadmin -report |  less".format(ip) ) 
        os.system("ssh root@{} ".format(ip) )  



    else:
        exit()

