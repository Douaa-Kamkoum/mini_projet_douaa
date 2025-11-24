class Tache:
    def __init__(self, id, titre, description, statut, auteur ):
        self.id =id
        self.titre = titre
        self.description = description
        # todo ou doing ou done pour l'attr statut
        self.statut = statut  
        self.auteur = auteur

    def __str__(self):
        return f"{self.id} , {self.titre} , {self.description} , {self.statut} , {self.auteur}"
