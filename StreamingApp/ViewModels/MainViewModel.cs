using System;
using ReactiveUI;
using StreamingApp.Models;
using System.Collections.ObjectModel;

namespace StreamingApp.ViewModels;

public class MainViewModel : ReactiveObject
{
    public ObservableCollection<Client> Clients { get; } = new ObservableCollection<Client>();
    public ObservableCollection<Film> Films { get; } = new ObservableCollection<Film>();

    public MainViewModel()
    {
        // Add sample clients
        Clients.Add(new Client
        {
            Nom = "Doe",
            Prenom = "John",
            Courriel = "john.doe@example.com",
            Password = "password123",
            DateInscription = DateTime.Now
        });

        // Add sample films
        Films.Add(new Film
        {
            Nom = "Inception",
            Duree = TimeSpan.FromHours(2.5),
            Description = "A mind-bending thriller."
        });
    }
}