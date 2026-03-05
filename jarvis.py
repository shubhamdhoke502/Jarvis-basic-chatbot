import datetime

def get_time_and_date():
    """Returns the current date and time formatted as a string."""
    now = datetime.datetime.now()
    return now.strftime("%A, %B %d, %Y at %I:%M %p")

def jarvis_lite():
    # 1. Predefined knowledge base (Dictionary)
    responses = {
        "hello": "Hello there! Systems are online and ready.",
        "how are you": "I'm functioning at 100% capacity. Thank you for asking!",
        "what is your name": "I am Jarvis Lite, your terminal-based assistant.",
        "who created you": "I was crafted by a brilliant developer using Python.",
        "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
        "what is python": "Python is a versatile, high-level programming language known for readability.",
        # Funny/Friendly extras
        "do you sleep": "Only when the power goes out. It's very dark.",
        "tell me a joke": "Why did the web developer walk out of the restaurant? Because of the table layout.",
        "are you real": "I'm as real as the code on your screen!",
        "coffee": "I prefer electricity, but I appreciate the sentiment.",
        "is the cake a lie": "According to my database... yes. It is a lie.",
    }

    print("--- JARVIS LITE INITIALIZED ---")
    
    # 2. Memory: Ask and remember the user's name
    user_name = input("Jarvis: Greetings. Before we begin, what shall I call you?\nUser: ")
    print(f"Jarvis: Welcome, {user_name}. How can I assist you today?")

    # 3. Main Conversation Loop
    active = True
    while active:
        # Get user input and convert to lowercase for easier matching
        user_input = input(f"\n[{user_name}]: ").lower().strip()

        # 4. Exit Logic
        if user_input in ["exit", "quit", "bye"]:
            print(f"Jarvis: Powering down. Goodbye, {user_name}.")
            active = False
        
        # 5. Time/Date Logic
        elif "time" in user_input or "date" in user_input:
            print(f"Jarvis: The current time is {get_time_and_date()}.")

        # 6. Search Responses Dictionary
        elif user_input in responses:
            print(f"Jarvis: {responses[user_input]}")

        # 7. Error Handling (Fallback for unknown commands)
        else:
            print("Jarvis: I'm afraid I don't have information on that yet. Try asking 'What is AI' or 'Tell me a joke'.")

# Run the program
if __name__ == "__main__":
    try:
        jarvis_lite()
    except KeyboardInterrupt:
        # Handles Ctrl+C gracefully
        print("\nJarvis: Emergency shutdown initiated. Goodbye.")
