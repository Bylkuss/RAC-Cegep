import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.film import Film
from classes.categorie import Categorie
from classes.acteur import Acteur

class TestFilm(unittest.TestCase):
    
    def test_create_film(self):
        film = Film(nom="Inception", duree=148, description="A mind-bending thriller")
        self.assertEqual(film.nom, "Inception")
        self.assertEqual(film.duree, 148)
        self.assertEqual(film.description, "A mind-bending thriller")
    
    def test_add_category(self):
        film = Film(nom="Inception", duree=148, description="A mind-bending thriller")
        film.ajouter_categorie("Sci-Fi")
        self.assertIn("Sci-Fi", film.categories)
    
    def test_remove_category(self):
        film = Film(nom="Inception", duree=148, description="A mind-bending thriller")
        film.ajouter_categorie("Sci-Fi")
        film.supprimer_categorie("Sci-Fi")
        self.assertNotIn("Sci-Fi", film.categories)

    def test_add_actor(self):
        film = Film(nom="Inception", duree=148, description="A mind-bending thriller")
        film.ajouter_acteur("Leonardo DiCaprio")
        self.assertIn("Leonardo DiCaprio", film.acteurs)
    
    def test_remove_actor(self):
        film = Film(nom="Inception", duree=148, description="A mind-bending thriller")
        film.ajouter_acteur("Leonardo DiCaprio")
        film.supprimer_acteur("Leonardo DiCaprio")
        self.assertNotIn("Leonardo DiCaprio", film.acteurs)


if __name__ == "__main__":
    unittest.main()
