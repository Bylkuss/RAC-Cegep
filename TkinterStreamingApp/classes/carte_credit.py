from datetime import datetime
class CarteCredit:
    def __init__(self, numero, date_expiration, code_secret):
        self.numero = numero
        self.date_expiration = date_expiration
        self.code_secret = code_secret

    def valider_numero(self):
        if len(self.numero) != 16 or not self.numero.isdigit():
            return "Le numéro de carte doit comporter 16 chiffres."
        return None

    def valider_date_expiration(self):
        try:
            exp_date = datetime.strptime(self.date_expiration, "%y/%m")
            if exp_date < datetime.now():
                return "La date d'expiration est antérieure à la date actuelle."
        except ValueError:
            return "Format de date invalide. Utilisez AA/MM."
        return None

    def valider_code_secret(self):
        if len(self.code_secret) != 3 or not self.code_secret.isdigit():
            return "Le code secret doit être un nombre à 3 chiffres."
        return None