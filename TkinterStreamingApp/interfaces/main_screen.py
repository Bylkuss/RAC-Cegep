import tkinter as tk
from interfaces.client_screen import ClientScreen

class MainScreen:
    def __init__(self, app, employe):
        self.root = app.root
        self.app = app
        self.employe = employe
        self.clients = app.clients  # Assuming clients are passed in from App
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the main screen."""
        self.label_welcome = tk.Label(self.root, text=f"Bienvenue {self.employe.nom}!")
        self.label_welcome.pack(pady=20)

        # Button to view clients
        self.button_view_clients = tk.Button(self.root, text="Voir les clients", command=self.view_clients)
        self.button_view_clients.pack(pady=10)

        # You can add more buttons here for other functionality if needed

    def view_clients(self):
        """Handle the logic for viewing clients."""
        self.clear_screen()

        # Create a label for the client list
        label_clients = tk.Label(self.root, text="Liste des clients", font=("Arial", 14))
        label_clients.pack(pady=10)

        # Create a scrollable frame to hold the list of clients
        canvas = tk.Canvas(self.root)
        canvas.pack(fill="both", expand=True, pady=10)

        scrollbar = tk.Scrollbar(canvas)
        scrollbar.pack(side="right", fill="y")

        client_frame = tk.Frame(canvas)
        client_frame.pack(fill="both", expand=True)

        canvas.create_window((0, 0), window=client_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Loop through clients and display them
        for client in self.clients:
            client_label = tk.Label(client_frame, text=f"{client.nom} {client.prenom} - {client.email}")
            client_label.pack(pady=5, anchor="w")

        # Update the scrollbar
        scrollbar.config(command=canvas.yview)

        # Add a back button
        self.button_back = tk.Button(self.root, text="Retour", command=self.app.show_main_screen)
        self.button_back.pack(pady=10)

    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()