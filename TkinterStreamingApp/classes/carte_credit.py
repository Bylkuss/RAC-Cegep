from datetime import datetime

class CarteCredit:
    def __init__(self, numero, date_expiration, code_secret):
        self.numero = numero
        self.date_expiration = date_expiration
        self.code_secret = code_secret

    def __str__(self):
        return f"Carte: {self.numero}, Exp: {self.date_expiration}"

    def valider_numero(self):
        if len(self.numero) != 16 or not self.numero.isdigit():
            return "Le numéro de carte doit comporter 16 chiffres."
        return None

    def valider_date_expiration(self):
        try:
            expiration_date = datetime.strptime(self.date_expiration, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Le format de la date d'expiration est invalide. Utiliser 'YYYY-MM-DD'.")

        if expiration_date <= datetime.now():
            return "La date d'expiration de la carte est dépassée."
        return None

    def valider_code_secret(self):
        if len(self.code_secret) != 3 or not self.code_secret.isdigit():
            return "Le code secret doit comporter 3 chiffres."
        return None
