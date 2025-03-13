import tkinter as tk
import re
from datetime import datetime
from tkinter import messagebox
from classes.carte_credit import CarteCredit
from .config import STYLE_CONFIG, apply_button_style, create_gradient

class ClientScreen:
    SENSITIVE_FIELDS = ["entry_password", "entry_secret_code"]

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

        # Form fields with placeholders
        fields = [
            ("entry_name", "Nom"),
            ("entry_prenom", "Prénom"),
            ("entry_email", "exemple@courriel.com"),
            ("entry_password", "Mot de passe"),
            ("entry_credit_card_digits", "1234 5678 9012 3456"),
            ("entry_expiration_date", "AAAA-MM-JJ"),
            ("entry_secret_code", "123")
        ]

        for entry_var, placeholder in fields:
            # Create entry
            entry = tk.Entry(
                self.form_frame,
                font=STYLE_CONFIG['font'],
                **STYLE_CONFIG['input_field']
            )
            
            # Set name for sensitive fields tracking
            entry._name = entry_var

            # Add placeholder
            entry.insert(0, placeholder)
            entry.config(fg='#888888')

            # Bind events for placeholder handling
            entry.bind("<FocusIn>", lambda e, entry=entry, ph=placeholder: self.clear_placeholder(e, entry, ph))
            entry.bind("<FocusOut>", lambda e, entry=entry, ph=placeholder: self.restore_placeholder(e, entry, ph))

            # Mask sensitive fields
            if entry_var in self.SENSITIVE_FIELDS:
                entry.config(show="")

            setattr(self, entry_var, entry)
            entry.pack(pady=5, ipady=3, ipadx=10)

        # Gender dropdown
        self.sexe_var = tk.StringVar(self.root)
        self.sexe_var.set("Homme")
        self.dropdown_sexe = tk.OptionMenu(
            self.form_frame,
            self.sexe_var,
            "Homme",
            "Femme"
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

        # Action buttons
        self.button_frame = tk.Frame(self.form_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.button_frame.pack(pady=20)

        self.button_save = tk.Button(self.button_frame, text="Ajouter client", command=self.save_client)
        apply_button_style(self.button_save, "Ajouter client")

        self.button_cancel = tk.Button(self.button_frame, text="Retour", command=self.cancel)
        apply_button_style(self.button_cancel, "Retour")

        self.button_save.pack(side=tk.LEFT, padx=10)
        self.button_cancel.pack(side=tk.LEFT, padx=10)

    def clear_placeholder(self, event, entry, placeholder):
        """Clear placeholder text on focus"""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=STYLE_CONFIG['input_field']['fg'])
            # Hide sensitive fields
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="*")

    def restore_placeholder(self, event, entry, placeholder):
        """Restore placeholder if empty"""
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='#888888')
            # Show sensitive fields as plain text if empty
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="")

    def is_valid_email(self, email):
        """Validate email format"""
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def save_client(self):
        """Save new client with validation"""
        from classes.client import Client
        
        # Get values with placeholder check
        fields = {
            'nom': (self.entry_name.get(), "Nom"),
            'prenom': (self.entry_prenom.get(), "Prénom"),
            'email': (self.entry_email.get(), "exemple@courriel.com"),
            'password': (self.entry_password.get(), "Mot de passe"),
            'credit_card': (self.entry_credit_card_digits.get(), "1234 5678 9012 3456"),
            'exp_date': (self.entry_expiration_date.get(), "AAAA-MM-JJ"),
            'secret_code': (self.entry_secret_code.get(), "123")
        }

        # Clean data (remove placeholders)
        clean_data = {field: value if value != placeholder else "" for field, (value, placeholder) in fields.items()}

        # Validate required fields
        if not all(clean_data.values()):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires!")
            return

        # Validate email format and uniqueness
        if not self.is_valid_email(clean_data['email']):
            messagebox.showerror("Erreur", "Format d'email invalide!")
            return
            
        if any(client.email == clean_data['email'] for client in self.app.clients):
            messagebox.showerror("Erreur", "Email déjà utilisé!")
            return

        # Validate password
        password_error = Client.valider_mot_de_passe(clean_data['password'])
        if password_error:
            messagebox.showerror("Erreur", password_error)
            return

        try:
            # Validate credit card data
            exp_date = datetime.strptime(clean_data['exp_date'], "%Y-%m-%d")
            carte_credit = CarteCredit(
                clean_data['credit_card'],
                clean_data['exp_date'],
                clean_data['secret_code']
            )

            # Check individual validation errors
            errors = []
            if error := carte_credit.valider_numero():
                errors.append(error)
            if error := carte_credit.valider_date_expiration():
                errors.append(error)
            if error := carte_credit.valider_code_secret():
                errors.append(error)

            if errors:
                messagebox.showerror("Erreur", "\n".join(errors))
                return

            # Save new client
            new_client = Client(
                clean_data['nom'],
                clean_data['prenom'],
                self.sexe_var.get(),
                datetime.now(),
                clean_data['email'],
                clean_data['password'],
                carte_credit
            )
            self.app.clients.append(new_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès!")
            self.app.update_client_list()
            self.cancel()

        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue: {str(e)}")

    def cancel(self):
        """Clear form and return to main screen"""
        for entry in [
            self.entry_name,
            self.entry_prenom,
            self.entry_email,
            self.entry_password,
            self.entry_credit_card_digits,
            self.entry_expiration_date,
            self.entry_secret_code
        ]:
            entry.delete(0, tk.END)
        
        self.app.show_main_screen(self.app.logged_in_employe)
