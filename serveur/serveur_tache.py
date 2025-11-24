import socket  # import d un modile standard
import threading
import json
from serveur.sauvegarde_json import sauvegarder_taches
import socket  # import d'un modile standard
import threading
import json
from serveur.sauvegarde_json import sauvegarder_taches
from serveur.gestionnaire_tache import GestionnaireTaches  # importe notre fonction pour sauvegarder les tâches dans un fichier JSON

class ServeurTaches:
    def __init__(self, adr_serv, port):
        self.adr_serv = adr_serv    # l'adresse ip du serv
        self.port = port            # le num de port de serv
        self.gestionnaire = GestionnaireTaches()  # on mettre l'objet creer par cette classe dans l'att pourquoi mehech fl init

    def demarrer(self):
        socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création du socket serveur
        socket_serv.bind((self.adr_serv, self.port))  # lier le serveur a une @ip et un port 
        socket_serv.listen()  # le serveur est activé en mode ecoute 

        print(f"le serveur est  demarre sur  :{self.adr_serv}:{self.port}")

        while True:
            canal_client, adr_client = socket_serv.accept()
            print(f"l adresse du client connecte : {adr_client}")

            # créer un thread/fil d’exécution pour gérer ce client
            thread_client = threading.Thread(
                target=self.gestion_client,
                args=(canal_client, adr_client)
            )
            thread_client.start()

    def gestion_client(self, canal_client, adr_client):
        try:
            # ---- Envoi du message de bienvenue ----
            canal_client.send("Bienvenue ! Vous êtes maintenant connecté au serveur.".encode())
            print(f"Message de bienvenue envoyé au client {adr_client}.")

            # boucle pour recevoir toutes les commandes du client
            while True:
                message = canal_client.recv(1024).decode()
                if not message:
                    break  # le client a fermé la connexion
                print(f"Commande reçue du client {adr_client} : {message}")
                reponse = self.traiter_commande(message)
                canal_client.send(reponse.encode())

        except Exception as erreur:
            print(f"une erreur avec le client {adr_client} : {erreur}")
        finally:
            canal_client.close()

    def traiter_commande(self, commande):  # c’est le message reçu du client
        try:
            dictio = json.loads(commande)  # transformer le JSON en dictionnaire
        except:
            return "erreur;JSON invalide"

        action = dictio.get("action", "").lower()

        # Ajouter une tâche
        if action == "add":
            titre = dictio.get("titre")
            desc = dictio.get("description") 
            auteur = dictio.get("auteur")
            if not titre or not desc:
                return "erreur;titre ou description manquant"
            tache = self.gestionnaire.ajouter_tache(titre, desc,"TODO",auteur)
            sauvegarder_taches(self.gestionnaire.lister_taches())
            return f"d'accord;tache ajoutee;id={tache.id}"

        # Lister toutes les tâches
        elif action == "list":
            return "\n".join(str(tache) for tache in self.gestionnaire.lister_taches())

        # Supprimer une tâche
        elif action == "del":
            try:
                id_tache = int(dictio.get("id", 0))
            except:
                return "erreur;id invalide"
            if self.gestionnaire.supprimer_tache(id_tache):
                sauvegarder_taches(self.gestionnaire.lister_taches())
                return "d'accord;Tâche supprimee"
            else:
                return "erreur;id inconnu"

        # Changer le statut d'une tâche
        elif action == "update":
            try:
                id_tache = int(dictio.get("id", 0))
                nouv_statut = dictio.get("statut")
                if nouv_statut not in ["TODO", "DOING", "DONE"]:
                    return "erreur;statut invalide"
            except:
                return "erreur;id ou statut invalide"
            if self.gestionnaire.changer_statut(id_tache, nouv_statut):
                return f"d'accord;statut de la tâche {id_tache} modifié"
            else:
                return "erreur;id inconnu"

        else:
            return "erreur;commande inconnue"
