from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Member(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length= 50)
    data_iscrizione = models.DateTimeField(auto_now_add = True)
    username = models.CharField(max_length = 50, unique = True)
    altezza = models.DecimalField(default=0,max_digits= 5, decimal_places=2, help_text="Inserisci l'altezza in cm")
    peso = models.DecimalField(default=0,max_digits= 5, decimal_places=2, help_text="Inserisci il peso in kg")
    
    def __str__(self):
        return f"Altezza: {self.altezza} cm, Peso: {self.peso} kg"
    
    REQUIRED_FIELDS = ['nome', 'cognome','peso','altezza']


    class Meta:
      verbose_name_plural = "Utenti"


    def __str__(self)->str:
      return self.username
      


class CaratteristicheFisiche(models.Model):
   SOTTOPESO = "SOTTOP"
   NORMOPESO = "NORMOP"
   SOVRAPPESO = "SOVRAP"
   


   SCELTA_TROVA_CARATTERISTICHE = [
      (SOTTOPESO,"Sottopeso"),
      (NORMOPESO,"Normopeso"),
      (SOVRAPPESO ,"Sovrappeso"),
   ]
   
   Scelta_Caratteristiche = models.CharField(
    max_length = 50,
    choices = SCELTA_TROVA_CARATTERISTICHE,
    default = "",
   )

   class Meta:
        verbose_name = "CaratteristicheFisiche"  # Nome singolare
        
   def __str__(self):
        return self.nome



class ObiettivoFitness(models.Model):
    UTENTE_OBIETTIVO_CHOICES = [
        ('D', 'Dimagrimento'),
        ('M', 'Massa muscolare'),
        ('F', 'Mantenere la forma fisica'),
        ('A', 'Altro'),
    ]




    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    obiettivo = models.CharField(max_length=1, choices=UTENTE_OBIETTIVO_CHOICES)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    note = models.TextField(blank=True)


    def __str__(self):
        return f"{self.utente.username} - {self.get_obiettivo_display()}"

