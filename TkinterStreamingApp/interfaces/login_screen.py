import tkinter as tk
from tkinter import messagebox
from classes.employe import Employe

class LoginScreen:
    def __init__(self, root, app, employes):
        self.root = root
        self.app = app  # Store reference to the App instance
        self.employes = employes

        self.label_code = tk.Label(self.root, text="Code utilisateur")
        self.label_code.pack(pady=5)

        self.entry_code = tk.Entry(self.root)
        self.entry_code.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Mot de passe")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self.root, text="Se connecter", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        """Validate the login credentials."""
        code = self.entry_code.get()
        password = self.entry_password.get()

        for employe in self.employes:
            if employe.code_utilisateur == code and employe.password == password:
                self.app.show_main_screen(employe)  # Allow login regardless of access level
                return

        messagebox.showerror("Erreur", "Code utilisateur ou mot de passe incorrect")

    def show(self):
        """Display the login screen."""
        self.root.mainloop()
