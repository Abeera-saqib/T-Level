import pyttsx3
import datetime
import webbrowser
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def get_time_date():
    """Return the current time, date, and day."""
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")  # Format: HH:MM AM/PM
    date = now.strftime("%B %d, %Y")  # Format: Month Day, Year
    day = now.strftime("%A")  # Full weekday name
    return time, date, day

def play_music():
    """Play music on YouTube."""
    speak("What song should I play?")
    song = input("Enter the song name: ")  # Replace with voice input if needed
    url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Playing {song} on YouTube.")

def random_question():
    """Ask a random question."""
    questions = [
        "What is your favorite hobby?",
        "If you could travel anywhere in the world, where would you go?",
        "What is your dream job?",
        "If you had a superpower, what would it be?",
        "What's the best book or movie you've ever experienced?"
    ]
    question = random.choice(questions)
    speak(question)
    print(question)

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your virtual assistant.")
    while True:
        print("\nOptions: 1. Time and Date 2. Play Music 3. Ask Question 4. Exit")
        speak("What would you like to do? Choose a number.")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            time, date, day = get_time_date()
            speak(f"The current time is {time}, the date is {date}, and today is {day}.")
            print(f"Time: {time}, Date: {date}, Day: {day}")
        elif choice == "2":
            play_music()
        elif choice == "3":
            random_question()
        elif choice == "4":
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Invalid choice. Please try again.")
