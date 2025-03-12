
import tkinter as tk
import re
from datetime import datetime
from tkinter import messagebox
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

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Save button
        self.button_save = tk.Button(self.button_frame, text="Ajouter client", command=self.save_client, width=15, height=2, bg="green", fg="white")
        self.button_save.pack(side=tk.LEFT, padx=10)

        # Cancel button to go back to the main screen
        self.button_cancel = tk.Button(self.button_frame, text="Retour", command=self.cancel, width=15, height=2, bg="red", fg="white")
        self.button_cancel.pack(side=tk.LEFT, padx=10)

    def is_valid_email(self, email):
        """Validates the email format with a simple check."""
        return "@" in email and "." in email

    def save_client(self):
        """Saves a new client."""
        from classes.client import Client
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

        # Validate email format
        if not self.is_valid_email(email):
            messagebox.showerror("Erreur", "L'adresse email est invalide!")
            return

        try:
            # Validate the password using Client's validation method
            password_error = Client.valider_mot_de_passe(password)
            if password_error:
                messagebox.showerror("Erreur", password_error)
                return

            # If expiration_date is a string, try to convert it to datetime
            if isinstance(expiration_date, str):
                try:
                    expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
                except ValueError:
                    messagebox.showerror("Erreur", "Le format de la date d'expiration est incorrect! (doit être AAAA-MM-JJ)")
                    return
            elif isinstance(expiration_date, datetime):
                # It's already a datetime object, so no need to parse
                pass
            else:
                raise ValueError("La date d'expiration doit être une chaîne ou un objet datetime.")

        except ValueError as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")
            return

        try:
            # Create a new client and add it to the list
            carte_credit = CarteCredit(credit_card_digits, expiration_date, secret_code)

            if carte_credit.valider_numero() is None and carte_credit.valider_date_expiration() is None and carte_credit.valider_code_secret() is None:
                new_client = Client(nom, prenom, sexe, datetime.now(), email, password, carte_credit)
                self.app.clients.append(new_client)
                messagebox.showinfo("Succès", "Client ajouté avec succès!")
                self.app.update_client_list()
                self.cancel()
            else:
                messagebox.showerror("Erreur", "La carte de crédit est invalide.")
                return
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")

    def cancel(self):
        """Handles the 'Retour' button. It clears the form and can go back to the previous screen."""
        # Clear the fields
        self.entry_name.delete(0, tk.END)
        self.entry_prenom.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_credit_card_digits.delete(0, tk.END)
        self.entry_expiration_date.delete(0, tk.END)
        self.entry_secret_code.delete(0, tk.END)

        # Optionally, go back to the main screen (if applicable)
        # Assuming `self.app.show_main_screen()` is already handling the employee as an argument
        self.app.show_main_screen(self.app.logged_in_employe)