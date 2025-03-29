import random

# Predefined responses
responses = {
    "hello": ["Hello! How can I help you?", "Hi there!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing fine!", "I'm good. How about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "your name": ["I'm a chatbot!", "Call me ChatGPT Lite!", "I'm just a simple bot."],
    "help": ["Sure! Ask me anything.", "I'm here to assist you.", "How can I help you?"],
}

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm not sure how to respond to that."

# Chatbot interaction loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break

        print("Chatbot:", get_response(user_input))

# Run chatbot
if __name__ == "__main__":
    chatbot()
