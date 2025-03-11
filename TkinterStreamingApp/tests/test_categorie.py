import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.categorie import Categorie

class TestCategorie(unittest.TestCase):
    def test_initialization(self):
        categorie = Categorie("Comédie", "Films drôles")
        self.assertEqual(categorie.nom, "Comédie")
        self.assertEqual(categorie.description, "Films drôles")

if __name__ == "__main__":
    unittest.main()
