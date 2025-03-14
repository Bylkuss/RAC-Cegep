import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.employe import Employe

class TestEmploye(unittest.TestCase):

    def test_create_employe_valid(self):
        employe = Employe(
            nom="Alice",
            prenom="Smith",
            sexe="F",
            date_embauche="2025-03-01",
            code_utilisateur="A123",
            password="password123",
            type_acces="total"
        )
        
        self.assertEqual(employe.nom, "Alice")
        self.assertEqual(employe.type_acces, "total")

    def test_invalid_password(self):
        # Create an employe with invalid password and check if the validation method is called.
        employe = Employe(
            nom="Alice",
            prenom="Smith",
            sexe="F",
            date_embauche="2025-03-01",
            code_utilisateur="A123",
            password="short",  # Invalid password
            type_acces="total"
        )
        
        # Check the error message from the password validation method
        self.assertEqual(employe.valider_mot_de_passe(), "Le mot de passe doit comporter au moins 8 caractères.")

    def test_access_check(self):
        employe = Employe(
            nom="Alice",
            prenom="Smith",
            sexe="F",
            date_embauche="2025-03-01",
            code_utilisateur="A123",
            password="password123",
            type_acces="lecture"
        )
        
        self.assertEqual(employe.a_acces_lecture(), None)
        self.assertEqual(employe.a_acces_total(), "L'employé n'a pas accès à toutes les fonctionnalités.")


if __name__ == "__main__":
    unittest.main()
