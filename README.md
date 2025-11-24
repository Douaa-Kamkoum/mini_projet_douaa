# mini_projet_douaa
projet gestionnaire de tâches partagé (client–serveur en Python + Git + Docker) 
description de mon mini projet , ce dernier contient :

dans la partie poo:
.un serveur qui gere des taches comme l ajout la suppression lister les taches et la modification du statut 
.un client qui envoie des requetes au serveur
.une communication  entre le client et le serveur selon un protocole basée 
. cette communication est basé sur des sockets
.les taches sont sauvegardées avec json

dans la partie git:
. un depot local conteint des branche , main l: la version stable , dev : integration 
   et les branches features feature/serveur, feature/client et feature/docker
. utilisation de merges 
.deposer le depot local en distant , github 

dans la partie docker:
.une containerisation Docker
.deux contenaires un pour clients l 'autre pour serveur , et bien sure deux image 
. deux Dockerfiles et docker_compose.yml

comment lancer le projet sans docker?
    >>>>pour lancer le serveur:
          dans terminal : python -m serveur.serveur_main  ou bien cd serveur  puis python serveur_main.py
    >>>>pour lancer le client
         dans terminal : python -m client.client_main   ou bien cd client  puis python client_main.py 
             remarque: le client doit recuperer l adresse et le num de port du serveur pour ce connecter

comment lancer le projet avec docker?
         >>>>construire les images:docker compose build
         >>>>lancer les conteneurs:docker compose up
    biensure Dockerfiles et docker-compose.yml existe
