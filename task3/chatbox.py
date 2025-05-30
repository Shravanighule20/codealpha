import nltk
import random
import string

from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

nltk.download('punkt')

responses = {
    "greeting": ["Hello! 👋", "Hi there!", "Hey! How can I help you today?"],
    "goodbye": ["Goodbye! 👋", "See you later!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime! 😊"],
    "unknown": ["I'm not sure I understand. Can you rephrase?", "Hmm, I didn’t get that."]
}


def get_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    if any(word in tokens for word in ['hi', 'hello', 'hey']):
        return "greeting"
    elif any(word in tokens for word in ['bye', 'goodbye', 'see you']):
        return "goodbye"
    elif any(word in tokens for word in ['thanks', 'thank you']):
        return "thanks"
    else:
        return "unknown"


def chatbot():
    print("🤖 Chatbot: Hello! Type 'quit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("🤖 Chatbot: Goodbye! 👋")
            break

        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    chatbot()
