import tkinter as tk
from tkinter import messagebox
from .config import STYLE_CONFIG, apply_button_style, apply_label_style

class ClientDisplay:
    def __init__(self, root, clients, employe, edit_callback, delete_callback, go_back_callback):
        self.root = root
        self.clients = clients
        self.employe = employe
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self.go_back_callback = go_back_callback

        self.display_clients()

    def display_clients(self):
        self.clear_screen()

        # Title Label
        label_clients = tk.Label(self.root, text="Liste des clients", font=STYLE_CONFIG['font_bold'], fg='white', bg=STYLE_CONFIG['background_color'])
        label_clients.pack(pady=10)

        # === Scrollable frame ===
        container = tk.Frame(self.root, bg=STYLE_CONFIG['background_color'])
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=STYLE_CONFIG['background_color'], bd=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=STYLE_CONFIG['background_color'])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # === TABLE HEADER ===
        header = tk.Frame(scrollable_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        header.grid(row=0, column=0, columnspan=4, sticky="ew")

        headers = ["Prénom", "Nom", "Email", "Date de création", "Actions"]
        for i, text in enumerate(headers):
            label = tk.Label(header, text=text, font=STYLE_CONFIG['font_bold'], fg='white', bg=STYLE_CONFIG['glassmorphism']['bg_color'], anchor="w", padx=10, pady=5)
            label.grid(row=0, column=i, sticky="ew", padx=1)
            header.grid_columnconfigure(i, weight=1)  # Ensure all columns are evenly spaced

        # === CLIENT DATA ===
        for row_index, client in enumerate(self.clients, start=1):
            row = tk.Frame(scrollable_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=1, relief="solid")
            row.grid(row=row_index, column=0, columnspan=5, sticky="ew", padx=1, pady=1)

            tk.Label(row, text=client.prenom, font=STYLE_CONFIG['font'], fg="white", bg=STYLE_CONFIG['glassmorphism']['bg_color'], anchor="w", padx=10, pady=5).grid(row=0, column=0, sticky="ew")
            tk.Label(row, text=client.nom, font=STYLE_CONFIG['font'], fg="white", bg=STYLE_CONFIG['glassmorphism']['bg_color'], anchor="w", padx=10, pady=5).grid(row=0, column=1, sticky="ew")
            tk.Label(row, text=client.email, font=STYLE_CONFIG['font'], fg="white", bg=STYLE_CONFIG['glassmorphism']['bg_color'], anchor="w", padx=10, pady=5).grid(row=0, column=2, sticky="ew")
            tk.Label(row, text=f"Créé(e) le : {client.date_creation}", font=STYLE_CONFIG['font'], fg="white", bg=STYLE_CONFIG['glassmorphism']['bg_color'], anchor="w", padx=10, pady=5).grid(row=0, column=3, sticky="ew")

            if self.employe.type_acces.lower() == "total":
                action_frame = tk.Frame(row, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
                action_frame.grid(row=0, column=4, sticky="ew")

                edit_button = tk.Button(action_frame, text="Modifier", command=lambda c=client: self.edit_callback(c))
                apply_button_style(edit_button, "Modifier")
                edit_button.pack(side="left", padx=5)

                delete_button = tk.Button(action_frame, text="Supprimer", command=lambda c=client: self.delete_client(c))
                apply_button_style(delete_button, "Supprimer", color=STYLE_CONFIG['danger_color'])
                delete_button.pack(side="left", padx=5)

            row.grid_columnconfigure(0, weight=1)
            row.grid_columnconfigure(1, weight=1)
            row.grid_columnconfigure(2, weight=2)
            row.grid_columnconfigure(3, weight=1)
            row.grid_columnconfigure(4, weight=0)
        
        # === Back Button ===
        back_button = tk.Button(self.root, text="Retour", command=self.go_back_callback)
        apply_button_style(back_button, "Retour", color=STYLE_CONFIG['neutral_color'])
        back_button.pack(pady=5)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def delete_client(self, client):
        response = messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer le client {client.nom} {client.prenom}?")
        if response:
            self.delete_callback(client)
            self.display_clients()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()