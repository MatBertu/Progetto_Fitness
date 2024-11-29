from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.db import models

from .models import Member
from langchain_ollama import OllamaLLM
import markdown
import pandas as pd 
from fatsecret import Fatsecret

def fitness(request):
  
  return render(request, 'fitness/fitness.html')



def workout(request):

  df=pd.read_csv('../megaGymDataset.csv')
    
  print(df.columns)
  tabella=df[['Title', 'Desc',"Type","BodyPart","Equipment","Level","Rating","RatingDesc"]]

      


  context ={
        'tabella':tabella.to_html()
        }    
  return render (request, "fitness/workout.html", context = context )

def ollama(request):


  model = OllamaLLM(model="llama3.2:latest")
  #qwen2.5:latest provato il 7b ma troppo lento 

  response = model.invoke(input="Comportati da personal trainer e consigliami qualche esercizio giornaliero di rilassamento ")
  
  context = {"response" : markdown.markdown(response, extensions =["extra","codehilite"])}
  
  return render(request,"fitness/ollama.html", context = context )



def foods(request, food=None):
  consumer_key = '92c4597e973d4bfe8c4b96f19ac473df'
  consumer_secret = '91808c0b278f48ababe8dbeaf75649a0'

  if food:
    try:
      fs = Fatsecret(consumer_key, consumer_secret)
      foods = fs.foods_search(food)
    except:
      foods = []
    print(foods)
  else:
    foods = []

  context = {
    'foods': foods,
  }
  return render(request, 'fitness/food.html', context=context)


