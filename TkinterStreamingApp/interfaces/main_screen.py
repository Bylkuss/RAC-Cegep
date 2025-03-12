import tkinter as tk
from tkinter import messagebox
from interfaces.client_screen import ClientScreen

class MainScreen:
    def __init__(self, app, employe):
        """
        Initializes the main screen for the application.

        Parameters:
            app (App): The main application instance.
            employe (Employe): The employee currently logged in.
        """
        self.root = app.root
        self.app = app
        self.employe = employe
        self.clients = app.clients  # List of clients from the application
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the main screen."""
        self.label_welcome = tk.Label(self.root, text=f"Bienvenue {self.employe.nom}!")
        self.label_welcome.pack(pady=20)

        self.button_view_clients = tk.Button(self.root, text="Voir les clients", command=self.view_clients)
        self.button_view_clients.pack(pady=10)

        self.button_add_client = tk.Button(self.root, text="Ajouter client", command=self.add_client)
        self.button_add_client.pack(pady=10)

        # Disable 'Ajouter client' button if the employee does not have full access
        if self.employe.type_acces.lower() != "total":
            self.button_add_client.config(state="disabled", command=lambda: messagebox.showerror("Erreur", "Accès refusé : L'employé n'a pas accès complet."))

        self.button_disconnect = tk.Button(self.root, text="Déconnexion", command=self.disconnect)
        self.button_disconnect.pack(pady=10)

    def add_client(self):
        """Opens the client screen for adding a new client."""
        self.clear_screen()
        ClientScreen(self.app)

    def view_clients(self):
        """Displays the list of clients."""
        self.clear_screen()

        label_clients = tk.Label(self.root, text="Liste des clients", font=("Arial", 14))
        label_clients.pack(pady=10)

        # Scrollable frame to display client list
        canvas = tk.Canvas(self.root)
        canvas.pack(fill="both", expand=True, pady=10)

        scrollbar = tk.Scrollbar(canvas)
        scrollbar.pack(side="right", fill="y")

        client_frame = tk.Frame(canvas)
        client_frame.pack(fill="both", expand=True)

        canvas.create_window((0, 0), window=client_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Display client details
        for client in self.clients:
            client_label = tk.Label(client_frame, text=f"{client.nom} {client.prenom} - {client.email} Crée le: {client.date_creation.strftime('%Y-%m-%d %H:%M')}")
            client_label.pack(pady=5, anchor="w")

        scrollbar.config(command=canvas.yview)

        # Back button
        self.button_back = tk.Button(self.root, text="Retour", command=lambda: self.app.show_main_screen(self.employe))
        self.button_back.pack(pady=10)

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
