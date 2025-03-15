import tkinter as tk
from tkinter import messagebox

from .client_screen import ClientScreen
from .config import STYLE_CONFIG, apply_button_style, create_gradient

class ClientEditScreen:
    SENSITIVE_FIELDS = ["entry_password"]

    def __init__(self, app, root, client_data, update_callback, email_exists):
        self.app = app
        self.root = root
        self.client_data = client_data
        self.update_callback = update_callback
        self.email_exists = email_exists

        # Set gradient background
        self.gradient_image = create_gradient(900, 600, "#1E1E1E", "#0A0A0A")
        self.background_label = tk.Label(self.root, image=self.gradient_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Glassmorphism form container
        self.form_frame = tk.Frame(self.root, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=0, highlightthickness=0)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # === Define Fields ===
        fields = [
            ("entry_name", "Nom", self.client_data.nom),
            ("entry_prenom", "Prénom", self.client_data.prenom),
            ("entry_email", "exemple@courriel.com", self.client_data.email),
            ("entry_password", "***", "")  # Add password field with hidden placeholder
        ]

        for entry_var, placeholder, value in fields:
            # Create entry fields, prefill with client data
            entry = tk.Entry(self.form_frame, font=STYLE_CONFIG['font'], **STYLE_CONFIG['input_field'])
            entry.insert(0, value)  # Set the current value
            entry._name = entry_var  # Set name for tracking
            entry.config(fg='#888888')
            entry.bind("<FocusIn>", lambda e, entry=entry, ph=placeholder: self.clear_placeholder(e, entry, ph))
            entry.bind("<FocusOut>", lambda e, entry=entry, ph=placeholder: self.restore_placeholder(e, entry, ph))

            # Mask password field
            if entry_var == "entry_password":
                entry.config(show="*")
                if not value:  # If no value, set placeholder as ***
                    entry.insert(0, placeholder)
                    entry.config(fg='#888888')

            setattr(self, entry_var, entry)
            entry.pack(pady=5, ipady=3, ipadx=10)

        # === Buttons ===
        self.button_frame = tk.Frame(self.form_frame, bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.button_frame.pack(pady=20)

        self.button_save = tk.Button(self.button_frame, text="Sauvegarder", command=self.save_changes)
        apply_button_style(self.button_save, "Sauvegarder")
        
        self.button_cancel = tk.Button(self.button_frame, text="Annuler", command=self.cancel)
        apply_button_style(self.button_cancel, "Annuler", color=STYLE_CONFIG['danger_color'])

        self.button_save.pack(side=tk.LEFT, padx=10)
        self.button_cancel.pack(side=tk.LEFT, padx=10)

    def save_changes(self):
        """Save changes made to the client data and call the update callback."""
        updated_name = self.entry_name.get()
        updated_prenom = self.entry_prenom.get()
        updated_email = self.entry_email.get()
        new_password = self.entry_password.get()

        # === Validate Email Uniqueness ===
        if self.email_exists(updated_email) and updated_email != self.client_data.email:
            messagebox.showerror("Erreur", "Email déjà utilisé!")
            return
        
        # === Validate Password ===
        if new_password and new_password != "***":  # Ignore placeholder
            if len(new_password) < 8:
                messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
                return

            if new_password == self.client_data.password:
                messagebox.showerror("Erreur", "Le nouveau mot de passe doit être différent de l'ancien.")
                return

        # === Call the update callback to apply the changes ===
        self.update_callback(
            self.client_data,
            updated_name,
            updated_prenom,
            updated_email,
            new_password if new_password and new_password != "***" else self.client_data.password  # Keep the old password if unchanged
        )

        messagebox.showinfo("Succès", "Client mis à jour avec succès!")

        # === Close the current screen ===
        self.cancel()

    def restore_placeholder(self, event, entry, placeholder):
        """Restore placeholder if empty"""
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg='#888888')
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="*")

    def clear_placeholder(self, event, entry, placeholder):
        """Clear placeholder on focus"""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")
            if entry._name in self.SENSITIVE_FIELDS:
                entry.config(show="*")

    def cancel(self):
        """Return to the previous screen."""
        self.app.show_main_screen(self.app.logged_in_employe)