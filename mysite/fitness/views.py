from django.shortcuts import render
from django.http import HttpResponse


def fitness(request):
    return HttpResponse("Hello, world. You're at the fitness site ")

