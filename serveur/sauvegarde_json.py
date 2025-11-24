import json

def sauvegarder_taches(taches, nom_fichier="taches.json"):
   
    # sauvegarde des taches dans le fichier json
    with open(nom_fichier, "w") as f:
        json.dump([t.__dict__ for t in taches], f, indent=4)
       

