from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Member(models.Model):
    data_iscrizione = models.DateTimeField(auto_now_add = True)
    altezza = models.DecimalField(max_digits= 5, decimal_places=2, help_text="Inserisci l'altezza in cm")
    peso = models.DecimalField(max_digits= 5, decimal_places=2, help_text="Inserisci il peso in kg")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.altezza} cm, {self.peso} kg)"
    

    class Meta:
      verbose_name_plural = "Members"
      


class CaratteristicheFisiche(models.Model):
   SOTTOPESO = "SOTTOP"
   NORMOPESO = "NORMOP"
   SOVRAPPESO = "SOVRAP"
   
   TIPI_PESO = [
      (SOTTOPESO,"Sottopeso"),
      (NORMOPESO,"Normopeso"),
      (SOVRAPPESO ,"Sovrappeso"),
   ]
   
   tipo_peso = models.CharField(
    max_length = 50,
    choices = TIPI_PESO,
    default = "",
   )
   member = models.ForeignKey(Member, on_delete=models.CASCADE)
   
   def __str__(self):
        return f"{self.member} - {self.get_tipo_peso_display()}"
   
   class Meta:
        verbose_name_plural = "CaratteristicheFisiche"  # Nome singolare
        



class ObiettivoFitness(models.Model):
    OBIETTIVO_CHOICES = [
        ('D', 'Dimagrimento'),
        ('M', 'Massa muscolare'),
        ('F', 'Mantenere la forma fisica'),
        ('A', 'Altro'),
    ]

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    obiettivo = models.CharField(max_length=1, choices=OBIETTIVO_CHOICES)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    note = models.TextField(blank=True)


    def __str__(self):
        return f"{self.member} - {self.get_obiettivo_display()}"

class Workout(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    type = models.CharField(max_length=100)
    bodypart = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    rating = models.FloatField()
    reatingdesc = models.TextField()


    def __str__(self):
        return self.title
    

class Plan(models.Model):
    title = models.CharField(max_length=100)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    workouts = models.ManyToManyField(Workout)

    def __str__(self):
        return f"{self.member} - {self.title}"
