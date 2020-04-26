import webbrowser
import schedule
import time
import os
import pyttsx3

def daily_habit(meditate_mins=10):
    # say good morning
    engine = pyttsx3.init()
    engine.say('Good morning Titus. My name is Jir Vas. Start your day with a good exercise.')
    engine.runAndWait()
    
    # play workout music to jumpstart your day
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=EX19iG5e68I')
    
    # meditate for 10 minutes
    engine.say('Great job! Now, start your meditation.')
    engine.runAndWait()
    time.sleep(60*meditate_mins)
    
    # end meditation
    engine.say('Awesome! Now you are calm and collected. Start with Duolingo now.')
    engine.runAndWait()
    
if __name__ == '__main__':
    daily_habit()