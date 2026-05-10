"""
        WelCome to CHATBOT
"""
def get_response(user_input):
 
    text = user_input.lower().strip()
    
    if text in ["hello", "hi", "hey", "howdy", "hiya"]:
        return "Hi there! How can I help you today?"

    elif text in ["good morning", "morning"]:
        return "Good morning!  Hope you have a great day!"

    elif text in ["good evening", "evening"]:
        return "Good evening! How's your day been?"

    elif text in ["good night", "goodnight"]:
        return "Good night! Sweet dreams!"
        
    elif text in ["how are you", "how r u", "how do you do"]:
        return "I'm doing great, thanks for asking! What about you?"

    elif text in ["i am fine",  "i am good", "fine", "good"]:
        return "That's wonderful to hear! "

    elif text in ["i'm sad", "i am sad", "not good", "not well",]:
        return "I'm sorry to hear that. I hope things get better soon!"
   
    elif text in ["thanks", "thank you", "thank you!", "thanks!", "thx"]:
        return "You're welcome! Always happy to help."

    elif text in ["bye", "goodbye", "by", "see ya", "tata",  "quit"]:
        return "QUIT"   

    else:
        return (
            "Hmm, I'm not sure I understand that.\n"
            "  Try typing 'help' to see what I can respond to!"
        )

def show_banner():
    print("\n" + "═" * 50)
    print(" WelCome to CHATBOT")
    print("═" * 50 + "\n")

def display_message(sender, message):
    """Prints a formatted chat bubble."""
    if sender == "You":
        print(f"\n  You     : {message}")
    else:
        print(f" ChatBot : {message}")

def main():
    show_banner()

    while True:
     
        user_input = input("  You → ").strip()

        if not user_input:
            print("    Please type something!")
            continue
        
        display_message("You", user_input)

        response = get_response(user_input)
    
        if response == "QUIT":
            print("  ChatBot : Goodbye! Have a wonderful day!\n")
            print("═" * 50)
            print("       Chat session ended. See you next time!")
            print("═" * 50 + "\n")
            break 

        display_message("ChatBot", response)

if __name__ == "__main__":
    main()
