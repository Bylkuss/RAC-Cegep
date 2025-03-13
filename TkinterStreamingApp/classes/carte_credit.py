from datetime import datetime
class CarteCredit:
    def __init__(self, numero, date_expiration, code_secret):
        self.numero = numero
        self.date_expiration = date_expiration
        self.code_secret = code_secret

    def valider_numero(self):
        """Validates the credit card number."""
        # Check if the card number is valid (e.g., length check, Luhn algorithm)
        if len(self.numero) != 16 or not self.numero.isdigit():
            return "Le numéro de carte doit comporter 16 chiffres."
        return None

    def valider_date_expiration(self):
        """Validates the expiration date with detailed errors"""
        try:
            if isinstance(self.date_expiration, str):
                # Convert string to datetime if needed
                self.date_expiration = datetime.strptime(self.date_expiration, "%Y-%m-%d")
                
            if self.date_expiration < datetime.now():
                return "La date d'expiration est antérieure à la date actuelle."
                
        except ValueError:
            return "Format de date invalide. Utilisez AAAA-MM-JJ."
            
        return None

    def valider_code_secret(self):
        """Validates the secret code."""
        if len(self.code_secret) != 3 or not self.code_secret.isdigit():
            return "Le code secret doit être un nombre à 3 chiffres."
        return None
