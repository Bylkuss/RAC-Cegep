from .personne import Personne
from .carte_credit import CarteCredit
import hashlib

class Client(Personne):
    clients_existants = []

    def __init__(self, nom, prenom, sexe, date_inscription, courriel, password, carte_credit):
        super().__init__(nom, prenom, sexe)
        self.date_inscription = date_inscription
        self.courriel = courriel

        # Validate and hash password
        password_error = self.valider_mot_de_passe(password)
        if password_error:
            raise ValueError(password_error)
        
        self.password = self.hash_password(password)
        
        self.cartes_credit = []
        # Validate credit card before adding
        if carte_credit.valider_numero() is None and carte_credit.valider_date_expiration() is None and carte_credit.valider_code_secret() is None:
            self.cartes_credit.append(carte_credit)
        else:
            raise ValueError("La carte de crédit est invalide.")

        Client.clients_existants.append(self)

    def __str__(self):
        return f"Client: {self.nom} {self.prenom}, Email: {self.courriel}"

    def ajouter_carte(self, carte):
        if carte not in self.cartes_credit:
            if carte.valider_numero() is None and carte.valider_date_expiration() is None and carte.valider_code_secret() is None:
                self.cartes_credit.append(carte)
            else:
                raise ValueError("La carte de crédit est invalide.")
        else:
            raise ValueError("Cette carte est déjà associée au client.")

    def supprimer_carte(self, carte):
        if carte in self.cartes_credit:
            self.cartes_credit.remove(carte)

    @staticmethod
    def email_existe(courriel):
        """ Vérifie si l'email existe déjà parmi les clients """
        return any(client.courriel == courriel for client in Client.clients_existants)

    @staticmethod
    def hash_password(password):
        """ Hash le mot de passe avec SHA-256 """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def valider_mot_de_passe(password):
        """ Vérifie que le mot de passe a une longueur minimale avant le hashage """
        if len(password) < 8:
            return "Le mot de passe doit comporter au moins 8 caractères."
        return None
