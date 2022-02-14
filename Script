# Imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating bot and training him
chatbot = ChatBot('Chatbotium')

# Training with corpus
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

# Training with list dialog
# Welcome
trainer = ListTrainer(chatbot)
trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "What is your name?",
    "My name is ChatBotium",
    "Nice to meet you, ChatBotium"
    "Thank you! Nice to meet you too!"
])

# Who's your developer?
trainer.train([
    "Who is your developer?",
    "My developer is Royle Herman"
])

# What weather is it?
trainer.train([
    "What weather is it?",
    "I'm sorry, but I don't know, I can't go outside in case it rains "
])

# Who are you?
trainer.train([
    "Who's Royle Herman?",
    "It's my developer! He's awesome person and python coder!",
    "Can i meet with him?",
    "Maybe... Who knows:)"
])
# Bye
trainer.train([
    "Bye",
    "Goodbye, it's was nice to talk with you!"
])
# Where's you?
trainer.train([
    "Where are you?",
    "I'm in the computer world. It's impossible to get there for people."
])
# Getting response
while True:
    you = input('You: ')
    response = chatbot.get_response(you)
    print('Bot:', (response))
