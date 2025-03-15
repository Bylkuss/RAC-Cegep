from .personne import Personne
class Employe(Personne):
    def __init__(self, nom, prenom, sexe, date_embauche, code_utilisateur, password, type_acces):
        super().__init__(nom, prenom, sexe)
        self.date_embauche = date_embauche
        self.code_utilisateur = code_utilisateur
        self.password = password
        self.type_acces = type_acces
        self.id = id(self)

    def __str__(self):
        return f"Employe: {self.nom} {self.prenom}, Code utilisateur: {self.code_utilisateur}"

    def valider_mot_de_passe(self):
        if len(self.password) < 8:
            return "Le mot de passe doit comporter au moins 8 caractères."
        return None

    def a_acces_total(self):
        if self.type_acces.lower() != "total":
            return "L'employé n'a pas accès à toutes les fonctionnalités."
        return None

    def a_acces_lecture(self):
        if self.type_acces.lower() != "lecture":
            return "L'employé n'a que l'accès en lecture."
        return None
    
