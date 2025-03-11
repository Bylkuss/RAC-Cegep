import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.acteur import Acteur
from classes.film import Film

class TestActeur(unittest.TestCase):

    def test_initialization(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        self.assertEqual(acteur.nom, "John")
        self.assertEqual(acteur.nom_personnage, "Héros")
        self.assertEqual(acteur.cachet, 1000)
        self.assertEqual(len(acteur.films), 0)

    def test_ajouter_film(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film = Film("Film Test", 120, "Description du film")
        result = acteur.ajouter_film(film)
        self.assertIsNone(result)
        self.assertIn(film, acteur.films)

    def test_ajouter_film_deja_associe(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film = Film("Film Test", 120, "Description du film")
        acteur.ajouter_film(film)
        result = acteur.ajouter_film(film)
        self.assertEqual(result, "Cet acteur est déjà associé à ce film.")

    def test_supprimer_film(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film = Film("Film Test", 120, "Description du film")
        acteur.ajouter_film(film)
        acteur.supprimer_film(film)
        self.assertNotIn(film, acteur.films)

    def test_supprimer_film_non_associe(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film = Film("Film Test", 120, "Description du film")
        result = acteur.supprimer_film(film)
        self.assertEqual(result, "L'acteur n'est pas associé à ce film.")

    def test_calculer_cachet_total(self):
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film1 = Film("Film Test", 120, "Description du film")
        film2 = Film("Film Another", 90, "Another description")
        acteur.ajouter_film(film1)
        acteur.ajouter_film(film2)
        self.assertEqual(acteur.calculer_cachet_total(), 2000)

if __name__ == "__main__":
    unittest.main()
