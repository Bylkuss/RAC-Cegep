import unittest
from datetime import datetime
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.client import Client
from classes.carte_credit import CarteCredit

class TestClient(unittest.TestCase):

    def test_create_client_valid(self):
        # Setup
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        
        # Test client creation
        client = Client(
            nom="John",
            prenom="Doe",
            sexe="M",
            email="john.doe@example.com",
            password="password123",
            carte_credit=carte_credit
        )
        
        self.assertEqual(client.nom, "John")
        self.assertEqual(client.email, "john.doe@example.com")
        self.assertEqual(len(client.cartes_credit), 1)

    def test_create_client_invalid_email(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        
        # Test client with duplicate email
        client1 = Client(
            nom="John",
            prenom="Doe",
            sexe="M",
            email="john.doe@example.com",
            password="password123",
            carte_credit=carte_credit
        )
        
        

    def test_create_client_invalid_password(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        
        # Check for ValueError when password is too short
        with self.assertRaises(ValueError) as context:
            client = Client(
                nom="John",
                prenom="Doe",
                sexe="M",
                email="john.doe@example.com",
                password="short",  # Invalid password
                carte_credit=carte_credit
            )
        
        # Ensure the exception message is as expected
        self.assertEqual(str(context.exception), "Le mot de passe doit comporter au moins 8 caractères.")

    def test_add_credit_card(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        client = Client(
            nom="John",
            prenom="Doe",
            sexe="M",
            email="john.doe@example.com",
            password="password123",
            carte_credit=carte_credit
        )
        
        new_card = CarteCredit("9876543210987654", "26/12", "456")
        client.ajouter_carte(new_card)
        
        self.assertEqual(len(client.cartes_credit), 2)

    def test_remove_credit_card(self):
        carte_credit = CarteCredit("1234567890123456", "25/12", "123")
        client = Client(
            nom="John",
            prenom="Doe",
            sexe="M",
            email="john.doe@example.com",
            password="password123",
            carte_credit=carte_credit
        )
        
        client.supprimer_carte(carte_credit)
        
        self.assertEqual(len(client.cartes_credit), 0)


if __name__ == "__main__":
    unittest.main()
