from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

new_bot = ChatBot('Norman')

prompts = ['What are some tips to stay warm',
           'How to beat the cold', 'how to beat the weather', ' staying warm']
answers = ['here are some tips for staying warm']

trainer = ListTrainer(new_bot)

for x in range(10):
    for i in prompts:
        conversation = []
        conversation.append(i)
        conversation.append(answers[0])
        print(conversation)
        trainer.train(conversation)

userInput = ""
while(userInput.lower() != "bye"):
    userInput = input("Enter Message: ")
    response = new_bot.get_response(userInput)
    print(response)
