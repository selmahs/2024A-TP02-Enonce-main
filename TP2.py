"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv 
bibliotheque={}
csvfile= open('collection_bibliotheque.csv', newline='') 
c= csv.DictReader(csvfile)
for row in c:
    cote_rangement = row["cote_rangement"]
    bibliotheque[cote_rangement] = {
        "Titre:" : row["titre"],
        "Auteur:" : row["auteur"],
        "date_de_publication:" : row["date_publication"],
    }

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici


csvfile= open('nouvelle_collection.csv', newline='') 
c= csv.DictReader(csvfile)
for row in c:
    cote_rangement = row["cote_rangement"]
    if cote_rangement not in bibliotheque:
        bibliotheque[cote_rangement] = {
            "Titre:" : row["titre"],
            "Auteur:" : row["auteur"],
            "date_de_publication:" : row["date_publication"],
        }
        print (f"Le livre {cote_rangement} ---- {row["titre"]} par {row["auteur"]} ---- a été ajouté avec succès")
    else:
        print(f"Le livre {cote_rangement} ---- {row["titre"]} par {row["auteur"]} ---- est déjà présent dans la bibliothèque")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici






