from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import UserRegistrationForm, MemberRegistrationForm,WorkoutForm, PlanForm, ObiettivoFitnessForm, CaratteristicheFisicheForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.template import loader
from django.db import models

from .models import Member,CaratteristicheFisiche,ObiettivoFitness,Plan,Workout

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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        member_form = MemberRegistrationForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            login(request, user)
            return redirect('/fitness/fitness')  # Modifica con la tua pagina di destinazione
    else:
        user_form = UserRegistrationForm()
        member_form = MemberRegistrationForm()
    return render(request, 'fitness/register.html', {'user_form': user_form, 'member_form': member_form})




# Aggiungi un nuovo workout
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fitness/overview')  # Sostituisci con la tua pagina
    else:
        form = WorkoutForm()
    return render(request, 'fitness/add_workout.html', {'form': form})



# Aggiungi un nuovo piano
def add_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.member = Member.objects.get(user=request.user)  # Associa il piano al membro autenticato
            plan.save()
            form.save_m2m()  # Salva i workout associati
            return redirect('fitness/overview')  # Sostituisci con la tua pagina
    else:
        form = PlanForm()
    return render(request, 'fitness/add_plan.html', {'form': form})

# Aggiungi un obiettivo fitness
def add_obiettivo_fitness(request):
    if request.method == 'POST':
        form = ObiettivoFitnessForm(request.POST, user =request.user)
        if form.is_valid():
            form.save()
            return redirect('fitness/overview')  # Sostituisci con la tua pagina
    else:
        form = ObiettivoFitnessForm()
    return render(request, 'fitness/add_obiettivo_fitness.html', {'form': form})

# Aggiungi una caratteristica fisica
def add_caratteristica_fisica(request):
    if request.method == 'POST':
        form = CaratteristicheFisicheForm(request.POST ,user =request.user)
        if form.is_valid():
            form.save()
            return redirect('fitness/overview')  # Sostituisci con la tua pagina
    else:
        form = CaratteristicheFisicheForm()
    return render(request, 'fitness/add_caratteristica_fisica.html', {'form': form})

def fitness_overview(request):
    # Ottieni il membro attualmente autenticato
    member = Member.objects.get(user=request.user)

    # Recupera i dati associati al membro
    caratteristiche = CaratteristicheFisiche.objects.filter(member=member)
    plans = Plan.objects.filter(member=member)
    workouts = Workout.objects.all()  # Mostra tutti i workout disponibili
    obiettivi = ObiettivoFitness.objects.filter(member=member)

    # Passa i dati al template
    context = {
        'member': member,
        'caratteristiche': caratteristiche,
        'plans': plans,
        'workouts': workouts,
        'obiettivi': obiettivi,
    }
    return render(request, 'fitness/overview.html', context)