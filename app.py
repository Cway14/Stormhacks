
from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

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