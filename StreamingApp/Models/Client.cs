using System;
using System.Collections.Generic;

namespace StreamingApp.Models;

public class Client : Personne
{
    public DateTime DateInscription { get; set; }
    public string Courriel { get; set; } = string.Empty;
    public string Password { get; set; } = string.Empty;
    public List<CarteCredit> CartesCredit { get; set; } = new List<CarteCredit>();
}
