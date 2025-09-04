from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

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
  
  return render(request, 'fitness/homepage.html')



def workout(request):

# Carica il dataset
    df = pd.read_csv('../megaGymDataset.csv')

    # Seleziona le colonne necessarie
    tabella = df[['Title', 'Desc', "Type", "BodyPart", "Equipment", "Level", "Rating", "RatingDesc"]]

    # Converti il DataFrame in una lista di dizionari
    workouts = tabella.to_dict(orient='records')

    # Applica la paginazione
    paginator = Paginator(workouts, 20)  # Mostra 20 righe per pagina
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Passa i dati al template
    context = {
        'page_obj': page_obj
    }
    return render(request, "fitness/workout.html", context=context)

def ollama(request):
    prompt_default = "Comportati da personal trainer e consigliami qualche esercizio giornaliero di rilassamento"
    if request.method == "POST":
        user_query = request.POST.get("query", "").strip()
        prompt = user_query if user_query else prompt_default
    else:
        prompt = prompt_default

    model = OllamaLLM(model="gemma3:4b")
    response = model.invoke(input=prompt)
    context = {"response": markdown.markdown(response, extensions=["extra", "codehilite"])}
    return render(request, "fitness/ollama.html", context=context)

def foods(request):
    consumer_key = '92c4597e973d4bfe8c4b96f19ac473df'
    consumer_secret = '91808c0b278f48ababe8dbeaf75649a0'
    
    query = ""
    foods_list = []

    # Controlla se il metodo della richiesta è POST (cioè se il form è stato inviato)
    if request.method == 'POST':
        # Ottieni il testo cercato dall'utente dal campo <input name="query">
        query = request.POST.get('query', '')
        
        if query:
            try:
                fs = Fatsecret(consumer_key, consumer_secret)
                # Esegui la ricerca con la query dell'utente
                foods_list = fs.foods_search(query)
            except Exception as e:
                # È una buona pratica gestire eventuali errori dall'API
                print(f"Errore durante la chiamata all'API Fatsecret: {e}")
                foods_list = []

    # Prepara il contesto da passare al template
    context = {
        'foods': foods_list,
        'query': query,  # Passiamo anche la query per mostrarla di nuovo nella barra di ricerca
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

            # Aggiungi qui il messaggio di successo! ✅
            messages.success(request, 'Registrazione avvenuta con successo!')

            return redirect('/fitness/overview')  # Modifica con la tua pagina di destinazione
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
    obiettivi = ObiettivoFitness.objects.filter(member=member)
    workouts = Workout.objects.all()  # Mostra tutti i workout disponibili

    # Applica la paginazione: mostra solo 20 righe per pagina
    paginator = Paginator(workouts, 20)  # Mostra 20 workout per pagina
    page_number = request.GET.get('page', 1)  # Ottieni il numero della pagina dalla query string
    page_obj = paginator.get_page(page_number)  # Ottieni i workout per la pagina corrente

    # Passa i dati al template
    context = {
        'member': member,
        'caratteristiche': caratteristiche,
        'plans': plans,
        'obiettivi': obiettivi,
        'page_obj': page_obj,  # Aggiungi l'oggetto della paginazione ai dati
    }
    return render(request, 'fitness/overview.html', context)

def unity_view(request):
    return render(request, 'fitness/unity.html')