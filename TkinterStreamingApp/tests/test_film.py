import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.film import Film
from classes.categorie import Categorie
from classes.acteur import Acteur

class TestFilm(unittest.TestCase):

    def test_initialization(self):
        film = Film("Film Test", 120, "Description du film")
        self.assertEqual(film.nom, "Film Test")
        self.assertEqual(film.duree, 120)
        self.assertEqual(film.description, "Description du film")
        self.assertEqual(len(film.categories), 0)
        self.assertEqual(len(film.acteurs), 0)

    def test_ajouter_categorie(self):
        film = Film("Film Test", 120, "Description du film")
        categorie = Categorie("Action", "Films d'action")
        result = film.ajouter_categorie(categorie)
        self.assertIsNone(result)
        self.assertIn(categorie, film.categories)

    def test_ajouter_categorie_deja_associee(self):
        film = Film("Film Test", 120, "Description du film")
        categorie = Categorie("Action", "Films d'action")
        film.ajouter_categorie(categorie)
        result = film.ajouter_categorie(categorie)
        self.assertEqual(result, "Cette catégorie est déjà associée à ce film.")

    def test_supprimer_categorie(self):
        film = Film("Film Test", 120, "Description du film")
        categorie = Categorie("Action", "Films d'action")
        film.ajouter_categorie(categorie)
        film.supprimer_categorie(categorie)
        self.assertNotIn(categorie, film.categories)

    def test_supprimer_categorie_non_associee(self):
        film = Film("Film Test", 120, "Description du film")
        categorie = Categorie("Action", "Films d'action")
        result = film.supprimer_categorie(categorie)
        self.assertEqual(result, "Cette catégorie n'est pas associée à ce film.")

    def test_ajouter_acteur(self):
        film = Film("Film Test", 120, "Description du film")
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        result = film.ajouter_acteur(acteur)
        self.assertIsNone(result)
        self.assertIn(acteur, film.acteurs)

    def test_ajouter_acteur_deja_associe(self):
        film = Film("Film Test", 120, "Description du film")
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film.ajouter_acteur(acteur)
        result = film.ajouter_acteur(acteur)
        self.assertEqual(result, "Cet acteur est déjà associé à ce film.")

    def test_supprimer_acteur(self):
        film = Film("Film Test", 120, "Description du film")
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        film.ajouter_acteur(acteur)
        film.supprimer_acteur(acteur)
        self.assertNotIn(acteur, film.acteurs)

    def test_supprimer_acteur_non_associe(self):
        film = Film("Film Test", 120, "Description du film")
        acteur = Acteur("John", "Doe", "M", "Héros", "2023-01-01", "2025-01-01", 1000)
        result = film.supprimer_acteur(acteur)
        self.assertEqual(result, "Cet acteur n'est pas associé à ce film.")

if __name__ == "__main__":
    unittest.main()
