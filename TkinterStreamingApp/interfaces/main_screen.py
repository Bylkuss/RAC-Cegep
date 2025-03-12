# main_screen.py
import tkinter as tk
from tkinter import messagebox
from interfaces.client_screen import ClientScreen
from .config import STYLE_CONFIG, apply_button_style, apply_label_style, create_gradient

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

    def view_clients(self):
        """Displays the list of clients."""
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
        canvas.configure(yscrollcommand=scrollbar.set)

        # Display client details
        for client in self.clients:
            client_label = tk.Label(client_frame, text=f"{client.nom} {client.prenom} - {client.email}", font=STYLE_CONFIG['font'], fg='white', bg=STYLE_CONFIG['background_color'])
            client_label.pack(pady=5, anchor="w")

        scrollbar.config(command=canvas.yview)

        # Back button
        self.button_back = tk.Button(self.root, text="Retour", command=lambda: self.app.show_main_screen(self.employe))
        apply_button_style(self.button_back, "Retour")
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
