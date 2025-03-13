import tkinter as tk
from tkinter import messagebox
from classes.carte_credit import CarteCredit # TODO TEST PUROPOSE
from classes.client import Client #TODO TEST PURPOSE
from interfaces.client_screen import ClientScreen
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
        self.button_view_clients = tk.Button(self.nav_frame, text="Voir les clients", command=self.view_clients)
        apply_button_style(self.button_view_clients, "Voir les clients")

        self.button_add_client = tk.Button(self.nav_frame, text="Ajouter client", command=self.add_client)
        apply_button_style(self.button_add_client, "Ajouter client")

        if self.employe.type_acces.lower() != "total":
            self.button_add_client.config(state="disabled")

        self.button_disconnect = tk.Button(self.nav_frame, text="Déconnexion", command=self.disconnect)
        apply_button_style(self.button_disconnect, "Déconnexion")

        # Pack navigation buttons
        self.button_view_clients.pack(side='left', padx=10)
        self.button_add_client.pack(side='left', padx=10)
        self.button_disconnect.pack(side='right', padx=10)

    def add_client(self):
        """Opens the client screen for adding a new client."""
        self.clear_screen()
        ClientScreen(self.app)

    def email_exists(self, email):
        """Check if the email already exists in the clients list."""
        return any(client.email == email for client in self.clients)

    def view_clients(self):
        """Displays the list of clients."""
        
        # TODO: TEST PURPOSE (Add a test client)
        credit_card = CarteCredit("1234567890123456", "2026-01-01", "123")
        self.clients.append(Client("Doe", "John", "Homme", "john@gmail.com", "Password123", credit_card, "2022-05-15"))
        
        self.clear_screen()

        label_clients = tk.Label(self.root, text="Liste des clients", font=STYLE_CONFIG['font_bold'], fg='white')
        label_clients.pack(pady=10)

        # Scrollable frame to display client list
        canvas = tk.Canvas(self.root, bg=STYLE_CONFIG['background_color'], bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True, pady=10)

        scrollbar = tk.Scrollbar(canvas)
        scrollbar.pack(side="right", fill="y")

        client_frame = tk.Frame(canvas, bg=STYLE_CONFIG['background_color'])
        client_frame.pack(fill="both", expand=True)

        canvas.create_window((0, 0), window=client_frame, anchor="nw")

        # Add scroll functionality
        canvas.config(scrollregion=canvas.bbox("all"))

        # Iterate through the clients and create buttons for each client
        for client in self.clients:
            client_frame_column = tk.Frame(client_frame, bg=STYLE_CONFIG['background_color'])
            client_frame_column.pack(fill="x", pady=5)

            client_name_label = tk.Label(client_frame_column, text=f"{client.nom} {client.prenom}", fg='gray', font=STYLE_CONFIG['font'])
            client_name_label.pack(side="left", padx=10)

            # Edit button (visible only for employees with full access)
            if self.employe.type_acces.lower() == "total":
                edit_button = tk.Button(client_frame_column, text="Modifier", command=lambda client=client: self.edit_client(client))
                apply_button_style(edit_button, "Modifier")
                edit_button.pack(side="right", padx=5)

            # Delete button (visible only for employees with full access)
            if self.employe.type_acces.lower() == "total":
                delete_button = tk.Button(client_frame_column, text="Supprimer", command=lambda client=client: self.delete_client(client))
                apply_button_style(delete_button, "Supprimer")
                delete_button.pack(side="right", padx=5)

        scrollbar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollbar.set)


    def edit_client(self, client):
        """Open the client edit screen."""
        # Pass the client data and callback to update the client info in MainScreen
        edit_screen = ClientEditScreen(self.app, self.root, client, self.update_client_info, self.email_exists)


    def update_client_info(self, client, new_name, new_prenom, new_email):
        """Update the client info in the clients list."""
        client.nom = new_name
        client.prenom = new_prenom
        client.email = new_email                
        

        print(f"Updated client: {new_name}, {new_email}")
    def delete_client(self, client):
        """Deletes a client from the list."""
        response = messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer le client {client.nom} {client.prenom}?")
        if response:
            self.app.clients.remove(client)
            self.view_clients()  # Refresh the client list


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
