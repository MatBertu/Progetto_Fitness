from django.urls import path
from . import views

urlpatterns = [
    path('fitness/', views.fitness, name='fitness'),
]