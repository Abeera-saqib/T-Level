import os
import webbrowser
import datetime
import random

def search_youtube(query):
    """
    Opens YouTube and searches for the given query.
    """
    base_url = "https://www.youtube.com/results?search_query="
    search_url = base_url + "+".join(query.split())
    webbrowser.open(search_url)
    print(f"Searching and playing on YouTube: {query}")

def interpret_command(command):
    """
    Basic NLP-like function to determine what the user wants.
    """
    if "open" in command and "website" in command:
        url = command.split("open website")[-1].strip()
        webbrowser.open(f"http://{url}")
        print(f"Opening website: {url}")
    elif "time" in command:
        print("The current time is:", datetime.datetime.now().strftime("%H:%M:%S"))
    elif "date" in command:
        print("Today's date is:", datetime.datetime.now().strftime("%Y-%m-%d"))
    elif "play music" in command:
        song_name = command.split("play music")[-1].strip()
        search_youtube(song_name)
    elif "joke" in command:
        print(random.choice(["Why did the chicken cross the road? To get to the other side!", 
                             "What do you call cheese that isn't yours? Nacho cheese!"]))
    else:
        print("I'm not sure how to handle that command.")

def main():
    print("Welcome to the versatile program!")
    print("Commands I understand: 'open website', 'time', 'date', 'play music <song_name>', 'joke'")
    while True:
        user_command = input("What would you like to do? ").lower()
        if user_command in ["exit", "quit"]:
            print("Goodbye!")
            break
        interpret_command(user_command)

if __name__ == "__main__":
    main()

