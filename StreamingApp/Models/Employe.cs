using System;

namespace StreamingApp.Models;

public class Employe : Personne
{
    public DateTime DateEmbauche { get; set; }
    public string CodeUtilisateur { get; set; } = string.Empty;
    public string Password { get; set; } = string.Empty;
    public string TypeAcces { get; set; } = string.Empty; // "acces total ou restreint"
    
}