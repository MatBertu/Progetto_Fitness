

## Fytex

# Idea di un sito per monitorare la salute fisica ,abbinata a un programma di allenamento specifico che varia per ogni singolo individuo , con possibilità di collegare tali dati ad uno smartwatch tipo Fitbit.


## Requirements

Questo progetto funziona con Python 3.12.

Necessarie tutte le dipendenze contenute nel file requirements.txt

## Step to run
```sh
1.clone the repo and enter the folder

git clone  ex:( https://github.com/bertux-8/Progetto_Fitness.git )

cd nome cartella >>(Progetto_Fitness)
```

```sh
2. create a Python venv

python3.12 -m venv .venv
```

```sh
3. activate the Python venv
a. (Linux/macOS)

source .venv/bin/activate

or

b.(Windows Command Prompt)

.venv/Scripts/activate.bat

or

c.(Windows Powershell)

.venv/Scripts/Activate.ps1


or ( Windows Git Bash)
d.

. .venv/Scripts/Activate

```


4.Install the dependencies

```sh
pip install -r requirements.txt
```

# If you install a new dependecy / library
1.install the new dependecy (es.Django)
```sh
pip install Django
```

2. Print the dependecy
```sh
pip freeze (Stampa la lista delle deps)
```

3.  update the deps file

```sh


pip freeze > requirements.txt

```
# Entra nella cartella del sito
```sh
1. cd (nome cartella)mysite
```

# Esegui le migrazioni se necessarie
```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```
# Esegui il seguente commando per importare la lista dei workout nel database:

```sh

python manage.py import_csv ../megaGymDataset.csv

```
# Run the server/site
```sh
1. python manage.py runserver
```

2. Si aprirà il Browser con l'host di defeault http://127.0.0.1:8000/

3. Aggiungi all'indirizzo sopra 'fitness' per visualizzare l'homepage  del progetto, oppure gli altri urls in base alla pagina che vuoi visualizzare.



# Elenco funzionalità del sito:
```sh
Un utente una volta loggato può eseguire le seguenti azioni ;

1 Scelta dei programmi di allenamento su misura per ogni singolo individuo

2 Possibilità di scegliere un tipo di workout da una lista all'interno di un database 

3 Consultare una pagina dove puoi controllare le calorie e le caratteristiche di ogni alimento(tramite le API fatsecret),per poterlo fare aggiungi all'indirizzo predefinito "fitness/foods/" qualsiasi tipo di alimento ex. pizza.

4 Chiedere ad un assistente digitale consigli giornalieri su ruoutine giornalieri di esercizi tipo stretching, puoi farlo da un bottone sull'homepage.


```



# Funzionalità in fase di sviluppo 
```sh
Allestimento dell'intefaccia grafica per il profilo di ogni singolo utente

Implementazione di una funzionalità per poter vedere i dati di uno smartwatch qualsiasi.

Implementazione di una stanza di palestra in 3D.

```

# Riferimenti delle librerie usate in rete 
```sh
Ollama:
https://ollama.com/library/llama3.2

Utilizzo delle API Fatsecret:

https://platform.fatsecret.com/platform-api
```