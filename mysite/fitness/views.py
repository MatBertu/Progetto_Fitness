from django.http import HttpResponse
from django.template import loader

from .models import Member

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