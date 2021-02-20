import nltk
nltk.download('popular')
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Chatbot Instance
chatbot = ChatBot("Test")

conversation = [
    "Hello",
    "Hi",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Bye",
    "Bye"
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

# interact with user
userInput = ""
while(userInput.lower() != "bye"):
    userInput = input("Enter Message: ")
    response = chatbot.get_response(userInput)
    print(response)