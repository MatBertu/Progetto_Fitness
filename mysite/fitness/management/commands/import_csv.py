import csv 
from django.core.management.base import BaseCommand, CommandParser
from fitness.models import Workout

class Command(BaseCommand):
    help = "importa dati da un file CSV nel database"

    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str, help="Percorso del file CSV" )
        
    def handle(self,*args,**kwargs):
        file_path = kwargs["file_path"] # Percorso del file CSV passato come argomento

        # Apertura del file CSV

        with open(file_path, newline = '', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)  # Lettura del file CSV come dizionari
            for row in reader:
                # Creazione e salvataggio di un oggetto Workout per ogni riga
                Workout.objects.create(
                    title = row ["Title"],
                    desc = row ["Desc"],
                    type = row ["Type"],
                    bodypart = row ["BodyPart"],
                    equipment=row['Equipment'],
                    level=row['Level'],
                    rating = float(row['Rating']) if row['Rating'] else 0.0,  # Imposta 0.0 quando il valore è vuoto # Gestisce valori vuoti  # Convertiamo Rating in un numero
                    reatingdesc=row['RatingDesc']
                )
        # Messaggio di successo
        self.stdout.write(self.style.SUCCESS('Dati importati con successo!'))


    