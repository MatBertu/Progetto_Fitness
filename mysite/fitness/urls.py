from django.urls import path
from . import views

urlpatterns = [
    path('fitness/<str:food>', views.fitness, name='fitness'),
    path('fitness/', views.fitness, name='fitness'),
    path("workout/",views.workout, name = " workout"),
    path("ollama/",views.ollama, name = "ollama"),
    path("foods/",views.foods, name = "foods"),
    path("foods/<str:food>",views.foods, name = "foods")
   
   
]