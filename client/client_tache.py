import socket
import json

class ClientTaches:
    def __init__(self, adr_serv, port):  # recuperation des infos de serveur 
        self.adr_serv = adr_serv
        self.port = port
        self.client_socket = None  # pour garder la connexion ouverte

    def connecter(self):
        """ Se connecter une seule fois au serveur et recevoir le message de bienvenue """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.adr_serv, self.port))

        # ---- Réception message de bienvenue ----
        msg_bienvenue = self.client_socket.recv(1024).decode()
        print(msg_bienvenue)  # s'affiche AVANT le menu

    def envoyer_commande(self, commande):
        """ Envoie une commande au serveur et reçoit la réponse """

        # Convertit un dictionnaire Python en texte JSON
        message = json.dumps(commande)

        # Envoi de la commande au serveur
        self.client_socket.send(message.encode())

        # Réception de la réponse
        reponse = self.client_socket.recv(1024).decode()
        print(f"la reponse du serveur : {reponse}")

    def ajouter_tache(self):
        nom_utilisateur = input("entrez votre nom : ")  # Demander le nom de l'utilisateur
        titre = input("entrez le titre de la tache : ")
        description = input("entrez la description de la tache : ")
        commande = {
            "action": "add",
            "titre": titre,
            "description": description,
            "auteur": nom_utilisateur  # envoyer le nom choisi par l'utilisateur
        }
        self.envoyer_commande(commande)

    def lister_taches(self):
        commande = {"action": "list"}
        self.envoyer_commande(commande)

    def supprimer_tache(self):
        id_tache = int(input("entrez l'id de la tache a supprimer : "))
        commande = {"action": "del", "id": id_tache}
        self.envoyer_commande(commande)

    def changer_statut(self):
        id_tache = int(input("entrez l'id de la tache a modifier : "))
        statut = input("entrez le nouveau statut (TODO, DOING, DONE) : ")
        commande = {"action": "update", "id": id_tache, "statut": statut}  # update pour modifer la tache comme add
        self.envoyer_commande(commande)
