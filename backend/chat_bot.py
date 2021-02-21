from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from weather import Weather


# Chatbot Instance
chatbot = ChatBot(
    "Test",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        {
            "import_path": "chatterbot.logic.BestMatch",
            "response_selection_method": get_random_response,
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

# Train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

print()
# interact with user
userInput = ""
while(userInput.lower() != "bye"):
    userInput = input("Enter Message: ").lower()
    if "weather" not in userInput:
        response = chatbot.get_response(userInput)
        print(response)
    else:
        print(Weather("a7b37fc8fa9faed677e7e0bd192282ed").get_weather())
