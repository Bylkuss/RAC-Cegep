import unittest
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.carte_credit import CarteCredit

class TestCarteCredit(unittest.TestCase):

    def test_valider_numero_correct(self):
        carte = CarteCredit("1234567812345678", "2030-12-31", "123")
        self.assertIsNone(carte.valider_numero())

    def test_valider_numero_incorrect_trop_court(self):
        carte = CarteCredit("1234", "2030-12-31", "123")
        self.assertEqual(carte.valider_numero(), "Le numéro de carte doit comporter 16 chiffres.")

    def test_valider_numero_incorrect_non_numerique(self):
        carte = CarteCredit("1234abcd5678efgh", "2030-12-31", "123")
        self.assertEqual(carte.valider_numero(), "Le numéro de carte doit comporter 16 chiffres.")

    def test_valider_date_expiration_correcte(self):
        future_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        carte = CarteCredit("1234567812345678", future_date, "123")
        self.assertIsNone(carte.valider_date_expiration())

    def test_valider_date_expiration_incorrecte(self):
        expired_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")
        carte = CarteCredit("1234567812345678", expired_date, "123")
        self.assertEqual(carte.valider_date_expiration(), "La date d'expiration de la carte est dépassée.")

    def test_valider_date_expiration_format_incorrect(self):
        carte = CarteCredit("1234567812345678", "12/26", "123")
        with self.assertRaises(ValueError):
            carte.valider_date_expiration()

    def test_valider_code_secret_correct(self):
        carte = CarteCredit("1234567812345678", "2030-12-31", "123")
        self.assertIsNone(carte.valider_code_secret())

    def test_valider_code_secret_incorrect_trop_court(self):
        carte = CarteCredit("1234567812345678", "2030-12-31", "12")
        self.assertEqual(carte.valider_code_secret(), "Le code secret doit comporter 3 chiffres.")

    def test_valider_code_secret_incorrect_non_numerique(self):
        carte = CarteCredit("1234567812345678", "2030-12-31", "abc")
        self.assertEqual(carte.valider_code_secret(), "Le code secret doit comporter 3 chiffres.")

    def test_str_method(self):
        carte = CarteCredit("1234567812345678", "2030-12-31", "123")
        self.assertEqual(str(carte), "Carte: 1234567812345678, Exp: 2030-12-31")

if __name__ == '__main__':
    unittest.main()
