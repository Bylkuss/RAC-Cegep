import unittest
from datetime import datetime
from classes.personne import Personne 

class TestPersonne(unittest.TestCase):
    def test_initialization(self):
        personne = Personne("John", "Doe", "M")
        self.assertEqual(personne.nom, "John")
        self.assertEqual(personne.prenom, "Doe")
        self.assertEqual(personne.sexe, "M")

if __name__ == "__main__":
    unittest.main()
