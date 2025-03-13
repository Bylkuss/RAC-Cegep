import tkinter as tk
from tkinter import messagebox
from classes.employe import Employe
from .config import STYLE_CONFIG, apply_button_style, apply_label_style, create_gradient

class LoginScreen:
    def __init__(self, root, app, employes):
        self.root = root
        self.app = app
        self.employes = employes

        # Set gradient background
        self.gradient_image = create_gradient(900, 600, "#1E1E1E", "#0A0A0A")
        self.background_label = tk.Label(self.root, image=self.gradient_image)
        self.background_label.place(relwidth=1, relheight=1)

        # Glassmorphism frame for login form
        self.login_frame = tk.Frame(self.root, bg=STYLE_CONFIG['glassmorphism']['bg_color'], bd=0, highlightthickness=0)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Username label and entry
        self.label_code = tk.Label(self.login_frame, text="Code utilisateur", font=STYLE_CONFIG['font'], fg='white', bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.label_code.pack(pady=(10, 5))
        self.entry_code = tk.Entry(self.login_frame, font=STYLE_CONFIG['font'], bg='white', fg='black', bd=0)
        self.entry_code.pack(pady=(0,10), padx=40)

        # Password label and entry
        self.label_password = tk.Label(self.login_frame, text="Mot de passe", font=STYLE_CONFIG['font'], fg='white', bg=STYLE_CONFIG['glassmorphism']['bg_color'])
        self.label_password.pack(pady=(10, 5))
        self.entry_password = tk.Entry(self.login_frame, show="*", font=STYLE_CONFIG['font'], bg='white', fg='black', bd=0)
        self.entry_password.pack(pady=(0, 20), padx=40)

        # Login button
        self.button_login = tk.Button(self.login_frame, text="Se connecter", command=self.login)
        apply_button_style(self.button_login, "Se connecter")
        self.button_login.pack(pady=10)

    def login(self):
        """Validate the login credentials."""
        code = self.entry_code.get()
        password = self.entry_password.get()

        for employe in self.employes:
            if employe.code_utilisateur == code and employe.password == password:
                self.app.show_main_screen(employe)
                return

        messagebox.showerror("Erreur", "Code utilisateur ou mot de passe incorrect")

    def show(self):
        """Display the login screen."""
        self.root.mainloop()
