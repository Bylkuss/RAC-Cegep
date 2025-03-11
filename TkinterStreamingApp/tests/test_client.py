import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.client import Client
from classes.carte_credit import CarteCredit
from classes.personne import Personne

class TestClient(unittest.TestCase):
    def test_initialization_with_card(self):
        carte = CarteCredit("1234567890123456", "12/26", "123")
        client = Client("John", "Doe", "Homme", "2025-03-10", "john.doe@example.com", "password123", carte)
        self.assertEqual(client.nom, "John")
        self.assertEqual(client.courriel, "john.doe@example.com")
        self.assertEqual(len(client.cartes_credit), 1)
        self.assertEqual(client.cartes_credit[0].numero, "1234567890123456")


    def test_ajouter_carte(self):
        carte = CarteCredit("1234567890123456", "12/26", "123")
        client = Client("John", "Doe", "Homme", "2025-03-10", "john.doe@example.com", "password123", carte)
        nouvelle_carte = CarteCredit("9876543210987654", "12/28", "321")
        client.ajouter_carte(nouvelle_carte)
        self.assertEqual(len(client.cartes_credit), 2)
        self.assertEqual(client.cartes_credit[1].numero, "9876543210987654")
    
    def test_invalid_card_should_fail(self):
        with self.assertRaises(ValueError):
            carte = CarteCredit("1234", "12/26", "123")  # Numéro invalide
            Client("Jane", "Doe", "F", "2025-03-10", "jane.doe@example.com", "password123", carte)

    def test_supprimer_carte(self):
        carte = CarteCredit("1234567890123456", "12/26", "123")
        client = Client("John", "Doe", "M", "2025-03-10", "john.doe@example.com", "password123", carte)
        carte_a_supprimer = CarteCredit("9876543210987654", "12/28", "321")
        client.ajouter_carte(carte_a_supprimer)
        client.supprimer_carte(carte_a_supprimer)
        self.assertEqual(len(client.cartes_credit), 1)
        self.assertEqual(client.cartes_credit[0].numero, "1234567890123456")


if __name__ == "__main__":
    unittest.main()