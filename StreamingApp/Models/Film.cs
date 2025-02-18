using System;
using System.Collections.Generic;

namespace StreamingApp.Models;

public class Film{
    public string Nom { get; set; } = string.Empty;
    public TimeSpan Duree { get; set; }
    public string Description { get; set; } = string.Empty;
    public List<Categorie> Categories { get; set; } = new List<Categorie>(); 
}

