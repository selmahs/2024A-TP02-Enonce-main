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
        "titre" : row["titre"],
        "auteur" : row["auteur"],
        "date_publication" : row["date_publication"],
    }

print(f' \n Bibliotheque initiale : {bibliotheque} \n')

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
            "titre" : row['titre'],
            "auteur" : row['auteur'],
            "date_publication" : row['date_publication'],
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
    # if "auteur" in details.keys() and details["auteur"] == "William Shakespeare" and coteRangement.startswith("S"):
    if details["auteur"] == "William Shakespeare" and coteRangement.startswith("S"):
        newCote = "WS" + coteRangement[1:]
        modif[coteRangement] = newCote

for ancienneCote, newCote in modif.items():
    bibliotheque[newCote] = bibliotheque.pop(ancienneCote)

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
       
#print(f"\n Bibliotheque avec ajout des emprunts : {bibliotheque} \n")


########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 
import datetime

dateToday = datetime.datetime.now()

for cote_rangement, detail in bibliotheque.items():
    
    if detail["emprunts"] == "emprunte":

        dateEmprunt = datetime.datetime.strptime(detail["date_emprunt"], "%Y-%m-%d")  
        dateDiff = (dateToday-dateEmprunt).days

        if dateDiff>30:
            frais= min((dateDiff-30)*2,100)
            detail["frais_retard"] = frais

        if dateDiff>365 : detail["livre_perdu"]= True

print(f"\n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n")