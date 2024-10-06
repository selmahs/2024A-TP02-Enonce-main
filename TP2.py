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

#print(f' \n Bibliotheque initiale : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici


csvfile= open('nouvelle_collection.csv', newline='') 
v= csv.DictReader(csvfile)
for row in v:
    cote_rangement = row["cote_rangement"]
    if cote_rangement not in bibliotheque:
        bibliotheque[cote_rangement] = {
            "Titre:" : row['titre'],
            "Auteur:" : row['auteur'],
            "date_de_publication:" : row['date_publication'],
        }
        print (f"Le livre {cote_rangement} ---- {row['titre']} par {row['auteur']} ---- a été ajouté avec succès")
    else:
        print(f"Le livre {cote_rangement} ---- {row['titre']} par {row['auteur']} ---- est déjà présent dans la bibliothèque")


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici
modif = {}
for coteRangement, details in bibliotheque.items():

    for coteRangement, details in bibliotheque.items():
        if "auteur" in details.keys() and details["auteur"] == "William Shakespeare" and coteRangement.startswith("S"):
            newCote = "WS" + coteRangement[1:]
            modif[coteRangement] = newCote

    for ancienneCote, newCote in modif.items():
        if ancienneCote in bibliotheque:
            bibliotheque[ancienneCote] = bibliotheque.pop(coteRangement[0])

print(f'\nBibliothèque avec modifications de cote : {bibliotheque}\n')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici

csvfile= open('emprunts.csv', newline='') 
c= csv.DictReader(csvfile)

for cote_rangement, info_livre in bibliotheque.items():
    info_livre['emprunts']= "disponible"

for row in c:
    cote_rangement = row['cote_rangement']
    if cote_rangement in bibliotheque:
        bibliotheque[cote_rangement]['emprunts']= "emprunte"
        bibliotheque[cote_rangement]['date_emprunt']= row['date_emprunt']
       
print(f"\n Bibliotheque avec ajout des emprunts : {bibliotheque} \n")


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 
from datetime import datetime

from datetime import timedelta

frais_retard_jour=2
frais_maximal=100
date_today=datetime.now()
delai_de_retour=timedelta (days=30)
livre_perdu=[]

for cote, informations in bibliotheque.items():
  if informations["emprunté"]=="emprunt":
    date_emprunt=datetime.strptime(informations["date_emprunt"], "%Y-%m-$d")
    late_days=(date_today-date_emprunt).days-delai_de_retour.jours

    if late_days>0:
      frais_retard_jour=str(min(late_days*frais_retard_jour,frais_maximal))+"$"
      bibliotheque[cote]["frais_retard"]=frais_retard_jour
    if late_days>365:
      livre_perdu.append(cote)
      bibliotheque[cote]["livre_perdu"]="Oui"
    if late_days<=365:
      livre_perdu.append(cote)
      bibliotheque[cote]["livre_perdu"]="Non"
    else:
      bibliotheque[cote]["livre_perdu"]="Non"


print(f"\nBibliotheque avec ajout des retards et frais: {bibliotheque} \n")