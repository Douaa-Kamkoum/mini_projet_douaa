import json

def sauvegarder_taches(taches, nom_fichier="taches.json"):
    """
    Sauvegarde la liste des tâches dans un fichier JSON.
    
    taches : liste d'objets tache
    nom_fichier : nom du fichier JSON
    """
    # Afficher les tâches avant de les sauvegarder pour vérifier l'attribut auteur
   
    
    # Sauvegarde des tâches dans le fichier JSON
    with open(nom_fichier, "w") as f:
        json.dump([t.__dict__ for t in taches], f, indent=4)
       

