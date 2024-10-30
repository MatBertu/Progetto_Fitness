from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.db import models 

from .models import Member
from langchain_ollama import OllamaLLM
import markdown


def fitness(request):
  members = Member.objects.all().values()
  template = loader.get_template('fitness.html')
 

  context = {
    'members': members
  }
  return HttpResponse(template.render(context, request))

def allenamenti(request):
  members = Member.objects.all().values()
  template = loader.get_template('allenamenti.html')
 

  context = {
    'members': members
  }
  return HttpResponse(template.render(context, request))



def ollama(request):

  
  model = OllamaLLM(model="gemma2:2b")
  
  response = model.invoke(input="Fai qualche esempio di progetto web")
  
  context = {"response" : markdown.markdown(response, extensions =["extra","codehilite"])}
  
  return render(request,"fitness/ollama.html", context = context )