import os
import json
import datetime

# on veut lire les données dans les fichiers contenue dans le répertoire "Doc Text"
# On veut construire une liste contenant les noms de toutes les personnes dans ces différents documents json.
# Malheureusement essayer de lire les documents dans la liste va généré des exceptions.
# On veut enregistré la date et heure de l'exception dans un fichier texte appellé log_erreur.txt

os.chdir(os.path.dirname(__file__))
os.chdir("Doc Text")

list_fichier_groupes = ['gr2010.json', 'gr2060.json', 'gr2100.json', 'gr2200.json', 'gr2300.json', 'gr3460.json', 'gr2001.json']

for fichier in list_fichier_groupes :
    try:
        with open(fichier,"r") as f_lu :
            texte = f_lu.read()
            data = json.loads(texte)
    except Exception as  e :
        with open("log_erreur.txt","a") as f_ecrit :
                f_ecrit.write(f"Une erreur lors de la lecture des données du fichier {fichier}. Date : {datetime.datetime.now()}\n")
