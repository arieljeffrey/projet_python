from django.shortcuts import render, redirect
from django.http import HttpResponse



# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer , ChatterBotCorpusTrainer
import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
nlp = en_core_web_sm.load()
bot=ChatBot('chatbot',read_only =False,
               logic_adapters =[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    #'default_response': 'Sorry,  i dont know what that means',
                    #'maximum_similarity_threshold':0.95
                }
                ])


 

list_to_train=[
     
     "hi",
     "hi,there",
     "what's your name?",
     "i'm just a chatbot",
     "what's your favorite foods",
     "it's like cheese",
     "what's your fav sport?",
     "swimming",
     "do you have a children?",
     "no"
]

ChatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
ChatterBotCorpusTrainer.train('chatterbot.corpus.spanish')

def index(request):
    return render(request,'chatApp_/index.html')

def specific(request):
    return HttpResponse('this is a specific urls')

def getResponse(request):
    userMessage =request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)



