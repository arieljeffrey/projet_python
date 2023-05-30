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
                    'default_response': 'Sorry,  for more details please get closer to schooling',
                    'maximum_similarity_threshold':0.95
                }
                ])


 

list_to_train=[
     "what's your name?",
     "i'm just a chatbot",
     "Tell us about yourself",
     "ESSFAR is the school of Applied Mathematics and Computer Science at the service of organizations and innovation.",
     "What's the next school year?",
     "The next school year starts in September for LECENCE level students and in October for Master students",
     "Where do you stand?",
     "Campus: Yaoundé Omnisport Mfandena, behind the tax office",
     "What are your different trainings?"
     "Initial training in 5 years (Master 2) after a scientific baccalaureate and Continuing education, ESSFAR Executive Education offers certified and tailor-made training in severals fields",
     "Tell me about continuing education",
     "Continuing education is based on 4 areas: Banking, Finance, Insurance and Risk Data Science,Information System and Digital Technologies,Leadership and Project Management",
     "Tell me about initial training",
     "The initial training in 5 years is based on the following business specialties: Actuarial, Statistics and Big Data, Financial Engineering, Information system",


]

ChatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot)
ChatterBotCorpusTrainer.train('chatterbot.corpus.english')
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)



def index(request):
    return render(request,'chatApp_/index1.html')

def specific(request):
    return HttpResponse('this is a specific urls')

def getResponse(request):
    userMessage =request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)



