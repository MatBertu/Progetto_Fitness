from django.urls import path
from . import views

urlpatterns = [
    path('fitness/', views.fitness, name='fitness'),
    path('allenamenti/', views.allenamenti, name='allenamenti'),
    path("ollama/",views.ollama, name = "ollama"),
    
]