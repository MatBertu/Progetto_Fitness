from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.db import models

from .models import Member
from langchain_ollama import OllamaLLM
import markdown
import pandas as pd 



def fitness(request):
  members = Member.objects.all().values()
  template = loader.get_template('fitness/fitness.html')
 

  context = {
    'members': members
  }
  return HttpResponse(template.render(context, request))

def allenamenti(request):
  members = Member.objects.all().values()
  template = loader.get_template('fitness/allenamenti.html')
 

  context = {
    'members': members
  }
  return HttpResponse(template.render(context, request))

  pass

def ollama(request):


  model = OllamaLLM(model="llama3.2:latest")
  #qwen2.5:latest provato il 7b ma troppo lento 

  response = model.invoke(input="Comportati da personal trainer e consigliami qualche esercizio giornaliero di rilassamento ")
  
  context = {"response" : markdown.markdown(response, extensions =["extra","codehilite"])}
  
  return render(request,"fitness/ollama.html", context = context )





def workout(request):

  df=pd.read_csv('../megaGymDataset.csv')
    
  print(df.columns)
  tabella=df[['Title', 'Desc',"Type","BodyPart","Equipment","Level","Rating","RatingDesc"]]

      


  context ={
        'tabella':tabella.to_html()
        }    
  return render (request, "fitness/workout.html", context = context )

 #WORKING IN PROGRESS VISTA API SPORT

def index(request):
 
  return render(request, 'fitness/index.html')