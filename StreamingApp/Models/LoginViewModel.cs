using System;
using System.Reactive;
using Avalonia.Controls;
using ReactiveUI;
using StreamingApp.Views;

namespace StreamingApp.ViewModels
{
    public class LoginViewModel : ReactiveObject
    {
        private string _userCode = string.Empty;
        private string _password = string.Empty;
        private string _errorMessage = string.Empty;

        public string UserCode
        {
            get => _userCode;
            set => this.RaiseAndSetIfChanged(ref _userCode, value);
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
            LoginCommand = ReactiveCommand.Create(Login);
        }

        private void Login()
        {
            // Example: Replace with real authentication logic
            if (UserCode == "admin" && Password == "password")
            {
                // Open Main Window
                var mainWindow = new MainWindow();
                mainWindow.Show();

                // Close the Login Window (Find the parent window and close it)
                var loginWindow = Avalonia.Application.Current?.ApplicationLifetime as
                                  Avalonia.Controls.ApplicationLifetimes.IClassicDesktopStyleApplicationLifetime;
                loginWindow?.MainWindow?.Close();
                
                // Set the main window as the new main window
                loginWindow!.MainWindow = mainWindow;
            }
            else
            {
                ErrorMessage = "Invalid credentials. Try again.";
            }
        }
    }
}
