from serveur.tache import Tache

class GestionnaireTaches:
    def __init__(self):
        self.taches = {}   # un dict 
        self.compteur_id = 1
        
#une methode pour ajouter une tache dans le dict et incrementer a chaque ajout l'id du prochaine tache 
    
    def ajouter_tache(self, titre, description, statut,auteur):
        if not statut:
            statut = "TODO"  #  par defaut si statut n'est pas specifie
        if not auteur:
            auteur = "client"  
        nouv_tache = Tache(self.compteur_id, titre, description, statut ,auteur)
        self.taches[self.compteur_id] = nouv_tache
        self.compteur_id += 1
        return nouv_tache
    
#une methode qui supprime une tache selon l'id  
  
    def supprimer_tache(self, id_tache):
        if id_tache in self.taches:
            del self.taches[id_tache]
            return True
        return False

#une methode sert a lister tout les taches de dict
    def lister_taches(self):
        return list(self.taches.values())

    
#une methode pour changer le statut(todo,doing,done)
    def changer_statut(self, id_tache, nouv_statut):
        if id_tache in self.taches:
            self.taches[id_tache].statut = nouv_statut
            return True
        return False
