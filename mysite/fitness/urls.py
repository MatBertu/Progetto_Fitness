from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('fitness/<str:food>', views.fitness, name='fitness'),
    path('homepage/', views.fitness, name='fitness'),
    path("workout/",views.workout, name = " workout"),
    path("ollama/",views.ollama, name = "ollama"),
    path("foods/",views.foods, name = "foods"),
    path("foods/<str:food>",views.foods, name = "foods"),
    path('login/', auth_views.LoginView.as_view(template_name='fitness/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Registrazione utente
    path('add_workout/', views.add_workout, name='fitness/add_workout'),
    path('add_plan/', views.add_plan, name='fitness/add_plan'),
    path('add_obiettivo_fitness/', views.add_obiettivo_fitness, name='fitness/add_obiettivo_fitness'),
    path('add_caratteristica_fisica/', views.add_caratteristica_fisica, name='fitness/add_caratteristica_fisica'),
    path('overview/',views.fitness_overview, name= 'fitness/overview'),
    path('unity/',views.unity_view, name="fitness/unity"),
  
]
   
   
