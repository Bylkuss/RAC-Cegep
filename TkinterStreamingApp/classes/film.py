class Film:
    def __init__(self, nom, duree, description):
        self.nom = nom
        self.duree = duree
        self.description = description
        self.categories = []
        self.acteurs = []
        self.id = id(self)

    def __str__(self):
        return f"Film: {self.nom}, Durée: {self.duree} min, Description: {self.description}"

    def ajouter_categorie(self, categorie):
        if categorie not in self.categories:
            self.categories.append(categorie)
        else:
            return "Cette catégorie est déjà associée à ce film."

    def supprimer_categorie(self, categorie):
        if categorie in self.categories:
            self.categories.remove(categorie)
        else:
            return "Cette catégorie n'est pas associée à ce film."

    def ajouter_acteur(self, acteur):
        if acteur not in self.acteurs:
            self.acteurs.append(acteur)
        else:
            return "Cet acteur est déjà associé à ce film."

    def supprimer_acteur(self, acteur):
        if acteur in self.acteurs:
            self.acteurs.remove(acteur)
        else:
            return "Cet acteur n'est pas associé à ce film."
