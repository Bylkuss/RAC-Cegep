import tkinter as tk
from tkinter import messagebox
from classes.carte_credit import CarteCredit  # TODO TEST PURPOSE
from classes.client import Client  # TODO TEST PURPOSE
from interfaces.client_display_screen import ClientDisplay
from interfaces.client_screen import ClientScreen
from interfaces.film_display_screen import FilmDisplay
from .config import STYLE_CONFIG, apply_button_style, apply_label_style, create_gradient
from interfaces.edit_client_screen import ClientEditScreen  # Import the ClientEditScreen class

class MainScreen:
    def __init__(self, app, employe):
        self.root = app.root
        self.app = app
        self.employe = employe
        self.clients = app.clients

        # Set gradient background
        self.gradient_image = create_gradient(900, 600, "#1E1E1E", "#0A0A0A")
        self.background_label = tk.Label(self.root, image=self.gradient_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Navigation bar
        self.nav_frame = tk.Frame(self.root, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=0, highlightthickness=0)
        self.nav_frame.pack(fill='x', pady=10)

        apply_label_style(tk.Label(self.nav_frame, text=f"Bienvenue {self.employe.nom}!"), f"Bienvenue {self.employe.nom}!")
        self.button_view_clients = tk.Button(self.nav_frame, text="Liste de clients", command=self.view_clients)
        apply_button_style(self.button_view_clients, "Liste de clients")

        self.button_add_client = tk.Button(self.nav_frame, text="Créer un client", command=self.add_client)
        apply_button_style(self.button_add_client, "Créer un client")

        if self.employe.type_acces.lower() != "total":
            self.button_add_client.config(state="disabled")

        self.button_disconnect = tk.Button(self.nav_frame, text="Déconnexion", command=self.disconnect)
        apply_button_style(self.button_disconnect, "Déconnexion", color=STYLE_CONFIG['danger_color'])

        # Pack navigation buttons
        self.button_view_clients.pack(side='left', padx=10)
        self.button_add_client.pack(side='left', padx=10)
        self.button_disconnect.pack(side='right', padx=10)

        # Add test clients if none exist
        if not self.clients:
            self.add_test_clients()

        # Display the film list
        self.film_display = FilmDisplay(self.root, "data/films.json")
    
    
    def add_test_clients(self):
        """Create sample test clients."""
        test_clients = [
            Client("Doe", "John", "Homme", "john@gmail.com", "Password123",
                   CarteCredit("1234567890123456", "26/01", "123"), "2022-05-15"),
            Client("Smith", "Jane", "Femme", "jane@gmail.com", "Password456",
                   CarteCredit("9876543210987654", "28/08", "456"), "2023-07-21"),
            Client("Johnson", "Mike", "Homme", "mike@gmail.com", "Password789",
                   CarteCredit("1111222233334444", "25/12", "789"), "2021-03-10"),
        ]

        self.clients.extend(test_clients)
    def add_client(self):
        """Opens the client screen for adding a new client."""
        self.clear_screen()
        ClientScreen(self.app)

    def email_exists(self, email):
        """Check if the email already exists in the clients list."""
        return any(client.email == email for client in self.clients)

    def view_clients(self):
        """Displays the list of clients using ClientDisplay class."""
        self.clear_screen()
        self.client_display = ClientDisplay(
            root=self.root,
            clients=self.clients,
            employe=self.employe,
            edit_callback=self.edit_client,
            delete_callback=self.delete_client,
            go_back_callback=self.show_main_screen  # Passe la fonction de retour
        )

    def show_main_screen(self):
        """Revenir à l'écran principal."""
        self.clear_screen()
        self.__init__(self.app, self.employe)  # Recharge l'écran principal


    def edit_client(self, client):
        """Open the client edit screen."""
        # Pass the client data and callback to update the client info in MainScreen
        edit_screen = ClientEditScreen(self.app, self.root, client, self.update_client_info, self.email_exists)


    def update_client_info(self, client, new_name, new_prenom, new_email, new_password):
        """Update the client info in the clients list."""
        client.nom = new_name
        client.prenom = new_prenom
        client.email = new_email                
        client.password = new_password

        print(f"Updated client: {new_name}, {new_email}")

    def delete_client(self, client):
        """Deletes a client from the list."""
        self.app.clients.remove(client)



    def disconnect(self):
        """Handles the logout functionality with a confirmation dialog."""
        if messagebox.askyesno("Déconnexion", "Voulez-vous vraiment vous déconnecter ?"):
            self.app.logged_in_employe = None
            self.app.login = None
            self.app.show_login_screen()

    def clear_screen(self):
        """Clears all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()
