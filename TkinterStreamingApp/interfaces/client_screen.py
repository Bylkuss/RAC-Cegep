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
        
        if not hasattr(self.app, 'clients'):
            self.app.clients = []

        self.gradient_image = create_gradient(900, 600, "#1E1E1E", "#0A0A0A")
        self.background_label = tk.Label(self.root, image=self.gradient_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.form_frame = tk.Frame(self.root, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=0, highlightthickness=0)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        fields = [
        ("entry_name", "Nom"),
        ("entry_prenom", "Prénom"),
        ("entry_email", "exemple@courriel.com"),
        ("entry_password", "Mot de passe"),
    ]

        # Create fields before the credit card label
        for entry_var, placeholder in fields:
            entry = tk.Entry(
                self.form_frame,
                font=STYLE_CONFIG['font'],
                **STYLE_CONFIG['input_field']
            )
            entry._name = entry_var
            entry.insert(0, placeholder)
            entry.config(fg='#888888')
            entry.bind("<FocusIn>", lambda e, entry=entry, ph=placeholder: self.clear_placeholder(e, entry, ph))
            entry.bind("<FocusOut>", lambda e, entry=entry, ph=placeholder: self.restore_placeholder(e, entry, ph))

            if entry_var in self.SENSITIVE_FIELDS:
                entry.config(show="")

            setattr(self, entry_var, entry)
            entry.pack(pady=5, ipady=3, ipadx=10)

        # === Label Carte de Crédit ===
        tk.Label(self.form_frame, text="Informations Carte de Crédit", 
                font=(STYLE_CONFIG['font'][0], 12, "bold"), 
                bg=STYLE_CONFIG['glassmorphism']['bg_color'], 
                fg='white').pack(pady=(15, 5))

        # Create credit card fields after the label
        fields = [
            ("entry_credit_card_digits", "1234 5678 9012 3456"),
            ("entry_expiration_date", "AA/MM"),
            ("entry_secret_code", "123")
        ]

        for entry_var, placeholder in fields:
            entry = tk.Entry(
                self.form_frame,
                font=STYLE_CONFIG['font'],
                **STYLE_CONFIG['input_field']
            )
            entry._name = entry_var
            entry.insert(0, placeholder)
            entry.config(fg='#888888')
            entry.bind("<FocusIn>", lambda e, entry=entry, ph=placeholder: self.clear_placeholder(e, entry, ph))
            entry.bind("<FocusOut>", lambda e, entry=entry, ph=placeholder: self.restore_placeholder(e, entry, ph))

            if entry_var in self.SENSITIVE_FIELDS:
                entry.config(show="")

            setattr(self, entry_var, entry)
            entry.pack(pady=5, ipady=3, ipadx=10)


        # Dropdown sexe
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

        # Boutons
        self.button_frame = tk.Frame(self.form_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.button_frame.pack(pady=20)

        self.button_save = tk.Button(self.button_frame, text="Ajouter", command=self.save_client)
        apply_button_style(self.button_save, "Ajouter")

        self.button_cancel = tk.Button(self.button_frame, text="Annuler", command=self.cancel)
        apply_button_style(self.button_cancel, "Annuler", color=STYLE_CONFIG['danger_color'])

        self.button_save.pack(side=tk.LEFT, padx=10)
        self.button_cancel.pack(side=tk.LEFT, padx=10)

    def clear_placeholder(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=STYLE_CONFIG['input_field']['fg'])
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="*")

    def restore_placeholder(self, event, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='#888888')
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="")

    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def save_client(self):
        from classes.client import Client
        
        fields = {
            'nom': (self.entry_name.get(), "Nom"),
            'prenom': (self.entry_prenom.get(), "Prénom"),
            'email': (self.entry_email.get(), "exemple@courriel.com"),
            'password': (self.entry_password.get(), "Mot de passe"),
            'credit_card': (self.entry_credit_card_digits.get(), "1234 5678 9012 3456"),
            'exp_date': (self.entry_expiration_date.get(), "AA/MM"),
            'secret_code': (self.entry_secret_code.get(), "123")
        }

        clean_data = {field: value if value != placeholder else "" for field, (value, placeholder) in fields.items()}

        if not all(clean_data.values()):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires!")
            return

        if not self.is_valid_email(clean_data['email']):
            messagebox.showerror("Erreur", "Format d'email invalid!")
            return

        if any(client.email == clean_data['email'] for client in self.app.clients):
            messagebox.showerror("Erreur", "Email déjà utilisé!")
            return

        password_error = Client.valider_mot_de_passe(clean_data['password'])
        if password_error:
            messagebox.showerror("Erreur", password_error)
            return

        try:
            carte_credit = CarteCredit(
                clean_data['credit_card'],
                clean_data['exp_date'],
                clean_data['secret_code']
            )

            errors = [
                carte_credit.valider_numero(),
                carte_credit.valider_date_expiration(),
                carte_credit.valider_code_secret()
            ]
            errors = [e for e in errors if e]

            if errors:
                messagebox.showerror("Erreur", "\n".join(errors))
                return

            new_client = Client(
                clean_data['nom'],
                clean_data['prenom'],
                self.sexe_var.get(),
                clean_data['email'],
                clean_data['password'],
                carte_credit
            )
            self.app.clients.append(new_client)
            messagebox.showinfo("Succès", "Client ajouté avec succès!")
            self.app.update_client_list()
            self.cancel()

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur inattendue: {str(e)}")

    def cancel(self):
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