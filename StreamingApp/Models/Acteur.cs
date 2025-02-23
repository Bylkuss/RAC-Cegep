using System;

namespace StreamingApp.Models;

public class Acteur : Personne{
    public string NomPersonnage { get; set; } = string.Empty;
    public DateTime DebutEmploi { get; set; }
    public DateTime FinEmploi { get; set; }
    public decimal Cachet { get; set; }
}
