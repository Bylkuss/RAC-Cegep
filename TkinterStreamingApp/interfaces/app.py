import tkinter as tk
from interfaces.login_screen import LoginScreen
from classes.employe import Employe
from interfaces.main_screen import MainScreen


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NETFLIX")
        self.root.geometry("800x600")
        self.root.configure(bg="gray")

        # Hardcoded clients (for testing)
        self.clients = []  # Define an empty list of clients
        self.employes = [
            Employe("Dupont", "Jean", "Homme", "2023-01-01", "admin", "123", "total"),
            Employe("Martin", "Sophie", "Femme", "2022-05-15", "user1", "lecture456", "lecture")
        ]
        self.logged_in_employe = None  # Variable to store the logged-in employee

        self.login_screen(self.employes)

    def login_screen(self, employes):
        """Create the login screen for employees."""
        self.clear_screen()

        # Here, you pass `self` as the app to the LoginScreen
        self.login = LoginScreen(self.root, self, employes)
        self.login.show()

    def show_main_screen(self, employe):
        """Display the main dashboard."""
        self.logged_in_employe = employe  # Store the logged-in employee
        from interfaces.main_screen import MainScreen
        self.clear_screen()
        MainScreen(self, employe)  # Ensure employe is passed here

    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()
