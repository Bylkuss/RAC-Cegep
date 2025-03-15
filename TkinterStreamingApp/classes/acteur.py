from .personne import Personne
class Acteur(Personne):
    def __init__(self, nom, prenom, sexe, nom_personnage, debut_emploi, fin_emploi, cachet):
        super().__init__(nom, prenom, sexe)
        self.nom_personnage = nom_personnage
        self.debut_emploi = debut_emploi
        self.fin_emploi = fin_emploi
        self.cachet = cachet
        self.films = []
        self.id = id(self)

    def __str__(self):
        return f"Acteur: {self.nom} {self.prenom}, Personnage: {self.nom_personnage}"

    def ajouter_film(self, film):
        if film not in self.films:
            self.films.append(film)
        else:
            return "Cet acteur est déjà associé à ce film."

    def supprimer_film(self, film):
        if film in self.films:
            self.films.remove(film)
        else:
            return "L'acteur n'est pas associé à ce film."

    def calculer_cachet_total(self):
        return len(self.films) * self.cachet
