# Imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import colorama

# Creating bot
chatbot = ChatBot('Chatbotium')

# Training
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.custom")

# Getting response
while True:
    you = input('You: ')
    response = chatbot.get_response(you)
    print('Bot:', (response))