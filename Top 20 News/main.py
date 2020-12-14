from bs4 import BeautifulSoup
import requests 
from win32com.client import Dispatch
import win32com.client as wincl
import datetime
import time

 
# def speak(text):         #  male voice
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(text)


def speak(text):   # female voice
    speaker_number = 1
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    SVSFlag = 11
    spk.Voice
    spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
    spk.Speak(text)



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning....")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon....")

    else:
        speak("Good Evening")
        print("Good Evening....")

    speak("I am Zira from Times of India ... here to tell you today's top twenty news !! so here I Begin....")




def get_fresh_news():

    url = 'https://timesofindia.indiatimes.com/briefs'
    r = requests.get(url)
    html_content = r.content 

    soup = BeautifulSoup(html_content,'html.parser')

    news_box = soup.find_all('div', class_='brief_box') 

    all_headings = []
    for news in news_box:
        if news != None:
            all_headings.append(news.find('h2'))

    i=1    
    top_20 = []
    for h in all_headings:
        if h != None:
            if i<=20: 
                top_20.append(h.text)
                i = i+1

    return top_20



if __name__ == "__main__":

    speak('hello')

    while True:
        
        wishme()
        news = get_fresh_news()

        for i in news:
            speak(i)
            time.sleep(2)
            
        speak('This was todays news Thankyou for Listening !!!')
        time.sleep(100)
            


