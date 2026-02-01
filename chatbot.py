print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How can I help you?")
    elif user == "how are you":
        print("Chatbot: I am fine, thank you!")
    elif user == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: Sorry, I didn’t understand.")
