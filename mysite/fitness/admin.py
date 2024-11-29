from django.contrib import admin

# Register your models here.
from .models import Member, Workout, Plan
from .models import CaratteristicheFisiche
from .models import ObiettivoFitness

admin.site.register(ObiettivoFitness)
admin.site.register(CaratteristicheFisiche)
admin.site.register(Member)
admin.site.register(Workout)
admin.site.register(Plan)

