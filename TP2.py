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

#csvfile= open('nouvelle_collection.csv', newline='') 
#c= csv.DictReader(csvfile)
#for row in c:
 #    cote_rangement = row['cote_rangement']
  #   if row['auteur'] == "William Shakespeare":
   #      nouvelle_cote = "WS" + cote_rangement[1:]
    #     valeur = bibliotheque.pop(cote_rangement)
     #    bibliotheque[nouvelle_cote] = valeur
#print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')
coteModif =[]
for cote_rangement, details in list(bibliotheque.items()):
   if 'auteur' in details and details['auteur'] == "William Shakespeare" :
        nouvelleCote = "WS" + cote_rangement[1:]
        coteModif.append((cote_rangement,nouvelleCote, details))
for ancienneCote, nouvelleCote, info in coteModif:
    bibliotheque[nouvelleCote] = info 
    del bibliotheque[ancienneCote]

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
       
print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici
from datetime import datetime,date
frais = 0

for row in c:
    cote_rangement = row["cote_rangement"]
    dateEmprunt = date(int(row['date_emprunt'][:4]), int(row['date_emprunt'][5:7]),int(row['date_emprunt'][8:10]))
    today= date.today()
    diffTemps= today - dateEmprunt
    diffJour= diffTemps.days
    if cote_rangement in bibliotheque and diffJour>30:
        frais= (diffJour-30)*2
        if frais<= 100:
            bibliotheque[cote_rangement]['frais_retars']= frais
        if frais>100:
            bibliotheque[cote_rangement]['frais_retars']= frais
        if diffJour> 365:
            bibliotheque[cote_rangement]['livre_perdus']= "perdus"

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')

