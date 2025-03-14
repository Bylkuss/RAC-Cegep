import tkinter as tk
from tkinter import ttk
import json
from .config import STYLE_CONFIG

class FilmDisplay:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.films = self.load_films()
        self.create_table()

    def load_films(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def create_table(self):
        frame = tk.Frame(self.root, bg=STYLE_CONFIG['background_color'])
        frame.pack(fill="both", expand=True, pady=10)

        canvas = tk.Canvas(frame, bg=STYLE_CONFIG['background_color'])
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        table_frame = tk.Frame(canvas, bg=STYLE_CONFIG['background_color'])
        canvas.create_window((0, 0), window=table_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Créer les entêtes du tableau
        headers = ["Nom", "Durée (min)", "Catégorie(s)", "Acteurs"]
        for col, header in enumerate(headers):
            label = tk.Label(table_frame, text=header, font=STYLE_CONFIG['font_bold'], fg="white", bg=STYLE_CONFIG['glassmorphism']['bg_color'], padx=5, pady=5)
            label.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        # Ajouter les films dans le tableau
        for row, film in enumerate(self.films, start=1):
            tk.Label(table_frame, text=film["nom"], fg="white", bg=STYLE_CONFIG['background_color'], font=STYLE_CONFIG['font']).grid(row=row, column=0, sticky="nsew", padx=1, pady=1)
            tk.Label(table_frame, text=film["duree"], fg="white", bg=STYLE_CONFIG['background_color'], font=STYLE_CONFIG['font']).grid(row=row, column=1, sticky="nsew", padx=1, pady=1)
            tk.Label(table_frame, text=", ".join(film["categories"]), fg="white", bg=STYLE_CONFIG['background_color'], font=STYLE_CONFIG['font']).grid(row=row, column=2, sticky="nsew", padx=1, pady=1)

            # Acteurs avec infobulle
            actor_label = tk.Label(table_frame, text="+", fg="#FFA500", cursor="hand2", bg=STYLE_CONFIG['background_color'], font=STYLE_CONFIG['font'])
            actor_label.grid(row=row, column=3, sticky="nsew", padx=1, pady=1)

            # Ajouter infobulle avec le nom des acteurs
            actor_names = "\n".join([f"{actor['nom_personnage']} ({actor['nom_acteur']})" for actor in film["acteurs"]])
            actor_label.bind("<Enter>", lambda e, names=actor_names: self.show_tooltip(e, names))
            actor_label.bind("<Leave>", self.hide_tooltip)

        # Redimensionnement automatique des colonnes
        for col in range(len(headers)):
            table_frame.grid_columnconfigure(col, weight=1)

        table_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def show_tooltip(self, event, text):
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(self.tooltip, text=text, justify="left", background="#333", foreground="white", relief="solid", borderwidth=1, padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
