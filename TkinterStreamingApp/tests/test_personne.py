import unittest
from datetime import datetime
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.personne import Personne

class TestPersonne(unittest.TestCase):

    def test_initialization(self):
        # Test valid initialization
        personne = Personne("John", "Doe", "Homme")
        self.assertEqual(personne.nom, "John")
        self.assertEqual(personne.sexe, "Homme")
  

if __name__ == "__main__":
    unittest.main()
