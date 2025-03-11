import tkinter as tk
from tkinter import messagebox
from classes.client import Client
from classes.carte_credit import CarteCredit

class ClientScreen:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.create_widgets()

    def create_widgets(self):
        """Creates the UI for adding a new client."""
        self.label_name = tk.Label(self.root, text="Nom")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack(pady=5)

        self.label_prenom = tk.Label(self.root, text="Prénom")
        self.label_prenom.pack(pady=5)
        self.entry_prenom = tk.Entry(self.root)
        self.entry_prenom.pack(pady=5)

        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Mot de passe")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        # Dropdown for gender
        self.label_sexe = tk.Label(self.root, text="Sexe")
        self.label_sexe.pack(pady=5)
        self.sexe_var = tk.StringVar(self.root)
        self.sexe_var.set("Homme")
        self.dropdown_sexe = tk.OptionMenu(self.root, self.sexe_var, "Homme", "Femme")
        self.dropdown_sexe.pack(pady=5)

        self.label_credit_card_digits = tk.Label(self.root, text="Numéro de carte")
        self.label_credit_card_digits.pack(pady=5)
        self.entry_credit_card_digits = tk.Entry(self.root)
        self.entry_credit_card_digits.pack(pady=5)

        self.label_expiration_date = tk.Label(self.root, text="Date d'expiration (AAAA-MM-JJ)")
        self.label_expiration_date.pack(pady=5)
        self.entry_expiration_date = tk.Entry(self.root)
        self.entry_expiration_date.pack(pady=5)

        self.label_secret_code = tk.Label(self.root, text="Code secret")
        self.label_secret_code.pack(pady=5)
        self.entry_secret_code = tk.Entry(self.root, show="*")
        self.entry_secret_code.pack(pady=5)

        self.button_save = tk.Button(self.root, text="Ajouter client", command=self.save_client)
        self.button_save.pack(pady=10)

        # Use lambda to pass logged_in_employe argument
        self.button_back = tk.Button(self.root, text="Retour", command=lambda: self.app.show_main_screen(self.app.logged_in_employe))
        self.button_back.pack(pady=5)

    def save_client(self):
        """Saves a new client."""
        nom = self.entry_name.get()
        prenom = self.entry_prenom.get()
        sexe = self.sexe_var.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        credit_card_digits = self.entry_credit_card_digits.get()
        expiration_date = self.entry_expiration_date.get()
        secret_code = self.entry_secret_code.get()

        # Check if all required fields are filled
        if not (nom and prenom and email and password and credit_card_digits and expiration_date and secret_code):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires!")
            return

        try:
            # Optionally, you can add validation for email format and credit card format here
            new_card = CarteCredit(credit_card_digits, expiration_date, secret_code)
            new_client = Client(nom, prenom, sexe, email, password, new_card)
            messagebox.showinfo("Succès", f"Client {nom} ajouté.")
            self.app.show_main_screen(self.app.logged_in_employe)  # Ensure employe is passed here
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
