import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from classes.carte_credit import CarteCredit
from .config import STYLE_CONFIG, apply_button_style, apply_label_style, create_gradient

class ClientScreen:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        
        # Set gradient background
        self.gradient_image = create_gradient(900, 600, "#1E1E1E", "#0A0A0A")
        self.background_label = tk.Label(self.root, image=self.gradient_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Glassmorphism form container
        self.form_frame = tk.Frame(self.root, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=0, highlightthickness=0)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Form fields with modern styling
        fields = [
            ("Nom", "entry_name"),
            ("Prénom", "entry_prenom"),
            ("Email", "entry_email"),
            ("Mot de passe", "entry_password"),
            ("Numéro de carte", "entry_credit_card_digits"),
            ("Date d'expiration (AAAA-MM-JJ)", "entry_expiration_date"),
            ("Code secret", "entry_secret_code")
        ]

        for label_text, entry_var in fields:
            apply_label_style(tk.Label(self.form_frame, text=label_text), label_text)
            entry = tk.Entry(
                self.form_frame,
                font=STYLE_CONFIG['font'],
                **STYLE_CONFIG['input_field']
            )
            if "password" in label_text.lower() or "secret" in label_text.lower():
                entry.config(show="*")
            entry.pack(pady=5, ipady=3, ipadx=10)

            # Store entries as instance variables
            setattr(self, entry_var, entry)

        # Gender dropdown with modern styling
        apply_label_style(tk.Label(self.form_frame, text="Sexe"), "Sexe")
        self.sexe_var = tk.StringVar(self.root)
        self.sexe_var.set("Homme")
        self.dropdown_sexe = tk.OptionMenu(
            self.form_frame,
            self.sexe_var,
            "Homme",
            "Femme",
        )
        self.dropdown_sexe.config(
            bg=STYLE_CONFIG['button_color'],
            fg='white',
            activebackground=STYLE_CONFIG['hover_effect']['bg_color'],
            activeforeground=STYLE_CONFIG['hover_effect']['fg_color'],
            bd=0,
            highlightthickness=0
        )
        self.dropdown_sexe.pack(pady=5)

        # Buttons with gradient and hover effects
        self.button_frame = tk.Frame(self.form_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.button_frame.pack(pady=20)

        self.button_save = tk.Button(self.button_frame, text="Ajouter client", command=self.save_client)
        apply_button_style(self.button_save, "Ajouter client")

        self.button_cancel = tk.Button(self.button_frame, text="Retour", command=self.cancel)
        apply_button_style(self.button_cancel, "Retour")

        self.button_save.pack(side=tk.LEFT, padx=10)
        self.button_cancel.pack(side=tk.LEFT, padx=10)

    def is_valid_email(self, email):
        """Validates the email format with a simple regex check."""
        return "@" in email and "." in email

    def save_client(self):
        """Saves a new client after validating input."""
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
        if not all([nom, prenom, email, password, credit_card_digits, expiration_date, secret_code]):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires!")
            return

        # Validate email format
        if not self.is_valid_email(email):
            messagebox.showerror("Erreur", "L'adresse email est invalide!")
            return
        
        # ✅ Check if email already exists
        if any(client.email == email for client in self.app.clients):
            messagebox.showerror("Erreur", "L'adresse email est déjà utilisée!")
            return

        try:
            # Validate password using Client's validation method
            password_error = Client.valider_mot_de_passe(password)
            if password_error:
                messagebox.showerror("Erreur", password_error)
                return

            # Convert expiration date string to datetime
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

        except ValueError as e:
            messagebox.showerror("Erreur", f"Format de date invalide: {e}")
            return

        try:
            # Create a new credit card object and validate
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
        self.app.show_main_screen(self.app.logged_in_employe)
