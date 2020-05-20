import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl

import urllib.request
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
from time import strftime

def sofiaResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command
def assistant(command):
    "if statements for executing commands"

#open subreddit Reddit
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        sofiaResponse('The Reddit content has been opened for you .')
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello . Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello . Good afternoon')
        else:
            sofiaResponse('Hello . Good evening')
    elif 'Thank you' in command:
        sofiaResponse('Bye bye . Have a nice day')
        sys.exit()
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain + '.com/watch?v=l9v1ewQXv5M'
            webbrowser.open(url)
            sofiaResponse('The website you have requested has been opened for you .')
        else:
            pass

while True:
    assistant(myCommand())
