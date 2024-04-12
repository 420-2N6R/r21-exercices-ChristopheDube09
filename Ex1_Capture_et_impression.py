# Voici un petit script pour renommer les fichers dans le répertoire VIDEOS
#    MAIS
# ce script va rencontrer des exceptions si certains des fichiers n'ont pas le bon format de nom
# ajouter un try...except qui va imprimer le nom des fichiers qui n'a pas pu être renommer ainsi que l'erreur causer.

import os
os.chdir(os.path.dirname(__file__))

os.chdir("csvs")

for fichier in os.listdir():
    nom_fichier, ext = os.path.splitext(fichier)
    titre, cours, num = nom_fichier.split()
    titre = titre.strip()
    cours = cours.strip()

    num = num.strip()
    num = num[1:]   # retire le dièse juste avant le numéro de cours
    num = num.zfill(2) # rajoute des 0 avec le numéro de cours pour obtenir un num de 2 caractères

    nouveau_nom = f"{num} {cours} {titre}{ext}"
    os.rename(fichier, nouveau_nom)