import os
import csv
os.chdir(os.path.dirname(__file__)) # Cette ligne fait que l'exécution du script aura toujours lieu dans le répertoire où il se trouve.

class Etudiant: 
    def __init__(self, id, nom, notes):
        self.id = id
        self.nom = nom
        self.notes = notes
        self.a_reussi = self.calculer_reussite()

    def calculer_reussite(self):
        moyenne = sum(self.notes) / len(self.notes)
        return moyenne >= 60  # Suppose que la note de passage est 60



class Bilan:
    def __init__(self, nom_cours, etudiants):
        self.nom_cours = nom_cours
        self.etudiants = etudiants
        self.moyenne = self.__calculer_moyenne()
        self.taux_succes =

    def nombre_reussis(self):
        return sum(1 for etudiant in self.etudiants if etudiant.a_reussi)

    def moyenne_reussis(self):
        notes_reussis = [etudiant for etudiant in self.etudiants if etudiant.a_reussi]
        return sum(sum(etudiant.notes) for etudiant in notes_reussis) / len(notes_reussis) if notes_reussis else 0

    def moyenne_tous(self):
        return sum(sum(etudiant.notes) for etudiant in self.etudiants) / len(self.etudiants) if self.etudiants else 0

    def taux_succes(self):
        return (self.nombre_reussis() / len(self.etudiants)) * 100 if self.etudiants else 0

    def __str__(self):
        result = f"Bilan pour le cours {self.nom_cours} :\n"
        result += f"Nombre d'étudiants ayant réussi : {self.nombre_reussis()}\n"
        result += f"Moyenne des étudiants ayant réussi : {self.moyenne_reussis()}\n"
        result += f"Moyenne de tous les étudiants : {self.moyenne_tous()}\n"
        result += f"Taux de succès au cours : {self.taux_succes()}%\n\n"
        for etudiant in self.etudiants:
            result += f"ID: {etudiant.id}, Nom: {etudiant.nom}, Notes: {etudiant.notes}, Réussi: {'Oui' if etudiant.a_reussi else 'Non'}\n"
        return result


def lire_CSV_notes(path) -> list[Etudiant]:
    with open(path, "r", encoding='utf-8') as f_lu:
        csv_reader = csv.reader(f_lu,delimiter=';')
        en_tete = next(csv_reader)
        liste_etudiants = []
        for ligne in csv_reader :
            id, nom = ligne[:2]
            notes = list(map(int, ligne[2:]))  # Convertir les notes en entiers
            etudiant = Etudiant(id, nom, notes)
            liste_etudiants.append(etudiant)
            
    return liste_etudiants



if __name__ == "__main__" :
    nom_cours = "Prog 2"
    étudiants = lire_CSV_notes("resultats_evaluation.csv")
    bilan_cours = Bilan(nom_cours, étudiants)
    print("Nombre d'étudiants ayant réussi :", bilan_cours.nombre_reussis())
    print("Moyenne des étudiants ayant réussi :", bilan_cours.moyenne_reussis())
    print("Moyenne de tous les étudiants :", bilan_cours.moyenne_tous())
    print("Taux de succès au cours :", bilan_cours.taux_succes(), "%")



# À la fin de cette partie, on veut imprimer : 
#           - Le nombre d'étudiants ayant passé.
#           - La moyenne de ces étudiants
#           - La moyenne de tous les étudiants
#           - Le taux de succès au cours (pourcentage d'étudiants ayant passé)

# Vous devez aussi imprimer les étudiants, leur id, et s'ils on passé ou non dans le terminal en imprimant l'instance de bilan.

