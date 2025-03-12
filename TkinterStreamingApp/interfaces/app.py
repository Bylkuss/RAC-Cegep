import tkinter as tk
from tkinter import messagebox
from interfaces.client_screen import ClientScreen
from interfaces.login_screen import LoginScreen
from classes.employe import Employe


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NETFLIX")
        self.root.geometry("900x600")
        self.root.configure(bg="gray")

        # Hardcoded clients (for testing)
        self.clients = []  # Define an empty list of clients
        self.employes = [
            Employe("Dupont", "Jean", "Homme", "2023-01-01", "admin", "123", "total"),
            Employe("Martin", "Sophie", "Femme", "2022-05-15", "user1", "123", "lecture")
        ]
        self.logged_in_employe = None  # Variable to store the logged-in employee

        self.show_login_screen()  # Show the login screen first

    def create_login_screen(self, employes):
        """Create the login screen for employees."""
        self.clear_screen()  # Clear the screen before creating the login screen

        # Create an instance of LoginScreen and show it
        self.login = LoginScreen(self.root, self, employes)
        self.login.show()  # Show the login screen

    def update_client_list(self):
        """Updates the list of clients on the UI."""
        self.refresh_client_list()

    def refresh_client_list(self):
        """Refreshes the client list display."""
        # Ensure the frame is valid before trying to destroy its children
        if hasattr(self, 'clients_list_frame') and self.clients_list_frame.winfo_exists():
            for widget in self.clients_list_frame.winfo_children():
                widget.destroy()

            # Re-display the updated list
            for client in self.clients:
                client_label = tk.Label(self.clients_list_frame, text=f"{client.nom} {client.prenom}")
                client_label.pack(pady=5)

    def show_login_screen(self):
        """Method to show the login screen."""
        if not hasattr(self, 'login') or self.login is None:  # Check if login is initialized
            self.create_login_screen(self.employes)
        else:
            self.clear_screen()  # Ensure the screen is cleared before showing the login
            self.login.show()  # Show the login screen

    def show_main_screen(self, employe):
        """Display the main dashboard."""
        self.logged_in_employe = employe  # Store the logged-in employee
        from interfaces.main_screen import MainScreen
        self.clear_screen()  # Clear the current screen before showing the main screen
        MainScreen(self, employe)  # Ensure employe is passed here

    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()