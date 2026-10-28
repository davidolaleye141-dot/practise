from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot("DAVID AI", read_only=False, logic_adapters=["chatterbot.logic.BestMatch"])
list_to_train = [
    "hi",
    "hi there",
    "what is your name?",
    "im a chatbot owns by david",
    "how old are you?"
    "i am ageless"
    
]
list_trainer = ListTrainer(bot)

list_trainer.train(list_to_train)

user_response = input("user: ")

print(bot.generate_response(user_response))
