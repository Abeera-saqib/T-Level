import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
from tkinter import messagebox, Tk

def assistant(audio):
    """Speak the given text using the TTS engine."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    """Greet the user."""
    assistant("Hello, I am your Virtual Assistant. How can i help you today?")

def open_youtube(query):
    """Handle Youtube channel or search queries."""
    assistant("Checking youtube for your request.")
    base_url = "https://www.youtube.com/results?search_query="
    channel_urls = {
        "pewdiepie": "https://www.youtube.com/user/PewDiePie",
        "mrbeast": "https://www.youtube.com/user/MrBeast6000",
        "official music": "https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ",
    }
    query = query.replace("on youtube", "").strip()

    for channel_name, channel_url in channel_urls.items():
        if channel_name in query:
            assistant(f"Opening {channel_name}'s channel on youtube.")
            webbroswer.open(search_url)
            return

    search_url = base_url + query.replace(" ", "+")
    assistant(f"Searching Youtube for {query}.")
    webbrowser.open(search_url)

def core_code():
    """Main functionality of the assistant."""
    greeting()
    while True:
        phrase = audioinput().lower()
        if "what is yoru name" in phrase:
            assistant("I am Kerry Casey, your virtual assitant.")
        elif "from wikipedia" in phrase:
            assistant("Checking Wikipedia.")
            query = phrase.replace("from wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                assistant("According to Wikipedia,")
                assistant(result)
            except wikipedia.exceptions.DisambiguationError:
                assistant("The query is ambiguous. Please be more specific.")
            except wikipedia.exceptions.pageError:
                assistant("I couldn't find any information about that.")
            except Exception:
                assistant("Sorry, I couldn't fetch any information.")

        elif "what time is it" in phrase:
            theTime()
        elif "what day is it" in phrase:
            theDay()
        elif "on youtube" in phrase:
            opne_youtube(phrase)
        elif "thank you" in phrase or "thanks" in phrase:
            assistant("You're welcome!")
        elif "stop" in phrase or "exit" in phrase:
            if iExitSystem():
                break
        else:
            assistant("I didn't understand that. Please try again.")

def theTime():
    """Provide the current time."""
    time = datetime.datetime.now().strftime("%H:%M")
    hour, minute = time.split(":")
    assistant(f"This time right now is {hour} hours and {minute} minutes.")

def theDay():
    """Provide the current day of the week."""
    day= datetime.datetime.today().weekday() + 1
    day_dict = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }
    weekday = day_dict.get(day, "unknown")
    assistant(f"Today is {weekday}.")

def audioinput():
    """Listen to and process audio input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.7
        try:
            audio = recognizer.listen(source)
            print("Processing input...")
            phrase = recognizer.recognize_google(audio, language='en-us')
            print(f"You said: {phrase}")
            return phrase
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            assistant("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError as e:
            print(f"Request error: {e}.")
            assistant("I'm having trouble connecting to the service.")
        except Exception as e:
            print(f"Error: {e}")
            assistant("An error occured. Please try again.")
        return ""

def iExitSystem():
    """Prompt the user to confirm exit."""
    root = Tk()
    root.withdraw()
    assistant("Confirm if you want to exit.")
    iExit = messagebox.askquestion("Exit", "Do you really want to exit?")
    root.destroy()
    if iExit == 'yes':
        messagebox.showinfo("Exit", "Goodbye!")
        assistant("Goodbye!")
        return True
    else:
        assistant("Alright! Please tell me your next request.")
        return False

if __name__ == '__main__':
    core_code()
        
