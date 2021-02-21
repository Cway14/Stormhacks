
from flask import Flask, render_template, request, jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response


# Chatbot Instance
chatbot = ChatBot(
    "Test",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        {
        "import_path": "chatterbot.logic.BestMatch",
        "response_selection_method": get_random_response ,
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.90
        }
        ]
    )

# Train chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return jsonify(response=str(chatbot.get_response(userText)))

if __name__ == "__main__":
    app.run()