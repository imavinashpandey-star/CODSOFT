# Rule-Based Chatbot

def chatbot():
    print("===================================")
    print(" Welcome to AI Rule-Based Chatbot ")
    print(" Type 'bye' to exit ")
    print("===================================")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "name" in user:
            print("Bot: My name is AI Chatbot.")

        elif "how are you" in user:
            print("Bot: I am fine. Thank you for asking!")

        elif "college" in user:
            print("Bot: I can provide information related to your college.")

        elif "course" in user:
            print("Bot: I can help you with course-related information.")

        elif "python" in user:
            print("Bot: Python is a popular programming language used in AI and Data Science.")

        elif "ai" in user:
            print("Bot: Artificial Intelligence enables machines to mimic human intelligence.")

        elif "help" in user:
            print("Bot: You can ask me about Python, AI, courses, or general greetings.")

        elif user in ["thanks", "thank you"]:
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

chatbot()
