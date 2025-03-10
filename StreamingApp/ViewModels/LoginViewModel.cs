using Avalonia.Threading;
using ReactiveUI;
using StreamingApp.Models;
using System;
using System.Diagnostics;
using System.Reactive;
using System.Reactive.Linq;
using System.Threading.Tasks;

namespace StreamingApp.ViewModels
{
    public class LoginViewModel : ReactiveObject
    {
        private string _codeUtilisateur = string.Empty;
        private string _password = string.Empty;
        private string _errorMessage = string.Empty;

        public string CodeUtilisateur
        {
            get => _codeUtilisateur;
            set => this.RaiseAndSetIfChanged(ref _codeUtilisateur, value);
        }

        public string Password
        {
            get => _password;
            set => this.RaiseAndSetIfChanged(ref _password, value);
        }

        public string ErrorMessage
        {
            get => _errorMessage;
            set => this.RaiseAndSetIfChanged(ref _errorMessage, value);
        }

        public ReactiveCommand<Unit, Unit> LoginCommand { get; }

        public LoginViewModel()
        {
            LoginCommand = ReactiveCommand.Create( () =>
            {
                Console.WriteLine("The submit command was run.");
            });

            // Gestion des exceptions
            /*LoginCommand.ThrownExceptions
                .ObserveOn(RxApp.MainThreadScheduler)
                .Subscribe(ex => Dispatcher.UIThread.InvokeAsync(() => ErrorMessage = $"Erreur : {ex.Message}"));
        */}

        private async Task LoginAsync()
        {
            try
            {
                Console.WriteLine("Tentative de connexion...");

                var employe = new Employe
                {
                    CodeUtilisateur = "admin",
                    Password = "password",
                    TypeAcces = "Accès Total"
                };

                if (string.IsNullOrWhiteSpace(CodeUtilisateur))
                {
                    await Dispatcher.UIThread.InvokeAsync(() => ErrorMessage = "Code utilisateur est requis.");
                    return;
                }

                if (string.IsNullOrWhiteSpace(Password))
                {
                    await Dispatcher.UIThread.InvokeAsync(() => ErrorMessage = "Mot de passe est requis.");
                    return;
                }

                var isValid = CodeUtilisateur == employe.CodeUtilisateur &&
                              Password == employe.Password;

                if (isValid)
                {
                    await Dispatcher.UIThread.InvokeAsync(() =>
                    {
                        ErrorMessage = string.Empty;
                        Console.WriteLine("Connexion réussie !");
                        // Navigation ici si nécessaire
                    });
                }
                else
                {
                    await Dispatcher.UIThread.InvokeAsync(() => ErrorMessage = "Identifiants invalides");
                }
            }
            catch (Exception ex)
            {
                await Dispatcher.UIThread.InvokeAsync(() => ErrorMessage = $"Erreur : {ex.Message}");
            }
        }
    }
}
