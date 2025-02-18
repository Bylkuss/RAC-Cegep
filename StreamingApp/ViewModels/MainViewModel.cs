using System;
using System.Collections.Generic;
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
            DateInscription = DateTime.Now,
            CartesCredit = new List<CarteCredit>
            {
                new CarteCredit { Numero = "1234-5678-9012-3456", DateExpiration = new DateTime(2025, 12, 31), CodeSecret = "123" }
            }
        });

        // Add sample films
        Films.Add(new Film
        {
            Nom = "Inception",
            Duree = TimeSpan.FromHours(2.5),
            Description = "A mind-bending thriller.",
            Categories = new List<Categorie>
            {
                new Categorie { Nom = "Science Fiction", Description = "Futuristic and speculative themes." },
                new Categorie { Nom = "Action", Description = "High-energy and thrilling sequences." }
            }
        });
    }
}