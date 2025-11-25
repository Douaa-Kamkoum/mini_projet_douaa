from menu_client import afficher_menu
from client_tache import ClientTaches



def main():
    # connexion au serveur
    adr_serv = input("entrez l'adresse ip du serveur : ")
    port = int(input("entrez le port du serveur : "))

    client = ClientTaches(adr_serv, port)  # connexion au serveur avec l'adresse et le port
    client.connecter()

    while True:
        afficher_menu()  #affichage du menu
        choix = input("choisissez une option (1-4) : ")

        if choix == "1":
            client.ajouter_tache()  
        elif choix == "2":
            client.lister_taches()  
        elif choix == "3":
            client.supprimer_tache()  
        elif choix == "4":
            client.changer_statut()  
        else:
            print("option invalide  essayez a nouveau.")

if __name__ == "__main__":
    main()

