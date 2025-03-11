import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.employe import Employe

class TestEmploye(unittest.TestCase):

    def test_initialization(self):
        employe = Employe("Alice", "Dupont", "F", "2025-03-10", "EMP123", "password123", "total")
        self.assertEqual(employe.nom, "Alice")
        self.assertEqual(employe.code_utilisateur, "EMP123")
        self.assertEqual(employe.type_acces, "total")

    def test_valider_mot_de_passe(self):
        employe = Employe("Alice", "Dupont", "F", "2025-03-10", "EMP123", "123", "total")
        result = employe.valider_mot_de_passe()
        self.assertEqual(result, "Le mot de passe doit comporter au moins 8 caractères.")

    def test_a_acces_total(self):
        employe = Employe("Alice", "Dupont", "F", "2025-03-10", "EMP123", "password123", "lecture")
        result = employe.a_acces_total()
        self.assertEqual(result, "L'employé n'a pas accès à toutes les fonctionnalités.")

    def test_a_acces_lecture(self):
        employe = Employe("Alice", "Dupont", "F", "2025-03-10", "EMP123", "password123", "total")
        result = employe.a_acces_lecture()
        self.assertEqual(result, "L'employé n'a que l'accès en lecture.")

if __name__ == "__main__":
    unittest.main()
