## Progetto_Fitness

# Idea di un sito per monitorare la salute fisica ,abbinata a un programma di allenamento specifico che varia per ogni singolo individuo , con possibilità di collegare tali dati ad uno smartwatch tipo Fitbit.

## Requirements

Questo progetto funziona con Python 3.12.

## Step to run
```sh
1.clone the repo and enter the folder

git clone  ex:( https://github.com/bertux-8/Progetto_Django.git )

cd nome cartella >>(Progetto_Django)
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

2.  update the deps file

```sh
pip freeze > requirements.txt

```
# Entra nella cartella del sito
```sh
1. cd (nome cartella)mysite
```
# Run the server/site
```sh
1. python manage.py runserver
```

2. Si aprirà il Browser con l'host di defeault http://127.0.0.1:8000/

3. Aggiungi all'indirizzo sopra fitness o allenamenti in base al sito che vuoi visualizzare.

# Esegui le migrazioni se necessarie
```sh
python manage.py migrate
```

#Funzionalità in fase di sviluppo 
```sh
Scelta dei programmi di allenamento su misura per ogni singolo individuo

Allestimento pagina di allenamenti e schede programmate 

Possibilità di scegliere un tipo di workout da una lista all'interno di un database .


```
# Esegui il seguente commando per importare la lista dei workout:

```sh

python manage.py import_csv ../megaGymDataset.csv

```
