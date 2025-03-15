class Categorie:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description
        self.films = []

    def __str__(self):
        return f"Catégorie: {self.nom}, Description: {self.description}"

    def ajouter_film(self, film):
        if film not in self.films:
            self.films.append(film)
        else:
            return "Ce film est déjà dans cette catégorie."

    def supprimer_film(self, film):
        if film in self.films:
            self.films.remove(film)
        else:
            return "Ce film n'est pas dans cette catégorie."
