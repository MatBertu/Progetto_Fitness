from django.urls import path
from . import views

urlpatterns = [
    path('fitness/', views.fitness, name='fitness'),
    path("workout/",views.workout, name = " workout"),
    path("ollama/",views.ollama, name = "ollama"),
    
   
]