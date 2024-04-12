import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

class Etudiant: pass

class Bilan : pass

def lire_CSV_notes(path) -> list[Etudiant]:
    with open(path, "r", encoding='utf-8') as f_lu:
        csv_reader = csv.reader(f_lu,delimiter=';')
        en_tete = next(csv_reader)
        liste_etudiants = []
        for ligne in csv_reader :
            # À COMPLETER, POUR CHAQUE LIGNE CRÉE UN ÉTUDIANT ET AJOUTER LE À LA liste_etudiants
            pass
            
    return liste_etudiants



if __name__ == "__main__" :
    nom_cours = "Prog 2"
    étudiants = lire_CSV_notes("resultats_evaluation.csv")
    
    #bilan_cours = Bilan()



# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)

# Vous devez aussi imprimer les étudiants, leur id, et s'ils on passé ou non dans le terminal en imprimant l'instance de bilan.