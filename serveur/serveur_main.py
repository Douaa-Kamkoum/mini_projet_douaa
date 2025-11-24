from serveur.tache import Tache
from serveur.gestionnaire_tache import GestionnaireTaches
from serveur.serveur_tache import ServeurTaches


# test des classes Tache et GestionnaireTaches
def tester_classes():
    # test simple de la classe Tache
    t = Tache(1, "revision", "la couche transport", "TODO", "Douaa")
    print("test de la classe Tache :")
    print(t)

    # tester GestionnaireTaches
    gest = GestionnaireTaches()
    print("ajout des taches") 
    t1 = gest.ajouter_tache("reviser", "poo", "TODO", "douaa")
    t2 = gest.ajouter_tache("coder", "mini-projet", "TODO", "baya")
    t3 = gest.ajouter_tache("sport", "gymnastique", "TODO", "hedi") 

    print("\ntaches apres l'ajout :") 
    for t in gest.lister_taches():
        print(t)

    # tester changement de statut
    print("\nchanger le statut de la tache 1 en DOING") 
    gest.changer_statut(1, "DOING")
    print(gest.taches[1])

    # tester suppression
    print("\nsuppression de la tâche 2") 
    gest.supprimer_tache(2)

    print("\ntaches restantes :") 
    for t in gest.lister_taches():
        print(t)



def main():
    # tester les classes Tache et GestionnaireTaches
    tester_classes()

    # demander à l'utilisateur l'adresse ip et le port du serveur
    adr_serv = input("entrez l'adresse ip du serveur : ")
    port = int(input("entrez le port du serveur : "))

    # créer et démarrer le serveur
    serveur = ServeurTaches(adr_serv, port)
    print("\ndemarrage du serveur")
    serveur.demarrer()

   

if __name__ == "__main__":
    main()
