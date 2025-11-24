import os
from serveur.serveur_tache import ServeurTaches

if __name__ == "__main__":
    # Lecture de l'adresse et du port depuis les variables d'environnement
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "5000"))

    # Creation du serveur et démarrage
    serveur = ServeurTaches(host, port)
    serveur.demarrer()
