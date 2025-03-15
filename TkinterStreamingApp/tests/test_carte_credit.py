import unittest
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.carte_credit import CarteCredit

class TestCarteCredit(unittest.TestCase):
    
    def test_valid_card_number(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        self.assertIsNone(carte_credit.valider_numero())
    
    def test_invalid_card_number(self):
        carte_credit = CarteCredit("12345", "25/12", "123")
        self.assertEqual(carte_credit.valider_numero(), "Le numéro de carte doit comporter 16 chiffres.")
    
    def test_valid_expiration_date(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        self.assertIsNone(carte_credit.valider_date_expiration())
    
    def test_invalid_expiration_date(self):
        carte_credit = CarteCredit("1234567890123456", "20/10", "123")
        self.assertEqual(carte_credit.valider_date_expiration(), "La date d'expiration est antérieure à la date actuelle.")
    
    def test_invalid_expiration_format(self):
        carte_credit = CarteCredit("1234567890123456", "2512", "123")
        self.assertEqual(carte_credit.valider_date_expiration(), "Format de date invalide. Utilisez AA/MM.")
    
    def test_valid_code_secret(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        self.assertIsNone(carte_credit.valider_code_secret())
    
    def test_invalid_code_secret(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "12")
        self.assertEqual(carte_credit.valider_code_secret(), "Le code secret doit être un nombre à 3 chiffres.")


if __name__ == "__main__":
    unittest.main()
